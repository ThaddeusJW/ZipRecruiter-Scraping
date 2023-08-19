import requests
from bs4 import BeautifulSoup
from selenium import webdriver


url = 'https://www.ziprecruiter.com/jobs-search?'
headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

_search = 'support'
_location = '48187'
_radius = ''
_days = ''


dr = webdriver.Chrome()
dr.get(f"{url}search={_search}&location={_location}&radius={_radius}&days={_days}")
bs = BeautifulSoup(dr.page_source, "html.parser")

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
for k, v in jobs_dict:
    print(f"Company: {k}\nRole: {v}\n")


class Positions:

        def __init__(self, company, job, perks):
             self.company = company
             self.job = job
             self.perks = perks

job1 = Positions(company_list[0], job_list[0], pay_list[0])

print(job1.company)