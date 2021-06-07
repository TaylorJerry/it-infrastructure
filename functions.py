import time, sys
import math

ingredients = []

## Functions for useful helpers and animations

# Text output animation
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  print()

def typingPrintBold(text):
  for character in text:
    sys.stdout.write("\033[1m" + character + "\033[0m")
    sys.stdout.flush()
    time.sleep(0.01)
  print()



def timer(task, duration):
    bar = [
    " [=     ]",
    " [==    ]",
    " [ ==   ]",
    " [  ==  ]",
    " [   == ]",
    " [    ==]",
    " [     =]",
    ]
    x = 0 

    for remaining in range(duration*5, 0, -1):
      count = math.ceil(remaining/5)
      sys.stdout.write("\r")
      print(f"{bar[x % len(bar)]} {task} dauert noch {count:2d} Minuten.", end="\r")
      sys.stdout.flush()
      x += 1
      time.sleep(0.2)
    print("\nFertig!\n")




def loading_animation(wait_time):
  bar = [
    " [=     ]",
    " [==    ]",
    " [ ==   ]",
    " [  ==  ]",
    " [   == ]",
    " [    ==]",
    " [     =]",
  ]
  i = 0

  for x in range(wait_time, 0, -1):
      print(bar[i % len(bar)], end="\r")
      time.sleep(0.3)
      i += 1

## Functions for validating user input


def ingredients_check(ingredient, user_input):
  if user_input == 'j':
    pass

  elif user_input == 'n':
    ingredients.append(ingredient)

  #elif user_input == 'c':
  #  cb.menu()

  else:
    typingPrint("Falsche Eingabe, versuch es noch einmal (j) (n):")
    new_input = input().lower()
    ingredients_check(ingredient, new_input)



        