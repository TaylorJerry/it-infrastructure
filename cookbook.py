import sys
import functions as fc

# TODO: Eventuell noch reinbringen was man für Equipment braucht? Springform z.B
# TODO: Im Menü könnte man noch das Rezept zur Übersicht einstellen. Bzw. auch das Equipment



current_step = []

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




#Geetings and Asking for Name
input_name = ""
def start():
  #current_step.append("start")
  fc.typingPrint("Hallo, lass uns eine Schwarzwälder Kirschtorte backen!\nWie ist dein Name?")
  input_name = input()
  fc.typingPrint(f"Wilkommen {input_name}!")
  menu()







#Main menu with overview of all functionalities
#Start the recipe
#Information about the recipe
#User manual for the interaction with the program
#Skip to the paused section
#End the program

def menu():
  #current_step.append("menu")
  fc.typingPrintBold("\nMenü:")
  fc.typingPrint("(S)tarten  (Ü)bersicht   (I)nformationen   (E)rklärung   (F)ortsetzen  (B)eenden")
  menu_selection = input().lower()

  if menu_selection == 'i':
      text = '''
            Arbeitszeit: 60 min
            Backen: 20 min
            Kühlen: 45 min
            Schwierigkeit: Mittel
            Link zum online Rezept: https://www.einfachbacken.de/rezepte/schwarzwaelder-kirschtorte-das-klassische-rezept
            '''
      print(text)
      menu()
  
  elif menu_selection == 'ü':
      text = '''
            Zu einem Schritt springen oder zurück zum (M)enü:
            - (Z)utaten
            - Schritt 1 (A): Biskuitboden vorbereiten
            - Schritt 2 (B): Biskuitboden backen
            - Schritt 3 (C): Füllung der Torte zubereiten
            - Schritt 4 (D): ...
             '''
      print(text)
      skip_input = input().lower()
      if skip_input == "m":
        menu()
      elif skip_input == "z":
        ingredients_list()
      elif skip_input == "a":
        prepare_base()
      elif skip_input == "b":
        prepare_base()
      else:
        fc.typingPrint("Keine gültige Eingabe. Wähle etwas anderes aus.")

  elif menu_selection == 'e':
      text = '''
            - Die Buchstaben in den Klammern geben an, welchen Buchstaben du eingeben musst 
              (Groß- und Kleinschreibung ist irrelevant).
            - Die Eingaben, die du machst, immer mit "Enter" bestätigen.
            - Falls du etwas falsches eingibst, wird deine Eingabe abgefangen und du kannst es noch einmal versuchen. 
             '''
      print(text)
      menu()

  elif menu_selection == 's':
    fc.typingPrint("Wir starten mit der Zutatenliste für den Biscuitteig!")
    ingredients_list()

  elif menu_selection == 'b':
    fc.typingPrint("Schade dass du das Backen jetzt schon beendest! Versuch es später nochmal! Jeder fäng mal klein an :-)")
    sys.exit()

  elif menu_selection == 'f':
    load_last_savepoint()


  else: 
    fc.typingPrint("Falsche Eingabe, versuch es noch einmal")
    menu()

#menu()


def load_last_savepoint():
  if len(current_step) > 0:
    fc.typingPrint("Letzten Stand laden")
    fc.timer( "Laden des alten Standes", 2)
    if current_step[len(current_step)-1] == "ingredients_list":
      ingredients_list()
    elif current_step[len(current_step)-1] == "shopping":
      shopping()
    elif current_step[len(current_step)-1] == "prepare_base":
      prepare_base()
    elif current_step[len(current_step)-1] == "prepare_cherries":
      prepare_cherrys()
  elif len(current_step) == 0:
      fc.typingPrint("Kein Speicherstand gefunden. Zurück zum Menü...")
      menu()



#Functions for the checking the ingredients
#Eggs
def eggs():
  fc.typingPrint("Hast du 6 Eier? (j) (n)")
  eggs = input().lower()
  fc.ingredients_check("Eier", eggs)

#Sugar
def sugar():
  fc.typingPrint("Hast du 250g Zucker? (j) (n)")
  sugar = input().lower()
  fc.ingredients_check("Zucker", sugar)

#MFlour
def flour():
  fc.typingPrint("Hast du 200g Mehl? (j) (n)")
  flour = input().lower()
  fc.ingredients_check("Mehl", flour)

#Food starch
def food_starch():
  fc.typingPrint("Hast du 50g Speisestärke? (j) (n)")
  food_starch = input().lower()
  fc.ingredients_check("Speisestärke", food_starch)

#Cocoa
def cocoa():
  fc.typingPrint("Hast du 50g Kakaopulver? (j) (n)")
  cocoa = input().lower()
  fc.ingredients_check("Kakaopulver", cocoa)

#baking Powder
def baking_powder():
  fc.typingPrint("Hast du Backpulver? (j) (n)")
  baking_powder = input().lower()
  fc.ingredients_check("Backpulver", baking_powder)

#Cherries
def cherries():
  fc.typingPrint("Hast du 350g Schattenmorellen (eine Kirschenart) im Glas? (j) (n)")
  cherries = input().lower()
  fc.ingredients_check("Schattenmorellen", cherries)

#Cream
def cream():
  fc.typingPrint("Hast du 1l Sahne? (j) (n)")
  cream = input().lower()
  fc.ingredients_check("Sahne", cream)

#Cream Stiff
def cream_stiff():
  fc.typingPrint("Hast du 5 Packungen Sahnesteif? (j) (n)")
  cream_stiff = input().lower()
  fc.ingredients_check("Sahnesteif", cream_stiff)

#Cherry Water
def cherry_water():
  fc.typingPrint("Hast du 125ml (9 Esslöffel) Kirschwasser? (j) (n)")
  cherry_water = input().lower()
  fc.ingredients_check("Kirschwasser", cherry_water)

#Chocolate Shavings
def chocolate_shavings():
  fc.typingPrint("Hast du 100g Schokoraspeln? (j) (n)")
  chocolate_shavings = input().lower()
  fc.ingredients_check("Schokoraspeln", chocolate_shavings)


#Ask for all the ingredients one after another
def ingredients_list():
  current_step.append("ingredients_list")
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








#Return all the missing ingredients and pause the recipe for 10 seconds if ingredients are missing
def shopping():
  current_step.append("shopping")
  if len(fc.ingredients) > 0: 
    fc.typingPrint(f"Das waren alle Zutaten, dir fehlen noch: {len(fc.ingredients)} Zutaten")
    for ingredients in fc.ingredients:
      fc.typingPrint(ingredients)
    fc.typingPrint("Lass uns die fehlenden Zutaten einkaufen!")
    print('''
              _
         ~     \________
      ~     ~   \######/       
         ~    ~  |____/
            ______o___o__________ 
                                  \_______
                        ''')
    fc.timer('Einkaufen', 10)

  else:
    fc.typingPrint("Super, dir fehlen keine Zutaten mehr!")
  
  prepare_base()

#current_step = "shopping"
#shopping()










# TODO: Den folgenden Code könnte man noch etwas interaktiver gestalten
# Eventuell (Z)urück? Aber eigentlich sieht man ja den Schritt davor in der Konsole.
def preparation_check(user_input):
    if user_input == 'w':
        pass
    elif user_input == 'm':
      menu()    
    else:
        fc.typingPrint("Falsche Eingabe, versuch es noch einmal (w):")
        new_input = input().lower()
        preparation_check(new_input) 



def prepare_base():
  current_step.append("prepare_base")
  fc.typingPrint("Lass uns mit dem Backvorgang beginnen, zuerst bereiten wir die den Biskuitboden vor!")
  fc.typingPrint("Dafür brauchst du: 6 Eier, 200g Zucker, 200g Mehl, 50g Speisestärke, 50g Kakaopulver, 2 TL Backpulver")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("Schritt 1:")
  fc.typingPrint('''Für den Biskuitboden 6 Eier mit Zucker und 6 EL Wasser in eine Schüssel geben \nund mit dem Rührgerät etwa 5 Minuten auf höchster Stufe schlagen, bis die Masse ihr Volumen etwa verdoppelt hat.''')
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)
  print('''
                 .-'"""""""\\
                |o\     __  )
                | ;`----||-'
                /  \   _||__
               |::: ||`"""""`|
               |:::O|=\     /=,
               `""""`'=`"""`=='
  ''')
  fc.timer('Rühren', 5)

  fc.typingPrintBold("Schritt 2:")
  fc.typingPrint("Mehl, Speisestärke, Kakaopulver und Backpulver in einer Schüssel vermischen.")
  fc.typingPrint("Ein Tipp von Profis: Wenn du die trockenen Zutaten siebst, wird der Teig viel luftiger!")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("Schritt 3:")
  fc.typingPrint("Ofen auf 180 Grad (Umluft: 160 Grad) vorheizen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)


  prepare_cherrys()




def prepare_cherrys():
  current_step.append("prepare_cherries")
  fc.typingPrintBold("Jetzt bereiten wir die Schattenmorellen vor und backen den Boden!")
  fc.typingPrint("Dafür brauchst du: etwas Butter für die Form, 1 Glas Schattenmorellen (Abtropfgewicht 350g), 2 EL Speisestärke ")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("Schritt 1:") 
  fc.typingPrint("Den Boden einer Springform (Ø 26 cm) einfetten und leicht bemehlen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("Schritt 2:") 
  fc.typingPrint("Die Biskuitmasse in die Springform hineingeben und glatt streichen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("Schritt 3:") 
  fc.typingPrint("Im vorgeheizten Ofen etwa 20 Minuten backen und danach vollständig auskühlen lassen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("Schritt 4:") 
  fc.typingPrint("Während der Boden backt bereiten wir die Füllung vor!")
  fc.typingPrint("Für die Füllung Schattenmorellen über einem Sieb abgießen, dabei den Saft auffangen. Stärke mit 2EL vom Saft anrühren.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("Schritt 4:") 
  fc.typingPrint("Den restlichen Kirschsaft aufkochen und die Speisestärke-Kirschsaft-Masse mit einrühren.") 
  fc.typingPrint("Dies kurz unter Rühren aufkochen lassen, dann direkt vom Herd nehmen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)
  print('''
                 _.-------------.
             .-''            .;'|
            ;==============;+'  |
            | (} (} {) (}  |    |
            | .==========. |    |
            | | _ .'"+_/)| |    |      
            | | ( (  _  )| |    ,
            | |  `--' `' | |  .'
            | `----------' |.'
            `--------------'
                
  ''')
  fc.timer('Backen', 20)
  # TODO: Kuchen in den Ofen einfügen








#Main Worfklow
start()

