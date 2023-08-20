import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.ziprecruiter.com/jobs-search?'
_search = 'support'
_location = '48187'
_radius = ''
_days = ''

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

dr = webdriver.Chrome(options=options)
dr.get(f"{url}search={_search}&location={_location}&radius={_radius}&days={_days}")

bs = BeautifulSoup(dr.page_source, "html.parser")

dr.close()

companies = bs.find_all("a", {"class":"company_name"})
jobs = bs.find_all("h2", {"class":"title"})
perks = bs.find_all("ul", {"class":"perk_items"})
company_list = []
job_list = []
pay_list = []

for job in jobs:
    job_list.append(job.text.strip())

for company in companies:
    company_list.append(company.text.strip())

for perk in perks:
    pay = perk.find("li", {"class":"perk_item"})
    pay_list.append(pay.text.strip())

jobs_dict = zip(company_list, job_list)
# for k, v in jobs_dict:
#     print(f"Company: {k}\nRole: {v}\n")


class Positions:

        def __init__(self, company, job, perks):
             self.company = company
             self.job = job
             self.perks = perks

job1 = Positions(company_list[0], job_list[0], pay_list[0])

print(job1.company)