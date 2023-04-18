import os
import sqlite3
import unittest
from datetime import datetime as dt
from openapi_server import db_connection as db_conn

class TestDatabaseApi(unittest.TestCase):
    """ Test of database api functions.
        NOTE: If a test fails, remember to delete its 
        database before running the test again.
    """

    def test_create_connection(self):
        """ test case for create_connection"""
        db_file_name = "test_db0.db"
        path = os.path.join(os.getcwd(), db_file_name)
        conn = db_conn.create_connection(path)
        self.assertEquals(os.path.exists(path), True)
        db_conn.close_connection(conn)
        os.remove(path)
    
    def test_close_connection(self):
        """ test case for close_connection"""
        db_file_name = "test_db1.db"
        path = os.path.join(os.getcwd(), db_file_name)
        conn = db_conn.create_connection(path)
        db_conn.close_connection(conn)

        test_exception = False
        try:
            cur = conn.cursor()
        except sqlite3.ProgrammingError as e:
            test_exception = True
        self.assertEqual(test_exception, True)
        os.remove(path)

    def test_create_table(self):
        """ test case for create_table"""
        db_file_name = "test_db2.db"
        path = os.path.join(os.getcwd(), db_file_name)
        conn = db_conn.create_connection(path)
        sql_table = """ CREATE TABLE IF NOT EXISTS test(
                    client_id text PRIMARY KEY);"""
        db_conn.create_table(conn, sql_table)

        cur = conn.cursor()
        cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='test';")
        self.assertEqual((cur.fetchone()[0]==1), True)
        db_conn.close_connection(conn)
        os.remove(path)

    def test_create_timings_table(self):
        """ test case for create_timings_table"""
        db_file_name = "test_db3.db"
        path = os.path.join(os.getcwd(), db_file_name)
        conn = db_conn.create_connection(path)
        db_conn.create_timings_table(conn)

        cur = conn.cursor()
        cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='timings';")
        self.assertEqual((cur.fetchone()[0]==1), True)
        db_conn.close_connection(conn)
        os.remove(path)
    
    def test_create_timing(self):
        """ test case for create_timing"""
        db_file_name = "test_db4.db"
        path = os.path.join(os.getcwd(), db_file_name)
        conn = db_conn.create_connection(path)
        db_conn.create_timings_table(conn)
        new_timing = ("request_id", "client_id", "4.42", str(dt.now()), str(dt.now()), str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now()))
        db_conn.create_timing(conn, new_timing)

        cur = conn.cursor()
        cur.execute("SELECT request_id, client_id, total_time, server_process_time, network_request_time, network_response_time, active_threads, cpu_load, gpu_load, memory_usage, received_at FROM timings WHERE id = 1")
        row = cur.fetchone()
        self.assertEqual(row, new_timing)
        db_conn.close_connection(conn)
        os.remove(path)

    def test_get_average_of_total_time(self):
        """ test case for get_average_of_all_timings"""
        db_file_name = "test_db5.db"
        path = os.path.join(os.getcwd(), db_file_name)
        conn = db_conn.create_connection(path)

        db_conn.create_timings_table(conn)
        db_conn.create_timing(conn, ("request_id", "client_id", "5", str(dt.now()), str(dt.now()), str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5", str(dt.now()), str(dt.now()), str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5", str(dt.now()), str(dt.now()), str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5", str(dt.now()), str(dt.now()), str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))

        avg_val = db_conn.get_average_of_total_time(conn)
        self.assertEqual(avg_val, 5)
        db_conn.close_connection(conn)
        os.remove(path)

    def test_get_average_of_server_process_time(self):
        """ test case for get_average_of_server_process_time"""
        db_file_name = "test_db6.db"
        path = os.path.join(os.getcwd(), db_file_name)
        conn = db_conn.create_connection(path)

        db_conn.create_timings_table(conn)
        db_conn.create_timing(conn, ("request_id", "client_id", "5", 4, str(dt.now()), str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5", 4, str(dt.now()), str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5", 4, str(dt.now()), str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5", 4, str(dt.now()), str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))

        avg_val = db_conn.get_average_of_server_process_time(conn)
        self.assertEqual(avg_val, 4)
        db_conn.close_connection(conn)
        os.remove(path)

    def test_get_average_of_network_request_time(self):
        """ test case for get_average_of_network_request_time"""
        db_file_name = "test_db7.db"
        path = os.path.join(os.getcwd(), db_file_name)
        conn = db_conn.create_connection(path)

        db_conn.create_timings_table(conn)
        db_conn.create_timing(conn, ("request_id", "client_id", "5", 4, 3, str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5", 4, 3, str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5", 4, 3, str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5", 4, 3, str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))

        avg_val = db_conn.get_average_of_network_request_time(conn)
        self.assertEqual(avg_val, 3)
        db_conn.close_connection(conn)
        os.remove(path)

    def test_get_average_of_network_response_time(self):
        """ test case for get_average_of_network_response_time"""
        db_file_name = "test_db8.db"
        path = os.path.join(os.getcwd(), db_file_name)
        conn = db_conn.create_connection(path)

        db_conn.create_timings_table(conn)
        db_conn.create_timing(conn, ("request_id", "client_id", "5", 4, 3, 2, 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5", 4, 3, 2, 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5", 4, 3, 2, 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5", 4, 3, 2, 1, 0.5, 0.5, 0.5, str(dt.now())))

        avg_val = db_conn.get_average_of_network_response_time(conn)
        self.assertEqual(avg_val, 2)
        db_conn.close_connection(conn)
        os.remove(path)

    def test_select_all_timings(self):
        """ test case for select_all_timings"""
        db_file_name = "test_db9.db"
        path = os.path.join(os.getcwd(), db_file_name)
        conn = db_conn.create_connection(path)

        db_conn.create_timings_table(conn)
        db_conn.create_timing(conn, ("request_id", "client_id", "5.123", str(dt.now()), str(dt.now()), str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5.123", str(dt.now()), str(dt.now()), str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5.123", str(dt.now()), str(dt.now()), str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))
        db_conn.create_timing(conn, ("request_id", "client_id", "5.123", str(dt.now()), str(dt.now()), str(dt.now()), 1, 0.5, 0.5, 0.5, str(dt.now())))

        rows = db_conn.select_all_timings(conn)
        list(rows)
        self.assertEqual(len(rows), 4)
        db_conn.close_connection(conn)
        os.remove(path)
