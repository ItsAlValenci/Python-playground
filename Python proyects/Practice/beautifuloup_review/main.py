from bs4 import BeautifulSoup
#import lxml 

web_path = "/Users/springfox/DEV/Personal/python_playground/Python proyects/beautiful_Soup/website.html"

with open (web_path, "r") as file:
    content = file.read()


soup = BeautifulSoup(content, "html.parser")

print(soup.find_all(name="p")) #returns a list of all <p> tags

for tag in soup.find_all(name="a"):
    print(tag.getText()) #prints the text inside each tag named <a>

for tag in soup.find_all(name="a"):
    print(tag.get("href")) #prints the link inside each <a> tag

heading = soup.find(name="h1", id="name") #finds the first <h1> tag with id="name"
print(heading)

heading = soup.find(name="h3", class_="heading") #finds the first <h3> tag with CLASS="heading"
print(heading)

company_url = soup.select_one(selector="p a") #selects the first <a> tag inside a <p> tag
print(company_url)

headings= soup.select(selector=".heading") #selects all elements with class="heading"
print(headings)


