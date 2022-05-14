import requests
import random


class DnD:
    def __init__(self):
      self.classFlag = 0
      self.raceFlag = 0
      self.bgFlag = 0
      print("Welcome to the DnD character generator!\n")
      yORn = str(input("Do you have a specific class/race/background in mind? [y] or [n]\n"))
      if yORn == "y":
        choice = str(input("Pick either [class], [race], or [background]: \n"))
        if choice == "class":
          self.classFlag = 1
          self.classChoice = str(input("Pick 1:\n[barbarian] [bard] [cleric]\n[druid] [fighter] [monk]\n[paladin] [ranger] [rogue]\n[sorcerer] [warlock] [wizard]\n"))
        elif choice == "race":
          self.raceFlag = 1
          self.raceChoice = str(input("Pick 1:\n[dragonborn] [dwarf] [elf]\n[gnome] [half-elf] [half-orc]\n[halfling] [human] [tiefling]\n"))
        elif choice == "background":
          self.bgFlag = 1
          self.bgChoice = str(input("Pick 1:\n[acolyte] [charlatan] [criminal]\n[entertainer] [folk hero] [gladiator]]\n[guild artisan] [hermit] [knight]\n[noble] [outlander] [pirate]\n[sage] [sailor] [soldier] [urchin]"))

      self.classList = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"]
      self.raceList = ["dragonborn", "dwarf", "elf", "gnome", "half-elf", "half-orc", "halfling", "human", "tiefling"]
      self.bgList = ["acolyte", "charlatan", "criminal", "entertainer", "folk-hero", "gladiator", "guild-artisan", "hermit", "knight", "noble", "outlander", "pirate", "sage", "sailor", "soldier", "urchin"]

      
    def generateClass(self):
      if self.classFlag == 1:
        r = requests.get("https://www.dnd5eapi.co/api/classes/"+str(self.classChoice))
        x = r.json()
        randomClass = x["name"]
        return randomClass
      else:
        rng = random.randint(0,len(self.classList))
        randomClass = self.classList[rng]
        r = requests.get("https://www.dnd5eapi.co/api/classes/"+str(randomClass))
        x = r.json()
        randomClass = x["name"]
        return randomClass

    def generateRace(self):
      if self.raceFlag == 1:
        r = requests.get("https://www.dnd5eapi.co/api/races/"+str(self.raceChoice))
        x = r.json()
        randomRace = x["name"]
        return randomRace
      else:
        rng = random.randint(0,len(self.raceList))
        randomRace = self.raceList[rng]
        r = requests.get("https://www.dnd5eapi.co/api/races/"+str(randomRace))
        x = r.json()
        randomRace = x["name"]
        return randomRace

    def generateBg(self): #unfortunately, the api only has acolyte for backgrounds so I just added all of the ones in the Players Handbook to a list and choice from there
      if self.bgFlag == 1:
        randomBg = self.bgChoice.capitalize()
        return randomBg
      else:
        rng = random.randint(0,len(self.bgList))
        randomBg = self.bgList[rng]
        randomBg = randomBg.capitalize()
        return randomBg

    def generateCharacter(self):
      rngClass = self.generateClass()
      rngRace = self.generateRace()
      rngBg = self.generateBg()
      print("Your random character is a " + rngRace + " " + rngClass + " with a(n) " + rngBg + " background!")
      