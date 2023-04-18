#!/usr/bin/env python3
import flask
import connexion
from openapi_server import encoder
from datetime import datetime as dt
from openapi_server import db_connection as db_conn

#Setup connexion for REST 
app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'EXOGEM'},
            pythonic_params=True)

def __get_HTML(avg_total_time, avg_srv_process_time, avg_network_req_time, avg_network_res_time):
    """ Returns the html code used for starting the tables

       :rtype: str
    """
    return """<html>
                <head> 
                    <style> table, th, td {border: 1px solid black;border-collapse: collapse;padding:5px}</style> 
                </head> 
                <body> 
                    <h3> <table> 
                    <tr> <td> Average total_time of all requests </td> <td>""" + avg_total_time + """ </td> </tr>
                    <tr> <td> Average server_process_time of all requests </td> <td>""" + avg_srv_process_time + """ </td> </tr>
                    <tr> <td> Average network_request_time of all requests </td> <td>""" + avg_network_req_time + """ </td> </tr>
                    <tr> <td> Average network_response_time of all requests </td> <td>""" + avg_network_res_time + """ </td> </tr>
                    </table> </h3>
                    <h4> Elements in the database </h4> 
                    <table> <tr> <th> row_id </th> <th> request_id </th> <th> client_id </th> <th> total_time</th>
                    <th>server_process_time</th><th>network_request_time</th><th>network_response_time</th>
                    <th>active_threads</th><th>CPU_load</th><th>GPU_load</th><th>memory_load</th><th>received_at</th></tr>"""



@app.route('/')
def home():
    """ The homepage used to display the monitoring data.         
    """
    #Gets all entries in the timings table and prints to homepage
    conn = db_conn.create_connection("monitor_db.db")
    rows = db_conn.select_all_timings(conn)

    # Get average timings that are monitored
    avg_total_time = db_conn.get_average_of_total_time(conn)
    avg_server_process_time = db_conn.get_average_of_server_process_time(conn)
    avg_network_request_time = db_conn.get_average_of_network_request_time(conn)
    avg_network_response_time = db_conn.get_average_of_network_response_time(conn) 
    
    db_conn.close_connection(conn)

    if avg_total_time is None:
        return "No elements in the database"

    #Pretty print (ish)
    html = __get_HTML(str(round(avg_total_time, 5)), str(round(avg_server_process_time, 5)), 
                      str(round(avg_network_request_time, 5)), str(round(avg_network_response_time, 5)))

    text = ""
    if rows:          
        for row in rows:
            list(row)
            text = text + "<tr>"
            for element in row:
                text = text + "<td>" + str(element) + "</td>"
            text = text + "</tr>"
    else:
        return "No elemets in the database"
    return html + text + "</table> </body> </html>"

if __name__ == '__main__':
    #Create connection to the database
    conn = db_conn.create_connection("monitor_db.db")

    #Create the tables if they dont exists
    try:
        db_conn.create_timings_table(conn)
    except Exception as e:
        print (e)
    db_conn.close_connection(conn)
    app.run(port=8080)
