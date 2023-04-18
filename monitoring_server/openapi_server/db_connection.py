import sqlite3
from sqlite3 import Error


TIMINGS_TABLE = """ CREATE TABLE IF NOT EXISTS timings(
                    id integer PRIMARY KEY,
                    request_id text NOT NULL,
                    client_id text NOT NULL,
                    total_time text NOT NULL,
                    server_process_time text NOT NULL,
                    network_request_time text NOT NULL,
                    network_response_time text NOT NULL,
                    active_threads integer NOT NULL, 
                    cpu_load real NOT NULL, 
                    gpu_load real NOT NULL, 
                    memory_usage real NOT NULL,
                    received_at text NOT NULL
                    );
                """

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_connection_in_memory():
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
    except Error as e:
        print(e)
    return conn

def close_connection(db_conn):
    """ close a database connection to a SQLite database """
    try:
        if db_conn:
            db_conn.close()
    except Error as e:
        print(e)

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_timings_table(conn):
    """ create a table from the TIMINGS_TABLE constant
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(TIMINGS_TABLE)
    except Error as e:
        print(e)


def create_timing(conn, timing):
    """
    Create a new timings entry
    :param conn: connection to db
    :param timing: the timing tuple to be added
    :return:
    """
    #Primary key "id" is automatically set by SQLite
    sql = """ INSERT INTO timings (request_id, client_id, total_time, server_process_time, network_request_time, 
                                   network_response_time, active_threads, cpu_load, gpu_load, memory_usage, received_at)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, timing)
    conn.commit()


def get_average_of_total_time(conn):
    """
    Returns the average of total_time entries
    :param conn: connection to db
    :return: average value of total_time entries
    """
    cur = conn.cursor()
    cur.execute("SELECT avg(total_time) FROM timings")

    val = cur.fetchone()[0]
    return val

def get_average_of_server_process_time(conn):
    """
    Returns the average of server_process_time entries
    :param conn: connection to db
    :return: average value of server_process_time entries
    """
    cur = conn.cursor()
    cur.execute("SELECT avg(server_process_time) FROM timings")

    val = cur.fetchone()[0]
    return val

def get_average_of_network_request_time(conn):
    """
    Returns the average of network_request_time entries
    :param conn: connection to db
    :return: average value of network_request_time entries
    """
    cur = conn.cursor()
    cur.execute("SELECT avg(network_request_time) FROM timings")

    val = cur.fetchone()[0]
    return val

def get_average_of_network_response_time(conn):
    """
    Returns the average of network_response_timeentries
    :param conn: connection to db
    :return: average value of network_response_time entries
    """
    cur = conn.cursor()
    cur.execute("SELECT avg(network_response_time) FROM timings")

    val = cur.fetchone()[0]
    return val

def select_all_timings(conn):
    """
    Returns all timings entries
    :param conn: connection to db
    :return: All rows in the timings table
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM timings")

    rows = cur.fetchall()
    return rows
