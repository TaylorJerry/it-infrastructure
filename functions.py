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
    time.sleep(0.01)
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
def timer(task):
    typingPrint(f"{task} dauert noch:")
    for remaining in range(10, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} Minuten".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rFertig!\n")