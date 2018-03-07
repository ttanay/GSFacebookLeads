import sqlite3
import time
from lead import Lead

def open_connection(db_name='gs_leads.db'):
    conn = sqlite3.connect(db_name)
    return conn

def create_table_leads(conn):
    sql_statement = '''CREATE TABLE IF NOT EXISTS leads(
                            fb_slug TEXT UNIQUE NOT NULL,
                            emails TEXT NULL,
                            booking_agent TEXT NULL,
                            contact_address TEXT NULL,
                            phone TEXT NULL,
                            category TEXT NULL
                        );
                        '''
    with conn:
        conn.execute(sql_statement)
    return 

def add_leads_to_db(conn, lead):
    sql_statement = '''INSERT INTO leads VALUES(?,?,?,?,?,?);'''
    with conn:
        conn.execute(sql_statement, lead.get_lead_tuple())
    return

def create_table_unexplored(conn):
    sql_statement = '''CREATE TABLE IF NOT EXISTS unexplored(
                            fb_slug TEXT UNIQUE NOT NULL,
                            timestamp REAl NOT NULL
                        );'''
    with conn:
        conn.execute(sql_statement)
    return

def add_to_unexplored_leads(conn, fb_slug):
    sql_statement = '''INSERT INTO unexplored VALUES(?, ?);'''
    data = (fb_slug, time.time())
    with conn:
        conn.execute(sql_statement, data)

def close_connection(conn):
    conn.close()

