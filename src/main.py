import utility

start_url = "https://www.facebook.com/petercatrecordingco/"

related_pages = utility.get_related_pages(start_url)
for page in related_pages:
    contact_details = utility.get_contact_details(utility.get_fb_slug(page))
    print(contact_details)
