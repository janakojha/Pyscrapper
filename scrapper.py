import requests
from bs4 import BeautifulSoup
def scrape_python_code(url):
  response = requests.get(url)
  html = response.text
  soup = BeautifulSoup(html, "html.parser")
  code_element = soup.find("div", class_="code")
  code = code_element.text
  return code
if __name__ == "__main__":
  url = input("Enter the URL of the Python code to scrape: ")
  code = scrape_python_code(url)
  print(code)