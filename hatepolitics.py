#!/usr/bin/env python
# coding: utf-8

# In[7]:


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

data = []
index = []
count = 0
for i in range(4000,4014):
    driver.get("https://www.ptt.cc/bbs/HatePolitics/index" + str(i) + ".html")
    time.sleep(0.5)
    sourcecode = BeautifulSoup(driver.page_source, "html.parser")
    sections = sourcecode.find_all("div","r-ent")
    for section in sections:
        sourcecode2 = BeautifulSoup(str(section), "html.parser")
        titles = sourcecode2.find_all("div","title")[0].text
        if titles.find("公告") == -1:
            push = sourcecode2.find_all("div","nrec")[0].text
            if push.find("X") == 0:
                data.append(-1)
                count += 1
                index.append(count)
            elif push.find("爆") == 0:
                data.append(99)
                count += 1
                index.append(count)
            elif push == '':
                data.append(0)
                count += 1
                index.append(count)
            else:
                data.append(push)
                count += 1
                index.append(count)
print(data)
print(index)

from bokeh.io import output_notebook, push_notebook, show
from bokeh.plotting import figure, output_file, show

p = figure(plot_height = 250, title = "HatePolitics")
p.line(index, data, line_width = 2, color = "navy")
p.y_range.start = -5
show(p)
output_notebook()


# In[ ]:




