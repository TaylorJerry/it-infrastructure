#from functions import print_menu
#import typing_extensions
import functions as fc

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
  current_step = "start"
  fc.typingPrint("Hallo, lass uns eine Schwarzwälder Kirschtorte backen!\nWie ist dein Name?")
  input_name = input()
  fc.typingPrint(f"Wilkommen {input_name}!")
start()





def menu():
  current_step = "menu"
  fc.typingPrint("Menü\n(S)tarten   (E)rklärung   (F)ortsetzen (...)")
  menu_selection = input().lower()

  if menu_selection == 'e':
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

  else: 
    fc.typingPrint("Falsche Eingabe, versuch es noch einmal")
    menu()

menu()




def eggs():
  fc.typingPrint("Hast du 6 Eier? (j) (n)")
  eggs = input().lower()
  fc.ingredients_check("Eier", eggs)
#eggs()
  
def sugar():
  fc.typingPrint("Hast du 250g Zucker? (j) (n)")
  sugar = input().lower()
  fc.ingredients_check("Zucker", sugar)
#sugar()

def flour():
  fc.typingPrint("Hast du 200g Mehl? (j) (n)")
  flour = input().lower()
  fc.ingredients_check("Mehl", flour)
#flour()

def food_starch():
  fc.typingPrint("Hast du 50g Speisestärke? (j) (n)")
  food_starch = input().lower()
  fc.ingredients_check("Speisestärke", food_starch)
#food_starch()

def cocoa():
  fc.typingPrint("Hast du 50g Kakaopulver? (j) (n)")
  cocoa = input().lower()
  fc.ingredients_check("Kakaopulver", cocoa)
#cocoa()

def baking_powder():
  fc.typingPrint("Hast du Backpulver? (j) (n)")
  baking_powder = input().lower()
  fc.ingredients_check("Backpulver", baking_powder)
#baking_powder()

def cherries():
  fc.typingPrint("Hast du 350g Schattenmorellen? (j) (n)")
  cherries = input().lower()
  fc.ingredients_check("Schattenmorellen", cherries)
#cherries()

def cream():
  fc.typingPrint("Hast du 1l Sahne? (j) (n)")
  cream = input().lower()
  fc.ingredients_check("Sahne", cream)
#cream()

def cream_stiff():
  fc.typingPrint("Hast du 5 Packungen Sahnesteif? (j) (n)")
  cream_stiff = input().lower()
  fc.ingredients_check("Sahnesteif", cream_stiff)
#cream_stiff()

def cherry_water():
  fc.typingPrint("Hast du 125ml (9 Esslöffel) Kirschwasser? (j) (n)")
  cherry_water = input().lower()
  fc.ingredients_check("Kirschwasser", cherry_water)
#cherry_water()

def chocolate_shavings():
  fc.typingPrint("Hast du 100g Schokoraspeln? (j) (n)")
  chocolate_shavings = input().lower()
  fc.ingredients_check("Schokoraspeln", chocolate_shavings)
#chocolate_shavings()


def ingredients_list():
  current_step = "ingredients_list"
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

def shopping():
  current_step = shopping()
  fc.typingPrint(f"Das waren alle Zutaten, dir fehlen noch: {len(fc.ingredients)} Zutaten")
  for ingredients in fc.ingredients:
    fc.typingPrint(ingredients)
      
  if fc.ingredients is not None: 
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
shopping()

#print("")