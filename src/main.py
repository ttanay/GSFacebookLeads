import sqlite3
import argparse
import sys
import datetime
import utility
import db_io
import file_io
import serializer

leads = []

def explore(conn, fb_profile_link):
    print('Exploring lead: {}'.format(fb_profile_link))
    if db_io.lead_exists(conn, fb_profile_link):
        print('Lead already exists in DB')
        return None
    db_io.add_to_unexplored_leads(conn, [(fb_profile_link,)])
    lead = utility.get_leads(fb_profile_link)
    lead['fb_profile_link'] = fb_profile_link
    db_io.add_leads_to_db(conn, fb_profile_link=fb_profile_link, name=lead['name'], emails=lead['emails'], booking_agent=lead['booking_agent'], contact_address=lead['contact_address'], phone=lead['phone'], category=lead['category'])
    related_pages = utility.get_related_pages(fb_profile_link)
    related_pages = utility.clean_urls(related_pages)
    #print(related_pages)
    db_io.add_to_unexplored_leads(conn, related_pages)
    db_io.delete_from_unexplored(conn, [(fb_profile_link,)])
    #WRITE RESULT TO CSV FILE
    #file_io.add_lead_to_csv_file(lead_file, lead)
    return lead 

if __name__ == '__main__':
    conn = sqlite3.connect('gs_leads.db')
    db_io.create_table_leads(conn)
    db_io.create_table_unexplored(conn)
    dt = datetime.datetime.now()
    date_string = dt.strftime("%d_%b_%yT%H_%M")
    #lead_file_name = 'lead' + date_string + '.csv'
    #lead_file = open(lead_file_name, 'w+')

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start_url", help="Enter the URL to get leads from", required=False, nargs=1)
    parser.add_argument("-n", "--number_of_leads", help="Enter no of leads", required=False, nargs=1)
    parser.add_argument("-d", help="Delete unexplored leads from DB", action="store_true", required=False)
    #parser.add_argument("--dump_leads", help="Dump all leads in DB to csv file", action="store_true", required=False)
    #parser.add_argument("--dump_unexplored_leads", help="Dump all unexxplored leads to csv file", action="store_true", required=False)
    args = parser.parse_args()
    #print(args)
    #print(type(args.start_url[0]))
    #print(type(args.number_of_leads[0]))
    #print(args.start_url[0])
    #print(int(args.number_of_leads[0]))
    try:
        if args.start_url:
            start_url = str(args.start_url[0])
            #print(type(start_url))
            #ADD URL VALIDATION
        else:
            start_url = None
            #print(type(start_url))
        #print(start_url)
    except ValueError:
        print('ERROR: -s flag should be a string')
    try:
        if args.number_of_leads:
            n = int(args.number_of_leads[0])
            #print(type(n))
        else:
            n = 10
    except ValueError:
        print('ERROR: -n flag should be a number(int)')
        sys.exit()
    
    '''if args.dump_leads:
        leads = db_io.get_all_leads(conn)
        print(leads)
        file_io.dump_all_leads(leads)

    if args.dump_unexplored_leads:
        unexplored_leads = db_io.get_all_unexplored_leads(conn)
        file_io.dump_all_unexplored_leads(unexplored_leads)'''

    if args.d:
        db_io.delete_all_from_unexplored(conn)
        print('Deleted unexplored leads from DB')
        sys.exit()

    if start_url is not None:
        print('start_url is not None')
        data_dump = db_io.get_all_unexplored_leads(conn)
        # SAVE UNEXPLORED DUMP DATA TO FILE
        serializer.serialize_dump(data_dump)
        db_io.delete_from_unexplored(conn, data_dump)
        lead = explore(conn, start_url)
        leads.append(lead)
        n -= 1
        #db_io.add_to_unexplored_leads(conn, [(start_url,)])
        while(n):
            unexplored_lead = db_io.get_unexplored_lead(conn)
            if not unexplored_lead:
                print('No new leads')
                break
            fb_profile_link = unexplored_lead[0]
            lead = explore(conn, fb_profile_link)
            #print(lead)
            if lead is not None:
                leads.append(lead)
            n -= 1
        #SAVE UNEXPLORED DUMP DATA BACK TO DB
        #dump_data = file_io.load_records_from_file(dump_file)
        data_dump = serializer.deserialize_dump()
        db_io.add_to_unexplored_leads(conn, data_dump)
    else:
        while(n):
            unexplored_lead = db_io.get_unexplored_lead(conn)
            if not unexplored_lead:
                print('No new leads')
                break
            fb_profile_link = unexplored_lead[0]
            lead = explore(conn, fb_profile_link)
            #print(lead)
            if lead is None:
                db_io.delete_from_unexplored(conn, [(fb_profile_link,)])
            else:
                leads.append(lead)
            leads.append(lead)
            n -= 1
    #SAVE CSV FILE
    #print(leads)
    if leads:
        lead_file_name = 'lead' + date_string + '.csv'
        lead_file = open(lead_file_name, 'w+')
        file_io.add_lead_to_csv_file(lead_file, leads)
        #close connections
        lead_file.close()
    conn.close()
    



    