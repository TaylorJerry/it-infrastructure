import sys
import functions as fc


current_step = []
input_name = ""


#Function that is called when you decide to cancel the recipe
#Canceling is only possible via the menu section
def cancel():
  fc.typingPrint("Möchtest du wirklich beenden? (j) (n)")
  cancel_input = input().lower()
  if cancel_input == "j":
    fc.typingPrint(f"Schade {input_name}, dass du das Backen jetzt schon beendest! Versuch es später nochmal! Jeder fängt mal klein an :-)")
    sys.exit()
  elif cancel_input == "n":
    menu()
  else:
    fc.typingPrint("Falsche Eingabe, versuch es noch einmal")
    cancel()






#Main menu with overview of all functionalities
#Start the recipe
#Information about the recipe
#User manual for the interaction with the program
#Skip to the paused section
#End the program
def menu():
  #current_step.append("menu")
  fc.typingPrintBold("\nMenü:")
  fc.typingPrint("(S)tarten  (Ü)bersicht   (I)nformationen   (E)rklärung   (F)ortsetzen  (C)redits  (B)eenden")
  menu_selection = input().lower()

  if menu_selection == 'i': #If i is pressed -> show general information about the recipe
      text = '''
            Arbeitszeit: 60 min
            Backen: 20 min
            Kühlen: 45 min
            Schwierigkeit: Mittel
            Link zum online Rezept: https://www.einfachbacken.de/rezepte/schwarzwaelder-kirschtorte-das-klassische-rezept
            '''
      print(text)
      menu()
  
  elif menu_selection == 'ü': #If ü is pressed -> get an overview about all steps of the recipe and skip to a section
      text = '''
            Zu einem Schritt springen oder zurück zum (M)enü:
            - (Z)utaten
            - Schritt 1 (A): Biskuitboden vorbereiten
            - Schritt 2 (B): Biskuitboden backen
            - Schritt 3 (C): Füllung der Torte vorbereiten
            - Schritt 4 (D): Erste Schicht der Torte auftragen
            - Schritt 5 (E): Torte vollenden und dekorieren
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
        baking()
      elif skip_input == "c":
        prepare_cherries()
      elif skip_input == "d":
        use_cherries()
      elif skip_input == "e":
        final_assembly()
      else:
        fc.typingPrint("Keine gültige Eingabe. Zurük zum Menü...")
        menu()


  elif menu_selection == 'e': #If e is pressed -> show the user manuel of the program
      text = '''
            - Die Buchstaben in den Klammern geben an, welchen Buchstaben du eingeben musst 
              (Groß- und Kleinschreibung ist irrelevant).
            - Die Eingaben, die du machst, immer mit "Enter" bestätigen.
            - Falls du etwas falsches eingibst, wird deine Eingabe abgefangen und du kannst es noch einmal versuchen. 
             '''
      print(text)
      menu()

  elif menu_selection == 's': #If s is pressed -> load function ingredients_list to start the program/recipe
    ingredients_list()

  elif menu_selection == 'b': #If b is pressed -> load function cancel to cancel the program
    cancel()

  elif menu_selection == 'f': #If f is pressed -> open function load_last_savepoint to reload last step
    load_last_savepoint()

  elif menu_selection == 'log': #If log is pressed -> show all the steps for each user in chronological order and reload menu
    fc.typingPrintBold(f"\nLogdaten für {input_name}:")
    for step in range(len(current_step)):
      fc.typingPrint(f"{step}: {current_step[step]}")
    menu()

  elif menu_selection == 'c': #If credits is pressed -> open function credits in file functions.py and reload menu
    fc.credits()
    menu()

  else: #wrong input -> Notify user and reload menu
    fc.typingPrint("Falsche Eingabe, versuch es noch einmal")
    menu()



#function that loads the last step the user took
def load_last_savepoint():
  if len(current_step) > 0:
    fc.typingPrint(f"Letzten Stand für {input_name} laden")
    fc.timer( "Laden des alten Standes", 2)
    if current_step[len(current_step)-1] == "ingredients_list":
      ingredients_list()
    elif current_step[len(current_step)-1] == "shopping":
      shopping()
    elif current_step[len(current_step)-1] == "prepare_base":
      prepare_base()
    elif current_step[len(current_step)-1] == "baking":
      baking()
    elif current_step[len(current_step)-1] == "prepare_cherries":
      prepare_cherries()
    elif current_step[len(current_step)-1] == "use_cherries":
      use_cherries()
    elif current_step[len(current_step)-1] == "final_assembly":
      final_assembly()
    elif current_step[len(current_step)-1] == "end":
      end()
  elif len(current_step) == 0:
      fc.typingPrint("Kein Speicherstand gefunden. Zurück zum Menü...")
      menu()



#Functions for the checking the ingredients
#Eggs
def eggs():
  fc.typingPrint("Hast du 6 Eier? (j) (n)")
  eggs = input().lower()
  fc.ingredients_check("6 Eier", eggs)

#Sugar
def sugar():
  fc.typingPrint("Hast du 250g Zucker? (j) (n)")
  sugar = input().lower()
  fc.ingredients_check("250g Zucker", sugar)

#MFlour
def flour():
  fc.typingPrint("Hast du 200g Mehl? (j) (n)")
  flour = input().lower()
  fc.ingredients_check("200g Mehl", flour)

#Food starch
def food_starch():
  fc.typingPrint("Hast du 50g Speisestärke? (j) (n)")
  food_starch = input().lower()
  fc.ingredients_check("50g Speisestärke", food_starch)

#Cocoa
def cocoa():
  fc.typingPrint("Hast du 50g Kakaopulver? (j) (n)")
  cocoa = input().lower()
  fc.ingredients_check("50g Kakaopulver", cocoa)

#baking Powder
def baking_powder():
  fc.typingPrint("Hast du Backpulver? (j) (n)")
  baking_powder = input().lower()
  fc.ingredients_check("Backpulver", baking_powder)

#Cherries
def cherries():
  fc.typingPrint("Hast du 350g Schattenmorellen (eine Kirschenart) im Glas? (j) (n)")
  cherries = input().lower()
  fc.ingredients_check("350g Schattenmorellen", cherries)

#Cream
def cream():
  fc.typingPrint("Hast du 1l Sahne? (j) (n)")
  cream = input().lower()
  fc.ingredients_check("1l Sahne", cream)

#Cream Stiff
def cream_stiff():
  fc.typingPrint("Hast du 5 Packungen Sahnesteif? (j) (n)")
  cream_stiff = input().lower()
  fc.ingredients_check("5 Packungen Sahnesteif", cream_stiff)

#Cherry Water
def cherry_water():
  fc.typingPrint("Hast du 125ml (9 Esslöffel) Kirschwasser? (j) (n)")
  cherry_water = input().lower()
  fc.ingredients_check("125ml Kirschwasser", cherry_water)

#Chocolate Shavings
def chocolate_shavings():
  fc.typingPrint("Hast du 100g Schokoraspeln? (j) (n)")
  chocolate_shavings = input().lower()
  fc.ingredients_check("100g Schokoraspeln", chocolate_shavings)






#Ask for all the ingredients one after another
def ingredients_list():
  current_step.append("ingredients_list")
  fc.typingPrintBold("\nWir starten mit der Zutatenliste für den Biscuitteig:")
  eggs()
  sugar()
  flour()
  food_starch()
  cocoa()
  baking_powder()
  fc.typingPrintBold("\nJetzt machen wir weiter mit den Zutaten für die Füllung:")
  cherries()
  cream()
  cream_stiff()
  cherry_water()
  chocolate_shavings()
  shopping()








#Return all the missing ingredients and pause the recipe for 10 seconds if ingredients are missing
def shopping():
  current_step.append("shopping")
  if len(fc.ingredients) > 0: 
    fc.typingPrintBold(f"\nDas waren alle Zutaten, dir fehlen noch: {len(fc.ingredients)} Zutaten")
    for ingredients in fc.ingredients:
      fc.typingPrint(ingredients)
    fc.typingPrint("\nLass uns die fehlenden Zutaten einkaufen!")
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
  fc.typingPrintBold(f"{input_name} bist zu bereit zum Starten? \nLass uns mit dem Backvorgang beginnen, zuerst bereiten wir die den Biskuitboden vor!")
  fc.typingPrint("Dafür brauchst du: 6 Eier, 200g Zucker, 200g Mehl, 50g Speisestärke, 50g Kakaopulver, 2 TL Backpulver")
  #fc.typingPrint("(W)eiter (M)enü") 
  #next = input().lower()
  #preparation_check(next)

  fc.typingPrintBold("\nSchritt 1:")
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

  fc.typingPrintBold("\nSchritt 2:")
  fc.typingPrint("Mehl, Speisestärke, Kakaopulver und Backpulver in einer Schüssel vermischen.")
  fc.typingPrint("Ein Tipp von Profis: Wenn du die trockenen Zutaten siebst, wird der Teig viel luftiger!")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("\nSchritt 3:")
  fc.typingPrint("Ofen auf 180 Grad (Umluft: 160 Grad) vorheizen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  baking()




def baking():
  current_step.append("baking")
  fc.typingPrintBold("\nJetzt bereiten wir die Schattenmorellen vor und backen den Boden!")
  fc.typingPrint("Dafür brauchst du: etwas Butter für die Form")
  #fc.typingPrint("(W)eiter (M)enü") 
  #next = input().lower()
  #preparation_check(next)

  fc.typingPrintBold("\nSchritt 1:") 
  fc.typingPrint("Den Boden einer Springform (Ø 26 cm) einfetten und leicht bemehlen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("\nSchritt 2:") 
  fc.typingPrint("Die Biskuitmasse in die Springform hineingeben und glatt streichen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("\nSchritt 3:") 
  fc.typingPrint("Im vorgeheizten Ofen etwa 20 Minuten backen und danach vollständig auskühlen lassen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)
  # TODO: Kuchen in den Ofen einfügen
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
  prepare_cherries()




def prepare_cherries():
  current_step.append("prepare_cherries")
  fc.typingPrintBold(f"\nSo... {input_name}, den ersten Teil des Rezepts hast du jetzt schonmal hinter dir. Jetzt kommt der leckere Teil der Torte dran.")
  fc.typingPrint("Dafür brauchst du: 1 Glas Schattenmorellen (Abtropfgewicht 350g), 2 EL Speisestärke")
  print(r"""
     __.--~~.,-.__
   `~-._.-(`-.__`-.
           \    `~~`
      .--./ \
     /#   \  \.--.
     \    /  /#   \
      '--'   \    /
              '--'
  """)
  fc.typingPrintBold("\nSchritt 1:")
  #fc.typingPrint("Während der Boden backt bereiten wir die Füllung vor!")
  fc.typingPrint("Für die Füllung Schattenmorellen über einem Sieb abgießen, dabei den Saft auffangen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("\nSchritt 2:") 
  fc.typingPrint("Stärke mit 2EL vom Saft anrühren.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("\nSchritt 3:") 
  fc.typingPrint("Den restlichen Kirschsaft aufkochen und die Speisestärke-Kirschsaft-Masse mit einrühren.") 
  fc.typingPrint("Dies kurz unter Rühren aufkochen lassen, dann direkt vom Herd nehmen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  use_cherries()


def use_cherries():
  current_step.append("use_cherries")
  fc.typingPrintBold(f"\nJetzt haben wir die Füllung vorbereitet und können damit die erste Schicht der Torte erstellen.")
  fc.typingPrint("Dafür brauchst du: 1 Liter Sahne, 5 Pck. Sahnesteif, 1 EL Zucker, 3 EL Kirschwasser")
  fc.typingPrintBold("\nSchritt 1:")
  fc.typingPrint("16 Schattenmorellen legen wir beiseite. Die benötigen wir später für die Deko der Torte.")
  fc.typingPrint("Die restlichen Schattenmorellen unter die Speisestärke-Kirschmasse heben.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("\nSchritt 2:")
  fc.typingPrint("Tortenboden zwei mal durchschneiden, sodass drei Böden entstehen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("\nSchritt 3:")
  fc.typingPrint("Auf den ersten Tortenboden 3EL Kirschwasser träufeln.")
  fc.typingPrint("Kirschmasse vollständig darauf verteilen und glatt streichen und abkühlen lassen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("\nSchritt 4:")
  fc.typingPrint("Sahne mit Sahnesteif und Zucker steif schlagen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("\nSchritt 5:")
  fc.typingPrint("Mit einem Löffel oder Palettenmesser etwa 3EL Sahne dünn auf die Kirschmasse streichen. ")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  final_assembly()


def final_assembly():
  current_step.append("final_assembly")
  fc.typingPrintBold(f"\nJetzt haben wir alle Vorbereitungen getroffen um die Torte zu vollenden.")
  fc.typingPrint("Dafür brauchst du: 6 EL Kirschwasser, 100 g Schokoraspeln")
  fc.typingPrintBold("\nSchritt 1:")
  fc.typingPrint("Etwa 4EL der Sahne in einen Spritzbeutel mit Sterntülle geben und beiseite legen.")
  fc.typingPrint("Zweiten Boden auf den ersten Boden legen und leicht andrücken.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("\nSchritt 2:")
  fc.typingPrint("Wieder 3EL Kirschwasser auf den Boden träufeln und etwa die Hälfte der restlichen Sahne auf den Boden streichen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("\nSchritt 3:")
  fc.typingPrint("Letzten Biskuitboden auflegen, mit dem restlichen Kirschwasser tränken, dann mit der restlichen Sahne die Torte verkleiden.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("\nSchritt 4:")
  fc.typingPrint("Mit dem Spritzbeutel 16 Sahnetuffs auf die Torte spritzen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)

  fc.typingPrintBold("\nSchritt 5:")
  fc.typingPrint("Jetzt die Kirschen obenauf setzen und mit der Raspelschokolade die Oberfläche und den Rand bestreuen. Bis zum Servieren kalt stellen.")
  fc.typingPrint("(W)eiter (M)enü") 
  next = input().lower()
  preparation_check(next)
  end()#Recipe finished -> call the end function






#End of recipe
#End program with a funny picture
def end():
  current_step.append("end")
  fc.typingPrintBold("\nDie Torte ist fertig!")
  fc.typingPrint(f"Toll {input_name}! Du hast dieses schwierige Rezept gemeistert und eine sagenhafte Torte gebacken!")
  fc.typingPrint("Jetzt nur noch Kaffe kochen, die Oma an den Tisch holen und es kann losgehen!")
  print("""
                   .---.
                  (_---_)
                 (_/$ $\_)
                  (  v  )
                   `\ /'
                .-'': ;``-.
               /   \,Y./   \\
              /     (:)___  \\
             :   .-'XXX`-.`\_;
              `.__.-XXX-.__.'
               /  / XXX \  \   
              /      XXX    \     
             /        XXX    \    
            /                 \  
           /                   \ 
           `--...___   ___...--' 


    (  )   (   )  )            (  )   (   )  )       
     ) (   )  (  (              ) (   )  (  (
     ( )  (    ) )              ( )  (    ) )
     _____________              _____________
    <_____________> ___        <_____________> ___
    |             |/ _ \\      |             |/ _ \\
    |               | | |      |               | | |
    |               |_| |      |               |_| |
 ___|             |\___/     __|             |\___/
/    \___________/    \\    /    \___________/    \\
\_____________________/     \_____________________/

  """)

  fc.typingPrint(f"Wir bedanken uns für deine Aufmerksamkeit {input_name}!")
  fc.typingPrint("Vielleicht hast du ja bald Lust wieder mit uns zu backen! :-)")
  fc.typingPrint("Tschüss!")
  menu()








#Main Worfklow
#Geetings and Asking for Name
#current_step.append("start")
#Print the ASCII Art as a kind of "welcome screen"
print(r"""

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
fc.typingPrint("Hallo, lass uns eine Schwarzwälder Kirschtorte backen!\nWie ist dein Name?")
input_name = input()
fc.typingPrint(f"Wilkommen {input_name}!")
menu()

