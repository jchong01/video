from BeautifulSoup import BeautifulSoup
import urllib

pageFile = urllib.urlopen("http://www.mynova.villanova.edu")
pageHtml = pageFile.read()
pageFile.close()

soup = BeautifulSoup("".join(pageHtml))

print(soup.prettify())
