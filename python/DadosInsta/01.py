import selenium
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome(executable_path=r"C:\Users\vbernardino-ieg\Downloads\chromedriver_win32\chromedriver.exe")

driver.get('https://www.instagram.com/kimkardashian/?hl=en')

Posts = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/ul/li[1]/a/span').text
Followers = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/ul/li[2]/a/span').text
Following = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/ul/li[3]/a/span').text


print(Posts)
print(Followers)
print(Following)

data1 = {'Posts':[], 'Followers':[], 'Following':[],}
fulldf = pd.DataFrame(data1)

row = [Posts, Followers, Following]
fulldf.loc[len(fulldf)] = row