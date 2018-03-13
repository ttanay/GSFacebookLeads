import csv

field_names = ['name', 'fb_profile_link', 'emails', 'booking_agent', 'contact_address', 'phone', 'category']

def add_lead_to_file(lead_file,lead):
    #print(lead['category'])
    lead_str = "name: {name}| fb_profile_link: {fb_profile_link}| emails: {emails}| booking_agent: {booking_agent}| contact_address: {contact_address}| phone: {phone}| category: {category}\n"
    lead_str = lead_str.format(name=lead['name'], fb_profile_link=lead['fb_profile_link'], emails=lead['emails'], booking_agent=lead['booking_agent'], contact_address=lead['contact_address'], phone=lead['phone'], category=lead['category'])
    lead_file.write(lead_str)
    return

def add_lead_to_csv_file(csv_file, leads):
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    for lead in leads:
        writer.writerow(lead)
    return