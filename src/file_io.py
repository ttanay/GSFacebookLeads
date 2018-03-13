import csv
import datetime

field_names = ['name', 'category', 'contact_address', 'phone', 'booking_agent', 'emails', 'fb_profile_link']

def add_lead_to_file(lead_file,lead):
    #print(lead['category'])
    lead_str = "name: {name}| fb_profile_link: {fb_profile_link}| emails: {emails}| booking_agent: {booking_agent}| contact_address: {contact_address}| phone: {phone}| category: {category}\n"
    lead_str = lead_str.format(name=lead['name'], fb_profile_link=lead['fb_profile_link'], emails=lead['emails'], booking_agent=lead['booking_agent'], contact_address=lead['contact_address'], phone=lead['phone'], category=lead['category'])
    lead_file.write(lead_str)
    return

def add_lead_to_csv_file(csv_file, leads):
    print(leads)
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    for lead in leads:
        if lead:
            writer.writerow(lead)
    return

'''def dump_all_leads(leads):
    dt = datetime.datetime.now()
    date_string = dt.strftime("%d_%b_%yT%H_%M")
    file_name = 'lead_dump' + date_string + '.csv'
    with open(file_name, 'a+') as csv_file:
        add_lead_to_csv_file(csv_file, leads)
    return'''

'''def dump_all_unexplored_leads(uneplored_leads):
    dt = datetime.datetime.now()
    date_string = dt.strftime("%d_%b_%yT%H_%M")
    file_name = 'unexplored_lead_dump' + date_string + '.csv'
    with open(file_name, 'a+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(uneplored_leads)
    return'''
    