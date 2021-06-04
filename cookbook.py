#from functions import print_menu
import functions as fc

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
                                                                           
                                                                           

""")

print(r"""\
                 .,a@@@@@@@@@@@@@@@@@@@@@@@@@@@a,. 
           .,a@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@a,. 
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

#Simple Text input from shell
fc.typingPrint("Hallo, lass uns eine Schwarzwälder Kirschtorte backen!\nWie ist dein Name?")

input_name = input()
fc.typingPrint(f"Wilkommen {input_name}!")

fc.typingPrint(fc.print_menu())

menu_selection = input()
if menu_selection == 'E':
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
  fc.typingPrint(text)



print("")