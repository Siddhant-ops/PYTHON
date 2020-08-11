print("================================================================================================")

import requests, bs4

# we are just gonna grab a title of a website which is present at the tab

# requests.get method will get the source code of the website

result = requests.get("http://example.com/")

print(type(result))

print("==================================================")

# this will print all the code

print(result.text)

print("==================================================")

# beautifulSoup will take all that code and make it a lmxl formatted code

soup = bs4.BeautifulSoup(result.text, "lxml")

print(soup)

print("==================================================")

mytitle = soup.select("title")

# it prints the output in list

print(mytitle)

print("==================================================")

print(soup.select("p"))

print("==================================================")

print(soup.select("h1"))

print('==================================================')

print(soup.select("p")[0])

print("==================================================")

# getText() will get the text of that tag

print(soup.select("p")[0].getText())

print('==================================================')

site_paragraphs = soup.select("p")

print(type(site_paragraphs[0]))