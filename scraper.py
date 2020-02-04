from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://anglish.fandom.com/wiki/English_Wordbook/A");
content = driver.page_source;
soup = BeautifulSoup(content, 'html.parser')
tables = soup.findAll("table");
for table in tables:
	if table.findParent("table") is None:
		print(str(table))
