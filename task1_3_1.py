#import requests as req
from cgitb import text
from encodings.utf_8_sig import encode
from time import sleep, time
from tkinter import N
from bs4 import BeautifulSoup
import json
from requests_tor import RequestsTor
import re
req =  RequestsTor()

data = {
    
    "data":[]
    }
#tag = soup.find(attrs={"data-qa":"data-qa="serp-item__title"})
for page in range(0,5):
    url = f"https://hh.ru/search/vacancy?area=113&clusters=true&enable_snippets=true&industry=7.540&label=with_address&ored_clusters=true&professional_role=96&search_field=name&search_field=description&text=Python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&search_period=7&hhtmFrom=vacancy_search_list&page={page}"
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all(attrs={"data-qa":"serp-item__title"})
    for iter in tags:
        sleep(2)
              
        url_sal = iter.attrs["href"]
        resp_sal = req.get(url_sal)
        soup_sal = BeautifulSoup(resp_sal.text, "lxml")
        tags_sal = soup_sal.find(class_=re.compile("vacancy")).find(class_="bloko-header-section-2 bloko-header-section-2_lite")
        url_exp = iter.attrs["href"]
        resp_exp = req.get(url_exp)
        soup_exp = BeautifulSoup(resp_exp.text, "lxml")
        tags_exp = soup_exp.find(attrs={"data-qa":"vacancy-experience"})
        url_reg = iter.attrs["href"]
        resp_reg = req.get(url_reg)
        soup_reg = BeautifulSoup(resp_reg.text, "lxml")
        tags_reg = soup_reg.find(attrs={"data-qa":"vacancy-company"}).find(attrs={"data-qa":re.compile("vacancy-view-")})
            
        data["data"].append({"Title":iter.text, 
                                "Work expiriens":tags_exp.text, 
                                "Salary":tags_sal.text,
                                "Region":tags_reg.text})
        with open("pars.json","w", encoding='utf8') as file:
                json.dump(data,file, ensure_ascii=False)
            #print(data)
