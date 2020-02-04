from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://anglish.fandom.com/wiki/English_Wordbook/A");
content = driver.page_source;
soup = BeautifulSoup(content, 'html.parser')
tables = soup.findAll("table");
for table in tables:
	if table.findParent("table") is None:
		table_body = table.find('tbody')

rows = table_body.find_all('tr')
rowtds = [row.findAll('td') for row in rows]
anglish_dictionary = {};

#word_columns = [rowtds.findAll('td') for rowtds_single in rowtds]

for word_column in rowtds[2:]:
	english_def = word_column[0].text.strip();
	class_type = word_column[1].text.strip();
	attested = word_column[2].text.strip();
	unattested = word_column[3].text.strip();
	print({english_def:{"class":class_type, "attested":attested, "unattested":unattested}})
	break;
	#anglish_dictionary[englishdef:{"class":class_type, "attested":attested, "unattested":unattested}})

#print(anglish_dictionary[6])

