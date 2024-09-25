
# ------- Imports ------- #

import os
import random
from time import *

clear = lambda: os.system('cls')

# ------- Subprograms ------- #

def choice():
    print("-"*20)
    cont = 0
    while cont > 4 or cont < 1:
        cont = int(input("Do you wanna\n1.Play\n2.Wipe Data\n3.Check History\n4.Exit\nChoice: "))
    if cont == 1:
      cont = 0
      while cont > 2 or cont < 1:
        cont = int(input("Do you wanna do:\n1.Minimums\n2.Maximums\nChoice: "))
      if cont == 1:
         return "PLAYL"
      else:
         return "PLAYH"
    elif cont == 2:
      return "WIPE"
    elif cont == 3:
       return "HISTORY"
    else:
      return "END"

def saveResults(a, b, c, d, e, low):
    r = open("results.txt","a")
    r.write("\n")
    r.write("-"*15)
    r.write("\nCount: "+str(a))
    r.write("\nTries: "+str(b))
    if low:
        r.write("\nMinimum Count: "+str(c))
        r.write("\nRandomiser: 1/"+str(d))
        r.write("\nChance: "+str(e)+"%")
        r.write("\nType: Lower Bound")
    else:
       r.write("\nMaximum Count: "+str(c))
       r.write("\nRandomiser: 1/"+str(d))
       r.write("\nChance: "+str(e)+"%")
       r.write("\nType : Upper Bound")
       
    r.close()  

def clearResults():
   r = open("results.txt","w")
   r.write("")
   r.close()

def showHistory():
   r = open("results.txt","r")
   count = 0
   for line in r:
      if line[0] == "-":
          count += 1
      print(line)
   print("-"*20)
   print("Total Results in History: "+str(count))

def rollL(min, uc):
  lc = 0
  while True:
    count = 0
    lc += 1
    while True:
      count += 1
      a=random.randint(1, uc)
      if a == uc:
        break
    print("-"*8)
    print("Tries: "+str(count))
    print("Line: "+str(lc))
    if count >= min:
      print("-"*8)
      print(str(count)+" >= "+str(min))
      chance = (((1/uc)/count)/lc) * 100
      break
  return count, lc, min, uc, chance

def rollH(max, uc):
  lc = 0
  while True:
    count = 0
    lc += 1
    while True:
      count += 1
      a=random.randint(1, uc)
      if a == uc:
        break
    print("-"*8)
    print("Tries: "+str(count))
    print("Line: "+str(lc))
    if count <= max:
      print("-"*8)
      print(str(count)+" <= "+str(max))
      chance = (((1/uc)/count)/lc) * 100
      break
  return count, lc, max, uc, chance

# ------- Main Program ------- #

while True:
    playing = False
    selection = choice()
    if selection == "PLAYL":
        print("-"*20)
        min = int(input("Enter minimum count for win: "))
        uc = int(input("Randomiser will be 1 in: "))
        a, b, c, d, e = rollL(min, uc)
        saveResults(a,b,c,d,e,True)
        sleep(1)
        input("Press ENTER to continue.")
        clear()
    elif selection == "PLAYH":
        print("-"*20)
        max = int(input("Enter maximum count for win: "))
        uc = int(input("Randomiser will be 1 in: "))
        a, b, c, d, e = rollH(max, uc)
        saveResults(a,b,c,d,e,False)
        sleep(1)
        input("Press ENTER to continue.")
        clear()
    elif selection == "WIPE":
       clearResults()
       sleep(1)
       clear()
    elif selection == "HISTORY":
       showHistory()
       sleep(1)
       input("Press ENTER to continue.")
       clear()
    else:
       break