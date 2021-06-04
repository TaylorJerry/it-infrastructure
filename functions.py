import time, sys


def print_menu():
  #print("Menü")
  #print("(E)klärung   (S)tarten   ()")
  return "Menü\n(E)klärung   (S)tarten (...)"

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)
  print()