import openpyxl
import datetime
import pathlib
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
import time


option = Options()
option.add_argument('--headless')
option.add_argument("--mute-audio")
def new_file():
    dt_now = datetime.datetime.now()
    dt_now = dt_now.strftime("%Y%m%d_%H%M%S")
    EXCEL_FILE_NAME = "YOUTUBE_SEARCH{}.xlsx".format(dt_now)
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "sheet1"
    wb.save(EXCEL_FILE_NAME)
    return


# target_URL = driver.current_url
# html = requests.get(target_URL)
# soup = BeautifulSoup(html.content,"html.parser")

def channel_search(channel_id):
    driver.get("https://www.youtube.com/channel/{}".format(channel_id))
    driver.find_element_by_xpath("//*[@id='tabsContent']/paper-tab[2]/div").click()
    movie_list_url = driver.current_url
    movie_list_url = movie_list_url + "?view=0&sort=da&flow=grid"
    driver.get(movie_list_url)
    movie_link = driver.find_element_by_xpath("//*[@id='thumbnail']").click()
    time.sleep(3)
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
    view = driver.find_element_by_xpath("//*[@id='count']/yt-view-count-renderer/span[1]").text
    date = driver.find_element_by_xpath("//*[@id='date']/yt-formatted-string").text
    return view, date

def file_READ(file_name):
    channel_list = []
    wb = openpyxl.load_workbook(file_name)
    ws = wb.worksheets[0]
    max_row = ws.max_row
    print(max_row)
    for i in range(max_row-1):
        channel_list.append(ws.cell(i+2,1).value)
    print(channel_list)
    return channel_list


def file_write(file_name,view_list,date_list):
    wb = openpyxl.load_workbook(file_name)
    ws = wb.worksheets[0]
    max_row = ws.max_row
    i = 2
    for v in view_list:
        cell = ws.cell(i,2)
        cell.value = v
        i += 1
    i = 2 
    for v in date_list:
        cell = ws.cell(i,3)
        cell.value = v
        i += 1
    wb.save(file_name)
    return


driver = webdriver.Chrome("c:\Program Files\JetBrains\PyCharm Community Edition 2019.1.1\\bin\webdriver\chromedriver.exe",chrome_options=option)
READ_FILE_NAME = "Channel_id_list.xlsx"
channel_list = file_READ(READ_FILE_NAME)
view_list = []
date_list = []

for v in channel_list:
    view, date = channel_search(v)
    view_list.append(view)
    date_list.append(date)
file_write(READ_FILE_NAME,view_list,date_list)
print(view_list)
print(date_list)
driver.close()