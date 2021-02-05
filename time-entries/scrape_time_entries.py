import json
import requests
from autoscraper import AutoScraper
import http.cookiejar as cookielib
from requests.utils import add_dict_to_cookiejar

from ipdb import set_trace

url = "https://app.hellobonsai.com/time_entries"

jar = cookielib.CookieJar()

with open("cookies.json") as f:
    cookies_dict = json.load(f)

for cookie_dict in cookies_dict:
    add_dict_to_cookiejar(jar, cookie_dict)

s = requests.Session()
s.cookies = jar

cookies_dict = requests.utils.dict_from_cookiejar(s.cookies)

scraper = AutoScraper()

wanted_list = ["Unbilled"]


result = scraper.build(url, wanted_list, request_args={"cookies": s.cookies})

print(result)

set_trace()



# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
# wanted_list = ["What are metaclasses in Python?"]

# scraper = AutoScraper()
# result = scraper.build(url, wanted_list)
# print(result)
