print("\n================================================================================================\n")

# here we are importing requests and bs4 libraries
import bs4, requests

# with requests.get method we select the website we want scrape from
result = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(result.text, "lxml")

myImage = soup.select(".thumbimage")

for item in myImage:
    print(item)

print("\n==================================================\n")

computer = soup.select(".thumbimage")[0]

print(computer["src"])

imageLink = requests.get("http://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg")

print(imageLink.content)

# with open("computer.jpg", "wb") as f:
#     f.write(imageLink.content)
#     f.close()
