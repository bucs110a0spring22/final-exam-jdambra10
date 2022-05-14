import requests
from datetime import date


class ACNH:
    def __init__(self):
        print("Welcome to ACNH Birthday Generator! Find out which characters share the same birthday!\n")
        choice = str(input("Would you like to use [today]'s date or your [birthday]?: \n"))
        if choice == "today":
          self.flag = 1
          today = date.today()
          self.tdDate = today.strftime("%B %d")
          day = int(today.strftime("%d"))
          if day == 1 or day == 21 or day == 31:
              self.tdDate += "st"
          elif day == 2 or day == 22:
              self.tdDate += "nd"
          elif day == 3 or day == 23:
              self.tdDate += "rd"
          elif day <= 20 or day <= 30:
              self.tdDate += "th"
        elif choice == "birthday":
          self.flag = 2
          self.bday = str(input("Enter your birthday (ex: August 17th): \n"))

    def sameBday(self):
        birthdayVillagers = []
        i = 1
        while i < 392:
            print(i)
            r = requests.get("https://acnhapi.com/v1/villagers/" + str(i))
            villager = r.json()
            enName = villager["name"]["name-USen"]
            birthday = villager["birthday-string"]
            if self.flag == 1:
              if birthday == self.tdDate:
                  birthdayVillagers.append(enName)
              i += 1
            elif self.flag == 2:
              if birthday == self.bday:
                  birthdayVillagers.append(enName)
              i += 1

        for i in range(0, len(birthdayVillagers)):
            print("Villagers who share a birthday!: " +
                  birthdayVillagers[i])