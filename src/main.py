import utility
import db_io
from lead import Lead

start_url = "https://www.facebook.com/petercatrecordingco/"

conn = db_io.open_connection()
db_io.create_table_leads(conn)
db_io.create_table_unexplored(conn)

lead = utility.get_leads(utility.get_fb_slug(start_url))
db_io.add_leads_to_db(conn, lead)
related_pages = utility.get_related_pages(start_url)
for page in related_pages:
    db_io.add_to_unexplored_leads(conn, utility.get_fb_slug(page))



