from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json
import time
from access import access_token

graph_call = 'https://graph.facebook.com/{}?access_token=' + access_token + '&fields=name,emails,booking_agent,contact_address,phone,category'
'''accepted_page_types = {
    "Artist",
    "Band",
    "Musician/Band",
    "Musician",
    "Orchestra",
    "DJ",
    "Music Production Studio",
    "Restaurant",
    "Bar",
    "Hotel"
}'''

def get_fb_slug(fb_profile_link):
    fb_profile_list = fb_profile_link.split('/')
    #print(fb_profile_list)
    return fb_profile_list[3]

def get_related_pages(fb_profile_link):
    related_pages = []
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(fb_profile_link)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_4-lu"))
        )
        elements = driver.find_elements_by_class_name('_4-lu')
        for a in elements:
            related_pages.append(a.get_property('href'))
            #print(get_fb_slug(a.get_property('href')))
       # print(element.text)
    except Exception:
        pass
    finally:
        driver.quit()
    return related_pages

def get_leads(fb_profile_link):
    # ADD LOCATION AND HOMETOWN
    fb_slug = get_fb_slug(fb_profile_link)
    #print(fb_slug)
    graph_url = graph_call.format(fb_slug)
    r = requests.get(graph_url)
    data = json.loads(r.text)
    #print('data: {}'.format(data))
    try:
        name = data['name']
    except Exception as e:
        name = None
        #print(e)
    try:
        emails = data['emails']
    except Exception as e:
        emails = None
        #print(e)
    try:
        booking_agent = data['booking_agent']
    except Exception as e:
        booking_agent = None
        #print(e)
    try:
        contact_address = data['contact_address']
    except Exception as e:
        contact_address = None
        #print(e)
    try:
        phone = data['phone']
    except Exception as e:
        phone = None
        #print(e)
    try:
        category = data['category']
    except Exception as e:
        category = None        
        #print(e)
    lead = {
        'name': name,
        'emails': emails,
        'booking_agent': booking_agent,
        'contact_address': contact_address,
        'phone': phone,
        'category': category,
    }
    return lead

def clean_urls(list_of_urls):
    fb_link = "https://www.facebook.com/{}"
    fb_list = []
    for url in list_of_urls:
        slug = get_fb_slug(url)
        url = fb_link.format(slug)
        fb_list.append((url,))
    return fb_list
