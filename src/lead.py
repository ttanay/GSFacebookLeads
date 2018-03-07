class Lead:

    fb_url = 'https://www.facebook.com/{}'

    def __init__(self, fb_slug, emails, booking_agent, contact_address, phone, category):
        self.fb_slug = fb_slug
        self.emails = emails
        self.booking_agent = booking_agent
        self.contact_address = contact_address
        self.phone = phone
        self.category = category
        return
    
    def get_fb_profile_link(self):
        return fb_url.format(self.fb_slug)

    def get_lead_tuple(self):
        data = (self.fb_slug, self.emails, self.booking_agent, self.contact_address, self.phone, self.category)
        return data