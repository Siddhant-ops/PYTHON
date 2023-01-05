print("\n================================================================================================\n")

import bs4, requests

result = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")

soup = bs4.BeautifulSoup(result.text, "lxml")

myclass = soup.select(".toctext")

print(myclass)

# now if we want to select the first span tag of .toctext

first_item = myclass[0]

print("\n==================================================\n")

print(type(first_item))

print("\n==================================================\n")

print(first_item)

print("\n==================================================\n")

print(first_item.text)

print("\n==================================================\n")

# now if you want to select all the texts in .toctext

for item in myclass:
    print(item.text)
