from lxml import html
import requests

price = ['']
name = ['']
links = ['']

def getData():
  with open('database.txt','r') as file:
    for line in file:
      page = requests.get(line)
      code = html.fromstring(page.content)
      price.append(code.xpath('/html/body/main/div[4]/section[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/dl/dd[6]/text()'))
      name.append(code.xpath('/html/body/main/div[3]/div[1]/h1/text()'))
    string = '**Kartenname -------- Kartenpreis**\n'
    for i in range(0,len(name)):
      string = string + str(name[i]) +' -> '+ str(price[i]) +'\n'
  return string

def insertData(link):
  with open('database.txt','w') as file:
    file.write(link)