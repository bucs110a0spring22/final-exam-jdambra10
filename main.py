import DnD5e
import ACNH
import time

def main():
  AC = ACNH.ACNH()
  '''
  I have AC.sameBday commented out by default. It does work, HOWEVER, it takes a very long time to go through all 391 villagers and prints each number so you know how far along it is. I would like to reduce the time it takes to run the loop but I couldn't figure out how so run if you have the time. Sorry!
  '''
  #AC.sameBday()
  time.sleep(5)
  print("\n\n")
  DnD = DnD5e.DnD()
  DnD.generateCharacter()
    


if __name__ == '__main__':
    main()
