import requests
import json
import datetime
from bs4 import BeautifulSoup
import re

class Menu:
    meals = []
    date = ""
    def __init__(self, date):
        self.date = date
 
class Meal:
    name = ""
    id = 0
    ingedients = []
    nutritionalValues = {}
    def __init__(self, name, id):
        self.name = name
        self.id = id
 
class Ingredient:
    name = ""
 
class Part:
    name = ""
    ingredients = []
 
def GetMenu(date):
    req = requests.get('https://webmenu.foodit.se/?r=20&m=2080&p=29&c=13833&w='
                       +RelativeWeek(date)+
                       '&v=Day&d='+str(date.weekday()))
    soup = BeautifulSoup(req.text, features="html.parser")
    menu = Menu(date)
   
    divs = soup.findAll("li", class_="li-menu")    
    for x in divs:
        menu.meals.append(Meal(x.find("div", class_="menu-text").text.strip(), int(re.sub("\D", "", x.attrs["id"]))))
    return menu
 
def GetDetails(meal):
    req = requests.get("https://webmenu.foodit.se/?r=20&m=2080&p=29&c=13833&v=Detail&rId="+str(meal.id))
    soup = BeautifulSoup(req.text, features="html.parser")
 
    all = soup.findAll("div", class_="italic")
    #print(all[0].text.strip())
    contents = '['+re.sub(r'(?<=\d),','.', all[0].text.strip()).replace('(',',[').replace(')',']').replace('. ',',')+']'
   
    contents = re.sub('([^\[\],\n]+)',r'"\1"', contents)
   
    nutritionList = re.sub(r'(?<=\d),', '.', all[1].text.strip()).split(', ')
    nutrition = {}
    for x in nutritionList:
        y = x.split(": ")
        nutrition[y[0]] = y[1]
 
    return contents, nutrition
 
 
def RelativeWeek(date):
    return str(int(date.strftime("%V"))-int(datetime.datetime.now().strftime("%V")))