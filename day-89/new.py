import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/blogpost/how-to-find-python-installation-path"
response = requests.get(url)

# print(response.text)


soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

for heading in soup.find_all("h3"):
    print(heading.text)
