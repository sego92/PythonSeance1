from lxml import html
import requests

pageWeb = requests.get('https://twitter.com/EmmanuelMacron')

tree = html.fromstring(pageWeb.content)

followerCount = tree.xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span[1]')

print (followerCount)

