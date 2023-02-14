from bs4 import BeautifulSoup
import requests 
import lxml
import os

# url = "http://suninjuly.github.io/file_input.html"
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
# }

# site = requests.get(url, headers=headers)
# src = site.text
path = os.path.abspath(os.path.dirname(__file__))

# with open(os.path.join(path, "scr.html"), "w", encoding="UTF-8") as txt:
#     print(src, file=txt)

with open(path+"\\scr.html", "r", encoding="UTF-8") as file:
    scr = file.read()

soup = BeautifulSoup(scr, "lxml")
print(soup)
# print(*soup.cdata_list_attributes, sep="\n")



