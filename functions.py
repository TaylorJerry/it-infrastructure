import time, sys

ingredients = []

## Functions for useful helpers and animations

# Text output animation
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  print()

# TODO: Counter Function for time
def timer(task, duration):
    for remaining in range(duration, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{task} dauert noch {count:2d} Minuten...".format(task=task, count=remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\nFertig!\n")

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

def preparation_check(user_input):
    if user_input == 'w':
        pass

    else:
        typingPrint("Falsche Eingabe, versuch es noch einmal (w):")
        new_input = input().lower()
        preparation_check(new_input) 