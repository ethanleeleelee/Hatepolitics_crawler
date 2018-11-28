#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
f = open(os.getcwd()+ "/data.txt",'w',encoding="utf8")

driver = webdriver.Chrome(os.getcwd() + "/chromedriver",chrome_options=options)

date = []
push = []
count = 0
for i in range(2000,4253):
    driver.get("https://www.ptt.cc/bbs/HatePolitics/index" + str(i) + ".html")
    time.sleep(0.5)
    sourcecode = BeautifulSoup(driver.page_source, "html.parser")
    sections = sourcecode.find_all("div","r-ent")
    for section in sections:
        sourcecode2 = BeautifulSoup(str(section), "html.parser")
        dates = sourcecode2.find_all("div","date")[0].text
        date.append(dates)
        pushs = sourcecode2.find_all("div","nrec")[0].text
        if pushs.find("X") == 0:
            push.append(-1)
            count += 1
        elif pushs.find("爆") == 0:
            push.append(99)
            count += 1
        elif pushs == '':
            push.append(0)
            count += 1
        else:
            push.append(int(pushs))
            count += 1
tpush = 0
data = []
day = []
#print(count)
#print(push)

date.append('end')
push.append(0)
#print(date)
for i in range(0, count):
    if date[i] == date[i+1]:
        tpush += push[i]
    else:
        tpush += push[i+1]
        data.append(tpush)
        day.append(date[i])
        tpush = 0
print(data)
print(day)

from bokeh.io import output_notebook, push_notebook, show
from bokeh.plotting import figure, output_file, show

p = figure(x_range = day, plot_height = 250, title = "HatePolitics")
p.vbar(x = day, width = 0.5, top = data, color = "navy")
p.y_range.start = 0
#p.y_range.end = 1000

show(p)
output_notebook()


# In[ ]:




