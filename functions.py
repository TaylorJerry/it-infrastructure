import time, sys

ingredients = []

def print_menu():
  #print("Menü")
  #print("(E)klärung   (S)tarten   ()")
  return "Menü\n(S)tarten   (E)rklärung   (...)"

# Text output animation
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)
  print()

def ingredients_check(ingredient, user_input):
  if user_input == 'j':
    pass

  elif user_input == 'n':
    ingredients.append(ingredient)

  else:
    typingPrint("Falsche Eingabe, versuch es noch einmal (j) (n):")
    new_input = input().lower()
    ingredients_check(ingredient, new_input)


# TODO: Counter Function for time