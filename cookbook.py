#from functions import print_menu
#import typing_extensions
import functions as fc

# TODO: Das mit dem current_step funktioniert irgendwie noch nicht, wir sollten das außerhalb der Funktion deklarieren.
current_step = "start"

print(r"""\

   _____      _                                    _   _ _     _           
  / ____|    | |                                  (_) (_) |   | |          
 | (___   ___| |____      ____ _ _ __ ______      ____ _| | __| | ___ _ __ 
  \___ \ / __| '_ \ \ /\ / / _` | '__|_  /\ \ /\ / / _` | |/ _` |/ _ \ '__|
  ____) | (__| | | \ V  V / (_| | |   / /  \ V  V / (_| | | (_| |  __/ |   
 |_____/ \___|_| |_|\_/\_/ \__,_|_|  /___| _\_/\_/ \__,_|_|\__,_|\___|_|   
            | |/ (_)             | |   | |           | |                              
            | ' / _ _ __ ___  ___| |__ | |_ ___  _ __| |_ ___                         
            |  < | | '__/ __|/ __| '_ \| __/ _ \| '__| __/ _ \                        
            | . \| | |  \__ \ (__| | | | || (_) | |  | ||  __/                        
            |_|\_\_|_|  |___/\___|_| |_|\__\___/|_|   \__\___| 
               .,a@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@a,.                       
            ,a@@@@@@@@@@@@@@@@@@@@@.@@@@@@@@@@@@@@@@@@@@@@@@a, 
            a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a 
            ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@'; 
            ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@; 
            ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@; 
            ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@; 
            ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;; 
            ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;; 
            ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@a; 
        ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%, 
    .%%%%%%;;;;;;;a@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%, 
    .%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%, 
    %%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%% 
    %%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%% 
    `%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%' 
      `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%' 
          `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'                                                                           
                                                                           

""")


def start():
  #current_step = "start"
  fc.typingPrint("Hallo, lass uns eine Schwarzwälder Kirschtorte backen!\nWie ist dein Name?")
  input_name = input()
  fc.typingPrint(f"Wilkommen {input_name}!")
start()

current_step = "menu"
def menu():
  fc.typingPrint("Menü\n(S)tarten   (Ü)bersicht   (E)rklärung   (F)ortsetzen")
  menu_selection = input().lower()

  if menu_selection == 'ü':
      text = '''
            Arbeitszeit: 60 min
            Backen: 20 min
            Kühlen: 45 min
            Schwierigkeit: Mittel
            Link zum online Rezept: https://www.einfachbacken.de/rezepte/schwarzwaelder-kirschtorte-das-klassische-rezept
            '''
                #Schwarzwälder Kirschtorte gehört einfach zu den beliebtesten Klassiker-Rezepten.
                #Wir haben ein ganz einfaches und gelingsicheres Rezept für den Klassiker entwickelt,
                #mit dem auch du die perfekte Schwarzwälder Kirschtorte zaubern kannst.
      print(text)
      menu()
  
  elif menu_selection == 'e':
      text = '''
            - Die Klammern geben an, welchen Buchstaben du eingeben musst.
            - Die Eingaben die du machst, immer mit "Enter" bestätigen.
            - Falls du etwas falsches eingibst, wird deine Eingabe abgefangen und du kannst es noch einmal versuchen. 
             '''
      print(text)
      menu()

  elif menu_selection == 's':
    fc.typingPrint("Wir starten mit der Zutatenliste für den Biscuitteig!")

  elif menu_selection == 'f':
    fc.typingPrint("Letzten Stand laden")
    fc.loading_animation(7)
    if current_step == "start":
      start()
    elif current_step == "menu":
      menu()
    elif current_step == "ingredients_list":
      ingredients_list()
    elif current_step == "shopping":
      shopping()
    elif current_step == "preparation":
      preparation

  else: 
    fc.typingPrint("Falsche Eingabe, versuch es noch einmal")
    menu()

menu()


def eggs():
  fc.typingPrint("Hast du 6 Eier? (j) (n)")
  eggs = input().lower()
  fc.ingredients_check("Eier", eggs)
  
def sugar():
  fc.typingPrint("Hast du 250g Zucker? (j) (n)")
  sugar = input().lower()
  fc.ingredients_check("Zucker", sugar)

def flour():
  fc.typingPrint("Hast du 200g Mehl? (j) (n)")
  flour = input().lower()
  fc.ingredients_check("Mehl", flour)

def food_starch():
  fc.typingPrint("Hast du 50g Speisestärke? (j) (n)")
  food_starch = input().lower()
  fc.ingredients_check("Speisestärke", food_starch)

def cocoa():
  fc.typingPrint("Hast du 50g Kakaopulver? (j) (n)")
  cocoa = input().lower()
  fc.ingredients_check("Kakaopulver", cocoa)

def baking_powder():
  fc.typingPrint("Hast du Backpulver? (j) (n)")
  baking_powder = input().lower()
  fc.ingredients_check("Backpulver", baking_powder)

def cherries():
  fc.typingPrint("Hast du 350g Schattenmorellen? (j) (n)")
  cherries = input().lower()
  fc.ingredients_check("Schattenmorellen", cherries)

def cream():
  fc.typingPrint("Hast du 1l Sahne? (j) (n)")
  cream = input().lower()
  fc.ingredients_check("Sahne", cream)

def cream_stiff():
  fc.typingPrint("Hast du 5 Packungen Sahnesteif? (j) (n)")
  cream_stiff = input().lower()
  fc.ingredients_check("Sahnesteif", cream_stiff)

def cherry_water():
  fc.typingPrint("Hast du 125ml (9 Esslöffel) Kirschwasser? (j) (n)")
  cherry_water = input().lower()
  fc.ingredients_check("Kirschwasser", cherry_water)

def chocolate_shavings():
  fc.typingPrint("Hast du 100g Schokoraspeln? (j) (n)")
  chocolate_shavings = input().lower()
  fc.ingredients_check("Schokoraspeln", chocolate_shavings)

current_step = "ingredients_list"
def ingredients_list():
  eggs()
  sugar()
  flour()
  food_starch()
  cocoa()
  baking_powder()
  fc.typingPrint("Jetzt machen wir weiter mit der Füllung!")
  cherries()
  cream()
  cream_stiff()
  cherry_water()
  chocolate_shavings()

ingredients_list()

current_step = "shopping"
def shopping():
  #current_step = shopping()
  fc.typingPrint(f"Das waren alle Zutaten, dir fehlen noch: {len(fc.ingredients)} Zutaten")
  for ingredients in fc.ingredients:
    fc.typingPrint(ingredients)
      
  if len(fc.ingredients) > 0: 
    fc.typingPrint("Lass uns die fehlenden Zutaten einkaufen!")
    print('''
            _
              \________
            ~   \######/       
              ~  |####/
            ~    |____.
            ______o____o__________ 
                                  \_______
                        ''')
    fc.timer('Einkaufen')

  else:
    fc.typingPrint("Super, dir fehlen keine Zutaten mehr!")

shopping()

menu()

current_step = "preparation"
def preparation():
  fc.typingPrint("Lass uns mit dem Backvorgang beginnen, zuerst bereiten wir die Zutaten vor.")
  fc.typingPrint("Dafür brauchst du: 6 Eier, 200g Zucker, 200g Mehl, 50g Speisestärke, 50g Kakaopulver, 2 TL Backpulver")
  fc.typingPrint("(W)eiter?") # Eventuell (Z)urück? Aber eigentlich sieht man ja den Schritt davor in der Konsole.
  next = input().lower()
  fc.preparation_check(next)

  fc.typingPrint("Schritt 1:")
  fc.typingPrint('''Für den Biskuitboden 6 Eier mit Zucker und 6 EL Wasser in eine Schüssel geben und mit dem Rührgerät etwa 5 Minuten auf höchster Stufe schlagen, bis die Masse ihr Volumen etwa verdoppelt hat.''')
  fc.typingPrint("(W)eiter?")
  next = input().lower()
  fc.preparation_check(next)

  fc.typingPrint("Schritt 2:")
  fc.typingPrint("Mehl, Speisestärke, Kakaopulver und Backpulver in einer Schüssel vermischen.")
  fc.typingPrint("(W)eiter?")
  next = input().lower()
  fc.preparation_check(next)

preparation()