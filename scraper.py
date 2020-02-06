import json
from selenium import webdriver
from bs4 import BeautifulSoup
from string import ascii_uppercase
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

anglish_dictionary = {};
for letter in ascii_uppercase:
	driver.get(f"https://anglish.fandom.com/wiki/English_Wordbook/{letter}");
	content = driver.page_source;
	soup = BeautifulSoup(content, 'html.parser')
	tables = soup.findAll("table");
	for table in tables:
		if table.findParent("table") is None:
			table_body = table.find('tbody')

	rows = table_body.find_all('tr')
	rowtds = [row.findAll('td') for row in rows]
	del rowtds[:2]	
	def remove_bad_rows(row):
		return len(row) > 3;	
	rowtds = list(filter(remove_bad_rows, rowtds))
	for i,row in enumerate(rowtds[:]):
		if len(row) < 4:
			previous_row_english = (rowtds[i-1])
			print("less than 4")
			rowtds[i].insert(0, previous_row_english)
			print(rowtds[i])

	for word_column in rowtds:
		english_def = word_column[0].text.strip();
		class_type = word_column[1].text.strip();
		attested = word_column[2].text.strip();
		unattested = word_column[3].text.strip();
		# print({english_def:{"class":class_type, "attested":attested, "unattested":unattested}})
		anglish_dictionary.update({english_def:{"class":class_type, "attested":attested, "unattested":unattested}})


with open("file.txt", "w") as f:
     json.dump(anglish_dictionary, f, indent=4)
