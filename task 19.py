#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Title of the webpage


# In[7]:


from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
import time
chrome_service = ChromeService(r"C:\Users\Nancy\OneDrive - ZF Friedrichshafen AG\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.saucedemo.com/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
title = driver.title
print(f'title is:{title}')
driver.quit()


# In[ ]:


# URL of current page


# In[10]:


from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
import time
chrome_service = ChromeService(r"C:\Users\Nancy\OneDrive - ZF Friedrichshafen AG\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.saucedemo.com/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
current_url=driver.current_url
print(f'url is:{current_url}')
driver.quit()


# In[ ]:


#Extracting the entire content of the page


# In[12]:


from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
import time
chrome_service = ChromeService(r"C:\Users\Nancy\OneDrive - ZF Friedrichshafen AG\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.saucedemo.com/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
webpage_content = driver.page_source
with open("webpage_content.txt", "w", encoding="utf-8") as file:file.write(webpage_content)


# In[ ]:




