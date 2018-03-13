import sqlite3
import time

def open_connection(db_name='gs_leads.db'):
    conn = sqlite3.connect(db_name)
    return conn

def create_table_leads(conn):
    sql_statement = '''CREATE TABLE IF NOT EXISTS leads(
                            fb_profile_link TEXT UNIQUE NOT NULL,
                            name TEXT NULL,
                            emails TEXT NULL,
                            booking_agent TEXT NULL,
                            contact_address TEXT NULL,
                            phone TEXT NULL,
                            category TEXT NULL,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                        );
                        '''
    with conn:
        conn.execute(sql_statement)
    return 

def lead_exists(conn, fb_profile_link):
    sql_statement = '''SELECT count(*) FROM leads WHERE fb_profile_link = ?;'''
    cur = conn.cursor()
    cur.execute(sql_statement, (fb_profile_link,))
    if cur.fetchall() == [(0,)]:
        return False
    else:
        return True
def add_leads_to_db(conn, fb_profile_link, name, emails, booking_agent, contact_address, phone, category):
    if lead_exists(conn, fb_profile_link):
        return
    else:
        sql_statement = '''INSERT INTO leads(fb_profile_link, name, emails, booking_agent, contact_address, phone, category) VALUES(:fb_profile_link,:name, :emails,:booking_agent,:contact_address,:phone, :category);'''
        data = {
            'fb_profile_link': fb_profile_link, 
            'name': name,
            'emails': str(emails), 
            'booking_agent': booking_agent, 
            'contact_address': contact_address, 
            'phone': phone, 
            'category': category
            }
        with conn:
            conn.execute(sql_statement, data)
    return

def get_all_leads(conn):
    sql_statement = '''SELECT * FROM leads;'''
    cur = conn.cursor()
    cur.execute(sql_statement)
    result = cur.fetchall()
    cur.close()
    return result

def create_table_unexplored(conn):
    sql_statement = '''CREATE TABLE IF NOT EXISTS unexplored(
                            fb_profile_link TEXT NOT NULL,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                        );'''
    with conn:
        conn.execute(sql_statement)
    return

def get_all_unexplored_leads(conn):
    sql_statement = '''SELECT fb_profile_link FROM unexplored ORDER BY timestamp;'''
    cur = conn.cursor()
    cur.execute(sql_statement)
    result = cur.fetchall()
    cur.close()
    return result

def get_unexplored_lead(conn):
    sql_statement = '''SELECT fb_profile_link FROM unexplored ORDER BY timestamp LIMIT 1;'''
    cur = conn.cursor()
    cur.execute(sql_statement)
    result = cur.fetchone()
    cur.close()
    return result

def add_to_unexplored_leads(conn, list_of_fb_profile_link):
    for fb_profile_link in list_of_fb_profile_link:
        sql_statement = '''SELECT count(*) FROM unexplored WHERE fb_profile_link = ?'''
        cur = conn.cursor()
        cur.execute(sql_statement, fb_profile_link)
        if cur.fetchall() != [(0,)]:
            list_of_fb_profile_link.remove(fb_profile_link)
    sql_statement = '''INSERT INTO unexplored(fb_profile_link) VALUES(?);'''
    with conn:
        conn.executemany(sql_statement, list_of_fb_profile_link)
    return 

def delete_all_from_unexplored(conn):
    sql_statement = '''DELETE FROM unexplored;'''
    with conn:
        conn.execute(sql_statement)
    return

def delete_from_unexplored(conn, list_of_fb_profile_link):
    sql_statement = '''DELETE FROM unexplored WHERE fb_profile_link = ?;'''
    with conn:
        conn.executemany(sql_statement, list_of_fb_profile_link)
    return

def close_connection(conn):
    conn.close()

