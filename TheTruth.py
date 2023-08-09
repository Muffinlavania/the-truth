import os,time as TY,sys,random,json,wave
from pygame import mixer
from threading import Thread


#minimap(prob) work, maybe add a little ui too?
#maybe add Module D skip count
#Module B cant be picked up from the right side in the truth
#Night Vision works in cavem1 and cavem2, its dark in the shed at night even when powered
istime=True
#so time.sleep also stops time lol
class time:
  def sleep(amo,TIME=False):
    global istime
    if not TIME:
      tmp=istime
      istime=False
      TY.sleep(amo)
      istime=tmp
    else:
      TY.sleep(amo)
  def time():
    return TY.time()


mixer.init()
Music = mixer.music
#pyinstaller -F --add-data "Truth/*.wav;Truth/" --add-data "Truth/*.mp3;Truth/" -i TRUTH.ico TheTruth.py

#bumba separator ૮ ˶* ᵕ *˶ ა


devz = ['Muffinlavania','LUCASLI4','Lucas','Cristian','Mr. Petroleum'] #if you want to play as a dev, look no further than naming yourself these..

WINDOWS = os.name=='nt'
if WINDOWS:
  import msvcrt

  #WALRUS OPERATOR OP 
  somekeys = {'H': 'up', 'P': 'down', 'K': 'left', 'M': 'right', '\\r': 'enter', '\\x08': 'backspace','\\xe0':'yippe yay','\\t':'tab'}
else:
  from getkey import keys
  from getkey import getkey as GETkey
def getkey():
  return (h if (h:=str(msvcrt.getch())[2:-1]) not in somekeys.keys() or h in ['P','H','K','M'] else somekeys[h] if h!='\\xe0' else somekeys[str(msvcrt.getch())[2:-1]]) if WINDOWS else GETkey()
UP='up' if WINDOWS else keys.UP
DOWN='down' if WINDOWS else keys.DOWN
RIGHT='right' if WINDOWS else keys.RIGHT
LEFT='left' if WINDOWS else keys.LEFT
BACKSPACE='backspace' if WINDOWS else keys.BACKSPACE
ENTER='enter' if WINDOWS else keys.ENTER
TAB='tab' if WINDOWS else keys.TAB

def underline(thio):
  return thio if WINDOWS else "\u0332".join(thio)
def c(ti=0):
  print(R);os.system('clear' if os.name!='nt' else 'cls');time.sleep(ti)
bold,R='\033[01m','\033[0m' #USE R INSTEAD OF RESET
c()

'''
SOME TODO: 

  sounds to yskysn (to show bumb) (threads for sound management???)
  make names actually work
  uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh


- test mining
- finish adding lean no hit for lucas lol
- HELL MODE
  - two phases, need to kill him for 2nd phase, which is a savepoint you can continue from (since phase 2 not gonna be easy at all)
  - 2nd phase is actually completlwey different
  - 100% random attack schedule thing, one more extra attack that can happen
  - he no longer has random dialogues, his health is times a random amount (which is also what your attack is multipled by)


- MODULE A CHEATER ENDING, CARRIES INTO NEXT GAME
- im just piling these up arent i
- make Module A in erase revive you, but also gives you a slight window to go back to the room, to which the erase will actually go into as well
- if you die in that room, secret dialogue with the start of you died dialogue, but \\\\VOID-A\\\\ actually decides to revive you himself, as that was not fair
- there is a discussion between B and A, and in the middle of it you revive
- beating erase leads to the same ending dialogue (Youre alive!), but without B, no other clues at all
- D does say one more line at the end though, something hinting toward not playing again (could be passive aggerssive lol)
- completley normal ending, BUT at key door, both B and A are not there (makes unspoken inpossible lol)
- after beating game and relogging, you are greeting with an impatient start screen, water glitching, and you need to get A, but when about to get it, you get a warning from D about stuff
- Every step closer you take to Module A makes D tell you more and more warnings, at one point the entire maze gets light and you can see theres walls in front of A by D (need to get B to pass)
- after getting A, EVERYTHING becomes the same exact color, and the only thing you can do is try to exit the cave, the right transitions wont work, youll be taken to nothing 
- equipping Mod A will result in nothing, when you go outside time goes x10 fold or something and its guaranteed death, with a special message and special achievement


'''
TEST = lambda tex: print(tex)
  
def THREAD(**targe):
  y = Thread(target = targe['target'])
  y.daemon = True
  return y
def p(ti):
  print(ti)
TEST = p
all_music = {}
def file_name(name):
  try:
      base_path = sys._MEIPASS # PyInstaller creates a temp folder and stores path in _MEIPASS
  except Exception:
      base_path = os.path.abspath(".")
  return os.path.join(base_path, name)

def sound(path:str):
  mixer.Sound.play(mixer.Sound(file_name(path)))
def music(name:str,music_path:str,canloop:bool=True):
  global all_music
  if not all_music.get(name,False):
    if all_music!={}:
      Music.unload()
    all_music = {name:True}
    Music.load(file_name(music_path))
    Music.play(-1 if canloop else 0)
def musicstop():
  global all_music
  Music.pause()
  all_music = {}

gGg=True #able to get achievements (used if youre cheating hehe)
achievements={"Horrible Game":False, "Bang":False, "Live on":False, "Rip bozo":False, "Escape?":False, "Raft":False,"The Lab":False,"The Plane":False, "What's this?":False, "Escape.":False, "Sped":False, "Poggers":False, "Pro fix":False, "Big lure":False, "ok":False, "classic":False, "afk":False, "???":False, "New game pog":False, "lanc":False, "mini":0,'end':0,'easter_cooldown':[1,69420]}
print('\033[?25l') #hide cursor

c()
if 'truthdata.json' not in os.listdir():
  print('What is your name? (THIS IS WHAT YOU WILL FOREVER BE CALLED, best not be xXballs_gamer69Xx!)\n')
  time.sleep(1)
  name=input(">").strip().title()
  input(f"Hello {name}!\n[Enter to continue]")
  with open('truthdata.json','w') as j:
    j.write(json.dumps({name:achievements}))
else:
  with open('truthdata.json','r') as j:
    achievements_temp=json.load(j)
  if "Horrible Game" in achievements_temp.keys() and type(achievements_temp["Horrible Game"])==bool: #first time in new update
    achievements_temp={achievements_temp.pop('name'):achievements_temp}
  names=list(achievements_temp.keys())
  def col(o):
    for ind,g in enumerate(o): yield f"{ind+1}) {g}\n" #YIELD IS COOL
  #do while but scuffed
  nameZ="".join([i for i in col(names)])
  j = input(f"\033[38;5;222mSave data detected!\033[0m\nIf you think this is a mistake, delete truthdata.json in this folder.\n(This folder is {os.getcwd()})\n\n\033[38;5;222mOtherwise, who are you?\033[0m (n for new user)\n"+nameZ+"\n\n>\033[38;5;222m ")
  while (int(j) if j.isdigit() else j) not in range(1,len(names)+1) and j!='n':
    c()
    j = input(f"\033[38;5;124mInvalid input!\n\n\033[38;5;222mWho are you?\033[0m (n for new user)\n"+nameZ+"\n\n>\033[38;5;222m ")
  c()
  if j=='n':
    j=names[0]
    while j in names:
      j = input(f"Welcome new person! You are a person right?\n\nWhat would you like to be called? \n\033[38;5;52m[must not be in \033[0m{nameZ.replace(os.linesep,',')[:-1]}\033[38;5;52m]\033[0m\n\n>\033[38;5;222m ") #pov os.linesep instead of \n lol
      c()
    name=j
    #printt but smaller
    for i in f"Welcome to this world {j}!":
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(.1)
    time.sleep(2)
    input(R+"\n[Any key to continue to the game]")
  else:
    name = names[int(j)-1]
c()

#initial writing (and making sure we arent overwriting anything else)
with open('truthdata.json','r') as wead:
  achievements2=json.load(wead)
if "Horrible Game" in achievements2.keys() and type(achievements2["Horrible Game"])==bool: #first time in new update
  achievements2={name:achievements2}
else:
  if name in achievements2.keys():
    achievements=achievements2[name]
  else:
    achievements2[name]=achievements
with open('truthdata.json','w') as j:
  j.write(json.dumps(achievements2))


def Sprint(text): #for printing special characters, should work?
  print(f"\033[48;5;232m{text}\033[0m")
# able to copy paste from here on (between versions)

tinyvars={'chest':True,'MYARMS':False,'firstmin':False,'othermin':False,'min3':False,'shrine1':0,'shrine2':0,'shrine3':0,'present1':0,'umev':0,'minydict':{'ˇ':"maze1",'∛':"maze2",'∜':"maze3",'♣':"maze4",'♦':"maze5",'♥':"maze6",'♠':"maze7",'☺':"maze8",'☻':"maze9",'♀':"maze10"}} #going to be for one time use variables, such as the variable for if you opened miner chest find small, find tinyvars, find smallvars, find small dict

def smallvarget(nam):
  global tinyvars
  return tinyvars.get(nam,False)
def smallvarchange(nam,value=True):
  global tinyvars
  tinyvars[nam] = value
smallvarset = smallvarchange
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#----------------------                                 ----------------------------
#----------------------              SETUP.PY           ----------------------------
#----------------------                                 ----------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

#This file is for the colors. And the mazes, like the templates below.
#for future me, some available characters: Y, i, s, ?, j
#and all the easter ones
#(H,N,n,z,U,u)

updatelogs='''
╔═════════════════════════════════════════════════════════════╗
║                       \033[38;5;44mThe Easter Update\033[0m               (4/08)║
║                                                             ║
║ - \033[38;5;5mAdded Easter event!\033[0m (You need to find it first..)         ║
║    +9 new event achievements                                ║
║    +Includes a huge maze with...                            ║
║      jésus (not sus)                                        ║
║      2 guys                                                 ║
║      A weird door (new ending!11!?!?!)                      ║
║      An \033[38;5;12measter egg hunt\033[0m, with 5 prizes                      ║
║      A secret or two somewhere.....                         ║
║ - Removed Valentines event                                  ║
║    +yea its like not valentines lol (teaser still there)    ║
║    +also removed the 2 lines of code for april fools...     ║
║ - Yet another secret... Get every ending first!             ║
║    +Unlocks the new true truth ending (lots more)           ║
║     Achievement remains locked until you get all endings... ║
║ - A lot of quality of life changes...                       ║
║    +Inventory UI changes (now shows name/easter stuff)      ║
║    +Fixed another good set of bugs...                       ║
║    +Added \033[38;5;48mbackpack\033[0m! (Gives +3 inventory, can be found..)    ║
║    +Added ingame button 'v', view achievements ingame       ║
║    +Added fixed(more fixed) night cycle                     ║
║    +\033[38;5;10mModules no longer disappear in the real world\033[0m           ║
║    +Oh yea, added this too... and the overview thing        ║
║ - Probably a few things I forgot...                         ║
║     --Things to come: new minigame?, lanc update, idk--     ║
║                                                             ║
║       Comment any bugs/suggestions! (my ideas are \033[38;5;88mdead\033[0m)     ║
╚═════════════════════════════════════════════════════════════╝

'''
updatelogs2='''
╔═════════════════════════════════════════════════════════════╗
║                       The \033[38;5;88mYSKYSN\033[0m Update               (5/10)║
║                                                             ║
║ - Added \033[38;5;88mYSKYSN\033[0m Boss Fight! (real)                           ║
║    +Adds onto the 'lanc' achievement, took way too long     ║
║        (Just do the lanc achievements twice lol)            ║
║    +Has its own page of new achievements...                 ║
║        Lean!/1???!?                                         ║
║    +And a bunch of harder modes... (maybe a bit too hard)   ║
║ - Fixed some more stuff, achievements were bugged lol       ║
║          --Things to come: update to the Miner--            ║
║            --probably fixes to this too lol--               ║
║                                                             ║
║       Comment any bugs/suggestions! (keep yourself safe)    ║
╚═════════════════════════════════════════════════════════════╝

'''
updatelogs3='''
╔═════════════════════════════════════════════════════════════╗
║                   The \033[38;5;95munlazy\033[0m (ish) \033[38;5;95mupdate\033[0m             (8/29)║
║                                                             ║
║ - fixed the achievements system  (again)                    ║
║    +literally just fixed it idk the website i used updated  ║
║       forking this will result in local saves if it breaks  ║
║       going to have to fix every other old version so yay   ║
║ - got lazy over the summer                                  ║
║    +forgot to remove easter event                           ║
║        i tried but it had bugs so gave up im so good        ║
║        wont remove it until i fix everything                ║
║       --Things to come: remove the easter event idk--       ║
║                --that one miner minigame--                  ║
║                                                             ║
║   i havent given up on this game just like summer moment    ║
║when i decide to truly learn c# probably going to remake this║
║                 \033[38;5;74m for now have fun :)\033[0m                        ║
╚═════════════════════════════════════════════════════════════╝

'''
updatelogs4='''
╔═════════════════════════════════════════════════════════════╗
║                 The \033[38;5;182mnot important\033[0m update             (10/14)║
║                                                             ║
║ - got slight motivation to work on truth again [happy :)]   ║
║ - fixed the achievements system  (again again)              ║
║    +I GOT THE DATA BACK YAYYYYYYYYY(i toggled a thing go me)║
║    +that took a while sheesh a lot of changes               ║
║ - removing easter event                                     ║
║    +changing cover image [no air fryer :(]                  ║
║                                                             ║
║                                                             ║
║    --Things to come: hopefully a huge christmas event--     ║
║            --that one miner minigame someday--              ║
║                                                             ║
║                                                             ║
║                                                             ║
║                 \033[38;5;91mi mean its kinda important\033[0m                  ║
╚═════════════════════════════════════════════════════════════╝

'''
updatelogs4='''
╔═════════════════════════════════════════════════════════════╗
║                       The Miner Update            (2/23-3/?)║
║                                                             ║
║ - technically shouldnt have motivation to work on this but  ║
║ - THE TRUTH.EXE YAYYYYYYYYYYYYYYYYYYYYYYYYYYYY              ║
║ - unremove easter event                                     ║
║    + idk i like the easter event                            ║
║    + also means there might be a later easter 2.0 event..   ║
║  - fixing A TON of code                                     ║
║    + fixing infinite useless lines, saving space overall    ║
║    + this bullet is so small but maybe took countless hours ║
║  - quality of life changes yay                              ║
║    + some examples (theres a lot of hidden ones)            ║
║         able to write notes with 'n'                        ║
║         button in lab actually changes color to indicate    ║
║         better error handling, achievements, etcetcetcetc   ║
║  - Caves and Cliffs (real)                                  ║
║    + got a reason to steal minecraft update name:           ║
║    + THE MINERVERSE!                                        ║
║         located in a new part of the caves                  ║
║         might want to hold off on giving the Old Pick...    ║
║                                                             ║
║    --Things to come: dont ask me bro probably events --     ║
║                                                             ║
║                                                             ║
║                                                             ║
║  IDK WHY I PUT OFF MAKING THIS AN EXE FOR SO LONG ITS COOL  ║
╚═════════════════════════════════════════════════════════════╝
'''
ditem={ #Just add ,[Itemname]:[Symbolforitem] to the end (Good luck trying to get the item to be actually useful if you did all the steps lol)
  'Wiring':'“',
  'Multi Wiring':'╼',
  'Super Wiring':'╾',
  'Thermometer':'^',
  'Diving Gear [Empty]':'&',
  'Diving Gear [Full]':'1',
  'Night Vision':'%',
  'Revolver':'r',
  'bana':'▣',
  'Revolver[Empty]':'I',
  'Lantern':'l',
  'The Key':'▸',
  'Flashlight':'=',
  'Module A':'A',
  'Module B':'B',
  'Module C':'C',
  'Module D':'D',
  'Module E':'E',
  'Watch':'{',
  'Plane Propeller':'V',
  'Plane Hull(Part)':'+',
  'Plane Fuel':'p',
  "Plank":'q',
  'Paddle':'0',
  'Old Pick':'W',
  'Voltage':'❖',
  'Boat':'▤',
}


#if you wanna try to add a maze or something uhhhhhhhhh good luck have fun lol

#MINER MINIGAME YES
miney=list('''
;;;;;;;;;;;;;#######################;;##;;;;;;;;;;;
;;;;;;#################UUUU###################;;;;;
;;####O-------####ii##T-┌┐-T##ii###--------####O#;;
;###------------#######-└┘-#######----------##--#;;
;##--------------####---------##----------------###
###---------------------------------------------###
###---------------------------------------------☒##
###---------------------------------------------###
###-----##########;-------------;####;---###----###
###----###########;-------------;#####---###----###
###----##########;---------------;####---###----###
###----#########;-----------------;###---###----###
###----#########;-----------------;###---;#;----##T
###-----########;-----------------;##;-------------
####-----########;---------------;###--------------
#####----#########;-◩◩◩--◊--◪◪◪-;####------#######T
#####----#########;;;;;;;;;;;;;;#####-----#########
#####----#########;##;#;;;##;#;;;####----##########
####T----T######;;#;##;;;;;##;;;;###T----T#########
''')

mineyex=list('''\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\niiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\n''')

'''
Miner minigame generation criteria:
MAZE DIMENSIONS: 51x19?

10x10 grid, top left is miney

1: MINEY b c d e f g h i j
2: a b c d e f g h i j
(etc)
In miney:
- a note explaining the mines
- a little shop that has a guy who takes ores for money  
- a bigger shop who has a guy who has items for sale (actual items??)
  - add an exclusive item for the shop?
    - The miner's cap: takes you to a whole mining simulator lol
- each ore adds to your inventory, making the backpack actually useful plus incentive to get Module E before
- New achievements:
  - Horder: have more than 1k (most items are 250?)
  - Naughty: Sell only all the coal to the seller
  - A whole new world: buy the miner's cap
  - Your new world: max yourself out in the miner's dimension

1b and 2a need to have space so the player can enter them, 
1b: entrances at 677-680, 729-732
2a: entrances at 6-9, 36-41 (and more below)

Otherwise all 1b-j and 2b-10j is randomly generated rock and ores
ORES:
  i: rock - 1 (maybe? stacks to )
  ₒ: coal - 15
  ॰: copper - 25
  °: iron - 50
  ৹: magnesium - 90
  ๐: chromium - 120
  𐤏: ruby - 200
  Ｏ: diamond - 250
  ⦿: emerald - 500

☒: note explaining the mining site, needs to be in the words of a miner or something 

'''
emaze=list('''
;zzzzzzzzzzzzzzzzzzz;;z-----zzz;zzzzzzzzzzzzzzzz;zz
];zz]zz]zzz]zzzzzzzzzzz-----╏z;zzzzzz]z]]zzz]zzzzz]
z]zzzz]]]zzzz]-----------------------]]zzz]]z]]zz]z
]zzzzz]]z]]]---------------------------]z]]zz]zz]]z
z]z]z]]z]]-------------------------------]]]]]z]]]z
]]z]]]]]]]--------------------------------]]]zz]]z]
]]]]]]]]]---------------------------------]]]]]]]]]
]]]]]]]]-----------------------------------]]]]]]]]
]]]]]]]]----------------------------------------]]]
]]]]]]]]--------------------------------------⍨-]]]
]]]]]]]]----------------------------------------]]]
]]]]]]]]-----------------------------------]]]]]]]]
]]]]]]]]]---------------------------------]]]]]]]]]
]]]]]]]]]---------------------------------]]]]]]]]]
]]]]]]]]]]---------┌┐--------------------]]]]]]]]]]
]]]]]]]]]]]]-------└┘-------------------]]]]]]]]]]]
]]]]]]]]]]]]]]-----------------------]]]]]]]]]]]]]]
]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
''')#row 1, 1
emaze1=list('''
;z;zz;;zz;;;zzzzzzzzzzzzzzzzzzzzz;zzzzz;zz;zzzzzz;z
;;z;z;z;zz;z;zzzzzzzzzzzzzZzzzzzzzzzz;zzzzzz;zzzzzz
;;;;z;zzz;z;zzzzzzzz-------------zz;zzz;zzzzzzzzzzz
;;z;zz;zzzzzzzzzzzzz-------------zzzzzzzzzzzzzzzzzz
;zz;;;zzzz-------------------------------zzz;zzzzzz
z;;;zz;zzz-------------------------------zzzzzzzz;z
zzzz;zz;z----zzzzzzzzzzzzzzzzzzzzzzzzz----zzzzzzzzz
z;;z;zzz-----z;z;;;;;z;;;;;;;;;;;;;;;z-----z;zzzzzz
;;z;zzz------z;;;;;;;;;;;;;;z;;;;z;;;z------zzzzzzz
;z;----------z;z;;;;;;;;;;;;;;;;;;z;;z---------N;zz
z;;----------z;;;z;;;;;;;z;;;;;;;;;;;z----------zz;
zzz----------z;;;;;;;;;;;;;;;;;;z;;;;z----------z;z
;z;----------zzzzzzzzzzzzzzzzzzzzzzzzz----------z;z
z;z---------------------------------------------;zz
z;z------------------------------------------------
zzzN---------zz;zzzzz;zzzz;zz;z;zzzz;z-------------
;;z;zzz;zz---zz;z;z;zzz;zzzzz;zz;;;zzz---zzzzzzzzzz
zzzz;z;zzz---;zzzzzzz;z;zzzzz;zzzzzz;z---zzz;zzzz;z
z;;;;;;zzz---zzzz;zz;zz;;;;z;zz;z;;;zz---zzzzz;zzzz
''')#row 1, 2
emaze2=list('''
;zzzzzzz;;;;;zzzzzzzzzzzzzzzzzzzzzzzzz;;;;;;;;;zzzz
;z;zzzzzzz;;zzzzzz;zzzzzzzz;zzz;z;zzzzzz;;;;zzzzzzz
zzzz;zzzzN-----------------------------------------
zzzzzz;zz------------------------------------------
;;;zzzzzz---;;z;z;;;zzzzzzzzzzz;z;;z;;;;zzzzzzzzzzz
zzzzz;zzz---;;zzzzzz;;;;zzz;z;;zzzzzzzzzz;z;zzzz;;z
;;zzzzzzz---zz;P-----------------------------------
;;z;zz;zz---z;z------------------------------------
z;zzzzzzz---zz;z;;z;;z;;zzzzzzzz;zz;z;zz;;zzzz;zz;;
;zz;zzz;z---z;;;zzzzzzzzz;z;zz;zzzzzzzzzzz;;;zzzzzz
zz;zz;zzz------------------------------------------
;;zzzzzzz------------------------------------------
;zzz;zz;z---;;z;zzzz;;;zz;zzzzzz;;;zzzzzzzzzzzzzzzz
z;zz;zz;z---;;;zzzzzzzz;zzzzzzzzz;zzzzzzzzzzzzzz;;;
---------------------------------------------------
---------------------------------------------------
zzzzzzzzz---z;zzzzzzzzzzzzzzzzzz;zzzzzzzzzzzzzzzzzz
zzzzzzz;;---;;zzzzzzzzzzzz;zz;zz;;z;;zzzzz;zzzzzzzz
zzzzz;;;z---zzz;zz;z;;z;;zzzzzz;;;;zzzzzzzzzzzzzzzz
''')#row 1, 3
emaze3=list('''
zz;;;;;z;zz;zzzzzzzzzzzzzz;zzzzzzzzzzzzzzzz;;;;;zzz
;z;;z;z;;z;zzzz;zzzz;zzzzzzzzzzz;;;zzzzzzzz;N--;zzz
---------zzzzzzzzzz;;z;;z;;;zzzzz;zzzzzzzzzz---zzzz
---------zzzz;zzzzz;z;;z;;;;zzzzzz;zzzzzzzzz---zzzz
zz;zz;---zzzzzzzzzzz;zz;z;;zz;zzz;zzzzzzzzzz---zzzz
;;zz;;---zzzz;z;z;;zzzzzzzz;z;;z;;zzzzzzzzzz---zzzz
-----------------------------------------------zzzz
---------------------------------------------------
;;zzzzzzzzzzzzzzzzz;;;;;;zzzzzzzzzzzzzzzzzz;;------
;;;zz;zz;;zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz;;------
---------------------------------------------------
-----------------------------------------------zzz;
;;zzzz;;;zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz;;zz---zz;z
z;z;z;zzzzzzz;;z;zzzzzzzz;zzzzz;zzzzzzzzz;;z---;zz;
-----------------------------------------------z;zz
-----------------------------------------------z;zz
zzzzz;zzzzzzz;zzzzzzz;;;;zz;;zzzzz;zzzzz;z;;--N;z;z
;zzzz;zzz;zzz;zzz;z;;;z;zzzzzzzzzzzzzzzzzzz;;;;;zzz
zz;zzzzz;zzzzz;z;;;;;;zzzzzzzzzzzz;zzzzzzzzzzzzzzzz
''')#row 1, 4
emaze4=list('''
;;zz;zzz;;;;zzzzz;zzzzzz;zzzzzzz;;;;zz;zzzz;z;;z;;z
;z--Nzzzz;z-----------------------------z;;;;zN--;;
;z---zzz;;z-----------------------------;;zz;;---;z
z;---zz;;;z---z;z;;;zzzzzzz;;zzzzz;;;---z;;;z;---zz
z;---zz;z;z---;;;zzzz;;;zzzz;;;;;;;zz---zzz;zz---;z
;;---z;z;zz---z;;zz------------Nzz;;;---z;;;;z---;z
z;---;;;;;z---;z;z;-------------;;;zz---;;z;;z---zz
-------------------------------------------------zz
-------------------------------------------------;z
-------------------------------------------------zz
-------------------------------------------------z;
zz---zz;;;;---;;zzz-------------zzz;;---zzzzzz;-zzz
;z---zzz;zz---z;;zz--N----------;;zzz---zzzzz;-;;zz
zz---z;;;zz---;;zz;zzzzzz;;zzzz;z;zzz---zzzzz;;-;zz
zz---;;zzzz---;zz;;;;;;;;;;;;z;z;;zzz---zzzzz;;;;zz
;z-------------------------------------- ;;;-;;;-zz
;z-------------------------------------N;-;z;-;z;;;
;;z;z;;;---zzz;;;zzzzzz;;;;zzzzz;;;;;;;;;;;zz;;z;;z
;;;zzzzz---zz;zzz;;zzz;;zzzz;;;;;zzzzzzzzzzzzzzzzzz
''')#row 2, 1
emaze5=list('''
;;;;;zzzzz---z;zzzzzzzzzz;;z;;;;;;zzzz---zzz;;zz;;z
;;;zzzzzzz---zz;;;;;zz;;;zzzzzz;zzzzzz---zzzzz;;;;z
;zzzzzzzzz---zzzzzzzzzzz;;zzzz;zzzzzzz---zzzzzzz;;;
zzzzzzzzzz---zzzzzzzzzzzzzz;z;;zzzzzzz---zzzzzzzzzz
zzz;;;;zzz----------zzzzzzzz;;zzzzzzzz---zzz;zzzzzz
z;z;;;zzzz----------zzzzzzzzzzzzzzzzzz---zzz;zzzzzz
z;z;;z;zzz;zzzzzz---z--------------------zzzzzzzzzz
;z;z;zz;;zzzzzzzz---zN-------------------zzzzzzzzzz
z;zz;z;z;zzzzzzzz---zzzzzzzzzzzz;;;;zz---zzzzz;zzzz
zzz;zzzzzzz---------zz;;zzz;zz;zzzzzzz---zzzzz;zzzz
zzzzzzzzzzz---------zzz;zzzzzzzz;zzzzz---zzzzzzzzzz
zz;z;zzzzzz---zz;zzz;zz;zz;;zz;z;;zzzz---zzzzzzzzzz
z;zz;zzzzzz---;;zzz--------------------------------
zz;zz;;zzzz---z;zzz--------------------------------
zzz;zz;z;zz---;zzzz----zzzz;zzzzzzzzz;zz;z;z;zz;;zz
z;;;z;zz;zz---zz;zz----zzzzzzz;;z;zzzzzzz;zzzzzz;zz
z;z;z;zzzzz---zz;;z----zzz;zzz;;;;zzz;zz;;;zzzzzzzz
z;;;;;zzzzz---zzz;z----zzzzzzzz;z;zzzzzz;z;z;zzzzzz
zzzz;zzzzzz---zzzz;----zzz;z;zzzzzzzzzzzz;z;;;z;;zz
''')#row 2, 2
emaze6=list('''
;z;;;zzzz---zzzzzz;;;;zzzzzzzzzz;;;;;;zzzz;;zzzzzzz
zz;zzz;zz-----------------------------zz;zzzz;;;;;;
zz;;z;zzz----------------------N------z;;N------z;z
zzz;zzzzz---;;zzzzzzz;---;zzzzzzz;;---;zz-------z;z
;z;zzzz;z---;zzzzzzz;;---;;zzzzzzz;---z;z-------z;z
zzz;z;z;z-----------------------------;z;-------;zz
zz;;zzzz;-----------------------------;;z------Nz;z
z;;zzz;zz---;zzzzzzz;;---;;zzzzzzz;---z;;-------zz;
zzz---------;;zzzzzzz;---;zzzzzzz;;---;z;-------z;;
z;z-----------------------------------z;z-------zz;
zzz---zzz----------------------------Oz;;-------;zz
;zz---zzz---zzzzzzzzzz;zzzzzzzzzzz;zzz;z;-------zz;
------zzz---zzz;zzzz;zzzz;zzzz;zzzzzzz;;z-------;z;
------zzz---zzzzzz;zzzzzzzzzzzz;zzz;zzz;;-------zz;
z;;z---zz------------------------------------------
z;;z---zz------------------------------------------
;;;;---zz---------------------------------------;z;
z;;z---zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz---z;;;zzz
z;;z---zz;;;;;zzzzzzzzzzzzzzzzzzzzzzzzzzz---zzzz;;;
''') #row 2, 3    next one has temple?

emaze7=list('''
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
----------;[[[[[[[[[[[[[[[[[[[[[[[[[[[[[;----------
---------;;]]]]]][[[[[[[[[[[[[[[[[[]]]]];;---------
---------[[[[[[[]]]][#########[[]]]][[[[[[---------
---------]]]]]]]]]]]]#########]]]]]]]]]]]]---------
---------]]]]]]]]]]]]#########]]]]]]]]]]]]---------
---------[[[[[[[]]]][#########[]]]][[[[[[[---------
---------;;]]]]]][[[[[[];;;][[[[[[]]]]]];;---------
----------;[[[[[[[[[[[]];;;]][[[[[[[[[[[;----------
---------------------------------------------------
z-------------------------------------------------z
zzzzzz---------------------------------------zzzzzz
zzzzzzzzz---------------------------------zzzzzzzzz
-----zzzzzz-----------------------------zzzzzzzzzzz
-----zzzzzzzzz-----------------------zzzzzzzzzzzzzz
zzzzzzzzzzzzzzzz-------------------zzzzzzzzzzzzzzzz
zzzzzzzzzzzzzzzzzz---------------zzzzzzzzzzzzzzzzzz
zzzzzzzzzzzzzzzzzzz-------------zzzzzzzzzzzzzzzzzzz
''')#row 2, 4
emaze8=list('''
;;;zzzzz---zz;zzzz;zzzz;zzzz;;;;zzzzzzzz;;zzzzzz;zz
z;;;;zzz---;zz----------------------------------;;z
zzzz;;;z---zz;---------------------------------Nz;;
zz---------zz;---zzzzzzzzzzzzzzz;;;;z;;-----;;zz;;;
zz---------z;z---zzzzzzzzzzz;z;;;;zz;---------z;z;;
zz---zzz---;zz----------=zzzz;zz;;z;-----------;zzz
zz---zzz---z;z-----------zzzz;zzzzz;-----------z;zz
zz---zzz---z;z---zzzzzzzzzzzz;zzzz;------------;zzz
zz---zzz---z;z---zzzzzzzzzzzzzzzzz;-------------;zz
zz---zzz---;zz---------zzz;;zz;;zzz-------------;zz
zz---zzz---;zz---------zz;;z;;;;;;---------------zz
zz---zzz---zzzzz;;zz---zzz;;;;;z;;---------------;z
zz---;zz---zzzz;z;zz---zzzz;;;;;zz;-----◉_◉-----;zz
zz---;;z---------------zz;;zz;zzzzz;;z;;;z;;;;z;zzz
zz---;;;---------------z;;;zzzzzz;zzzzzzzzzzzzzzzzz
zz---------------------;;zz--------------------zzzz
zz---------------------z;zzN-------------------zzzz
;;zz;z---zzzzzzz;z;z;zz;;zzzzzzzzzzzzzzzzzzz---zzzz
;;;;zz---zzzzzzzzzzzzzzzzzzzz;;;z;;;z;;;zzzz---zzzz
''')#row 3, 1
emaze9=list('''
zzzzzzzzzzz---;zzz;----zz;zz;zzz;;zz;zzzzzzzzzzzzzz
zzzzzzzzzzz---z;zz;----zz;z;;;z;zz;z;;;zz;zzzzzz;zz
;;;;zzzzzzz---;z;;z----zz;;zzzz;z;;z;zz;zz;zzzzz;zz
;zzzzzzzzzz---zz;z;----zz;zzzzzz;z;z;z;zzzz;zzz;zzz
zzz;zzzzzzz---z;zzz----zzzzzzzzzzzzzzzzzzzz;zz;zzzz
z;zzzzzzzzz---;zzz;---------------------zzzz;;zzzzz
;;zzzzzzzz----z;zz;---------------------zzzz;;zzzzz
;zzzzzzzzz----zzzz;----zzzz;zzz;z;zz----zzz;;zzzzzz
;;;zzzzzzz---z;zzzz----z;;zz;;;;zzzz----zzz;zz;zzzz
z;;z;zzzz----zz;zz;----zz;zz;z;z;;zz----zzz;;zz;zzz
z;;;;zzzz----zzzzzz----z;zzzzzzzzzzz----zzzzzzzz;;z
z;;;zzzzz---zz;;zz;----zz;z;z----------------------
z;zz;z------;z;zzzz----zz;zzz---N------------------
z;z;zN------zzz;zz;----zzzz;zzzzzzzzzzzzzzzz;----zz
zz;;z;------;;;;;;;----zzzzzzz;zz;zzzzzzzzzzz----;z
z;z;;z------zzzzzzz------------------------------;z
zzz;;zzzz---;zz;zzz------------------------------;z
z;;z;;zzz---;zzzzzz;;;;;;;zzzzzzzzzzzzzzzzzzzzz;;;z
zzzzz;;zz---zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
''')#row 3, 2
emaze10=list('''
zzzz---zz;zzz;;;;;;zzzzzzzzzzzzzzzzzzzzzz---zzzzzz;
z;zz---zzzzzzzzzzzzzz;zzz;;;;;;;zzzzzzzzz---zz;;;;;
zzzz----------------------------------------zz;;zzz
zzzz----------------------------------------z;;;zzz
z;zz---zzzz;zzzzzzzzzz;;;;;;zzzzzzzzz;zzz---;;zzzzz
zzzz-----------------------------------------------
zzzzN----------------------------------------------
zz;zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
zz;;zzzzz;;z;;; ;;;z-------------------------------
zzzz;;;zzzz;;;;z;;zzO------------------------------
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz---zzzzzz
-----------------------------------------z---zzzzzz
-----------------------------------------z---z;zzzz
zzzzzzz;zzzzzzzzzz;zzzzzzzzzzzzzzz;z;z---z---z;zzzz
zzzzz;zz;zzzzzzzzzz;zzzzzzz;z;zzzzzzzz---z---z;;zzz
zzzzzz;z;;;;;;;;zzzz;z;zz;zzzz;zzzzzzz---z---zzz;zz
zzzzzz;zzzzzzzzzz;z;;;;;zzzzzzzzzzzzzz---z---zz;;zz
z;;;;;z;;;;;z;zzzzz;zzzzzzzzz;zzzzzzzz---z---zzz;;z
zzzzzzzzzzzzzz;;zzzzzzzzzzzzzzzzzzzzzz---z---zzzzz;
''')#row 3, 3 
emaze11=list('''
;;z;;z;;;zzzzzzzz;;nnnnnnnnnnnnn;;zzzzzzzzzzzzzzzzz
;;;zzzzzz;;;;zzzz;;-------------;;zz;;zzzzzzzzzzzzz
zzzzzzzzzzzzzzzzz;;;-----------;;;zzzz;;;;;zzzzzzzz
zzzzzzzzzz;;;;zzzz;;-----------;;;z;;;z;;;;;zzzzzzz
zzzzzzzzzzzzzzzzz;;;;---------;;;;zzzzzzzzz;;;;;;;;
------------------------------;zzzzzzzzzzzzzzzzzzzz
---------------------------------------------------
zzzz;;zzz------------------------------------------
------------zzzzzzzzzzzzzzzzzzzzzz---zzzzzzzzzzzzzz
------------zzzz;z;zz;;;z;;;;zzzzz---zzzzz;;zzzzzzz
zz;;zzzzz---zzzzzzzzzzzzzzzzzzzzzz---zzzzz;z;;zz;zz
zzzzzzzzz----------------------------zzz;zzzzzz;zzz
zzzzzzzzz----------------------------zzz;zzzzzz;;zz
zzz;;zzzzzzzzzzzzzzzzzzzzzzzzzzzzz---z;;z;z;z;;;;zz
zz;;zzzzzO---------Rzzzzzz;zz;zzzz---zz;z;zz;zz;zzz
zz;zzzzzz-----------zzzz; ;;;;zzzz---z;;;;;;;;z;zzz
zz;zzzzzzN---------Nzzzzzz;;;;zzzz---z;z;;z;z;;z;zz
;;;zzzzzzzzzz---zzzzzzzzzz;zzzz;zz---zz;;zzzzz;zzzz
;;zzzzzzzzzzz---zzz;;;;;;;;;;;zzzz---zz;zzzzz;zzzzz
''')#row 3, 4
emaze12=list('''
zzzzzz---zzzzzzzzzzzzzzzzzzzzzzzzzzzz;z;;zzz---zzz;
zzzzzz---zzzzzz;;zzzzzzzzzzzzz;;z;;zzzzzzzzz---zzz;
zzzzzz---z;z;;;z;;;;zz;zz;;;;;zzzzzzzzzzzzzz---zzzz
;zzzzz---zz;zzzzzzzzzzzz;;zz;zzzzzzzzzzzzzzz---zz;z
;zzzzz-----------------------------------------zz;;
zzzzzz-----------------------------------------zz;z
---------zzzzz;zzzz---zzzzzzzzzzzzzzzzz;zzzz---zzzz
---------z;;z;z;;zz---zz;;;;zz;zzz;;;;;z;zzz---z;zz
zz;zzz---zzzzz;zzzz---z;zzzzzzzzzzzzzzzz;zzz---z;;z
zzzzzz------------------------------------Nz---zzzz
zzzz;z-------------------------------------z---zzzz
zzzz;z---zzzzzzzzzz--Nzzzzzzzzzzzzzzzzzz---z---z;zz
zzz;zz---zz;zz;;zzz---zzzzzzz;;;zzzzzzzz---;---z;zz
zz;;zz---z;zzz;zzz-----zzz;zz;;z;zzzzzzz---;---z;zz
z;;;zz---zzz;z;zz-------z;zz;zzzzzzzzzzz---z---;zzz
z;z;zz---zzz;z;zzO-----Ozzzzzzzzzz-------------zzzz
z;zz;z---zz;zzz;;z;zz;z;zzzzzzzzzz-------------zzzz
z;zz;z---z;zzzzzz;;z;;;;zzzzzzzzzz-----zzzzzz;zzzzz
;zzzzz---zz;zzzzzzzzzzzzzzzzzzzzzz-----zzzzz;zzzzzz
''') #row 4, 1     start
emaze13=list('''
zzzzzzzzz---zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
;;zzzzzzz------------------------------------------
z;zzzzzzz------------------------------------------
z;;;;;zzz---zzzzzzzzzzzzzzzzzzzzzzzzzzz;;;;zzzzzzzz
z;zzzzzzz---zz;;;zzzzzzzzzzzzzzzzzzzzzzzz;;;;;;;zzz
;;zzzzzzz---;z;;;;;zzzzz------------------------zz;
------------;;;;;;---zzz------------------------zzz
------------zzzzzz---zzz---zzzz---zzzzzzzzzzz---zzz
zzzzz;;;z---zzzzzz---zzz---zzzz---z;zzzzzzzzz---zzz
zzzz;z;;z------------zzz---zzzz---z;;zzzzzzzz---zzz
zzz;;zzzz------------zzz---zzzz---zz;;;;zzzzz---zzz
zzz;zzzzz---zzzzzzzzzzzz---zzzz---z;;;;zzzzzz---zzz
z;;;;;;;z---zzzzzzzzzzzz---zzzz---z;zzzzzzzzz---zzz
--------------------------------------zzzzzzz------
--------------------------------------zzzzzzz------
zzz;---zzzzzzzzzzzzzzz;z---zz;zzzzz---zzzzzzzzzz;;;
zz;;---;zzzzzzzzzzzzzz;-----;zzzzzz--Nzzzzzzzzz;z;;
zzzz;z;zzzzzzzzzzzzz;;z-----;zzzzzzzzzzzzzzzzz;zz;;
zzzzzzzzzzzzzzzzzzzzzzz-----zzzzzzzzzzzzzzzzzz;zzz;
''')#row 4, 2
emaze14=list('''
zzzzzzzzzzzzzz;;;;zzzzzzzzzzzzzzzzzzzz---;---zzzz;;
------zzzzzzzzzzz;;;;;;;zzzzzzzzzzzzzz---;---zz;;z;
------;zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz---;---zzzzzz
;;z--------------------------------------;---z---zz
zz;--------------------------------------;---z---zz
zzz---zzzzzzzzzzzzzz---zzzzzzzzzzzzz;;---;---z---zz
zzz---------------Oz---zzzzzzzzzz---zz---;---z-----
zzz----------------z---zz;;;;;zzz---zz---;---z-----
zzzzzzzzzzzzzzzzzzzzN--z;-----------zz---;---z---zz
zzzz;;;z;z;;zzzzzzzzzzzz;-----------zz---;---z---zz
zzzzz;z;z;;zzzzzzzzz---zz;zzzzzzz---zz---;---z---zz
zzzz;;z;;z;;zzzzzzzz---zz;;zzzzzz---zz---;---z---zz
zzzzzzzzzzzzzzzzzzzz---zzz;;;;zzz----------------zz
-----------------zzz---zzzzzzzzzz----------------zz
--------------------------------------zzzzzzzz---zz
zzzzzzzz-----------------------------------------zz
;zz;;;zzzzzzzzzzzzzzzzzzzzzzzzzzz----------------zz
;zzz;;;;zzzzzzzzzzzzzzzzzzzz;;;zzzzzzzzzzzzzzzzz;;;
;;zzzzzzzzzzzzzzzzzzzzzzzzzzzz;;;zzzzzzzzzzzzzzzzz;
''')#row 4, 3
emaze15=list('''
;;;;;zzzzzzzz---zzz;;;;;z;zz;;;zzz---zzzzzzzzzzzzzz
;z;zzzzzzzzzz---zzzzzzzzzzzzzzzzzz---zzzzzzzzzzzzzz
;;zzzzzzzz---------------------------z;;-----------
zzzzzzzzzz---------------------------;z;-----------
zzzzzzzzzz---zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
zzzzzzzzzz---zzzzzzz;;;zzzz;zzzzzzzz;;z;;zzzz;zzzzz
-------------zzzz;;;zz;zzzzzzzzzzzzzzzzz;zzz;zzzzzz
-------------zzzzzz;zzzzzzzzzz;zzzzzzzzzz;zzzzz;;zz
zzzzzzzzzz---zzzz;zzzzzzN-----------zzzzzzzzzzzzzzz
zzzzzzzzzz---zzzz;zzzzz----------------------------
zzzzzzzzzz---zzzz;zzzzz----------------------------
zzzzzzzzzz---zzzz;zzzzz----------------zzzzzzzzzzzz
zzzzz--------zzzzzzzzz------------------zzzzzzzzzzz
zzzzzN-------zzzzzz;----------------------;zzzzz;zz
z;z;;;;;;zzzzzzzzzz------------------------zzzz;;zz
zz;z-;;;;zzzzzzzzzz;----------ಠ_ಠ---------;zzzz;zzz
z;;;--;;z;zz;zzzzzzzzzzzzzzzzzzzzzzzzzzzz;zzzzz;zzz
zzz;;;-;;z;;zz;zzzzzzz;;;;zzz;;;;zzz;;;;;zzzzzzzzzz
zzzzzzzzzzzzzzz;;;;;;zzzzzzz;;zzzzzzzzzzzzzzzzzzzzz
''')#row 4, 4
emaze16=list('''
zzzzzz---zzzzzzzzzzzzzzzzzzzzz;;zz-----zzzzzzzz;;;z
zz;;z;---zzzzzzzzzzzzz;zzzzzz;zzzz-----z;;;zzz;zzzz
---------zzzzzzz;z;;;;;zzzzz;zzzzz-----zzzz;;zz;;zz
---------zz;;;;;zzzzzz;z;;;;zzzzzz-----zzzzzz;z;zzz
;;zzzzzzzzzzz--------------------------zzzzzz;;;zzz
z;;z;;zz;zzzz--------------------------zzzzz;;zzzzz
z;;;;;zzz;zzzz;;;z;;;;;zzzzzzzzzzz-----zzzzzz;zzzzz
z;;zz;z;;;;;z;z;zzz;;zz;;;zzzzzzzz-----zz;z;z;zz;zz
zzzzzz;zzzzzzzz;zzzzzzzzzz;;zzzzzz-----zz;zzz;zzzzz
---------------------------------------zzz;zzz;zz;z
--------------------------------------Nz;z;zzz;;z;;
zzzzzzzzzzzzzzzzzzzz;;;z;zzzzzz----zz;zz;zzzzz;;;;;
;;zzzzzzzzzzzzzzzz;z;zzzzzzzzzz----z;zz;;zzzz;;z;;;
z;;zzzzzz;zz;;zz;z;zzzzzzzzzzzz----;zzzzzzzz;;;;;;;
zz;;zzzzz;z;--------------------------------------!
zzz;zzz;zzzz=-------------------------------------!
zzz;zz;;zz;;;;zz;zz;;zzzzzzzzzzzzzzzzzzzzzzz;;;;;;;
zzz;;;z;zzzzzzzzzzzzz;z;z;z;zzzzz;zzzz;zzzzz;;z;;;;
zzz;;;z;zzzzzzzzzzzzzzzzzzzzzzzzzzzz;z;zzzzzzz;;;;;
''')
emaze17=list('''
z;;;;;zzz;zzzz;;;z;;;;;zzzz;;;;;z;;;;;;zzzzzz;zzzzz
z;;zz;z;;;;;z;z;zzz;;zz;;;z;;;;;;zzzzz;;;;z;z;zz;zz
zzzzzz;zzzzzzzz;zzzzzzzzzz;;zz;;zzzzz;;zz;;;;;zzzzz
z;;;zzz;;;zzz;z;zzzzz;zzzzz;;;;;zzz;;;zzzz;zzz;zz;z
;zz;zz;z;z;z;;zz;zz;zzz;z;;z;;z;z;zzz;zz;z;zzz;;z;;
;;;zzz;;;;zzzzz;;;;;;;;z;zzzzzzz;;zzz;zz;zzzzz;;;;;
;;z;;;;z;;;;zzz;zz;z;zzzz;;;;;;z;;zz;zz;;zzzz;;z;;;
z;;zzzzzz;zz;;zz;z;;;;;;;;zzzzz;zz;;zzzzzzzz;;;;;;;
!--------------------------------------------------
!-┌┐-----------------------------------------------
!-└┘-----------------------------------------------
zzz;;;z;zzzzzzzzzzzzz;z;z;z;zzzzz;zzzz;zzzzz;;z;;;;
zzz;;;z;zzzzzzzzzzzzzzzzzzzzzzzzzzzz;z;zzzzzzz;;;;;
zzzzzzz;z;;;;;zzzzzz;;zzzz;;z;;;zzz;;;;zzzzzzzz;;;z
zz;;z;;;;zz;;;;;;;;;;z;;;;zzz;zzzzz;;z;z;;;zzz;zzzz
zz;;;;;zzzzzzzzz;z;;;;;zzzzz;zzzzzzz;;;zzzz;;zz;;zz
z;;zzz;;;zz;;;;;zzzzzz;z;;;;zzzzzzzz;;;zzzzzz;z;zzz
;;zzzzzzzzzzzz;;;;;z;z;z;z;z;;z;z;;;zz;zzzzzz;;;zzz
z;;z;;zz;zzzzz;z;;z;;;zz;;;;z;;;z;;;z;;zzzzz;;zzzzz
''')
emaze18=list('''
;;;;;;zzz;zzzz;;;z;;;;;;;;;;;;;;z;;;;;;zzzzzz;;;;;;
;;;;;;z;;;;;z;z;zz;;;;;;;;;;;;;;;zzzzz;;;;z;z;;z;;;
z;;;;z;;;;zzzzz;;;;;;;zzzz;;zz;;zzzzz;;;;;;;;;;;;;z
z;;;;;;;;;zzz;;;;;;;;;zzzzz;;;;;zzz;;;zzzz;zz;; z;;
;zz;z;;z;z;;;;;z;zz;zzz;z;;z;;;;;;;;;;zz;z;;;;;;z;;
;;;zzz;;;;;;;;;;;;;zzz;;;zzzzzzz;;;;;;zz;z;;zz;;;; 
;;z;;;;z;;;;;;;;zz;z;zzzz;;;;;;z;;;;;zz;;z;;z;;zz;;
z;;zzzzzz;zz;;;;;;;;;;;;;;zzz;;;zz;;;;zzz;;;;;z;;;;
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
zzz;;;z;zzzz;;;;;;;;z;z;z;z;zzzzz;zzzz;;;;;;;;;;;;;
zzz;;;z;;;;;;;;;;;;;zzzz;;;;;;;;;;zz;z;;;;;;;;;;; ;
zzzzzzz;z;;;;;zzzzzz;;zzzz;;z;;;zzz;;;;;;;;;;;z;;;;
zz;;z;;;;zz;;;;;;;;;;z;;;;zzz;zzzzz;;z;z;;;z;;;;;;;
zz;;;;;zzzzzzzzz;z;;;;;zzzzz;zzzzzzz;;;zz;;;;;z;;;;
z;;zzz;;;zz;;;;;zzzzzz;z;;;;zzzzzzzz;;;zzz;;;;z;; ;
;;zz;;;;;;;;;;;;;;;;z;z;z;z;z;;z;z;;;zz;;;;;z;;;;;;
z;;z;;zz;zzzzz;z;;z;;;zz;;;;z;;;z;;;z;;zz;;z;;;; ;;
''')
emaze19=list('''
z;;;;;zzz;;zz ;;;z;;;;;;;zz;; ;;;;;;; ;;;;;; ;;;;  
z;;zz;;;;;;;z;z;;zz;;zz;;;z;;;;;;;;;;;;;;; ;;;;;; ;
;;z;;z;zzz;;;;z;;;;;z;;;zz;;zz;;; ;;;;;; ;;;; ;;;; 
z;;;;; ;;;zzz;;;;;z;z;;;;z;;;;;;;;;;;;;; ;;;;;;;   
;;z;;;;z;;;z;;;;; z;;;z;z;;z;;z;;;; ;;;;;; ;;;;; ;;
;;;;;;;;;;z;;;;;;;;;;;;;;;;;;;;; ;;;; ;;;;;;; ; ; ;
;;;;;;;z;;;;z;;;;;;z;zz;;;;;;;;;;;; ;;;; ;;;;; ;;; 
z;;;;;z;z;;zzz;;;;;;;;;;;;zz;;;;;;;;;;;;;;;;; ; ; ;
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
z;;;;;z;z;;;;;;;zz;;;;z;z; ;;;;;;;;;;;;;;;; ;;; ;; 
;zz;;;z;zzz;;;;;;;;;;zzzz;;;;;;;;;;;;; ;;;;;;;;   ;
zz;zzz;;z;;;;;;z;;;z;;zzzz;;;;; ;;;;;;;;; ;;; ; ;  
zz;;z;;;;zz;;;;;;;; ;z;;;;z;;;;;;;;;;;;;;;; ;;;; ; 
zz;;;;;z;;zzz;;;;z;;;;;zz;;;;;;;;;;;; ;;;;;;  ; ; ;
z;;z;;;;;; ;;;;;zz;;z;;z;;;;z;;;;;;;;; ;;;; ;;;  ; 
;;zz;zz;;;;;;;;;;; z;z;;;z;;;;;;;; ;;;;;;;;;;; ;; ;
;;;z;;;z;zz;;;;;;;;;z;;;;z; ;;;;;;;;;;;;;;;; ;; ;;;
''')
emaze20=list('''
 ;;;;;;; ; ;    ;;;;; ;;;; ;;;; ;;;; ;;;;;;; ;;;   
;; ; ;;;;; ;; ;;;; ; ;;;; ;;;;   ; ;; ;;;;;;    ; ;
; ;; ;;;;; ;;  ;;;;; ;;;; ;;; ; ; ;;;  ;; ;  ;     
  ;;;;;; ;;;;;; ;;; ;;;; ;; ;;;; ;;;  ;;;;; ;      
;;;;; ;;;;; ;; ;;;; ;;;; ;;;; ;;;;  ;;; ;          
;;; ;; ;;;; ;;; ;;; ; ;;;;;     ;;;;;;; ;; ;; ; ;  
;; ; ;; ;;;;;; ;;; ;;; ;;;; ;;;; ; ;;  ;;;; ;  ;   
;;;;;;; ;;; ;; ;; ;;;; ; ;; ;;; ;;;;;;;;z; ;;   ; ;
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
;; ;;;;; ;;;;;;;; ;; ; ;; ;;;  ;; ;;;;;--; ;    ;; 
; ;  ;;; ; ;;; ; ;;; ;;; ;  ;;; ; ;;    ;      ;   
; ;;;; ; ;; ;; ;;; ; ;;;;;   ; ; ;; ;  ;          ;
 ;;;  ;;;;;;; ;  ;;   ;;;; ; ;; ;;;               ;
;; ; ;;;; ; ;;;;  ;;;  ;;;;  ;;   ;;       ;       
;;;; ;; ; ;; ;;; ;;; ;;; ;; ; ;; ;;   ; ;;        ;
;; ;; ; ;;;; ;;;;;;;; ;;;; ;; ; ; ;!!!; ; ;;;  ; ;;
;; z;; ;; ;   ;;; ;; ;;;; ;;; ;; ;    ; ;;; ;;;;   
''')
#chaos, chaos
emaze21=list('''
 ;    ;        ;   ;  ;  ;      ; ; ;;  ; ;; ;  ;  
; ;  ;; ;    ;  ; ;   ;;  ;   ; ;; ;;  ;;; ;;;  ; ;
-┌┐---------------------------------------------; ;
-└┘---------------------------------------------  ;
;; ;  ;;--;--; ;; -- ; ;;  ;;  ;; ;;  ;--; ;       
 ;   ; ;--;--;  ; -- ;  ; ; ;  ;  ;  ; --; ;      ;
        -- -- -; ;--   ; ;  --; ;      --      ;   
        --;---------;    ;-     ;  ;  ;--  ;; ; ;  
;  ; ;-------- --- - ;   -   - ; ;  ;  -     ;   ; 
 ; ;  ------; ;  ;;   ;  ; - -; ;;         ;      ;
 ; ; ; ;; ---; ;  ;;;  ;;;;  -;    ;;   - -  -     
; ;     ; --  ;; ;-- ;;; ;; - ;; ;;   ; ;;         
;       ;--- ;------; ; ;  -- ; ; ;    ;   ;;;  ; ;
     ;   --   --- ---;-------  -;-    ;---- --;;   
  ;      ; -    ----- ---- --;; --;; ;  ;--- ;;-  ;
   ;  ;; ; -- ----------- --;- --- ;; ;;;---    - !
;       ;; ;;  ; ;;- -; ; ---      -   ---- --    !
    ;     ;  ;  ;-- ;  ; ;- ---- --   ----- -      
;       ;    ;   ;;   ;; ;;;; ;  ;   ;; ;          
''')
emaze22=list('''
 ;   ; ; ;      ;    ;  ; ;    ;     ; ; ;;;      ;
;    ; ;   ;            ;   ;  ; ;;      ;    ; ; ;
 ; ; ;    !;    ;    ;  ;       ;    ; ;   ;   ;   
     ;    ! ;   ;    ;    ;;;  ;     ;   ;   ;   ; 
 ; ;      ;             ;  ;    ; ;;     ;;;  ; ;  
;         ;  ;; ;   ;;  ;      ;  ;  ; z   ;;   ; ;
       ; ;;  ;   ;   ;  ; ;;             ; ;  ;;  ;
 ;     ;; ;               ; ;  ;  ;  ;   ;     ;   
          ;               ;    ;  ;      ; ;   ;   
;; ;        ;    ;         ; ;             ;      ;
;         ;  ;       ;               ;   ;  ;    ;;
          ; ;;;      ;  ;      ;     ;   ;     ;   
 ;      ; ;  ;          ;;;       ;       ;;   ;  ;
   ;  ;            ;;;                   ; ;  ;    
; ;     ;;;          ;  ;   ;  ;          ; ;  ;; ;
            ; ;;     ;            ;  ;   ;      ┌┐;
                            ;  ;;               └┘;
 ; ;                 ; ;; ;                  ;; ;  
 ;  ;; ;  ; ;;  ;  ; ;;              ; ;  ;;      ;
''')
emaze21=list(emaze21)
emaze22=list(emaze22)
emaze132=list('''
z;z;;zzzzzzzzzzzzzzzzz;;;zzzzzzzzzzzzzzzzzzzzzzzzzz
z;;;zzzzzzzzzzzzz;;zzzzz;zzzzzzzzzzzzzzzzzzzzzzzz;;
;zz;zzzzzzzzzzzzzzzzzzzz;zzzzzzzzzzzzzzzzzzzzzzzz;z
zzzzzzzzzzzzzzzzzz;;zzzz;;zzzzzzzzzzzzzzzzzzzzzz;;z
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz;;z
zzzzzz;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
zzzzz;;--------------------------------------------
;;zz;;P--------------------------------------------
;z;;z;-------------------------------;;;;;;;;;;;;;;
;;zzz;P----------------------------O;;zzzzzzzzzzzzz
zzzz;;;---------------------------O;;zzzzzzzzzz;zzz
zzzzzz;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;zzzzzzzzzz;;zzz
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz;zz;
zzzzzzzzzzzzzzzzzzz;zzzzzzz;zzzzzzzzzzzzzzz--------
;zzzzzzzzzzzzzzzzz;;z;;zzzz;;zzz;zzzzzzzzzz--------
z;;zzzzzzzzzzzz;;;;;;;;zz;;zzz;zzz;zzzzzzzzzzzzzzzz
;;z;;zzzzzzzzzzzzz;;;zzzzzzzzzz;;zzzzzzzzzzzzzzzzzz
z;;z;;zzzzzzzzzzzzzzzzzzzzzzzz;zz;zzzzzzzzzzzzzzzzz
z;;;;;;zzzzzzzzzzzzzzzzzzzzz;;;;;;;;zzzzzzzzzzzzzzz
''')#row 4, 2


#end easter


d_green='\033[48;5;64m'
yum2='''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXQQQXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX◴◵◶
XXˇˇˇ╤╤╤╤╤╤╤╤╤ˇˇˇ ∛∛∛∛∛∛∛∛∛∛∛∛ ∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜ ♣♣♣♣}}}}}}}♣♣♣♣ ♦♦♦♦♦♦♦♦♦♦♦♦♦[[[)[[[[[[XX
XXˇˇ╤╤╤╤╤╤╤╤╤╤╤ˇˇ ∛∛∛∛∛∛∛∛∛∛∛∛ ∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜ ♣♣♣♣♣||||}}♣♣♣♣ ♦♦♦♦♦♦♦♦♦♦♦♦♦[[[[[[)[)[XX
XXˇ╤╤╤╤╤╤╤╤╤╤╤╤╤ˇ ∛∛∛∛∛∛∛∛∛∛∛∛ ∜∜)))))))))))))))))))))∜ ♣♣♣♣♣||||}}♣♣♣♣ ♦♦♦♦♦♦♦♦♦♦♦♦♦[[[♦♦♦♦♦♦♦XX
XXˇ╤╤╤╤╤≣≣≣╤╤╤╤╤ˇ ∛∛∛∛∛∛∛∛∛∛∛∛ ∜∜)[d[[[[[[[[[[[[[[[w[)∜ ♣♣♣♣♣||||}}♣♣♣♣ ♦♦♦♦♦♦♦♦♦♦♦♦♦[[[♦♦♦♦♦♦♦XX
XXˇ╤╤╤╤╤ˇˇˇ╤╤╤╤╤ˇ ∛∛∛∛∛∛∛∛∛∛∛∛ ∜∜)∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜)∜ ♣♣♣♣}}}}}}}♣♣♣♣ ♦♦♦♦♦♦♦♦♦♦♦♦♦***♦♦♦♦♦!!XX
XXˇ╤╤╤╤ˇˇˇˇˇ╤╤╤╤ˇ ∛∛∛∛∛∛∛∛∛∛∛∛ ∜∜)∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜)∜ ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ ♦♦♦♦♦♦♦♦♦♦♦♦♦***♦♦♦♦♦!!XX
XXˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ ∛∛∛∛∛∛∛∛∛∛∛∛ ∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜g)∜ ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ ♦♦♦♦♦♦♦♦♦♦♦♦♦[[[♦♦♦♦♦♦♦XX
XXˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ ∛∛∛∛∛∛∛∛∛∛∛∛ ∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜g)∜ ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ ♦♦♦♦♦♦♦♦♦♦♦♦♦[[[♦♦♦♦♦♦♦XX
XXˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ ∛∛∛∛∛∛∛∛∛∛∛∛ ∜∜)∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜)∜ ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ ♦♦♦♦♦♦♦♦♦♦♦♦♦[[[[)[[[[[XX
XXˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ ∛∛∛∛∛∛∛∛∛∛∛∛ ∜∜)∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜∜)∜ ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ ♦♦♦♦♦♦♦♦♦♦♦♦♦[[[[)[[[[[XX
XXˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ ∛∛∛∛∛∛∛∛∛∛∛∛ ∜∜)[f[[[[[[[[[[[[[[[L[)∜ ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦XX
XXˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ ∛∛∛∛∛∛∛∛∛∛∛∛ ∜∜)))))))))))))))))))))∜ ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦XX
XX                                                                                             XX
XX♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ♠♠♠♠♠♠♠♠♠♠♠♠ ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺ ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ ♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀XX
XX♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ♠♠♠♠♠♠♠♠♠♠♠♠ ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺ ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ ♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀XX
XX♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ♠♠♠♠♠♠♠♠♠♠♠♠ ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺ ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ ♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀XX
XX♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ♠♠♠♠♠♠♠♠♠♠♠♠ ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺ ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ ♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀k♀♀♀XX
XX♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ♠♠♠♠♠♠♠♠♠♠♠♠ ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺ ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ ♀♀♀♀♀♀♀♀♀♀k♀♀♀♀♀♀♀♀kk♀♀XX
XX♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ♠♠♠♠♠♠♠♠♠♠♠♠ ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺ ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ ♀♀♀♀♀♀♀♀♀♀kk♀♀♀♀♀♀kkkk♀XX
XX♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ♠♠♠♠♠♠♠♠♠♠♠♠ ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺ ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ ♀♀♀♀♀♀♀♀♀♀k~~~``~~~kkk_XX
XX♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ♠♠♠♠♠♠♠♠♠♠♠♠ ☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺☺ ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ ♀♀♀♀♀♀♀♀♀♀k~~~~~~~~kkk_XX
XX♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ♠♠♠♠♠♠♠♠♠♠♠♠ ☺☺☺☺☺☺☺@@@@@☺☺☺☺☺☺☺☺☺☺☺☺ ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ ♀♀♀♀♀♀♀♀♀♀kk♀♀♀♀♀♀kkkk♀XX
XX♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ♠♠♠♠♠♠♠♠♠♠♠♠ ☺☺☺@@@@@@@@@@☺☺☺☺☺☺☺☺☺☺☺ ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ ♀’’’tt’’’♀k♀♀♀♀♀♀♀♀kk♀♀XX
XX♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ♠♠♠♠♠♠♠♠♠♠♠♠ ☺@@@@@@@@@@@@@☺☺☺☺☺☺☺☺☺☺ ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ ♀’’’’’’’’♀♀♀♀♀♀♀♀♀♀k♀♀♀XX
XX♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ ♠♠♠♠♠♠♠♠♠♠♠♠ @@@@@@@@@@@@@@@☺☺☺☺☺☺☺☺☺ ☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻ ♀’’’’’’’’♀♀♀♀♀♀♀♀♀♀♀♀♀♀XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''

yl='\nXXXXXXXXXXXXXXXXXXXXXXXXXXXQQQXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX◴◵◶X'+("\nXX╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳╳XX"*25)+"\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

'''

SIGNS: ╽ ┑ ┓ ┒ ╿


'''

maze1=list('''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXe---╤╤╤╤╤╤╤-----------------------------------
XXXXX---╤╤╤╤╤╤╤╤-----------------------------------
XXXXX--╤╤╤╤╤╤╤╤╤╤╤╤╤╤╤-----------------------------
XXXXX--╤╤╤╤╤╤≣≣≣╤╤╤╤╤╤-----------------------------
XXXXX--╤╤╤╤╤╤---╤╤╤╤╤╤-----------------------------
XXXXX-▒╤╤╤╤╤-----╤╤╤╤╤-----------------------------
XXXXX----------------------------------------------
XXXXX------┑---------------------------------------
XXXXX----------------------------------------------
XXXXX----------------------------------------------
---------------------------------------------------
---------------------------------------------------
XXXXX-R--------------------------------------------
XXXXX----------------------------------------------
XXXXX----------------------------------------------
XXXXX----------------------------------------------
XXXXX----------------------------------------------
''') #easter (the part for u)
themine=list('''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
######╤╤XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
╤╤╤╤-╤╤#-----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
-----#╤--------------------XXXXXXXXXXXXXXXXXXXXXXXX
╤╤╤-╤╤╤╤#---------------------------XXXXXXXXXXXXXXX
╤╤╤╤╤╤╤╤#╤-----------------------------XXXXXXXXXXXX
╤╤╤╤╤╤╤╤╤╤##-------------------------------XXXXXXXX
!----------*--------------------------------XXXXXXX
!----------*--------------------------------XXXXXXX
!----------*--------------------------------XXXXXXX
!----------*---------------------------------XXXXXX
╤╤╤╤╤╤╤╤╤╤#╤----------------------------------XXXXX
╤╤╤╤╤╤╤╤╤╤-----------------------------------------
╤╤╤╤╤╤╤##------------------------------------------
---╤##╤╤--------------------------------------XXXXX
---#╤╤╤-------------------------------------XXXXXXX
╤╤╤╤#╤╤╤-----------------------------XXXX   XXXXXXX
#╤╤#####----------XXXXXXXXXXXXXXXXXXXXXXX u XXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
''')
maze2=list('''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!!!!!XXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXQQQQQXXXXXX
--------------------------------------4------e-----
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
''')
maze3=list('''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
---------------------------------------------------
---------------------------------------------------
-----------------------4---------------------------
------------))))))))))))))))))))))-----------------
------------)[d[[[[[[[[[[[[[[[[w[)-----------------
-----------┓)-------------------“))----------------
------------)--------------------)))---------------
--------------------------------g))!---------------
--------------------------------g))!---------------
--------------------------------g))!---------------
------------)--------------------)))---------------
------------)-------------------O))----------------
------------)[f[[[[[[[[[[[[[[[[L[)-----------------
------------))))))))))))))))))))))-----------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
''')
maze4=list('''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
----------4------------}}}}}}}--&---&---&----------
------------------------||||}}---------------------
------------------------||||}}---------------------
------------------------||||}}---------------------
--------------------┒--}}}}}}}---------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
''')
maze5=list('''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
-----------------------------------[[[)[[[[[[[XXXXX
-----------------------------------[[[[[[[)[)[XXXXX
-----------------------------------[[[---v----XXXXX
-----------------------------------[[[--------XXXXX
-----------------------------------***------!!XXXXX
-----------------------------------***------!!XXXXX
-----------------------------------[[[--------XXXXX
-----------------------------------[[[--4-----XXXXX
-----------------------------------[[)[[[[[[)[XXXXX
-----------------------------------[[[[)[[[[[[XXXXX
-----------------------------------╽----------XXXXX
---------------------------------------------eXXXXX
----------------------------------------------XXXXX
----------------------------------------------XXXXX
----------------------------------------------XXXXX
----------------------------------------------XXXXX
----------------------------------------------XXXXX
''')
maze6=list('''
XXXXX----------------------------------------------
XXXXX----------------------------------------------
XXXXX----R-----------------------------------------
XXXXX----------------------------------------------
XXXXX----------------------------------------------
XXXXX----------------------------------------------
XXXXX----------------------------------------------
XXXXX----------------------------------------------
XXXXX----------------------------------------------
XXXXX----------------------------------------------
XXXXX----------------------------------------------
XXXXX----------------------------------------------
XXXXX----------------------------------------------
XXXXF----------------------------4-----------------
XXXXX-┌┐-------------------------------------------
XXXX--└┘-------------------------------------------
XXXXZ----------------------------------------------
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
''')
maze7=list('''
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
--------------------------U------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
------------------------------------O--------------
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
''')
maze8=list('''
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
----------------@@@@@------------------------------
------------@@@@@@@@@@-----------------------------
----------@@@@@@@@@@@@@----------------------------
-------╿-@@@@@@@@@@@@@@@--------------------e------
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
''')
maze9=list('''
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
--------------------------------P------------------
----------------e----------------------------------
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
''')
maze10=list('''
----------------------------------------------XXXXX
----------------------------------------------XXXXX
----------------------------------------------XXXXX
----------------------------------------------XXXXX
----------------------------------------------XXXXX
----------------------------------------------XXXXX
----------------------------------------------XXXXX
----------------------------------------------XXXXX
-------------------------------------k--------XXXXX
----------------------------k--------kk-------XXXXX
----------------------------kk------kkkk------XXXXX
----------------------------k~~~``~~~kkk_-----XXXXX
----------------------------k~~~~~~~~kkk_-----XXXXX
----------------------------kk------kkkk------XXXXX
-----------’’’’ttt’’’’------k--------kk-------XXXXX
-----------’’’’’’’’’’’---------------k--------XXXXX
-----------’’’’’’’’’’’-----------------------eXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
''')
cavem1=list('''
##;################################################
######;#################################;#;;;;;#;##
≣--┌┐---------;####;▒----------------R###---E---###
≣--└┘---------;##;##-----------------####-------###
###---#;####--###;#;----##;#;####----#;#;-------;##
#;#---######--#;####----####;###;----####-------###
#;#---###;##--####;#----#;####;##----####O-----O###
###----------------------#######;----;###;#GGG#####
##-----------------------#;####;#---4######GGG#####
;#----###########;#####---##;#####;#####;##GGG#####
########;####;#####;###-----------------------;####
#######################-----------------------#####
######;############;##-----#####;#############;####
###########;####;#####-----#########;#######;######
#######;#-----------------------------------------≣
#######;#-----------------------------------------≣
#####;##########;######;##########;#######;########
#####;#########;#######;#############;#############
''')
#98% sure the ' ' next to the 9s is un needed but idrc
cavem2=list('''
#############;####;######;######;#####;#;##########
###########;####;###;###;####;#####;#####;##;######
##--A--###;----------------------------------;#####
#P-----P###----------------------------------#;####
##-----###;---###;#########;######-----##;##;######
##-----9999  ##;######;#####;#####-----###;###;####
##-----9999--#####;###4----###;###-----;###########
######;###;--##;####;#-----#;###;#-----##;#########
#;#;#--------#########---------------------------~~
##;#;--------#;###;###---------------------------~~
#;###O-------##########;###;#####;#################
####;##;###---#;####;##;###;###;#####;#############
##;####;###---##;####;###;####;########;###########
###;#;###;#----------------------###;#####;=;######
≣--┌┐-------------------------------------------###
≣--└┘-------------------------------------------###
##;######;#######;####;######;##;##;######;####;###
######;##########;#######;#######;#####;####;######
''')

#some symbols: ┌┐└┘◓○▒╦╇⎾⏋⎿⏌┬┬╚╝╔╕≣

#Miner moment
#h is chest, _ is light
Mining=list('''
╦;╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦;╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦;╦╦╦╦╦╦╦╦╦╦╦
╦╦╦╦;╦╦╦╦╦;╦╦╦╦╦╦╦╦;╦╦╦╦╦╦╦;╦╦╦╦╦╦╦╦╦╦╦;╦╦╦╦╦╦;╦╦╦╦
╦╦╦;-----[--------[-------------[--------[----▒╦╦╦;
╦;╦╦-----[-------___-----------___-------[-----╦╦╦╦
╦╦;╦----___-----------------------------___----╦;╦╦
╦╦╦╦-------------------------------------------╦╦╦╦
╦╦;╦-------------------------------------------╦╦╦;
╦╦╦╦-------------------------------------------╦╦╦╦
╦╦╦;-------------------------------------------;╦╦╦
~~┌┐---------------------------------------------~~
~~└┘---------------------------------------------~~
╦╦╦;-------------------------------------------;╦╦╦
;╦╦╦-------------------------------------------╦╦╦╦
╦╦╦╦-------------------------------------------╦╦╦╦
╦;╦╦---------------------------------------4---╦╦;╦
╦╦╦╦-----------_--------╔╕--------_------------╦╦╦╦
╦╦╦╦hh---------[--------╚╝--------[------------╦;╦╦
;╦╦╦╦╦╦╦╦╦;╦╦╦╦╦╦╦;╦╦╦╦;╦╦;╦╦╦╦╦╦╦╦╦╦╦╦;╦╦╦╦╦╦╦╦╦;╦
╦╦;╦;╦╦╦╦╦╦╦╦;╦╦╦╦╦;╦╦╦╦╦;╦╦╦╦╦╦╦╦;╦╦╦╦╦;╦╦╦╦╦╦╦;╦╦
''')
lanc1=list('''
666666666666744444476666666666744444476666666666666
666666666666674444766666666666674444766666666666666
666666666666674444766667777666674444766666666666666
666677777766674444766677887766674444766677777766666
666778888776674444766678888766674444766778888776666
666788888876674444766778888776674444766788888876666
667788888877674444767788888877674444767788888877666
667888888887674444767888888887674444767888888887666
667777777777674444767777777777674444767777777777666
666666666666674444766666666666674444766666666666666
666666666666674444766666666666674444766666666666666
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---┌┐----------------------------------------------
---└┘----------------------------------------------
---------------------------------------------------
---------------------------------------------------
''')
lanc2=list('''
666666666666744444476666666666744444476666666666666
666666666666674444766666666666674444766666666666666
666667777666674444766666666666674444766667777666666
666677887766674444766677777766674444766677887766666
666678888766674444766778888776674444766678888766666
666778888776674444766788888876674444766778888776666
667788888877674444767788888877674444767788888877666
667888888887674444767888888887674444767888888887666
667777777777674444767777777777674444767777777777666
666666666666674444766666666666674444766666666666666
666666666666674444766666666666674444766666666666666
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---┌┐----------------------------------------------
---└┘----------------------------------------------
---------------------------------------------------
---------------------------------------------------
''')
lanc3=list('''
666666666666744444476666666666744444476666666666666
666666666666674444766666666666674444766666666666666
666666666666674444766667777666674444766666666666666
666677777766674444766677887766674444766677777766666
666778888776674444766678888766674444766778888776666
666788888876674444766778888776674444766788888876666
667788888877674444767788888877674444767788888877666
667888888887674444767888888887674444767888888887666
667777777777674444767777777777674444767777777777666
666666666666674444766666666666674444766666666666666
666666666666674444766666666666674444766666666666666
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---┌┐----------------------------------------------
---└┘----------------------------------------------
---------------------------------------------------
---------------------------------------------------
''')
lanc4=list('''
666666666666744444476666666666744444476666666666666
666666666666674444766666666666674444766666666666666
666667777666674444766666666666674444766667777666666
666677887766674444766677777766674444766677887766666
666678888766674444766778888776674444766678888766666
666778888776674444766788888876674444766778888776666
667788888877674444767788888877674444767788888877666
667888888887674444767888888887674444767888888887666
667777777777674444767777777777674444767777777777666
666666666666674444766666666666674444766666666666666
666666666666674444766666666666674444766666666666666
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---┌┐-----------------------------------------┬┬---
---└┘-----------------------------------------└┘---
---------------------------------------------------
---------------------------------------------------
''')
lanc6=list('''
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
MMM⎾⏋MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM┬┬MMM
MMM⎿⏌MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM⎿⏌MMM
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
''')
lanchm=list('''
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
777777777777777777777777777777777777777777777777777
''')
lanc55=list('''
666666666666744444476666666666666666666666666666666
666╱◝◝◝◝◝◝666744447666666666666666╱◝◝◝◝◝◝◝◝◝◝◝◝◝◝66
666666666666674444766667777666666666666666666666666
666677777766674444766677☼☼7766666666666677777766666
66677☼☼☼☼77667444476667☼☼☼☼76666666666677☼☼☼☼776666
6667☼☼☼☼☼☼7667444476677☼☼☼☼7766666666667☼☼☼☼☼☼76666
6677☼☼☼☼☼☼776744447677☼☼☼☼☼☼776666666677☼☼☼☼☼☼77666
667☼☼☼☼☼☼☼☼7674444767☼☼☼☼☼☼☼☼7666666667☼☼☼☼☼☼☼☼7666
667777777777674444767777777777666666667777777777666
666666666666674444766666666666666666666666666666666
666666666666674444766666666666666666666666666666666
-----------------------------------e-------◔◔◔◔◔◔◔◔
-----------------------------------e---◔-◔◔◔◔◔◔◔◔◔◔
-----------------------------------e----◔◔◔◔◔◔◔◔◔◔◔
-----------------------------------e----◔◔◔◔◔⎾⏋◔◔◔◔
---┌┐------------------------------e--◔◔◔◔◔◔◔╘╛◔◔◔◔
---└┘------------------------------e---◔◔◔◔◔◔◔◔◔◔◔◔
-----------------------------------e---◔◔◔◔◔◔◔◔◔◔◔◔
-----------------------------------e-----◔◔◔◔◔◔◔◔◔◔
''')
easterblack=lanchm.copy() #easter
#W = pickaxe, color = \033[48;5;254m 
Mining2=list('''
###################################################
###################################################
####----------------------------;###TTTTTTTTT----!!
###O---------------------------##;##-TTTWTTT-----!!
##;#######;###----########----#;##;#--TTTTT------!!
####----------------#;#;#-----#;#;;#-------------##
##;#4----------------##;------;#;####;;;;######;;##
#######;###;##----;#;#####----#;;----------------##
#;##;####;###;----;###;###----##;----------------##
~~┌┐-----------------------------------##;;##----~~
~~└┘---------------------------------------#;----~~
#;###;#####---;-----;############;####;##;#;#######
###;#####;----#---------;#;####;-----------------##
########;##;;##--------;;;###;##-----------------##
##########;###;-----###########;----;##;#;#;;###;##
##########---##---------------------------------###
##########---##---------------------------------P##
################;########;#########;###############
###################################################
''')
Mining3=list('''
###################################################
###################################################
!!---------------------------------------4------###
!!----------------------------------------------###
!!----------------------------------------------###
###-------;###-----##;#;-----####;-----#;###----###
##;-------###;-----#;##;-----#;###-----;####----###
###-------#;##-----#;###-----####;-----#####----###
#;#-------####-----###;#-----#;###-----##;;#----###
~~┌┐--------------------------------------------TTT
~~└┘--------------------------------------------TTT
###----;###-----#####-----;##;##;#-----#####----###
###----#;#;-----#####-----;####;#;-----;####----###
###---------------------------------------------###
###---------------------------------------------###
###----;##;-----#####;----#;####;#-----;##;#----###
###----#;#;-----;#;#T#UUUU#T##;###-----#;#;;----###
################;#####UUUU#########;###############
###################################################
''')
newthing1=list('''
###################################################
###################################################
#####-----------▒-------------------------------TTT
####--------------------------------------------###
###---------------------------------------------###
###---------------------------------------ggggggg☼#
###-------------------------------------gggGGGGGG##
###------------------------------------gGGGGG7GGG##
###-----------------------------------gGGGGGG7GGG##
TT-┌┐---------------------------------gGGGGGGGGGG##
TT-└┘---------------------------------gGGGGGG7GGG##
###-----------------------------------gG77777GGGG##
###------------------------------------ggGGGGGGGG##
###--------------------------------------gggggggg☼#
###---------------------------------------------###
####-------------------------------------------####
#####-----------------------------------------#####
################;########;#########;###############
###################################################
''')
newthing2=list('''
###################################################
###################################################
###################################################
#######################################---------###
##################################--------------###
################################-----------ggggg###
###############################---------gggGGGGG###
##############################--------ggGGGGG7GGK##
###----------------------------------gGGGGGGG7GGK##
TT-┌┐--------------------------------ggggGGGGGGGK##
TT-└┘-----------------------------------gG7777GGK##
###-------------------------------------ggGGGGGG###
##############################-----------ggggggg###
###############################-----------------###
################################----------------###
################################TT#####---------###
################################TT#################
################################TT#################
###################################################
''')
newthing3=list('''
########################TTT########################
########################TTT########################
########################---########################
###################-------------###################
################-------------------################
############-------------┌┐------------############
###########--------------└┘-------------###########
##########-------------------------------##########
##########-------------------------------##########
##########-------------------------------##########
##########-------------------------------##########
##########-------------------------------##########
####-----#-------------------------------#-----####
###----------------ggggggggggggg----------------###
###----------------gGGG77777GGGg----------------##!
###-KK☼KKKK☼KK----ggGGG7GGG7GGGgg---------------##!
###-☼☼☼☼☼☼☼☼☼☼---ggGG7GGGGGGG7GGgg----------○---###
###-KK☼KKKK☼KK-##########☼#################◓◓◓#####
###################################################
''')

labm1=list('''
[][[[[[[][[)[[[[[[[[[[[[[)[[[[))[[[[][[[[[[][[)[[][
!--┌┐--------------------------------------v[[][[[[
!--└┘---------------------------------------[[[[[)[
][[)[[][[[[[][[)[[[[[)[[][[)[[][[[-----[[[[)[[[[[)[
[[[[[[][[)[[[[[)[[][[)[[[[[[[[][[)-----[][[[[[[[[[[
[[[------------------------------2-----[][[)[[][[)[
[[B------------------------------2-----[[[[)[[[[[)[
[[[------------------------------2-----[][[)[[][[)[
][[)[[][[[[[[[[[[[][[)[[[[[[[[][[)-----[[[[[[[][[[[
[[[)[[[[O)[[][[[[[[[[)[[R[[)[[[[[)-----[][[[[[[[[)[
[[[------------------------------:--------------[[[
[[[------------------------------:-------------▒[[[
[[[------------------------------:--------------[[[
[[[[[P[------------------------[[)-----[][[[[[][[)[
][[)[[[[[)[[][[)[[][[[[[][[)[[[[[[-----[[[[)[[][[[[
[[P------------------------------:-----[][[)[[[[[)[
[[[------------------------------:-----[][[[[[[[[)[
[[[[[[[------------------------R[[!!!!![][[)[[][[)[
][[)[[][[)[[[[[[[[[[[[[[][[)[[][[)[[[]][[[[[[[[][[[
''') 
labm2=list('''
)[[)!!!!!!)[[)yyyyy)[[)mmmmm)[[)ooooo)[[)$$$$$$)[[)
)[[)------)[[)-----)[[)-----)[[)-----)[[)------)[[)
)[[)--┌┐--)[[)-----)[[)-----)[[)-----)[[)------)[[)
)[[)--└┘--)[[)-----)[[)-----)[[)-----)[[)------)[[)
)[[)------)[[)-----)[[)-----)[[)-----)[[)------)[[)
)[[)------)[[)-----)[[)-----)[[)-----)[[)------)[[)
)[[)------)[[)-----)[[)-----)[[)-----)[[)-------[[)
)[[)------)[[)-----)[[)-----)[[)-----)[[)-------[[)
)[[)------)[[)-----)[[)-----)[[)-----)[[)------R[[)
)[[)------)[[)-----)[[)-----)[[)-----)[[)-------[[)
)[[)------)[[)-----)[[)-----)[[)-----)[[)------O[[)
)[[)------)[[)-----)[[)-----)[[)-----)[[)------)[[)
)[[)------)[[)-----)[[)-----)[[)-----)[[)------)[[)
)[[)------)[[)-----)[[)-----)[[)-----)[[)--//--)[[)
)[[)------)[[)-----)[[)-----)[[)-----)[[)╇╇╇╇╇╇)[[)
)[[)------)[[)-----)[[)-----)[[)-----)[[)╇╇╇╇╇╇)[[)
)[[)------)[[)-----)[[)-----)[[)-----)[[)555555)[[)
)[[)yyyyyy)[[)mmmmm)[[)ooooo)[[)$$$$$)[[)[[[[[[)[[)
''')
Portal=list('''
)[[)!!!![][][][][][][][][][][][][][][][][][][][)[[)
)[[)!!!![][][][][][][][][][][][][][][][][][][][)[[)
)[[)--------------------------------------------J[)
)[[)--------------------------------------------JJ)
)[[)--------------------------------------------JJ)
)[[)--------------------------------------------JJ)
)[[)--------------------------------------------JJ)
)[[)--------------------------------------------JJ)
)[[)--------------------------------------------JJ)
)[[)--------------------------------------------JJ)
)[[)--------------------------------------------JJ)
)[[)--------------------------------------------JJ)
)[[)--------------------------------------------JJ)
)[[)--------------------------------------------JJ)
)[[)--------------------------------------------JJ)
)[[)--------------------┌┐----------------------JJ)
)[[)--------------------└┘----------------------J[)
)[[)[][][][][][][][][][][][][][][][][][][][][][)[[)
)[[)[][][][][][][][][][][][][][][][][][][][][][)[[)
''')

HEAHE=list('''
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
’’’’                         7777777           ’’’’
’’’’                      77777777777777777777 ’’’’
’’’’                     777777777777777777777 ’’’’
’’’’                    7╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸777   ’’’’
’’’’                   7╸╸╸77777╸77777╸╸╸╸7    ’’’’
’’’’                   7╸╸7ppppp7yyyyy7╸╸╸7    ’’’’
’’’’                   7╸╸7ppppp7yyyyy77777    ’’’’
’’’’                7777╸╸╸77777╸777777╸╸╸╸7   ’’’’
’’’’           777777╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸7   ’’’’
’’’’          77╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸7╸╸╸╸╸╸╸7   ’’’’
’’’’           7777777777╸╸╸77777777╸╸╸╸╸╸7    ’’’’
’’’’                    7╸╸╸╸7RRRR7╸╸╸╸╸╸7     ’’’’
’’’’                    7╸╸╸╸╸7777╸╸╸╸╸77      ’’’’
’’’’                     77777777777777        ’’’’
~~~~  ┌┐                                       ’’’’
~~~~  └┘                                       ’’’’
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
''')
HEAHE2=list('\n’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’\n’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’'+("\n’’’’                                           ’’’’"*16)+'\n’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’\n’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’')
hehe=HEAHE.copy() #for checking
festivehall=list('''
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
’’’’’’’’’’’’’’’’’KKKK☼KKK☼☼KKK☼KKKK’’’’’’’’’’’’’’’’
’’’’’’’’’’’’---------------------------’’’’’’’’’’’’
’’’’’’K’-----------------------------------’’’’’’’’
’’’’’’’-------------------------------------K’’’’’’
’’’’’’’-------------------------------------☼’’’’’’
’’’’’’’-------------------------------------’’’’’’’
’’’’’KK-------------------------------------’’’’’’’
’’’’’’’-------------------------------------’’’’’’’
’’’’’’’-------------------------------------KK’’’’’
’’’’’’’-------------------------------------’K’’’’’
’’’’’K’-------------------------------------’’’’’’’
’’’’’’’-------------------------------------’’’’’’’
’’’’’’’-------------------------------------☼’’’’’’
’’’’’’K------------------┌┐-----------------’’’’’’’
’’’’’’’’-----------------└┘----------------’K’’’’’’
’’’’’’’’’’-------------------------------’’’’’’’’’’
’’’’’’’’’’’’’’[[[K[[[K[[[[[[[[[[[K[[’’’’’’’’’’’’’’’
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
''')
Shed=list('''
’’’’’’’’’’’’’’’’’’’ttttttttttttt’’’’’’’’’’’’’’’’’’’
’’’’’’’’’’’’’’’’’’’ttttttttttttt’’’’’’’’’’’’’’’’’’’
’’’’O-----------------------------------------O’’’’
’’’’---R-----------------------------------P---’’’’
’’’’-------------------------------------------’’’’
’’’’-------------------------------------------’’’’
’’’’-------------------------------------------’’’’
’’’’-------------------------------------------’’’’
’’’’--------------------┌┐---------------------’’’’
’’’’--------------------└┘----------------------ñññ
’’’’--------------------------------------------ñññ
’’’’-------------------------------------------’’’’
’’’’-------------------------------------“-----’’’’
’’’’---------“---------------------------------’’’’
’’’’-------------------------------------------’’’’
’’’’------------------------------------------▒’’’’
’’’’v-----------------------4-----------------v’’’’
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
''')
Shed2=list('''
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
’’’’-------------------------------------------’’’’
’’’’-------------------------------------------’’’’
’’’’-------------------------------------------’’’’
’’’’-----------------------------------------];’’’’
’’’’---------------------------------------];];’’’’
’’’’---------------------------------------;;;]’’’’
’’’’----------------------------------------[[[’’’’
ñññ--┌┐------------------------------------é[[[’’’’
ñññ--└┘-------------------------------------[[[’’’’
’’’’---------------------------------------];;]’’’’
’’’’---------------------------------------;]];’’’’
’’’’-----------------------------------------];’’’’
’’’’-------------------------------------------’’’’
’’’’-------------------------------------------’’’’
’’’’“------------------------------------------’’’’
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
''')
#sacrifice room
theroom=list("""
[[[[[[[[[[[[[[[[[[[[[[[>>>>[[[[[[[[[[[[[[[[[[[[[[[[
[[[[[[a[[[[[[[[[b[[[[[[<<<<[[[[c[[[[[[[[[[[['[[[[[[
[[[[[[[[[[[[[[[[[[[[[[[(((([[[[[[[[[[[[[[[[[[[[[[[[
[[[[xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx][[)
[[[[-------------------------------------------][[)
[[[[-------------------------------------------][[[
[[[[-------------------------------------------[[[[
[[[[-------------------------------------------[[[[
[[[[-------------------------------------------][[[
[[[[-------------------------------------------][[[
[[[[-------------------------------------------[[[)
[[[[-------------------------------------------[[[[
[[[[-------------------------------------------][[[
[[[[-------------------------------------------][[[
[[[[-----------------------------------------┌┐][[)
[[[[-----------------------------------------└┘[[[)
[[[[-------------------------------------------][[[
[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[!!!!!!![[[[
[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[!!!!!!!][[)
""")
theTruth=list("""
╦╦@@@@╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦!!!╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦@@
╦@@@@╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦!!!╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦@
╦@@@╦╦╦╦╦╦╦╦---------------------------╦╦╦╦╦╦╦╦╦╦╦╦
@@@@╦╦╦╦╦---------------------------------╦╦╦╦╦╦╦╦╦
@@@╦╦╦╦╦-----------------------------------╦╦╦╦╦╦╦╦
@@╦╦╦╦---------------------------------------╦╦╦╦╦╦
@@╦---------------------------------------------╦╦╦
@╦╦---------------------------------------------╦╦╦
╦╦╦---------------------------------------------╦╦@
╦╦╦----------------------D----------------------╦@@
╦╦╦---------------------------------------------╦╦@
╦╦╦---------------------------------------------╦╦╦
╦╦╦╦-------------------------------------------╦╦╦╦
╦╦╦╦╦-----------------------------------------╦╦╦╦╦
@@╦╦╦╦╦-------------------------------------╦╦╦╦╦╦╦
@@╦╦╦╦╦╦╦---------------------------------╦╦╦╦╦╦╦╦╦
@@@╦╦╦╦╦╦╦-------------------------------╦╦╦╦╦╦╦╦╦╦
@@@@╦╦╦╦╦╦╦╦╦╦-----------------------╦╦╦╦╦╦@@@@╦╦╦╦
@@@╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦!!!╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦@@@@@@╦╦╦
""")
theLake=list('''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;
;;@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;#;;#
#;;#;@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;;;####
##;#;;#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;;;######
#####----------------------------------------######
####-------------------------------------------####
###---------------------┌┐------------------4---###
###---------------------└┘----------------------###
;;;---------------------------------------------###
!!----------------------------------------------###
!!----------------------------------------------###
;;;;------------------------------------------O####
#####v----------------------------------------#####
#########--------------------------------O#########
################“--------C--------“################
###################################################
###################################################
''') 
theLake2=list('''
@@@@@;###;;;;;;;;@@@;;###;;@@@@@@@@;##########;@@@;
@@@@;;####;;;;;;;@@@@;;;;@@@@@@@@@;###########;@@@;
@@@@;######;!!!;;;@@@@@;@@@@@@@@@;;##########;@@@;#
@@@;;######;###;#;;@@@@@@@@@@@@@;##########;;@@@;##
@@@;#######;;##;##;;;;;;;;;@@@@;#########;;@@@@;###
@@;;#######;---;#########;;@@@;;;;;;;;;;;;@@@;;;###
;;;########;---;##########;@@@@@@@@@@@@@@@@;;;#####
###########;---;##########;;@@@@@@@@@@;;;;;########
###########;---;###########;;;;;;;;;;;;############
############---;###################################
############----------------------------------┌┐-!!
;;##########----------------------------------└┘-!!
@;;;########..#####################################
@@@@;;##            ;;;;;;;;;;;;;;;;;;;;###########
;@@@@@;;            ;@@@@@@@@@@@@@@@@@@;;;;########
;;;@@@@@;     ╥    ;@@@@@@@@@@@@@@@@@@@@@@;;;######
##;;;;@@@;#######;;@@;;;;;;;;;;@@@@;;;;@@@@@;;;####
####;;;@@@;#####;;@@;;;;####;;;;@@;;##;;;@@@@@;####
''') 
#Was suposed to be a dev secret never really tried to make it tho 
#Since i didnt make it i will avenge luci by making monke
devyboi=list('''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;
;;@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;#;;#
#;;#;@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;;;####
##;#;;#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@;;;######
#####----------------------------------------######
####-------------------------------------------####
###---------------------┌┐----------------------###
###---------------------└┘----------------------###
;;;---------------------------------------------###
------------------------------------------------###
------------------------------------------------###
;;;;------------------------------------------O####
#####v----------------------------------------#####
#########--------------------------------O#########
################“--------C--------“################
###################################################
###################################################
''') 
#The Truth (only true gamers can make it to this point)
#all hackers will see da ez
Modulea=list("""
[[;;;;#######################################;;;;[[
;;;;##33333############!!!!!#############33333#;;;;
;;####3##############!!!!A!!!!##############3####;;
######33333########!!!!!!!!!!!!!###########3#######
######3#########;]]]]]]]]]]]]]]]]];#######3########
######33333;]]]]]]---------------]]]]]]];33333#####
#######;]]]]]--------------------------]]]];#######
####;]]]]---------------------------------]]]];####
###]]]---------------------------------------]]]###
###]-------------------------------------------]###
###]---------------------┌┐--------------------]###
###]---------------------└┘--------------------]###
###]-------------------------------------------]###
###]-------------------------------------------]###
###]-------------------------------------------]###
###]]]---------------------------------------]]]###
####;]]-------------------------------------]];####
#####;]]]]]]]]]]]]][[[;!!!!!;[[[]]]]]]]]]]]];######
######################;!!!!!;######################
""")
Boss1=list("""
╳##################################################
###################################################
####-------------------------------------------####
####-------------------------------------------####
####-----##############33333##############-----####
####-----##############33333##############-----####
####-----##############33333##############-----####
####-----##############33333##############-----####
####-------------------------------------------!!!!
####-------------------------------------------!!!!
####-------------------------------------------!!!!
####-----##############33333##############-----####
####-----##############33333##############-----####
####-----##############33333##############-----####
####-----##############33333##############-----####
####-┌┐----------------------------------------####
####-└┘----------------------------------------####
###################################################
###################################################
""")
Boss2=list("""
╳##################################################
###################################################
###################################################
##################-----------------------##########
#################-------------------------#########
#################-------------------------#########
#################----------3333####--------########
#################---------33333#####--------#######
#################----------3333######--------######
#################------------33######----------!!!!
##################------------3#######---------!!!!
#####################----------####################
######################---------####################
#######################---------###################
#######################--------####################
####-┌┐------------------------####################
####-└┘-----------------------#####################
###################################################
###################################################
""")
Boss3=list("""
╳##################################################
###################################################
###################################################
#################################--------##########
################################----------#########
###############################------------########
##############################------###-----#######
##############################-----#####----#######
##############################-----#####----#######
##############################-----#####----#######
##############################-----#####----#######
###############-------------##-----#####!!!!#######
###############-------------33-----################
###############----#####-----------################
###############----#####-----------################
####-┌┐------------3333333333######################
####-└┘------------3333333333######################
###################################################
###################################################
""")
Boss4=list("""
╳##################################################
###################################################
###################################-------------###
###################################-------------###
########################---------##---3333333---###
########################---------##---3333333---###
########################---------##---#######---###
########################----##---##---#######---###
################------------##---##---#######---###
################------------##---##---#######---###
################33333###----##--------#######---###
########-------------###----##--------#######---###
########-------------###----##--------#######---###
########----#####----###----#################---!!!
########----#####-----------#################---!!!
########-┌┐-#####-----------#################---###
########-└┘-#################################---###
###################################################
###################################################
""")
Boss5=list("""
╳##################################################
####################################┋┋┋┋┋┋┋┋┋┋┊####
####################################┋┋┋┋┋┋┋┋┋┋┊####
####################################┋┋┋┋###########
####################################┋┋┋┋###########
####################################┋┋┋┋###########
######-------------------------#####┋┋┋┋###########
######-------------------------#####┋┋┋┋###########
######----33333333333333333-------------###########
######----33333333333333333-------------###########
######----##########################╫╫╫╫###########
######----##########################╫╫╫╫###########
######-┌┐-##########################╫╫╫╫###########
######-└┘-##########################╫╫╫╫###########
####################################╫╫╫╫###########
####################################╫╫╫╫###########
####################################╫╫╫╫###########
####################################!!!!###########
###################################################
""")
Boss6=list("""
###################################╪╪╪╪╪##########╳
###################################╪╪╪╪╪###########
333################################╪╪╪╪╪###########
!!--------------------------------------###########
!!-----------------------------------┌┐-###########
!!-----------------------------------└┘-###########
!!--------------------------------------###########
!!--------------------------------------###########
!!--------------------------------------###########
!!--------------------------------------###########
!!--------------------------------------###########
!!--------------------------------------###########
!!--------------------------------------###########
!!--------------------------------------###########
!!--------------------------------------###########
!!--------------------------------------###########
!!--------------------------------------###########
333################################################
###################################################
""")
Boss7=list("""
###################################################
###################################################
###################################################
####################--------------------###########
################----------------------------------╳
###########---------------------------------------╳
###-----------------------------------------------╳
#!!-----------------------------------------------╳
#!!--------------------------------------┌┐-------╳
#!!--------------------------------------└┘-------╳
#!!-----------------------------------------------╳
###-----------------------------------------------╳
##########----------------------------------------╳
##############------------------------------------╳
################----------------------------------╳
####################--------------------###########
###################################################
###################################################
###################################################
""")
Boss8=list("""
###################################################
###################################################
###################################################
##------------#####################################
##------------#####################################
##------------#####################################
##----3333----#########-----------------###########
##----3333----########-------------------##########
##----####----########-----33333333--------┌┐-----╳
##----####----########----##########-------└┘-----╳
##----####----########----#########################
##----####----########----#########################
##----####----------------#########################
##----####----------------#########################
##----#############################################
##----#############################################
##!!!!#############################################
###################################################
###################################################
""")
Boss9=list("""
╳#################################################╳
###################################################
######################---┌┐---#####################
#####################----└┘----####################
####################------------###################
################--------------------###############
###############----------------------##############
###############------3########3------##############
###############-----33########33-----##############
###############-----33########33-----##############
###############-----33########33-----##############
###############-----33########33-----##############
###############-----33########33-----##############
###############------3########3------##############
###############----------------------##############
################--------------------###############
######################--------#####################
#######################!!!!!!######################
###################################################
""")
Boss10=list("""
╳#################################################╳
###################################################
######################---┌┐---#####################
######################---└┘---#####################
######################--------#####################
######################--------#####################
######################--------#####################
######################--------#####################
######################--------#####################
######################--------#####################
######################--------#####################
######################--------#####################
######################--------##########3##########
######################--------#########3####3######
######################--------#########3###########
######################--------#########3####3######
######################--------##########3##########
######################!!!!!!!!#####################
###################################################
""")
ast='\033[0m\033[0m\033[0m\033[0m' #for stalling purposes lol
#The Truth ending, only true true gamers make it here
#x,x,x,4,5,6,7,8,9,10,11,12,13,14 
dialogue1_1="Y'know ever since I got out of that capsule this corner has intrigued me."+ast+'\nSuch detail. Nothing like what you see in that thing.' #find dias
dialogue1_2='I mean sure its a corner but its a cool one alright.'+ast+'\nAnyway I don\' know what to do so let me be.'+R+"\n(She returns to staring at the wall...)"
dialogue2_1='Yo what the hell this looks just like the lab.'+ast+'\nCmon man, I was litterally picking up Module B when you let us all out.'+ast+"\nSame wall color, but it's weirdly.... real, I guess."+ast+'\nEven the blue of the capsule, its just so real and like look...'+R+'\n(You decide to leave before he keeps speaking...)'
dialogue2_2='(Hes still muttering something.)'+ast+"\n(Something about Module D and a key.)"
dialogue3_1='whats good man'+ast+'\nim guessing you are the person who let us all out by the way you move'+ast+'\nthanks for that dude thats like totally rad'
dialogue3_2='wait why does no one else move...'+ast+'\nwhy dont i move???'+ast+'\n(You expect him to move, but he doesn\'t...)'
dialogue4_1='Hey '+name+" whats up!!"+ast+'\nYou\'re like totally cool man!'+ast+'\nMy only request is you don\'t erase me out of existance...'
dialogue4_2='Well you \033[38;5;12mcan\'t'+R+' do that by going below me and moving up into me.'+ast+'\nYou \033[38;5;12mcan\'t'+R+' do it with items too, \nI \033[38;5;12mdidn\'t'+R+' find that out when going for the raft ending and lost my paddle...'+ast+'\nHorrible game please fix you stupid muffin developer.'
dialogue5_1='Thats like a pretty cool terminal thing right there.'+ast+'\nIt says its a map of the island but like cmon even the generator lights are on'+ast+'\nIm pretty sure its like a projection of your version of the island or something idk'
dialogue5_2='Then again items dont appear other than the guaranteed ones...'+ast+'\nIt\'s as if the maker just decided to reuse some stuff'+ast+'\nNo shot the developers that lazy right?'
dialogue6_1='i just saw someone straight go through that door....'+ast+"\ni know you need "+bold+"The Key"+R+" but like what"+ast+"\nthat door is client side or soemthing like bro wth" 
dialogue6_2='i mean i was gonna get the key but its kinda annoying...'+ast+'\ntbh the game in the capsule was fun tho like cmon it even got updates'+ast+'\ni hope im not a box in a bigger game that would be uncool'
dkey1='\033[38;5;21mno shot your like so cool god damn\033[38;5;21m\033[38;5;21m\ni thought i had seen it all since like the halloween event but god damn\033[38;5;21m\033[38;5;21m\nyou like totally destroyed my record bro even i couldnt do that'+R
dkey2='\033[38;5;21mlike bro i got all the achievements\033[38;5;21m\033[38;5;21m\nsince day 1 everythings been so easy bro i got em all\033[38;5;21m\033[38;5;21m\nbut god damn you just did like the coolest thing\033[38;5;21m\033[38;5;21m\nngl i kinda liked that place tho i even got my own achievement lol'+R
dpor1='hihihih '+name+" is a cool name being honest"+ast+'\nim pretty sure thats the way out, but like...'+ast+'\n(She stops speaking)'
dpor2='(She looks at you, then back at the opening)'
dialogue3_1_1 = f"yk i really thought that this whole real life thing would actually be cool bro\ni was so mad at that stupid plane it actually sucks\nHOW DOES THIS GAME THINK I CAN JUST FLY IT!{ast}\nbut anyway i get kicked out of the game cause of you thanks btw\nbut then i wake up and its just the same thing without the water and like more techy things{ast}\nlike i swear to god if theres aggressive stuff outside like in the game."
dialogue3_1_2 = "wait what is outside? you been out there yet\nthis is outside right?\nwait what is real\nIS THIS ALL STILL A SIMULATION AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
dialogue3_2_1 = "I'm pretty sure you're the one who set us free right? Thank you!\nI have to say though, that game was FUCKING DOGSHIT HOLY SHIT LOL\nEVERYTIME I TRIED TO DO THAT BOSS FIGHT I WOULD GET THAT IMPOSSIBLE ATTACK AND JUST BE LEFT AT 1 HP LIKE WTF YOU WANT ME TO DO BRO??????\nABSOLUTE SHIT DEVELOPER DUDE WHAT A BITCH"
dialogue3_2_2 = "wait actually\nwho is the developer?\nwhy has no one thought of this who tf put us in there\nwho are the scientists man i read all the lore on those note scrap thingies it was cool and all but still\nwho was actually behind all this????\nthey must be hiding behind a handle or something, theres a few secrets that mention something like 'the muffin man'\ni dont know what a muffin is, but im guessing its not a good thing\nor maybe it could be something like a very tasty pastry that british people abuse the word of, i dont know."
t1_1='This is dirt right?'+ast+' At least thats what I heard...'+ast+'\nIma be real kinda looking like The Shed walls.'+ast+'\nAnd that blue stuff... literally the exact same as The Lake.'+ast+'\nSimilarities everywhere I guess.'
t1_2='The sky too... everything but the silence reminds me of the ocean.'+ast+'\nAnd the grass, kinda looks like Module E, and the....'+ast+'\n(You can tell that he\'s been in the capsule a little too long)'
t31_1='Look at how big they are...'+ast+"\nI used to know so much about these things... at least I think."+ast+"\nNow, I don't even know the name of them."
t31_2='So many types, so many connections.'+ast+'\nDo you know trees "talk" to each other?'+ast+"\nTrees! Thats the word.\n"+ast+'(She seems excited about her rediscovered knowledge)'
l1_1='I think this little passage way just opened...'+ast+'\nMost likely cause of you :)'
l1_2='But thats weird... How could that open because of you?'+ast+'\nWAIT NO SHOT BRO ITS GOD HES GOD BROOOOO'
l2_1='Pretty sure im supposed to be up there with those guys...'+ast+'\ngod damn it'
l2_2='(Hes moving?'+ast+' If so, very very slowly)'
tolook4={
  'TheOne1':['⊡⋄⎔⎚','▀▁▂▃'],
  'TheOne2':['█▉▊▋','⊞⊟⊠░'],
  'TheOne3':['⊡⋄⎔⎚',"▀▁▂▃"],
  'TheOne4':['⊞⊟⊠░'],
  'TheOne5':['▄▅▆▇'],
  'TheOne6':['⊡⋄⎔⎚'],
  'KeyRoom':['▀▁▂▃'],
  'True1':['█▉▊▋'],
  'True2':[],
  'True3':['▄▅▆▇'],
  'True4':['█▉▊▋','▄▅▆▇','▀▁▂▃','⊡⋄⎔⎚','⊞⊟⊠░'],
}

#FIX DIALOGUE THING

thedictionwords={
  '⊡⋄⎔⎚':{'theone1':0,'theone3':0,'theone6':0,"TheOne3":[dialogue3_1_1,dialogue3_1_2],'TheOne1':[dialogue1_1,dialogue1_2],'TheOne6':[dialogue6_1,dialogue6_2]},
  '▀▁▂▃':{'theone1':0,'theone3':0,'keyroom':0,"TheOne3":[dialogue3_2_1,dialogue3_2_2],'TheOne1':[dialogue2_1,dialogue2_2],'KeyRoom':[dkey1,dkey2]},
 '█▉▊▋':{'theone2':0,'true1':0,'true4':0,'TheOne2':[dialogue3_1,dialogue3_2],'True1':[t1_1,t1_2],"True4":[l1_1,l1_2]},
  '⊞⊟⊠░':{'theone2':0,'theone4':0,'TheOne2':[dialogue4_1,dialogue4_2],'TheOne4':[dpor1,dpor2]},
  '▄▅▆▇':{'true3':0,'true4':0,'theone5':0,'True3':[t31_1,t31_2],"True4":[l2_1,l2_2],'TheOne5':[dialogue5_1,dialogue5_2]},
}
TheOne1=list("""
[][[)[[[[[)[[][[)[[[[[[[[[[[)[[][[)[[[[[[[[][[)[[][
[[[[)[[[[[[[[][[[[[[[[)[[][[)[[[[[[[[][[)[[[[[)[[[[
[][[[[[][[[[[[[[)[[][[)[[][[[[[][[)[[][[)[[][[[[[][
[][[-----------------[[◌◌◌◌▀▁◌◌◌◌╊╊◌◌◌◌⊡⋄◌◌◌◌█▉◌◌◌◌
[[[[-----------------[[◌◌◌◌▂▃◌◌◌◌╊╊◌◌◌◌⎔⎚◌◌◌◌▊▋◌◌◌◌
[][[-----------------[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[
[][[-----------------------------------------------
[][[-----------------------------------------------
[[[[-----------------------------------------------
[][[-----------------------------------------------
[][[-----------------------------------------------
[[[[-┌┐--------------------------------------------
[][[-└┘--------------------------------------------
[][[-----------------------------------------------
[][[-----------------------------------------------
[][[-----------------------------------------------
[[[[)[[[[[)[[[[[[[[][[)[[[[[)[[][[)[[[[[)[[][[[[[][
[][[[[[][[)[[][[)[[][[)[[][[[[[][[[[[][[)[[[[[)[[][
[][[)[[[[[[[[[[[)[[][[[[[][[)[[[[[)[[[[[[[[][[)[[][
""")
TheOne2=list("""
[][[)[[[[[)[[][[)[[[[[[[[[[[)[[][[)[[[[[[[[][[)[[][
[[[[)[[[[[[[[][[[[[[[[)[[][[)[[[[[[[[][[)[[[[[)[[[[
[][[[[[][[[[[[[[)[[][[)[[][[[[[][[)[[][[)[[][[[[[][
◌◌◌◌◌⊞⊟◌◌◌◌◌◌◌⊡⋄◌◌◌◌◌◌◌▀▁◌◌◌◌◌◌◌◌▄▅◌◌◌◌◌◌◌◌█▉◌◌◌◌◌◌
◌◌◌◌◌⊠░◌◌◌◌◌◌◌⎔⎚◌◌◌◌◌◌◌▂▃◌◌◌◌◌◌◌◌▆▇◌◌◌◌◌◌◌◌▊▋◌◌◌◌◌◌
[[[[[]][[[[[[[]][[[[[[[]][[[[[[[[]][[[[[[[[]][[[[[[
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
[][[-----------------------------------------------
[][[-----------------------------------------------
[[[[-----------------------------------------------
""")
TheOne3=list("""
[][[)[[[[[)[[][[)[[[[[[[[[[[)[[][[)[[[[[[[[][[)[[][
[[[[)[[[[[[[[][[[[[[[[)[[][[)[[[[[[[[][[)[[[[[)[[[[
[][[[[[][[[[[[[[)[[][[)[[][[[[[][[)[[][[)[[][[[[[][
◌◌◌◌◌⊡⋄◌◌◌◌◌◌◌⊞⊟◌◌◌◌◌◌◌█▉◌◌◌◌◌◌◌◌▄▅◌◌◌◌◌◌◌◌▀▁◌◌◌◌◌◌
◌◌◌◌◌⎔⎚◌◌◌◌◌◌◌⊠░◌◌◌◌◌◌◌▊▋◌◌◌◌◌◌◌◌▆▇◌◌◌◌◌◌◌◌▂▃◌◌◌◌◌◌
[[[[[]][[[[[[[]][[[[[[[]][[[[[[[[]][[[[[[[[]][[[[[[
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
---------------------------------------------------
-----------------------------------------------[[][
-----------------------------------------------[[][
-----------------------------------------------[[][
""")
TheOne4=list("""
[][[)[[[[[)[[][[)[[[[[[[[[[[)[[][[)[[[[[[[[][[)[[][
[[[[)[[[[[[[[][[[[[[[[)[[][[)[[[[[[[[][[)[[[[[)[[[[
[][[[[[][[[[[[[[)[[][[)[[][[[[[][[)[[][[)[[][[[[[][
◌◌◌[[------------------------------------------[[][
◌◌◌[[------------------------------------------[[[[
[[[[[------------------------------------------[[][
-----------------------------------------------[[!!
------------------------------------------------!!!
------------------------------------------------!!!
------------------------------------------------!!!
------------------------------------------------!!!
------------------------------------------------!!!
-----------------------------------------------[[!!
-----------------------------------------------[[[[
-----------------------------------------------[[][
-----------------------------------------------[[[[
[[[[)[[[[[)[[[[[[[[][[)[[[[[)[[][[)[[[[[)[[][[[[[][
[][[[[[][[)[[][[)[[][[)[[][[[[[][[[[[][[)[[[[[)[[][
[][[)[[[[[[[[[[[)[[][[[[[][[)[[[[[)[[[[[[[[][[)[[[[
""")
TheOne5=list("""
[[[[-----------------------------------------------
[][[-----------------------------------------------
[][[-----------------------------------------------
[[[[-----------------------------------------------
[][[-----------------------------------------------
[][[-----------------------------------------------
[][[-----------------------------------------------
[][[-----------------------------------------------
[][[-----------------------------------------------
[[[[-----------------------------------------------
[][[-----------------------------------------------
[][[-----------------------------------------------
[[[[-----------------------------------------------
[][[-----------------------------------------------
[[[[-------------------------’’’’’’’’’’’’’---------
[][[-------------------------’’’@@@!@@@’’’---------
[[[[)[[[[[)[[[[[)[[][[)[[[[[)[[][[)[[][[[[[][[)[[][
[][[[[[][[)[[][[)[[[[[[[[][[[[[][[[[[][[[[[[[[)[[][
[[[[[[[[[[[[[][[[[[][[[[[][[[[[][[)[[[[[)[[][[[[[[[
""")
#Structure thing will be a map of the island, easter egg go brrrrrr
yum='''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XX---╤╤╤╤╤╤╤╤╤--------------------------------------------------}}}}}}}-&-&-&--------[[[)[[[[[[XX
XX--╤╤╤╤╤╤╤╤╤╤╤--------------------------------------------------||||}}--------------[[[[[[)[)[XX
XX-╤╤╤╤╤╤╤╤╤╤╤╤╤-----------------)))))))))))))))))))))-----------||||}}--------------[[[-------XX
XX-╤╤╤╤╤≣≣≣╤╤╤╤╤-----------------)[d[[[[[[[[[[[[[[[w[)-----------||||}}--------------[[[-------XX
XX-╤╤╤╤╤---╤╤╤╤╤-----------------)-------------------)----------}}}}}}}--------------***-----!!XX
XX-╤╤╤╤-----╤╤╤╤-----------------)-------------------)-------------------------------***-----!!XX
XX--------------------------------------------------g)-------------------------------[[[-------XX
XX--------------------------------------------------g)-------------------------------[[[-------XX
XX-------------------------------)-------------------)-------------------------------[[[[)[[[[[XX
XX-------------------------------)-------------------)-------------------------------[[[[)[[[[[XX
XX-------------------------------)[f[[[[[[[[[[[[[[[L[)-----------------------------------------XX
XX-------------------------------)))))))))))))))))))))-----------------------------------------XX
XX---------------------------------------------------------------------------------------------XX
XX---------------------------------------------------------------------------------------------XX
XX---------------------------------------------------------------------------------------------XX
XX---------------------------------------------------------------------------------------------XX
XX-------------------------------------------------------------------------------------k-------XX
XX----------------------------------------------------------------------------k--------kk------XX
XX----------------------------------------------------------------------------kk------kkkk-----XX
XX----------------------------------------------------------------------------k~~~``~~~kkk_----XX
XX----------------------------------------------------------------------------k~~~~~~~~kkk_----XX
XX------------------------------------@@@@@-----------------------------------kk------kkkk-----XX
XX--------------------------------@@@@@@@@@@-----------------------’’’tt’’’---k--------kk------XX
XX------------------------------@@@@@@@@@@@@@----------------------’’’’’’’’------------k-------XX
XX-----------------------------@@@@@@@@@@@@@@@---------------------’’’’’’’’--------------------XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''


TheOne6=list("""
-----------------------------------------------[[[[
-----------------------------------------------[[][
-----------------------------------------------[[][
-----------------------------------------------[[[[
-----------------------------------------------[[][
-----------------------------------------------[[][
-----------------------------------------------[[[[
-----------------------------------------------[[][
-----------------------------------------------[[][
---------------------------------A--B--C--D--E-[[][
---------------------------[[[[[[[[[[[[[[[[[[[[[[[[
---------------------------[[][[[[[][[[[][[[[][[[][
-----------------------------------------------[[][
-----------------------------------------------!!!!
-----------------------------------------------!!!!
-----------------------------------------------[[][
[[[[)[[[[[)[[[[[[[[][[)[[[[[)[[][[)[[[[[)[[][[[[[[[
[][[[[[][[)[[][[)[[][[)[[][[[[[][[[[[][[)[[[[[)[[][
[][[)[[[[[[[[[[[)[[][[[[[][[)[[[[[)[[[[[[[[][[)[[][
""")

#Idk what this is, pretty sure only epic chad gamers can access it
KeyRoom=list("""
[[[[)[[[[[][[[[[[[[][[)[[[[[[[[][[)[[[[[)[[][[[[[[[
[[[[[[[[[[)[[[[[)[[[[[][[[[[)[[][[)[[[[[)[[][[[[[][
[[[[][[[[[)[[[[[)[[][[)[[[[[)[[)[[[[[[[[[[[][[[[[[[
[][[-◠◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝◝[[[[
[[[[-------------------------------------------[[][
[][[------------------------------------------{[[][
[][[-------------------------------------------[[[[
[[[[---┌┐-------------------------------------V[[][
!!!!---└┘--------------------------------------[[][
!!!!------------------------------------------+[[][
[][[-------------------------------------------[[[[
[][[------------------------------------------p[[][
[][[-------------------------------------------[[][
[][[-------------------------------------------Z[][
[][[-------------------------------------------Z[][
[[[[---------0--q--^--“--%--1--&--r--I--l--=---[[][
[[[[)[[[[[)[[[[[[[[][[)[[[[[)[[][[)[[[[[)[[][[[[[[[
[][[[[[][[)[[][[)[[][[)[[][[[[[][[[[[][[)[[[[[)[[][
[][[)[[[[[[[[[[[)[[][[[[[][[)[[[[[)[[[[[[[[][[)[[][
""")

True1=list('''
@@’’’eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee’’’’@
@’’’’’eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee’’’@@
@’’’’’---------------------------------------’’’’’@
’’’’’-----------------------------------------’’’’’
’’’’’-----------------------------------------’’’’’
’’’’’’-----------------------------------------’’’’
’’’’’------------------------------------------’’’’
’’’’-------------------------------------------’’’’
’’’’-------------------------------------------’’’’
’’’’’-----------------------------------------’’’’’
’’’’’---------------------------------------’’’’’’’
’’’’’’’-------------------------------------’’’’’’’
’’’’’’’-----------------------------------’’’’’’’’’
’’’’’];[;---------------------------------;[;]’’’’’
’’’;;;[;]][-------------┌┐---------------][[;];;’’’
];;]]][[]]]]------------└┘------------[[]]][]]];];]
;][;]][]][];[[]]------------------;;[]]]];]][[[][]]
[][][]]][][][][][][!!!!!!!!!!!![][[[][][[[][][][][[
][][[[][][][]]][][!!!!!!!!!!!!!![][][][][][[[][][][
''')
True2=list('''
’’’’’’’’’’’’eeeeeeeeeeeeeeeeeeeeeeeeeee’’’’’’’’’’’’
’’’’’’’’’’’eeeeeeeeeeeeeeeeeeeeeeeeeeeee’’’’’’’’’’’
’’’’’’’’’’-------------------------------’’’’’’’’’’
’’’’’’’’’--------------------------------’’’’’’’’’’
’’’’’’’’’---------------------------------’’’’’’’’’
’’’’’’’’---------------------------------’’’’’’’’’’
’’’’’’’------------------------------------’’’’’’’’
’’’’’’’’-----------------------------------’’’’’’’’
’’’’’’’’------------------------------------’’’’’’’
’’’’’’’-------------------------------------’’’’’’’
’’’’’’’-------------------------------------’’’’’’’
’’’’’’--------------------------------------’’’’’’’
’’’’’’’------------------------------------’’’’’’’’
’’’’’’---------------------------------------’’’’’’
’’’’’’------------------┌┐------------------’’’’’’’
’’’’’’’-----------------└┘-----------------’’’’’’’’
’’’’’’’’-----------------------------------’’’’’’’’
@@@’’’’’’eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee’’’’’’’’’
@@@@’’’’’’’eeeeeeeeeeeeeeeeeeeeeeeeeeeee’’’’’’’’’’@
''')
True3=list('''
’’’’eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee’’’
───’’eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee’’──
────’-----------------------------------------’’───
───’’-----------------------------------------’’’──
’’’’’------------------------------------------’’’’
─’’’’------------------------------------------’’’─
──’’------------------------------------------’’’──
─’’’------------------------------------------’’’’─
’’’’------------------------------------------’’’’’
──’’’-----------------------------------------’’’──
───’’-----------------------------------------’’───
──’’’----------------------------------------’’’’──
’’’’’’---------------------------------------’’’’’’
’────’’-----------------┌┐------------------’’────’
──────’-----------------└┘-----------------’’──────
’────’’’-----------------------------------’’’────’
’’’’’’’’-----------------------------------’’’’’’’’
’’’’’’’’’eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee’’’’’’’’’
’’’’’’’’eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee’’’’’’’’
''')
blue1='\033[48;5;26m'
blue2='\033[48;5;32m'
blue3='\033[48;5;38m'
True4=list('''
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
’’’’’’’’’’’’’’’’----;;;;;;;;;;----’’’’’’’’’’’’’’’’’
’’’’’’’’’’----------;--’’’’--;----------’’’’’’’’’’’
’’’’’’’’’-OR╦╦╦RO---;;;;;;;;;;---OR╦╦╦RO-’’’’’’’’’’
’’’’’’’’--OR╦╦╦RO----------------OR╦╦╦RO--’’’’’’’’’
’’’’’’’eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee’’’’’’’’
’’’’’’’------------------------------------’’’’’’’’
’’’’’’---------------------------------------’’’’’’
’’’’’’----------------------------------------’’’’’
’’’’’’----------------------------------------’’’’’
’’’’’-----------------------------------------’’’’’
┄┄┄┄┄----------------------------------------’’’’’’
┄┄┄┄┄┄---------------------------------------’’’’’’
’’’’’’’-----------------┌┐------------------’’’’’’’
’’’’’’’-----------------└┘-----------------’’’’’’’’
’’’’’’’’-----------------------------------’’’’’’’’
’’’’’’’’-----------------------------------’’’’’’’’
’’’’’’’’’eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee’’’’’’’’’
’’’’’’’’eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee’’’’’’’’
''')
True5=list('''
────────----------------’’’’’────’’’’’’’’’’’’’’’’’’
───────-----------────--’’’’──────’’’’’’’’’’’’’’’’’
────’’’’’--------──────-’’’’’────’’’’’’’’’’’’’’’’’’
’’’’’’’’’’’’’’’’--────-’’’’’’’’’’’’’’’’’’’’’’’’’’’’
’’’’’’-------’’’’’’’’’’’’’’----’’’’’’’--’----’’’’’’
’’’’’-----------------------------------------’’’’’
’’’’’-----------------------------------------’’’’’
’’’’’’---------------------------------------’’’’’’
’’’’’’’---------------------------------------’’’’’
’’’’’╭╮---------------------------------------’’’’’
’’’’-╰╯---------------------------------------’’’’’
’’’’’’’-------------------------------------┌┐---ee
’’’’’’--------------------------------------└┘---ee
’’’’’’--------------------------------------’’’’’’’
’’’’’’’------------------------------------’’’’’’’’
’’’’’’’’’------------------------------------’’’’’’
’’’’’’’’’’’’’’-------’’’’’’’’’’’’-----------’’’’’’’
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’’
''')
Lesgo=list("""
[][[[[[][[)[[][[)[[][[)[[][[[[[][[[[[][[)[[[[[)[[][
[[[[)[[[[[◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘[[][[[[[[[
[][[[[[][[)[[][[)[[][[)[[][[[[[][[[[[][[)[[[[[)[[][
[]⊖⊖⊖⊖⊖⊖⊖⊖⊖⊖⊖⊖⊖⊖⊖⊖⊖⊖⊖⊖⊖⊖⊖[⊘⊘⊘⊘⊘⊘⊘⊘⊘⊘⊘⊘⊘⊘⊘⊘⊘⊘⊘⊘⊘⊘⊘][
[[⊖⊖-------------------------------------------⊘⊘[[
[]⊖⊖-------------------------------------------⊘⊘][
[]⊖⊖-------------------------------------------⊘⊘][
[[⊖⊖-------------------------------------------⊘⊘[[
[]⊖⊖-------------------------------------------⊘⊘][
[]⊖⊖-------------------------------------------⊘⊘][
[]⊖⊖--------------------┌┐---------------------⊘⊘][
[]⊚⊚--------------------└┘---------------------⊙⊙][
[[⊚⊚-------------------------------------------⊙⊙[[
[]⊚⊚-------------------------------------------⊙⊙][
[]⊚⊚-------------------------------------------⊙⊙][
[]⊚⊚-------------------------------------------⊙⊙][
[]⊚⊚-------------------------------------------⊙⊙][
[[⊚⊚-------------------------------------------⊙⊙[[
[[⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚⊚[⊙⊙⊙⊙⊙⊙⊙⊙⊙⊙⊙⊙⊙⊙⊙⊙⊙⊙⊙⊙⊙⊙⊙[[
[][[[[[][[)[[][[)[[][[)[[][[[[[][[[[[][[)[[[[[)[[][
""")



playinref='''
 wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwR\n wgwwggggggggggggggggggggggggggggggggggggggggggggggggggggwwwwwR\n wwwg____________________________________________________gggwwR\n wgg__~_______~_______~_______~_______~_______~_______~____ggwR\n wwg_____________________________________________________ggggwR\n wwwg____________________________________________________gwwgwR\n wwwg_~_______~_______~_______~_______~_______~_______~__ggwwwR\n wgwg_____________________________________________________gwgwR\n wgg______________________________________________________ggwwR\n wg___~_______~_______~_______~_______~_______~_______~___wgwwR\n wwg_____________________________________________________ggwwwR\n wgwg____________________________________________________gwgwwR\n wwwg_~_______~_______~_______~_______~_______~_______~__gwwgwR\n wwwg____________________________________________________gwwgwR\n wwwwggggggggggggggggggggggggggggggggggggggggggggggggggggggwwwR\n wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwR'''
playinref=list(playinref)
#Yes im hiding these variables down here so no one can see the stupidly long lists lol (Dont show this to anyone know whos how to make a list or else they will die of cringe)

#this looks like ["1:00",'1:01','1:02',...............,"12:59"] (idk why i didnt start at 12 or like 6 lol)
timez = [f"{i}:{i2:0>{2}}" for i in range(1,13) for i2 in range(0,60)]

miniA=[
213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,
265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,
317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,
369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,
421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,
473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,
525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545]
miniB=[235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567]
miniD=[577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,
629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,
681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,
733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,
785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,
837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,
889,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909]
miniC=[599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931]

YL='''\nooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\no----------------------GGGGGGGGGGGGG--------------------------o\no--------------------GGGGGGGGGGGGGGGG-------------------------o\no--------------------GbbbbbbbbbbbbbGGG------------------------o\no--------------------bbbbbbbbbbbbbbbGG------------------------o\no--------------------bbbWWWbbbbWWWbbbB------------------------o\no--------------------bbbbbbbbbbbbbbbbB------------------------o\no---------------------bbbbbbbbbbbbbbB-------------------------o\no---------------------BbbbmmmmmbbbBB--------------------------o\no----------------------BbbbbbbbbbBB---------------------------o\no-----------------------BBBBBBBBBBb---------------------------o\no-------------------nnnnbbbbbbbbbbbnnn------------------------o\no---------------nnnnnnnnnnnnnnnnnnnnnnn-----------------------o\no--------------nnnnnnnnnnnnnnnnnnnnnnnnn----------------------o\no--------------nnnnnnnnnnnnnnnnnnnnnnnnnnn--------------------o\no-------------nnnnnnnnnnnnnnnnnnnnnnnnnnnnn-------------------o\no-------------nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn------------------o\no-------------nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn------------------o'''
YS='''\nooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\no--__gggwwgg_--------rrGGGGGGGGGGGGGr---------------__gwg__---o\no--__ggwwwgg_-------rGGGGGGGGGGGGGGGGr--------------_gwwgg_---o\no--__gwwggg_--------rGBbbbbbbbbbbbBGGGr------------__ggwwg_---o\no--__ggwwggg_-------rBBBBBBbbbBBBBBBGGr-----------__gggwwg_---o\no--__gggwwwg__------rbbbWWWbbbbWWWbbbr------------_ggwwwgg_---o\no--__ggggwwgg_------rbbbbbbbbbbbbbbbbr----------___gwwwgg__---o\no-__gggwwwwgg_------rrbbbbbbbbbbbbbbrr----------_ggwgwwgg__---o\no-__ggwwwgggg_-------rrbbbmmmmmbbbBrr----------__gwwggwwgg__--o\no-__gggwwwgg_---------rrBbbbbbbbBBBr-----------__gwwgggwwgg__-o\no-__ggggwwwgg_-----rrrrnBBBBBBBBBbbrrr-----_____ggwwgggwgwgg_-o\no--_gggwwggg_--rrrrrnnnnnbbbbbbbbbnnnnrr____gggggwwwggwggwwgg_o\no-_gggwwgg____rrnnnnnwwwwwwnnnnnnnnnnnnrrggggwwwwggwgwggggwwggo\no__ggwwgggggggrnnwwwwwwwwwwwwwwwnnnnnnnnrrwwwwggggggwggg_ggwwwo\no__gwwggggggwwwwwwwnnnnnnnnnnnwwwwnnnnnwwwwrrggggwwwwwwgg_ggggo\no_gggwwwwwwwwwwnnnnnnnnnnnnnnnnnnwwwwwwwnnnnrwwwwwwgggwwgg___-o\no-_gggwwgggggrnnnnnnnnnnnnnnnnnnnnnnwwwwwwwwwggggggg_ggwwgg_--o\no-__gggggg___rnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnrgg_______ggwwg_--o'''
'''

easter notes (kinda outdated but sure your here why not read em)

---------1---2---3---4---------------
-------------------------------------
---------5---6--B7--D8---------------
-------------------------------------
---------9--10--11--12--17--18--19---
-------------------------------------
--132---13A-14--15C-16---------------

- add a tp someone that like changes current to 200
- A:   start is 13, the bottom mid
- B:   7 has new ending (door from 6?) the shapes
- C:   15 has guy
- D:   8 has guy2
- SOMEWHERE add 17, 18 [19,20?] (The Dark End)


emaze is the entrance, cool easter egg that took too many lines probably lol

z = green maze color  ; = substantional amount of texture
Z = note in emaze1    n = door to the temple, need color



H = easter egg
N = easter egg spawns

⍨      
'''






#----------------------------------------------------------------
#----------------------------------------------------------------
#-------------                                      -------------
#-------------              NOTES.PY                -------------
#-------------                                      -------------
#----------------------------------------------------------------
#----------------------------------------------------------------


def s(jh):
  try:
    if achievements[jh]==True or achievements[jh]=='1':
      return '\033[48;5;46m'+' '+R
    else:
      return '\033[48;5;160m'+" "+R
  except:
    return '\033[48;5;160m'+" "+R

achieve5alt='''
┌────────────────────────────────────────────────┐
|                     \033[38;5;88mLOCKED\033[0m                     |
|---|----------------------------------------|---|
|---|----------------------------------------|---|
|---|----------------------------------------|---|
|---|----------------------------------------|---|
|---|----------------------------------------|---|
└────────────────────────────────────────────────┘
'''
achieve5='''
┌────────────────────────────────────────────────┐
|                       It.                      |
|---\033[48;5;196m \033[0m----------------------------------------\033[48;5;208m \033[0m---|
|------------------------------------------------|
|          Can you experience the \033[38;5;12mTruth\033[0m?         |
|------------------------------------------------|
|---\033[48;5;74m \033[0m----------------------------------------\033[48;5;82m \033[0m---|
└────────────────────────────────────────────────┘
'''
achieve5true=f'''
┌────────────────────────────────────────────────┐
|                 \033[38;5;18mThe True Truth\033[0m                 |
|                      Done.                     |
|{"You, "+name+" are them.":^48}|
|\033[48;5;196m                                                \033[0m|
|\033[48;5;208m                                                \033[0m|
|\033[48;5;126m       And they say this game is hard :)        \033[0m|
|\033[48;5;74m                                                \033[0m|
|\033[48;5;82m                                                \033[0m|
└────────────────────────────────────────────────┘
'''
def updateq(): #idk it doesnt work lol
  global achieve1,achieve2,achieve3,achieve4,achieve5_1,achieve5_2,achieve5_3,achieve5_4
  achieve1='''
  ┌────────────────────────────────────────────────┐
  |                  Achievements      (easy ones) |
  |------------------------------------------------|
  |Horrible Game - Die                            '''+s('Horrible Game')+'''|
  |------------------------------------------------|
  |Pro fix - Completely fix the powerplant        '''+s('Pro fix')+'''|
  |------------------------------------------------|
  |minecraft - bro wth bro this isnt minecraft    '''+s('minecraft')+'''|
  |------------------------------------------------|
  |Bang - Use the revolver                        '''+s('Bang')+'''|
  |------------------------------------------------|
  |Rip bozo - Kill '''+bold+'''him'''+R+'''                            '''+s('Rip bozo')+'''|
  |------------------------------------------------|
  |Escape? - Find a way out                       '''+s('Escape?')+'''|
  |------------------------------------------------|
  |Raft -  A way out?                             '''+s('Raft')+'''|
  |The Lab -  A way out?                          '''+s('The Lab')+'''|
  |The Plane -  A way out?                        '''+s('The Plane')+'''|
  |The Cart -  A way out?                         '''+s('The Cart')+'''|
  └────────────────────────────────────────────────┘
  '''
  achieve2='''
  ┌────────────────────────────────────────────────┐
  |                  Achievements      (hard ones) |
  |------------------------------------------------|
  |What's this? - Find the room                   '''+s('What\'s this?')+'''|
  |------------------------------------------------|
  |Live on - Cheat death                          '''+s('Live on')+'''|
  |------------------------------------------------|
  |Overclock - power level over 200!1!111!        '''+s('Overclock')+'''|
  |------------------------------------------------|
  |Escape. - Find THE way out                     '''+s('Escape.')+'''|
  |------------------------------------------------|
  |Sped - Escape., but in 1 day                   '''+s('Sped')+'''|
  |------------------------------------------------|
  |New feature pog - Find the minigame            '''+s('New game pog')+'''|
  |------------------------------------------------|
  |Poggers - Get 3,000 points in the minigame     '''+s('Poggers')+'''|
  |------------------------------------------------|
  |Big lure - Get all 9 notes                     '''+s('Big lure')+'''|
  └────────────────────────────────────────────────┘
  '''
  achieve3='''
  ┌────────────────────────────────────────────────┐
  |                  Achievements           (bruj) |
  |------------------------------------------------|
  |ok - wow how cool you found it                 '''+s('ok')+'''|
  |------------------------------------------------|
  |classic - how cool useless secret #2           '''+s('classic')+'''|
  |------------------------------------------------|
  |afk - a masterpiece, i know                    '''+s('afk')+'''|
  |(hint: can only be done before entering game)   |
  |------------------------------------------------|
  |??? - Get the 10th Note                        '''+s('???')+'''|
  |------------------------------------------------|
  |luci - look at this m o n k e                  '''+s('luci')+'''|
  |------------------------------------------------|
  |loser - imagine losing to a kid                '''+s('loser')+'''|
  └────────────────────────────────────────────────┘
  '''
  achieve4='''
  ┌────────────────────────────────────────────────┐
  |                  Achievements        (\033[38;5;88mYS\033[0mN\033[38;5;88mKYSN\033[0m) |
  |------------------------------------------------|
  |lanc - "ok" ~ the only real npc in the game    '''+s('lanc')+'''|
  |------------------------------------------------|
  |lanc2 - "yskysn" ~ dont return.                '''+s('lanc2')+'''|
  |------------------------------------------------|
  |LYS - guys, love yourself                      '''+s('LYS')+'''|
  |------------------------------------------------|
  |True chad - average no heal enjoyer            '''+s('True Chad')+'''|
  |lean destroyer - stop what you started         '''+s('LEAN')+'''|
  |Double takedown - window needs a nerf lowkey   '''+s('Double takedown')+'''|
  |YSLYSN - The TRUE ending, good luck...         '''+s('YSLYSN')+'''|
  └────────────────────────────────────────────────┘
  ''' 
  #omgomgOGMgmgmg
  #to add more events, add a next achieve4 thing and change the numbers at the 'find achievements' to increase by one
  achieve5_1='''
  ┌────────────────────────────────────────────────┐
  |\033[48;5;202m(halloween)       Achievements     (true chaos) \033[0m|
  |------------------------------------------------|
  |Bat - '''+'\033[38;5;13m'+'''YOU TOOK THE         [Deal]'''+R+'''              '''+s('Bat')+'''|
  └────────────────────────────────────────────────┘
  '''
  achieve5_2='''
  ┌────────────────────────────────────────────────┐
  |\033[48;5;2m(christmas)       Achievements     (true chaos) \033[0m|
  |------------------------------------------------|
  |jingy bells -    \033[38;5;65myay                           '''+s('thisachievementispissingmeoff')+'''|
  |------------------------------------------------|
  |Too Festive - \033[38;5;160mGet 100 Festivity\033[0m                '''+s('Too Festive')+'''|
  └────────────────────────────────────────────────┘
  '''
  achieve5_3='''
  ┌────────────────────────────────────────────────┐
  |\033[48;5;13m(valentines)      Achievements     (true chaos) \033[0m|
  |------------------------------------------------|
  |\033[38;5;200ma lovely treat\033[0m - nice chocolates               '''+s('a lovely treat')+'''|
  |------------------------------------------------|
  |\033[38;5;200ma lovely mistake\033[0m - why?                        '''+s('insane')+'''|
  |------------------------------------------------|
  |\033[38;5;200ma lovely gift\033[0m - a true mr beast at heart       '''+s('valentine')+'''|
  └────────────────────────────────────────────────┘
  '''
  achieve5_4='''
  ┌────────────────────────────────────────────────┐
  |\033[48;5;4m(easter)          Achievements     (true chaos) \033[0m|
  |------------------------------------------------|
  |\033[38;5;226mThe Sun Temple\033[0m - Chichen Itza is that you?     '''+s('The Temple')+'''|
  |\033[38;5;124mThe Air Fryer\033[0m - a gift from the gods           '''+s('The Fryer')+'''|
  |------------------------------------------------|
  |\033[38;5;5mThe Emblem\033[0m - quite epic                        '''+s('The Emblem')+'''|
  |\033[38;5;4mThe Egg\033[0m - very much epic                       '''+s('The Egg')+'''|
  |\033[38;5;5mThe Picture\033[0m - memories of days before          '''+s('The Picture')+'''|
  |\033[38;5;4mThe Banner\033[0m - name be lookin different          '''+s('The Banner')+'''|
  |\033[38;5;5mThe \033[38;5;196mR\033[38;5;202ma\033[38;5;220mi\033[38;5;46mn\033[38;5;45mb\033[38;5;19mo\033[38;5;90mw\033[0m - inventory lookin different       '''+s('The Rainbow')+'''|
  |------------------------------------------------|
  |The Dark End - never to be found               '''+s('The Dark End')+'''|
  |The Darkest End - never.                       '''+s('The Darkest End')+'''|
  └────────────────────────────────────────────────┘
  '''
updateq()


#----------------------------------------------------------------
#----------------------------------------------------------------
#-------------                                      -------------
#-------------               MAIN.PY                -------------
#-------------                                      -------------
#----------------------------------------------------------------
#----------------------------------------------------------------








notes=['☰','☱','☲','☳','☴','☵','☶','☷','▧','◫']
volts=0
festivity=-1 #....
eaten_it=False #....
mgreen='\033[48;5;46m'
myellow='\033[48;5;190m'
mred='\033[48;5;196m'
viewing=False
Day=1
timeboss={
  'Boss 1':.3,'Boss 2':.25,'Boss 3':.25,'Boss 4':.4,'Boss 5':.3,'Boss 6':.1,'Boss 7':.1,'Boss 8':.22,'Boss 9':.3,'Boss 10':.15}
timebossC={
  'Boss 1':.35,'Boss 2':.28,'Boss 3':.28,'Boss 4':.44,'Boss 5':.33,'Boss 6':.12,'Boss 7':.12,'Boss 8':.25,'Boss 9':.34,'Boss 10':.2}
Bosses=['Boss 1','Boss 2','Boss 3','Boss 4','Boss 5','Boss 6','Boss 7','Boss 8','Boss 9','Boss 10']
Finale=['TheOne1','TheOne2','TheOne3','TheOne4','TheOne5','TheOne6','KeyRoom','Lesgo']
minimapa=False

#easter variables easter vars
didbite15=False
didbite8=False
eastervar1=0
eastervar2=0
easterlist12=['\033[48;5;6m ','\033[48;5;5m ','\033[48;5;12m ']
shapes={
  '◯':random.randrange(1,4),
  '△':random.randrange(1,5),
  '▢':random.randrange(1,6),
  '⭔':random.randrange(1,7),
  '⎔':random.randrange(1,8)
}
easterdict1={
  5:'●',
  6:'▲',
  7:'■',
  8:'⭓',
  9:'⬢'
}
doorcode='''\033[01m
◯    ⭔             ▢
◯    ⭔    △    ⎔   ▢
◯              ⎔   ▢ \033[0m
'''
doornumber=str(shapes['◯']*3)+str(shapes['⭔']*2)+str(shapes['△'])+str(shapes['⎔']*2)+str(shapes['▢']*3)
itscold=[418,422,428,433,435,438,440,444,446,448,450,451,452,454,455,458,459,460,462,463,466,467,471,477,482,484,489,491,494,495,499,500,502,505,507,508,509,512,514,516,518,519,526,531,537,540,545,548,550,552,555,557,559,561,563,565,566,567,569,570,571]
possibleprizes=['The Emblem','The Egg','The Picture','The Banner','The Rainbow']


symboldi={
  '⊞':'┍','⊡':'┎','▀':'┏','▄':'╒','█':'╔',
  '⊟':'┑','⋄':'┒','▁':'┓','▅':'╕','▉':'╗',
  '⊠':'┕','⎔':'┖','▂':'┗','▆':'╘','▊':'╚',
  '░':'┙','⎚':'┚','▃':'┛','▇':'╛','▋':'╝','╊':' '}
isright=False
isleft=True
colname={
  'Module A':'Life',
  'Module B':'Interconnection',
  'Module C':'Transendence',
  'Module D':'The Final Key',
  'Module E':'Infinity'
}
wiringvar=0 #used for multi wiring since idk how to code well

hminiscore,miniscore=0,0
coloredp={ '>':'\033[48;5;196m','<':'\033[48;5;208m','(':'\033[48;5;74m','x':'\033[48;5;82m'}
active={
  'Module A':'No','Module B':'No','Module C':'No','Module E':'No',
  'Module A.':'>','Module B.':'<','Module C.':'(','Module E.':"x",
  '>':'No','<':'No','(':'No','x':'No',
}
over='-' #find over, find replace
monkehappy,istrue,literallyvented,screenup,facbelike,docksbelike,labbelike,planebelike,startnight1,startnight2,startnight3,night=False,False,False,False,False,False,False,False,False,False,False,False
current=6
waterc,waterc2='\033[48;5;39m','\033[48;5;39m'
lab1,lab2,lab3,gens='\033[48;5;242m','\033[48;5;243m','\033[48;5;245m','\033[48;5;234m'
ArtA,ArtB,ArtC,ArtD,ArtE,ArtA1,ArtB1,ArtC1,ArtD1=('\033[38;5;196m','\033[38;5;208m','\033[38;5;74m','\033[38;5;126m','\033[38;5;82m',
'\033[48;5;196m','\033[48;5;208m','\033[48;5;74m','\033[48;5;126m')
purp = '\033[48;5;165m'
yelo='\033[48;5;226m'
moddict={'Module A':ArtA,'Module B':ArtB,'Module C':ArtC,'Module D':ArtD,'Module E':ArtE}
cavecolor,cave2color='\033[48;5;8m','\033[48;5;95m'
signc='\033[48;5;146m'
plane1,plane2,plane3='\033[48;5;7m','\033[48;5;9m','\033[48;5;252m'
cavein1,cavein2,cavein3='\033[48;5;236m','\033[48;5;8m','\033[48;5;235m'
neverrel=[1,49,53,101,105,153,157,205,209,257,261,309,313,361,365,413,417,465,469,517,521,569,573,621,625,673,677,725,729,777,781,829,833,881,885,933,937]
posleft=[0,53,105,157,209,261,313,365,417,469,521,573,625,677,729,781,833,885]
posright=[51,103,155,207,259,311,363,415,467,519,571,623,675,727,779,831,883,935]
posup=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
posdown=[885,886,887,888,889,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931,932,933,934,935]
decis=[.03,.02,.04,.05,.06,.07,.08,.09,.1,.2,.01,.005]
keyz=''

#PRINTT, PRINTT2, SLEPY
#what you can do, printt(string,delay time/enter at end?/slepy time at end,enter at end?/slepy time at end)
def printt(thingggg,dela=.03,iiu=True,SANS=False):
  global keyz2,istime
  keyz2,indeci,unsp='',dela in decis,"Unspoken Relic" in inventory
  j = istime
  istime=False
  if type(thingggg)!=str: #FOR LISTS ONLY, NEEDS EQUAL LENGTHS FOR THING AND DELA UNPACKING GO BRRRRRR
    for ind,i in enumerate(thingggg):
      printt(thingggg[ind],dela[ind] if ind<len(dela) else .03,True if type(iiu)!=list or ind<len(dela) else iiu[ind]) #if anything just pass in False to printt no line between each hehe
    return 'recursion :)'
  for ind,i in enumerate(thingggg):
    sys.stdout.write(i)
    sys.stdout.flush()
    if keyz2!='x':
      if SANS and ind%2==0 and i!=' ':
        sound("Truth/sans.wav")
      time.sleep(dela if indeci else .04 if unsp else .02)
  if dela!=False and iiu!=False: #i get lazy lol
    print("")
  if dela>=.5 or type(iiu)!=bool: #thank you binary for existing
    slepy(dela if type(iiu)==bool else iiu) #you can put in the waiting time for each char or at the end for dela
  keyz2=''
  istime=j
def printt2(thing1,thing2,thecenter,dela=.04): #huge thing literally just for monke text (i want to practice lol)
  global keyz2,istime
  keyz2=''
  j = istime
  istime=False
  TheUnitedStatesCIA=-1 #friend does a little trolling
  thingy=len(thing1)
  center1,center2=round(thecenter-len(thing1)//2),round(thecenter-len(thing2)//2)
  if len(thing2)>len(thing1):
    thingy=len(thing2)
  number1=center2-center1#the amount it needs to go left and right from 1st to 2nd
  number2=center1-center2#the opposite
  dir1,dir2='\x1b[1C','\x1b[1C'
  if number1<0:
    number1=abs(number1)
    dir1='\x1b[1D'
  if number2<0:
    number2=abs(number2)
    dir2='\x1b[1D'
  print(' '*(center1+len(thing1)),end='')
  for _ in range(len(thing1)):
    sys.stdout.write('\x1b[1D')
  sys.stdout.write('\x1b[1B')
  print(' '*(center2+len(thing2)),end='')
  for _ in range(len(thing2)):
    sys.stdout.write('\x1b[1D')
  sys.stdout.write('\x1b[1A')
  for _ in range(number2):
    sys.stdout.write(dir2)
  ive1=False
  ive2=False
  for i in range(thingy):
    TheUnitedStatesCIA+=1
    try:
      sys.stdout.write(thing1[TheUnitedStatesCIA])
    except:
      if not ive1:
        ive1=True
        number1+=1
    sys.stdout.flush()
    sys.stdout.write('\x1b[1B')
    for i in range(number1-1):
      sys.stdout.write(dir1)
    sys.stdout.flush()
    try:
      sys.stdout.write(thing2[TheUnitedStatesCIA])
    except:
      if not ive2:
        ive2=True
        number2-=1
    sys.stdout.flush()
    sys.stdout.write('\x1b[1A')
    for i in range(number2):
      sys.stdout.write(dir2)
    sys.stdout.flush()
    if keyz2!='x':
      time.sleep(dela)
  print('\n')
  keyz2=''
  istime=j
def slepy(amonu):
  global keyz2,istime
  j=istime
  istime=False
  for _ in range(6):
    if keyz2!='x':
      time.sleep(amonu/6)
  keyz2=''
  istime=j
  

mR,minicolor,inventory='\033[48;5;254m','\033[48;5;254m',[] #find inventory
def set_inv():
  return list(set(inventory))
def setall(li):
	global mazeq
	for i in li:
		for i2 in i:
			mazeq[i2]='X'
	
tydict={
  'up':{'$':867,'o':858,'m':849,'y':840},
  'down':{'$':96,'o':87,'m':78,'y':69}
}

def dprint(thi,dela=.04,up=False,count=None):
  numh=dela//count
  dela2=dela
  if up==True: #IF you want the cursor to go up a line to start put up as true
    sys.stdout.write('\x1b[1A')
    for i in range(thi):
      sys.stdout.write('\x1b[1C')
  c=0
  for _ in range(thi):
    c+=1
    sys.stdout.write(' \x1b[2D')
    if c==count:
      sys.stdout.write('\x1b[1A')
      c=0
      dela2-=numh*2
      sys.stdout.write(f'\x1b[{count}C')
    sys.stdout.flush()
    time.sleep(dela2)
  for i in range(thi):
    sys.stdout.write('\x1b[2D')
def clearline(rheffds=1):
  for i in range(rheffds):
    sys.stdout.write('\x1b[1A\x1b[2K')
  sys.stdout.flush()
listoqs=[387,388,389,390,391,392,393,438,439,440,441,442,443,444,445,446,490,491,492,493,494,495,496,497,498,542,543,544,545,546,547,548,549,550,595,596,597,598,599,600,601]
box1,box2,box3,box4=maze6.index('┌'),maze6.index('┐'),maze6.index('└'),maze6.index('┘')
#find nextone, find progression dict, find dict
nextone={-69:emaze17,-68:emaze18,-67:emaze19,-66:emaze20,-65:easterblack,-120:emaze1,-119:emaze2,-118:emaze3,-117:emaze4,-115:emaze5,-114:emaze6,-113:emaze7,-112:emaze8,-110:emaze9,-109:emaze10,-108:emaze11,-107:emaze12,-106:emaze132,-105:emaze13,-104:emaze14,-103:emaze15,-102:emaze16,-100:emaze,-8:theTruth,-3:theroom,0:themine,1:maze1,2:maze2,3:maze3,4:maze4,5:maze5,6:maze6,7:maze7,8:maze8,9:maze9,10:maze10,50:TheOne1,51:TheOne2,52:TheOne3,53:TheOne4,56:TheOne5,57:TheOne6,100:lanc1,101:lanc2,102:lanc3,103:lanc55} #easter things in here
mcolor='\033[38;5;131m'
modli=['Module A','Module B','Module C','Module E','Module D']
gisforgree='\033[48;5;35m'
gisforgree2='\033[48;5;40m'

bossnumbu=1
nextonboss={
  1:Boss1,2:Boss2,3:Boss3,4:Boss4,5:Boss5,6:Boss6,7:Boss7,8:Boss8,9:Boss9,10:Boss10
}

#find items
items=['“','^','&','%','=','r','l','A','B','C','D','E','+','p','V','{','q','0','I','1','▸','W','☰','☱','☲','☳','☴','☵','☶','☷','◫','▣','╾','╼','❖','▤','i','ₒ','॰','°','৹','๐','𐤏','Ｏ','⦿']


gensdict={
  True:'\033[48;5;46m'+' '+R,False:'\033[48;5;160m'+' '+R,
}
itemdict={ #If you want to add an item go check the temmiecolor dictionary and add your item to here like this (put this at the end of the dictionary): ,[Itemname]:'No',[Symbolforitem]:'Itemname'
  '▧':'Note 9','◫':'Note ?','☰':'Note 1','☱':'Note 2','☲':'Note 3','☳':'Note 4','☴':'Note 5','☵':'Note 6','☶':'Note 7','☷':'Note 8','“':'Wiring','W':'Old Pick','▣':'bana','^':'Thermometer','&':'Diving Gear [Empty]','1':'Diving Gear [Full]','%':'Night Vision','r':'Revolver','I':'Revolver[Empty]','l':'Lantern','=':'Flashlight','A':'Module A','B':'Module B','C':'Module C','D':'Module D','E':'Module E','{':'Watch','V':'Plane Propeller','+':'Plane Hull(Part)','▸':'The Key','p':'Plane Fuel','q':"Plank",'0':'Paddle','╼':'Multi Wiring','╾':'Super Wiring','❖':'Voltage','▤':'Boat','Boat':'NA','Voltage':'NA',"Plank":'NA','The Key':'NA','Paddle':'NA','Plane Propeller':'NA','Plane Hull(Part)':'NA','Plane Fuel':'NA','Watch':'NA','Wiring':'NA','Thermometer':'NA','Diving Gear [Empty]':'No','Diving Gear [Full]':'No','Night Vision':'No','Revolver':'NA','Revolver[Empty]':'NA','Lantern':'No','Flashlight':'No','Module A':'No','Module B':'No','Module C':'No','Module D':'No','Module E':'No','Old Pick':'No','bana':'NA','Multi Wiring':'NA','Super Wiring':'NA','Unspoken Relic':'NA'
}
item4dev=["Plank",'Paddle','Plane Propeller','Plane Hull(Part)','Plane Fuel','Watch','Wiring','Multi Wiring','Super Wiring','Thermometer','Diving Gear [Empty]','Diving Gear [Full]','Night Vision','Revolver','Revolver[Empty]','Lantern','Flashlight','Module A','Module B','Module C','Module E','Old Pick','bana','Boat']
notec='\033[38;5;189m'
notedict={
  'Note 1':[False,'...3 entire veins of the stuff, more than anyone could think of. Hes sure gonna be happy when we come back.\nDay 1 and this is already looking way better than we thought.'],
  'Note 2':[False,'...today. This isnt at all normal, but we aint complaining. Few more days and we will already be set.\nGives me the chills just to be in here, but with this much we just cant leave, not without our fair share.'],
  'Note 3':[False,'...in the arm, quite nasty hit too. It seemed to just bounce off that wall, saw it clear with my own eyes.\nPaul\'ll be back soon, few herbs aint too hard to find.'],
  'Note 4':[False,'..., but nothing at all. No footprints, no nothing. Just rained too, my footprints were clear as day.\nHe\'s done this before though, and if anything we got this log to remember him by.'],
  'Note 5':[False,'...in the air, there has to be. Tension? Emotions? I don\'t think so.\n We are on our last 3 days, just gotta make it till then. This sure as hell has been an experience.\nStill no Paul.'],
  'Note 6':[False,'...came back, but just for a second. We just chased after him... I dont know what we just saw.\nThat wasn\'t Paul, nothing you can say can convince me of that. God help us, please.'],
  'Note 7':[False,'...hearing them. The screams. Not of pain, but of anger. From the middle of nothing, sometimes right in front of us with nothing there.\nI dont think we can make it the last 2 days. Me and my pal found a plane. Other guy\'s gonna take some makeshift boat.\n'],
  'Note 8':[False,'...on Paul, but that one guy cant let him go. Makes sense, they were best friends. Hes gonna go to the building. Whatever that place is.\nThis is the last I write in this log. They better believe every word I say when I get back. Theres no way 3 hours of fuel isnt enough.'],
  'Note 9':[False,'...I hope. That was crazy. Literally insane.\nIt\'s like he wanted us to die, if only we coulda saved him.\nThis is actually the last time I write in this log. Might try to burn a few pages or something.'],
  'Note ?':[False,'...\n'+mcolor+'...'+mcolor+"I thought that was the end. It had to be.\nBut Paul wasn't done. What did we do Paul?\n"+mcolor+"We searched for hours.\n"+mcolor+"We called and called.\n"+mcolor+"We cant let this cycle continue. We have decided to do it.\n"+mcolor+"It didnt have to be like this Paul. We woulda came back for you.\nWe could have saved you Paul. You just had to let us go.\nI know it cant be Paul. We arent that dumb.\nIts "+R+"him"+mcolor+"."]
}


def acheck(thing):
  return achievements[thing] if thing in achievements.keys() else False
def funnyfunction(b=27):
  for i in range(b):
    clearline()
    time.sleep(abs(.7-(b/50)))
def printnotes():
  c()
  loc=[]
  for i in notedict.keys():
    if notedict[i][0]==True:
      if len(loc)+1!=10:
        print(str(len(loc)+1)+") "+i)
      else:
        print('0) '+i)
      loc.append(i)
  if len(loc)!=0:
    print('\n(Press the number of the note you want to open, x to exit)')
    key=''
    e=range(1,len(loc)+1)
    aa=[]
    for e2 in e:
      if e2!=10:
        aa.append(str(e2))
      else:
        aa.append('0')
    aa.append('x')
    while key not in aa:
      key=getkey1()
    if key=='0':
      key='10'
    if key!='x':
      c()
      printt(['Only a portion of the note is legible.\n'+notec,bold+notedict[loc[int(key)-1]][1]],[.01,.06],[True,3])
      anykey()

    c()

def picky(m):
  global minimapa,inventory
  c()
  print(mcolor,end='')
  if m=='1':
    inventory.remove('Old Pick')
    printt(["Thanks for that bud! Ive only been wanting that for the last few decades.. heh.",\
    "Anyway heres a little something I whipped up myself.\n"+mcolor+"Its not very pretty, but it lets you see where you are in the main island.\n",\
    "It relies on some strange power source, being honest I dont even know about it.",\
    "Anyway you should be able to access it anytime!",R+"(You have the sudden urge to press q)"],[1,2,2,3,2]) #DUDE THIS IS SO PRETTY AAAAAAAAAAAAAAAAAAAAAAAAAAA
    minimapa=True
  else:
    printt("Oh... "+(R*3)+mcolor+' So that pickaxe that looks exactly like mine isnt mine, makes sense.',2)
  anykey()
#Omg minER@!?/!?

def evenspace(stril,numb=40,g=False):
  return (stril if g else '')+(" "*(numb-len(stril)))
def amount(min,amoun):
  return [f"{min}"+('\033[38;5;82m' if shopkeep.count(min)>=amoun else '\033[38;5;196m')+ f" ({shopkeep.count(min)}/{amoun})"+r, f"{min} ({shopkeep.count(min)}/{amoun})"]

#find shop, find mineral shop, find ore shop, find mine shop
howthehellyaben=False
shopkeep=[]
factz=['You can press n in a certain boss fight for your stats...','There\'s a true ending, a true true ending, and ...','Press "R" for a list of all *accessible* keys.','After every event, it never truly goes away...','Events are never truly limited...','There are two modules hidden in the caves.','The first version of this... world, was questionable.','Like every good game, this one relies on randomness.','Make sure you magically get a certain item in a certain boss fight...','There are way too many secrets in this game.',"Naming yourself the name of the creator gives you special powers...","There are more than 20 random messages that can appear here.","Past events (in order): Halloween, Christmas, Valentines, Easter","If a secret item were to pop into the game, it might be here...",'This game has been worked on since 2019.',"The creator of this world actually enjoys making it.","You are cool :)","There's a way to play tic-tac-toe in this game... (its not easy)","Getting every ending unlocks a new ending...","This game will eventually be made in unity :O","Never gonna give you up, never gonna let you down.","The 'afk' achievement is so stupid... just wait through the entire audio prompt at the start.","This was used as a break from actually making the game.","happy :)","Games in this game: the minigame, YSKYSN boss, tic-tac-toe","This is 100% a 4th wall break",""]
def minshop():
  global howthehellyaben,shopkeep
  c()
  if not howthehellyaben:
    printt(["An old man seems to be asleep at the stand...","The old man raises his head, revealing an ancient face crowned with an old samurai-looking hat.","\n\033[38;5;17m...",'\033[38;5;17mAt least thats what they all say, yea?\n\033[38;5;17m\033[38;5;17mYou know, all those suspenseful conversations that always start with '+bold,"...",R+'\033[38;5;17mPersonally dont give two damns about other people, in fact haven\'t seen a real one in 200 years.\n\033[38;5;17mNeither have you huh?'],[2,1,2,False,.5,2],[True,True,True,1,2,True])
    anykey()
    printt(["\033[38;5;17mWell at any rate, might as well tell you the gist.\nI like those ores in there, even the rock, nothing is a waste in these eyes.\n\nYou might not realize the potential of these items, but use that old pick of yours and get me some of them eh?","And no, this isn't some random quest some guy sets you off on, I would be prefered to be called a shop.","\nEvery item, at least that I know of, can be made from these precious minerals, and for a small upcharge, they will be yours.", "And make sure to deposit your ores into my shop storage, only one way to pay after all.","\n\nSorry for such a long conversation, wouldn't want the player getting bored would you?"],[2,2,4,1])
    anykey()
  print('\033[38;5;17m'+('Welcome to my store!' if not 
howthehellyaben else ('Fun fact: '+random.choice(factz)) if random.randrange(1,2)==2 else random.choice(['How goes the day?','"Hello traveler, I\'ve seen you come quite the distance!"\nThat was your expectation, right?','"Greeting adventurer, look around, we have everything you need!"\nThat was your expectation, right?','I don\'t know, something?','me encantan los minerales','More ores for me?','You better not be poor...']))+R)
  howthehellyaben=True
  print("\n"+evenspace("Wiring",40,True)+"Revolver\n  "+amount('Coal',1)[0]+evenspace(amount("Coal",1)[1])+amount("Rock",100)[0]+evenspace(amount("Rock",100)[1])+\
  '\n  '+amount("Copper",1)[0]+'\n  '+amount("Iron",1)[0]+"\n\n"+evenspace("Multi Wiring",40,True)+"Super Wiring\n  "+amount("Rock",50)[0]+evenspace(amount("Rock",50)[1])+amount("Rock",200)[0]+\
  '\n  '+amount("Iron",2)[0]+evenspace(amount("Iron",2)[1])+amount("Chromium",1)[0]+'\n  '+evenspace('')+amount('Ruby',1)[0]+'\n\n'+evenspace("Night Vision",40,True)+"Watch\n  "+\
  amount("Magnesium",2)[0]+evenspace(amount("Magnesium",2)[1])+amount("Magnesium",1)[0]+'\n\n'+bold+evenspace("bana",40,True)+"Miner's Cap\n  "+R+amount("Diamond",1)[0]+evenspace(amount("Diamond",1)[1])+amount("Emerald",1)[0]+'\n  '+\
  amount("Coal",1)[0]+evenspace(amount("Coal",1)[1])+amount("Diamond",1)[0]+"\n  "+evenspace('')+amount("Ruby",1)[0]+'\n') #big shop print, miner shop
  pobre=getkey1()
  c()

#find miner generation, find mining generation
mindict={
'i':['Rock',100],
'ₒ':['Coal',5],
'॰':['Copper',5],
'°':['Iron',4],
'৹':['Magnesium',3],
'๐':['Chromium',3],
'𐤏':['Ruby',2],
'Ｏ':['Diamond',2],
'⦿':['Emerald',1]}

def minegen():
  #each up/down is 10, up is -10 (change down/up)
  #top left is 150
  global nextone, current
  try:
    return nextone[151]
  except:#generation
    current=150
    nextone[150]=miney
    for i in range(99):
      current+=1
      newthin=mineyex.copy()
      for ind,i2 in enumerate(newthin):
        if newthin[ind]!='\n':
          if (current%10==0 and ind in posleft) or (str(current)[-1]=='9' and ind in posright) or (current<160 and ind in range(0,52)) or (current>239 and (ind in posdown or ind>posdown[0])):
            newthin[ind]='#'
          elif (ind in (list(range(677,681))+list(range(729,733))) and current==151) or (ind in (list(range(6,9))+list(range(58,61))+list(range(36,40))+list(range(88,91))) and current==160):
            newthin[ind]='-'
          elif (newthin[ind-1]=='i' and random.randrange(1,3)==2): 
            if random.randrange(1,50)==1:#decreases some ore spawns
              theyi=random.randrange(1,(349-current))
              newthin[ind]=('ₒ' if theyi in range(0,20) else '॰' if theyi in range(20,35) else '°' if theyi in range(35,45) else '৹' if theyi in range(45,55) else '๐' if theyi in range(85,90) else '𐤏' if theyi in range(90,93) else 'Ｏ' if theyi in range(93,95) else '⦿' if theyi==99 else 'i')
      nextone[current]=newthin
  current=150
mission=False
def mineIn():
  q='e'
  while q not in ['1','2','3','4']:
    q=getkey1()
  c()
  return q
def dialogue():
  global mazeq,tinyvars,alive,mission,theroom,achievements,current,istime
  istime=False
  print()
  try:
    if mission==False:
      if 'The Key' not in inventory:
        iui='\033[48;5;82m' if 'Old Pick' in inventory or itemdict["Module C"]=='Yes' else ''
        print(mcolor,end='')
        if tinyvars['firstmin']==False:
          printt((random.choice(["Hello! You must be "+name+"! What brings you to these parts?","Oh, I didnt see you there "+name+"! May I ask how you found me?"]) if not tinyvars['firstmin'] else "Hello "+name+"! What brings you here?"),.04,1)
        if 'Module B' in inventory or itemdict['Module B']=='Yes':
          printt(R+"(The Miner seems very energetic...)")
        tinyvars['firstmin']=True
        print(R+'''\n\t1 - How do you know my name?\n\t2 - I was exploring the caves and found you.\n\t3 - Who are you?\n\t4 - Just kinda leave''')
        m=mineIn()
        if m=='4':
          error
        printt(mcolor+('Oh thats not a problem. You\'re the only other person here, except '+R+"Him."+R+mcolor+' \nYou have to know that right?' if m=='1' else "Oh that makes sense, sorry for bugging ya, usually its not that simple. \n"+R+"He"+mcolor+" is usually bugging me." if m=='2' else "Being honest, I dont know."+mcolor+" Who are you?\nYou only know what you named yourself, "+name+", and"+mcolor+" well,"+mcolor+" me and "+R+"Him"+mcolor+" never got that choice."),2) #HERE
        print(R+'''\n\t1 - Who is "Him"?\n\t'''+iui+'''2 - What happened to your arm?'''+R+'''\n\t3 - What is this place?\n\t4 - Just kinda leave''')
        
        m=mineIn()
        print(mcolor,end='')
        if m=='1': #maybe optimize
          printt((("."+mcolor)*3)+" I can't really answer that."+R+" He"+mcolor+" gets mad if you mention him.",3)
          choice='''\n\t1 - Who is He?\n\t2 - Do you know how to leave this place?\n\t3 - Why not?\n\t4 - Leave'''
        if m=='2':
          printt("Just a little accident down in the mines. Back when this place existed, I lost an arm due to some dynamite."+mcolor+"\nI have just been sitting here since then, however long thats been.",3)
          choice='''
          '''+iui+'''\n\t1 - Is there anything I can do to help you?'''+R+'''\n\t2 - Do you know how to leave this place?\n\t3 - Have you ever seen anyone else?\n\t4 - Just kinda leave'''
        if m=='3':
          printt("This is just an old mine pal. \nBack when this place existed there would be a whole crew down here, this island sure had plenty of ores.\n"+R+mcolor+"But then "+R+"He"+mcolor+" showed up. \nMost of the crew left, and the 3 others that stayed seem to almost stop existing.\nIt makes sense if you dont think about it.",3)
          choice='''\n\t1 - Is there anything I can do to help you?\n\t2 - Do you know the 3 other miners?\n\t3 - Wh▖⋄s 💧︎⧫︎♋︎■︎?\n\t4 - Just kinda leave'''
        if m=='4':
          error
        print(R+choice)
        X=int(m)
        mE=mineIn()
        if mE=='4':
          error
        print(mcolor,end='')
        prompt=(('mission-bad' if X==1 else 'mission' if X==2 else 'escape') if mE=='1' else ("escape" if X!=3 else "4miners") if mE=='2' else ('mission-bad' if X!=2 else 'exit'))
        if not all([X==3,mE=='3']):
          printt(("Cmon man, I already told you. Stop talking about him so much, ya know? If you'd like I got a little mission for you." if X==1 else "Well there is something. I used to love my old pickaxe back in my mining days. If you could bring it back to me I have something you might like!" if X==2 else "I've already told you...\nAs long as .. is alive we cant really make em mad...\nIf only there was a way.") if mE=='1' else \
            ("I can only say I've tried. And guess where that led me." if X in [2,1] else "Well ever since that day I've never actually seen them, atleast not really..."+mcolor+"\nBut I know they are still here.") if mE=='2' else ("Cmon man, I already told you. Stop talking about him so much, ya know? If you'd like I got a little mission for you." if X==1 else 
        "Funny that you ask that. I was wondering that myself. Maybe a few resets ago I might have remembered.\nBeing honest, get out while you still can. Time doesnt matter, the past doesnt matter, just get out before the 6th day.\n"+R+R+R+R+bold+"(The Miner seems to catch himself)"+R*4+mcolor+"\nOh... Im sorry. I thought you might have known. Maybe our little chat has been going a bit too long."+(R*2)+bold+"\nRight?"))
        else:
          c()
          printt(bold+'...',1)
          printt("Are you sure you want to choose this option?\n>")
          n=getkey1()
          if n=='y':
            c()
            printt(bold+'...',1)
            printt("You must misunderstand what im saying. You dont want to do this.\nPress any key but 'Y'. Please.\n>",.05)
            n=getkey1()
            if n=='y':
              c()
              printt(bold+"...",1)
              printt("Okay.",2)
              c()
              time.sleep(1)
              printt(R+bold+"(The Miner stops and looks at you.)"+R,3)
              printt(mcolor+"\n✡︎□︎◆︎ ♒︎♋︎♎︎ ⧫︎□︎ ♎︎□︎ ⧫︎♒︎♓︎⬧︎✍︎")
              time.sleep(.5)
              c()
              prompt='ded'
            else:
              printt("Thank you.")
          else:
            printt("Good...")
        if mE=='3' and X==2:
          time.sleep(2)
          c()
        if prompt=='exit':
          error
        elif prompt=='ded':
          for i in ['╔','╕','╚','╝']:
            overide(i)
          error
        #elif prompt=='bigbad': there was a hidden unused prompt??????? bro what was i doing
        print(R+('\n\t1 - What do you need?\n\t2 - Who is he?\n\t3 - Who is HE?\n\t4 - '+bold+'Quit it.'+R if prompt=='mission-bad' else '\n\t1 - Do you need help with anything?\n\t2 - How do you know they are here?\n\t3 - Is there anything you need?\n\t4 - Just kinda leave' if prompt=='4miners' else '\n\t1 - Have you tried everything?\n\t2 - How long have you been trapped here?\n\t3 - Is there anything you need?\n\t4 - Just kinda leave' if prompt=='escape' else '\n\t1 - Sure thing!\n\t2 - Where is your pickaxe?\n\t3 - ok\n\t4 - Just kinda leave'))
        m=mineIn()
        if all([m!=4, not (prompt=='mission' and m=='1')]):
          print(mcolor,end='') #takes away the time to wait for it lol
          printt(("I used to love my old pickaxe back in my mining days. If you could bring it back to me I have something you might like!" if m=='1' else (R+bold+"But nobody came :)"+R if random.randrange(1,10)==5 else "The miner just stops."+R+bold*3+"\nYou're lucky he did."+R)) if prompt=='mission-bad' else ("Well there is something. I used to love my old pickaxe back in my mining days. If you could bring it back to me I have something you might like!" if m!='2' else "Now that is a bit harder to explain. I doubt you wanna hear everything, and even if you did I dont have that much time.\nBut basically its as if, cheesy as it sounds, we all all connected. Like we have a purpose only together we can achieve. And somehow you tie into all of this.\nI don't know the entire deal, but it doesnt seem easy.") if prompt=='4miners' else ("Pretty much, at least I think so. Ever since that one day I feel as if a new path opened up. I dont know what it is, but its bound to be complicated.\nIf I were you I would check the "+bold+"Grand Lake"+R+mcolor+" if you havent already..." if m=='1' else "Time doesnt matter kiddo. Either way, it only really matters for you. Just get out of this place by the 6th day, or you might never make it out again." if m=='2' else "Well there is something. I used to love my old pickaxe back in my mining days. If you could bring it back to me I have something you might like!") if prompt=='escape' else ('ok' if m=='3' else "Oh.. Being honest I forget. It has to be somewhere In the mines to the right though, probably not that far. Be careful, every so often a new piece of those mines collapes."),2)
        mission = True if any([prompt=='mission-bad' and m=='1',prompt=='4miners' and m in ['1','3'], prompt=='escape' and m=='3',prompt=='mission']) else False
        if all([prompt=='mission',m=='3']):
          c()
          slepy(1)
          printt(["Something deep within your SOUL starts to wake up...","The Power of Ok.","The Power of Lanc.",'The Power of Determination.'],[2,1,1,.1],[True,True,True,2])
          mazeq,current=lanc1,100
          c()
          for (ij,j) in zip([784,785,836,837],['┌','┐','└','┘']):
            lanc1[ij]=j
          error
        anykey()
      else: #if you have the key
        p=0
        if tinyvars['min3']!='e':
          for i in ['Note 1','Note 2','Note 3','Note 4','Note 5','Note 6','Note 7','Note 8','Note 9']:
            if notedict[i][0]==True:
              p+=1
          tinyvars['min3']=p==9
        c()
        if tinyvars['othermin']==False:
          print(mcolor,end='')
          printt('Hello '+name[0:round(len(name)/2)]+'-',.06)
          time.sleep(.5)
          c()
          printt(R+"The miner seems to know."+R+R+" Somehow, he already knows."+R+R+"\nMaybe it was his presence."+R+" Maybe it was his power."+R+R+R+"\nBut somehow, he knew.")
          slepy(3)
          c()
        print(mcolor+"Hello "+name+". What would you like to know?\nMaybe I know something you dont.\n",end='')
        tinyvars['othermin']=True
        print(R+'''
        1 - Who was he?
        2 - What is this island?
        3 - The Key.
        4 - What happened to us?\n\n(Press 1,2,3,4 or 5)''')
        m='e'
        while m not in ['1','2','3','4','5']:
          m=getkey1()
        if m=='5' and smallvarget('min3')==True:
          clearline(2)
          print('        ',end='')
          printt(bold+'5 - Who is Paul?',.1)
          time.sleep(2)
        c()
        print(mcolor,end='')
        if m=='1':
          printt("Thats a hard one.\n"+mcolor+"The obvious answer is it wasnt human, but im not too sure about that...\n"+mcolor+"Its as if "+R+'He'+mcolor+' was supposed to be like one of us four, but something happened.\n'+R+"He"+mcolor+" got mad. Real mad. No one knows his name, but all I can say is something happened to his."+mcolor+"."+mcolor+"."+mcolor+" host.")
        elif m=='2':
          printt('Island you say?'+mcolor+" I would rather call it a prison.\nEverything seems to keep us in, even nature itself.\nIt's as if something doesnt want us to leave, or we just cant.\n"+mcolor+"Reminds me of a movie I used to love...")
        elif m=='3':
          printt("Yeah I figured. One of these days "+R+"he"+mcolor+" was bound to be figured out.\nMy only advice is to find out the truth. I would come with you if I could, but this isnt my world.\nBe warned, You might have found the exit, but that doesnt mean its the end.")
        elif m=='5':
          if smallvarget('min3')==True:
            printt('...'+mcolor+mcolor+'\nI thought I had forgotten.'+mcolor+' I guess not.',.04)
            slepy(4)
            c()
            printt(R+bold+"(Something new appears at the end...)")
            time.sleep(3)
            tinyvars['min3']='e'
            theroom[494]='◫'
          else:
            printt('...')
        else:
          printt("Well as of now, we are safe. At least until the 6th day.\nThats the only reason I have said "+R+"Him"+mcolor+" more than once.\nSomething seems to have cleared in my mind, as if I can see the end.\nI feel almost.. accomplished, like I did something. Weird.")
        time.sleep(2)
        anykey()
    else:
      if minimapa==False:
        if 'Old Pick' not in inventory:
          printt(mcolor+random.choice(['You\'re bringing that pickaxe back right?','Still searching for it huh?','My pickaxe should be to the right, gonna go get it?']),2)
          print(R+"\n1) Yep!\n2) nah (back to main dialogue)")
          m=mineIn()
          print(mcolor,end='')
          if m!='2':
            printt("p o g")
            time.sleep(.5)
            c()
          else:
            printt(R+"(You gave up on the mission)",2)
            c()
            mission=False
        else:
          printt(mcolor+'Oh is that my pick!\n'+R,1)
          print("1) Yep!\n2) nope")
          m='e'
          while m not in ['1','2']:
            m=getkey1()
          picky(m)
          c()
      else:
        print(mcolor,end='')
        printt("It only really works if you get out of the caves...\n"+R+"(Because thats balanced game design not me being lazy to make maps for every section)",2)
        print(R+'1) bruj\n2) ok\n3) i want old dialogue\n4) me no care')
        y=mineIn()
        if y=='3':
          printt('ok fine here it is pls dont ask for the mission again it might break the game idk i havent really tested it and like if you break it you migt softlock yourself uh yea thats about it for this text box i thnk well uh yea and uh you kinda looking like a sussy imposter amongus baka funny fortnite gameplay roleplay 3am clickbait sugmona #dream #funny #puppycute #plsclickineedview')
          mission=False
        elif y=='4':
          printt(":(",2)
        c()
  except:
    c()
  istime=True
raftper=False
zerosad={
  0:51,1:103,2:155,3:207,4:259,5:311,6:363,7:415,8:467,9:519,10:571,11:623,12:675,13:727,14:779,15:831,16:883,17:935,18:987,19:51}

spawndict={
  'v':['V','+','p','-','-'], #plen
  'P':['r','^','%','“'], #good spawn
  'O':['=','l','l','=','l','“','{'], #bad spawn
  'R':['=','^','%','{','{','“'], #mid spawn
  'e':['q','0','0','-','-','-'], #raft
  '4':['☰','☱','☲','☳','☴','☵','☶','☷','-','-','-','-'], #notes
  '▒':['▣','-','-','-','-','-'], #monke
  'N':['H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','-','-','-','-','-','-','-','-'], #easter
}
spawnlist=[maze1,maze2,maze3,maze4,maze5,maze6,maze7,maze8,maze9,maze10,Shed,theLake,labm1,labm2,cavem2,cavem1,theroom,Mining,Mining2,Mining3,festivehall,newthing1,newthing2,newthing3,theLake2,TheOne5,theTruth,\
emaze132,emaze1,emaze2,emaze3,emaze4,emaze5,emaze6,emaze7,emaze8,emaze9,emaze10,emaze11,emaze12,emaze13,emaze14,emaze15,emaze16]
#ADD MAZES WITH SPAWNS TO THIS


#find spawns
for i in spawnlist: 
  for ppo,i2 in enumerate(i):
    if i2 in spawndict.keys():
      i[ppo]=(t0:=random.choice(spawndict[i2]))
      if i2 not in ['O','P','R']:
        spawndict[i2].remove(t0)
def returnword(ERT): #Spaget moment, being honest idk why this exists but i use it anyway lol
  return 'maze1' if ERT==maze1 else 'maze2' if ERT==maze2 else 'maze3' if ERT==maze3 else 'maze4' if ERT==maze4 else 'maze5' if ERT==maze5 else 'maze6' if ERT==maze6 else 'maze7' if ERT==maze7 else 'maze8' if ERT==maze8 else 'maze9' if ERT==maze9 else 'maze10' if ERT==maze10 else 'cavem1' if ERT==cavem1 else 'cavem2' if ERT==cavem2 else 'labm1' if ERT==labm1 else 'labm2' if ERT==labm2 else 'theLake' if ERT==theLake else 'themine' if ERT==themine else 'theLake2' if ERT==theLake2 else 'theroom' if ERT==theroom else 'Shed' if ERT==Shed else 'theTruth' if ERT==theTruth else 'KeyRoom' if ERT==KeyRoom else 'Boss 1' if ERT==Boss1 else 'Boss 2' if ERT==Boss2 else 'Boss 3' if ERT==Boss3 else 'Boss 4' if ERT==Boss4 else 'Boss 5' if ERT==Boss5 else 'Boss 6' if ERT==Boss6 else 'Boss 7' if ERT==Boss7 else 'Boss 8' if ERT==Boss8 else 'Boss 9' if ERT==Boss9 else 'Boss 10' if ERT==Boss10 else 'TheOne1' if ERT==TheOne1 else 'TheOne2' if ERT==TheOne2 else 'TheOne3' if ERT==TheOne3 else 'TheOne4' if ERT==TheOne4 else 'TheOne5' if ERT==TheOne5 else 'TheOne6' if ERT==TheOne6 else 'Lesgo' if '⊚' in ERT else 'Modulea' if ERT==Modulea else 'Mining' if ERT==Mining else 'Mining2' if ERT==Mining2 else 'Mining3' if ERT==Mining3 else 'Portal' if ERT==Portal else 'True1' if ERT==True1 else 'True2' if ERT==True2 else 'True3' if ERT==True3 else 'True4' if ERT==True4 else 'lanc1' if ERT==lanc1 else 'lanc2' if ERT==lanc2 else 'lanc3' if ERT==lanc3 else "lanc55" if ERT==lanc55 else "lanc4" if ERT=="lanc4"else 'emaze21' if ERT==emaze21 else 'emaze22' if ERT==emaze22 else 'emaze' if ERT==emaze else 'newthing1' if ERT==newthing1 else 'newthing2' if ERT==newthing2 else 'newthing3' if ERT==newthing3 else 'Halloween' if ERT==HEAHE else 'festivehall' if ERT==festivehall else 'Shed2' if ERT==Shed2 else 'None'
mazesec={
  'maze1':['','','Maybe'],'maze2':['','','Maybe'],'maze3':['','','Maybe'],'maze4':['','','Maybe'],'maze5':['','','Maybe'],'maze6':['','','Maybe'],'maze7':['','','Maybe'],'maze8':['','','Maybe'],'maze9':['','','Maybe'],'maze10':['','','Maybe'],
  'True1':[70,'Imperfectly Perfect.','No'],'True2':[70,'Imperfectly Perfect.','No'],'True3':[70,'Imperfectly Perfect.','No'],'True4':[70,'Imperfectly Perfect.','No'],'cavem2':[85,'Warm','No'],'cavem1':[90,'Warm','No'],'labm2':[78,'Warm','No'],'labm1':[78,'Warm','No'],'Shed':[80,'Warm','No'],'theLake':[80,'Warm','No'],'theroom':[75,'Perfect.','No'],'theTruth':[75,'Perfect.','No'],'theLake2':[80,'Warm','No'],'Boss 1':[99,'Hot','No'],'Boss 2':[99,'Hot','No'],'Boss 3':[99,'Hot','No'],'Boss 4':[99,'Hot','No'],'Boss 5':[99,'Hot','No'],'Boss 6':[99,'Hot','No'],'Boss 7':[99,'Hot','No'],'Boss 8':[99,'Hot','No'],'Boss 9':[99,'Hot','No'],'Boss 10':[99,'Hot','No'],'TheOne1':[75,'Perfect.','No'],'TheOne2':[75,'Perfect.','No'],'TheOne3':[75,'Perfect.','No'],'TheOne4':[75,'Perfect.','No'],'TheOne5':[75,'Perfect.','No'],'TheOne6':[75,'Perfect.','No'],'KeyRoom':[75,'Perfect.','No'],'Lesgo':[69,'Kinda Epic','No'],'Portal':[87,'Warm','No'],'Mining':[80,'Warm','No'],'Mining2':[80,'Warm','No'],'Mining3':[80,'Warm','No'],'Modulea':[7,'Lucky.','No']
}
listothem=['maze1','maze2','maze3','maze4','maze5','maze6','maze7','maze8','maze9','maze10']
for e in listothem:
  rere=random.choice(range(15,70))
  mazesec[e][0]=rere
  if rere>50:
    mazesec[e][1]='Pretty warm'
  elif rere>30:
    mazesec[e][1]='Chilly'
  elif rere>10:
    mazesec[e][1]='Cold'
for r in range(2):
  por=random.choice(listothem)
  listothem.remove(por)
  mazesec[por][2]='Yes'
  mazesec[por][1]='Cold'
  por2=por
  while por2==por:
    por2=random.choice(listothem)
  listothem.remove(por2)
  mazesec[por2][2]='No'
goods=['-','R','O','9',' ','╫']
cavemazes=[cavem1,cavem2]
labmazes=[labm1,labm2]


#find maze
mazeq=maze6
daco='white'

miniX={'⊖':'red','⊘':'orange','⊚':'purple','⊙':'blue'}
minico={'⊖':miniA,'⊘':miniB,'⊚':miniC,'⊙':miniD}
minio={'⊖':'◰','⊘':'◱','⊚':'◲','⊙':'◳'}
miniesPUMA=False
dictm={
  1:2,2:1.8,3:1.7,4:1.6,5:1.55,6:1.5,7:1.45,8:1.4,9:1.35,10:1.3,11:1.2,12:1.15,13:1.1,14:1.05,15:1,16:.95,17:.9,18:.85,19:.8,20:.75,21:.7,22:.7,23:.69,23:.68,24:.68,25:.68,26:.67,27:.67,28:.67,29:.66,30:.66,31:.65,32:.65,33:.64,34:.63,35:.63,36:.63,37:.62,38:.61,39:.61,40:.6,
}
jing=False
def mini(pol=True):
  global daco,miniesPUMA,miniscore,hminiscore,mazeq,achievements,jing,okvar
  miniscore=0
  jing=True
  minn=0
  mazew=mazeq.copy()
  miniesPUMA=True
  TY.sleep(2)
  while jing:
    minn+=1
    color22=random.choice(['⊖','⊘','⊚','⊙'])
    daco=miniX[color22]
    c()
    print('Score:'+str(miniscore))
    printmaze(mazeq)
    try:
      idmu=dictm[minn]
      IdD=2
    except:
      idmu=.5
      IdD=3.5-(minn/20) #The time the parts are there is decreased
      if IdD<1:
        IdD=1
    TY.sleep(idmu)
    mazew=mazeq.copy()
    if pol==True:
      for i in minico[color22]:
        mazew[i]=minio[color22]
    else:
      for i in [miniA,miniB,miniC,miniD]:
        for i2 in i:
          if i!=minico[color22]:
            mazew[i2]={miniA:'◰',miniB:'◱',miniC:'◲',miniD:'◳'}[i]
    mazeq=mazew
    c()
    print('Score:'+str(miniscore))
    printmaze(mazeq)
    #Check if the player is ded or not
    if '└' in mazeq and '┘' in mazeq and '┌' in mazeq and '┐' in mazeq:
      miniscore+=100
      TY.sleep(IdD)
      for i in ['◳','◲','◱','◰']:
        while i in mazeq:
          mazeq[mazeq.index(i)]='-'
    else:
      jing=False#IUFnfnfeiufunefnnuefefnenfniefefienfienfinefnefiu (its true)
  #Dead stuff idk
  if miniscore>hminiscore:
    hminiscore=miniscore
  achieve('mini',False)
  miniesPUMA=False
  while minio[color22] in mazeq:
    mazeq[mazeq.index(minio[color22])]='-'
  mazeq=KeyRoom if not okvar else okvar2
  okvar=False
  daco='white'
  c()
  print('RIP')
  if miniscore>2999:
    achieve('Poggers')



try:
    hminiscore=achievements['mini']
    succe=all([achievements['The Lab'],achievements['The Plane'],achievements['Raft'],achievements['The Cart'],achievements['Escape.']])
except:
  succe=False
gettingkey=False
def achieve(h='`',h1=True):
  global achievements
  f=achievements[h] if h in achievements.keys() else False
  if h!='`' and gGg:
    if not f or h in ['end','easter_cooldown','s']:
      achievements[h]=h1
      if h1==True:
        print(R+'[You got \033[38;5;86m'+h+R+'!]')
  with open("truthdata.json",'r') as k: #make sure you dont override things, with yourself AND others
     achievements2=json.load(k)
  for i in achievements2[name].keys():
    if achievements2[name][i] in [False,True] and type(achievements2[name][i])==bool:
      achievements[i]=True if achievements2[name][i] else achievements[i]
  achievements2[name]=achievements
  with open('truthdata.json','w') as j:
    j.write(json.dumps(achievements2)) 
    
def getkey1(HI=False):
  global istime,afk,gettingkey,keyz
  tmp = istime
  gettingkey,afk,istime=True,True,False
  while afk:
    pass
  po0=keyz
  keyz=''
  gettingkey,istime=False,tmp
  return po0.lower() if not HI else po0
def chest():
  global tinyvars,notedict
  if smallvarget('chest'):
    printt("The chest is completly empty, expect for a scrap of paper at the bottom.",1)
    printt("Pick it up? (y/n)")
    h=getkey1()
    c()
    if h=='y':
      print("You found: Note 9\n(Press 'E' to access your notes)")
      notedict['Note 9'][0],tinyvars['chest']=True,False
      getkey1()

def ischar(direc,chars,canerror=True):
  chars=[chars] if type(chars)==str else chars
  try:
    return (mazeq[box1-1] in chars or mazeq[box3-1] in chars) if direc=='left' else (mazeq[box2+1] in chars or mazeq[box4+1] in chars) if direc=='right' else (mazeq[box2-52] in chars or mazeq[box1-52] in chars) if direc=='up' else (mazeq[box3+52] in chars or mazeq[box4+52] in chars) if direc=='down' else False
  except: #for down cases
    return (IMTOTALLYFINE if canerror else False)
def npctalker(direc):
  global thedictionwords,tinyvars
  if mazeq in [TheOne1,TheOne2,TheOne3,TheOne4,TheOne5,TheOne6,KeyRoom,True1,True2,True3,True4] and 'Unspoken Relic' in inventory:
    thethinger,mName='',returnword(mazeq)
    for i in tolook4[mName]:
      for i2 in i:
        if ischar(direc,i2):
          thethinger=thedictionwords[i][mName][thedictionwords[i][mName.lower()]]
          thedictionwords[i][mName.lower()]=1
          break
    if thethinger=='':
      return
    if not any([direc=='left' and ischar('left','⊞'),direc=='right' and ischar('right','⊟'),smallvarget('MYARMS') and '\033[38;5;12m' in thethinger]):
      printt(thethinger,2)
    else:
      tinyvars['MYARMS']=True
      printt("MY ARMS MY POOR ARMSSSSSSSSSSSS\n"+ast+'I CANT FEEL THEM I CANTTTTTTTTTTTTTTTTTTTT\n'+ast+'jk lol im just a box chill if you wanna eat the other half go ahead',1)
    time.sleep(2)
    anykey()
getoitem=False
unlockdict={
  'Plank':['Boat'],
  'Paddle':['Boat'],
  'Wiring':['Multi Wiring'],
  'Multi Wiring':['Super Wiring']
}
thelimiter=3
def itempick(dire,hehe=False,recursion=False):
  global inventory,itemdict,mazeq,items,getoitem,notedict,tinyvars,craftablelol,craftdict,volts,istime
  hehe2=False
  liop,liop2='```','```'
  for nu in {'left':[box1-1,box3-1],'right':[box2+1,box4+1],'up':[box1-52,box2-52],'down':[box3+52,box4+52]}[dire]:
    if mazeq[nu] in items:
      liop,liop2=mazeq[nu],nu
   
  if liop!='```' and liop!='❖':
    istime=False
    print((('\n\nYou found:'+bold+'\n'+itemdict[liop]+R+'\n\n') if liop in itemdict else ''),end='')
    if liop not in notes and liop not in mindict.keys():
      print('\nWould you like to pick this up (y for yes, n for no)?\n',end='')
      resr=getkey1()
      if resr in ['y','yes','ye']:
        if len(inventory)<thelimiter or itemdict['Module E']=='Yes' and 'Unspoken Relic' not in inventory:
          getoitem=True
          if itemdict[liop] not in modli:
            print("Item added to inventory")
          if itemdict[liop] in unlockdict.keys():
            for i in unlockdict[itemdict[liop]]:
              if not craftdict[i][0]:
                print(bold+"(Unlocked "+i+' recipe!)'+R)
                craftdict[i][0]=True
                craftablelol=True
          inventory.append(itemdict[liop])
          mazeq[liop2]='-'
          if itemdict[liop] in modli and returnword(mazeq)!='TheOne6':
            printt("You reach for the item....",2)
          if itemdict[liop]=='Module A':
            if not smallvarget("Aa") and returnword(mazeq)!='TheOne6':
              smallvarchange("Aa")
              if itemdict['Module C']=='Yes':
                printt(bold+"Life.",2)
                printt("Made by the island to give those who equip it another chance."+R,3)
              else:
                printt("You feel lighter, almost stronger upon touching the object.",2)
                printt("You have a sudden urge to equip it.",3)
          if itemdict[liop]=='Module B':
            if not smallvarget("Bb") and returnword(mazeq)!='TheOne6':
              smallvarchange("Bb")
              printt(bold+"Interconnection.",1)
              printt(bold+"This part of the island is the Land.",2)
              printt("The Ancestors of this place made walls interconnected with this module, allowing the passing through these special walls.",2)
              printt("Equip this module and go to the cave."+R,3)
          if itemdict[liop]=='Module C':
            if not smallvarget("Cc") and returnword(mazeq)!='TheOne6':
              smallvarchange("Cc")
              printt("It calls your name, putting thoughts into your head",1)
              printt("You instantly feel soothed, "+bold+'and for good reason.'+R,3)
            if returnword(mazeq)=='TheOne6':
              printt(bold+"So... You made it out.",2)
              if 'The Key' in inventory:
                printt(["You even managed to kill "+R+"him."+bold,"You truly deserve this ending. \nBefore you leave, you should check out the door to the right...","With the power of all the modules, the simulation inside should be interesting."],[2,2,2])
              else:
                printt(["But does it feel like you\'re missing something?",'Perhaps... A key?',"...","Well I didn't expect you to find out what "+ArtD+"it"+R+bold+" can do anyway...\nNo one ever does. It brought you here, and I guess that's all that matters.","When you are ready, the door is wide open.\nThis is no prison "+name+', more of a collection of prisons...'],[2,1,2,3,2])
                printt("Were you prepared for the truth?")
                time.sleep(2)
          if itemdict[liop]=='Module D':
            if not smallvarget("Dd") and returnword(mazeq)!='TheOne6':
              smallvarchange("Dd")
              printt([bold+"The Final Test.","Made to award the real survivors of this place.",bold+"The key to escaping this place."],[2,1,2])
              printt(bold+"Dont give up now."+R)
              time.sleep(2)
          if itemdict[liop]=='Module E':
            if not smallvarget("Ee") and returnword(mazeq)!='TheOne6':
              smallvarchange("Ee")
              if itemdict['Module C']=='Yes':
                printt(bold+"Go beyond what human limits are",2)
                printt(bold+"Upon equipping you shall gain infinite storage."+R)
              else:
                printt("It seems to weigh nothing.",2)
                printt("Other than that, nothing else sticks out.")
              time.sleep(2)
        else:
          print("Inventory full. (Cannot pick up)")
        anykey()
        c()
      else:
        c()
    else:
      if liop not in mindict.keys(): #NOTES PICKING UP
        notedict[itemdict[liop]][0]=True
        m=0
        for i in ['Note 1','Note 2','Note 3','Note 4','Note 5','Note 6','Note 7','Note 8','Note 9','Note ?']:
          if notedict[i][0]==True:
            m+=1
        if m==9:
          achieve('Big lure')
        if m==10:
          achieve('???')
        mazeq[liop2]='-'
        print("Press 'E' to access your notes.")
        time.sleep(1)
        anykey()
      else: #MINER MINIGAME THINGS
        if (len(set_inv())<thelimiter or itemdict['Module E']=='Yes' or mindict[liop][0] in inventory) and inventory.count(mindict[liop][0])<mindict[liop][1]:
          if mindict[liop][0]!='Rock': #for minerals
            print("You found: "+mindict[liop][0]+"!")
            anykey()
          inventory.append(mindict[liop][0])
          mazeq[liop2]='-'
        else:
          if not hehe:
            print("Inventory full!")
            anykey()
            hehe2=True
        if (dire in ['left','right'] and (mazeq[liop2+52]=='i' or (mindict[liop][0]=='Rock' and mazeq[liop2+52] in mindict.keys()))) or (dire in ['up','down'] and (mazeq[liop2+1]=='i' or (mindict[liop][0]=='Rock' and mazeq[liop2+52] in mindict.keys()))):
          if (len(set_inv())<thelimiter or itemdict['Module E']=='Yes' or (mindict[liop][0] in inventory and inventory.count(mindict[liop][0])<mindict[liop][1])) and not recursion:
            itempick(dire,hehe2,True) #for eating through two rocks at once basically, added a 3rd option because idk how to fix this lol
      istime=True
  else:
    if liop!='```':
      mazeq[liop2]='-'
      if volts==0:
        print("\nA volt...")
      else:
        print("\nAnother volt... ")
      volts+=1
      print(str(volts*10)+'% collected')
      if volts==20:
        achieve('Overclock')
      anykey()
def detup(r=True):
  return mazeq[box1-52 if r else box3+52]
f=''
redc=ArtD
grec=ArtB


id1='\\\\VOID-D\\\\'
id2='\\\\VOID-B\\\\'
Truth=''
def truthtime():
  global istime,Truth,mazeq,erasin,timec,timero,itemdict,afk,goods
  istime=False
  timec=timez[300]
  timero=300
  try:
    Truth.paused=True
  except:
    pass
  c()
  slepy(1)
  printt(R+"\nSimulation: Part 1",.09,1)
  printt(bold+"Complete.",.09,2)
  printt("\nExit Activated."+R,.09,3)
  c()
  musicstop()
  time.sleep(1)
  if 'Bat' in achievements.keys(): #outdated stuff but maybe i keep
    printt(colorsp()+'HEYA KID!!!!!!!!!!')
    slepy(2)
    printt(colorsp()+'WAIT WHY ARE YOU [In existence.]')
    slepy(1)
    printt(colorsp()+"YOU FREED YOURSELF????? [[Almost]] NOW THATS WHAT I LIKE TO SEE.")
    slepy(1)
    printt(colorsp()+"LETS HOPE YOU DONT DIE LIKE ALL THE OTHERS HAAAAAAAAHAHAHA [[Everyone is dead.]]"+R)
    slepy(4)
    c()
  if name!='Muffinlavania':
    printt(redc+'User "'+name+'" not in moderator list.',0.05,False,True)
  else:
    printt("'Muffinlavania' is cool. Because he made me.")
  time.sleep(1)
  printt("Identify yourself."+R,0.03,False)
  if acheck('Escape.'):
    print('(Press s to skip the dialogue)')
  print(">")
  h=getkey1()
  if not (h=='s' and acheck('Escape.')):
    c()
    printt(redc+"Invalid Syntax."+R,.02,False)
    slepy(2)
    c()
    printt(redc+"Restarting Simulation..."+R,0.05,False)
    slepy(3)
    c()
    printt(grec+id1+", the player has already gone through the simulation.\n",0.05,False)
    slepy(2)
    printt(redc+"I am merely doing my duties, "+id2+'.\nThis player is not special.\n',0.03,False)
    slepy(3)
    printt(grec+"It seems like the player somehow got here... ",False,False)
    slepy(1)
    printt("intentionally.",0.05,False)
    slepy(3)
    printt(redc+'\n'+id2+", the user is not a developer, nor a "+bold+"Carrier"+R+redc+" like you and me.",0.05,False)
    slepy(2)
    printt('\n'+grec+"The player bears the 5 "+bold+"Keys"+R+grec+".",0.05,False)
    slepy(3)
    if 'The Key' in inventory:
      printt("They also possess knowledge about "+R+"him.")
      slepy(2)
    printt("\n"+redc+"The Keys were meant to be hidden away, never to be found again.",0.05,False)
    slepy(1)
    if 'The Key' in inventory:
      printt("As for "+R+'him'+redc+", I thought we had agreed to leave that behind us.")
      slepy(2)
    printt("This ending is supposed to be impossible "+id2+".\n",0.05,False)
    slepy(3)
    printt(grec+"You know the rules "+id1+", no matter the player, they must be given a chance.\n",0.05,False)
    slepy(3)
    printt(redc+"...",0.05,False)
    slepy(1)
    printt("If you insist "+id2+"."+R,0.09)
    slepy(4.5)
    c()
    slepy(1)
    printt(redc+name+', you are about to be transported into'+bold+" The Truth"+R+redc+".")
    slepy(2)
    printt("There is no going back from here, the only way out is to outrun The Erase.")
    slepy(2)
    printt(grec+"\nWhat we mean by 'The Erase' is the Simulation's way of keeping its participants inside.\n")
    slepy(3)
    printt(redc+"Once inside, you might see... something out of the ordinary.")
    slepy(1)
    printt(grec+"\nWhatever you do, do not touch The Erase.\nThe island does not give second chances.")
    slepy(2)
    printt("Good luck, and may the island be in your favor.")
    slepy(2)
    printt(R+"\n\n[Enter to continue to "+bold+"The Truth"+R+"]")
    getkey1()
  c()
  themod=random.choice(['Module C','Module A','Module B','Module D','Module E'])
  if name=='Muffinlavania':
    themod='Module D'
  itemdict['Module D']="No"
  if themod!=None:
    if themod!='Module E':
      itemdict[themod]='Yes'
    if themod=='Module A':
      printt(ArtA+'...')
      slepy(1)
      printt("You seem quite determined.")
      slepy(2)
      printt("With the help of "+bold+'Module A,'+R+ArtA+' you shall gain one extra life.')
      slepy(1)
      printt("Use it wisely."+R)
    if themod=='Module B':
      printt(ArtB+"...")
      slepy(1)
      printt("I can only assist you by giving you "+bold+"Module B."+R+ArtB)
      slepy(1)
      printt("I see some walls at this stage get influenced by its power...")
      goods.append('3')
    if themod=='Module C':
      printt(ArtC+bold+"...")
      slepy(1)
      printt("This is it huh.")
      slepy(2)
      printt("I can slow down the Erase, but the rest is up to you..")
      slepy(2)
      printt("Good luck out there.")
    if themod=='Module D':
      printt(ArtD+'...')
      slepy(1)
      printt('Maybe you can be the player who makes it out.')
      slepy(1)
      printt("With the help of "+bold+"Module D,"+R+ArtD+" you can stop The Erase quickly three times with the press of 'E'.")
      slepy(2)
      printt("Use it wisely.")
    if themod=='Module E':
      printt(ArtE+'...')
      slepy(1)
      printt("With the power of "+bold+'Module E,'+R+ArtE+' you shall gain access to any other Module...')
      printt("Which module would you like to have?")
      slepy(1)
      hhe=0
      pki={'Module A':ArtE+'Another life. Good choice.','Module B':ArtE+'Easier Maps. Good choice.','Module C':ArtE+'Influence on The Erase. Good choice.','Module D':ArtE+'A buffer. Good choice'}
      pki2={'Module A':'(Module A gives you another life!)','Module B':'(Module B lets you take shortcuts!)','Module C':'(Module C slows down the Erase permanently!)','Module D':'(Module D allows you to stop the erase shortly three times with \'E\'!)'}
      print(R,end='')
      for i in pki.keys():
        hhe+=1
        print(str(hhe)+') '+i)
        slepy(.5)
      while hhe not in ['1','2','3','4']:
        hhe=getkey1()
      hhe=int(hhe)-1
      j=['Module A','Module B','Module C','Module D']
      printt(pki[j[hhe]])
      slepy(2)
      printt(pki2[j[hhe]])
      itemdict[j[hhe]]='Yes'
      if j[hhe]=='Module B':
        goods.append('3')
    time.sleep(2)
    print(R+"[Any key to continue to "+bold+"The Erase]")
    getkey1()



  mazeq=Boss1
  erasin=True
  istime=True
  q2 = THREAD(target=TheErase)
  q2.start()
  c()
#START YSKYSN
r='\033[0m'
def yskysn():
  global istime,afk
  istime=False #disables time
  playin=list('''
 wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwR
 wgwwggggggggggggggggggggggggggggggggggggggggggggggggggggwwwwwR
 wwwg____________________________________________________gggwwR
 wgg__~_______~_______~_______~_______~_______~_______~___gwwwR
 wwg_____________________________________________________ggggwR
 wwwg____________________________________________________gwwgwR
 wwwg_~_______~_______~_______▢_______~_______~_______~__ggwwwR
 wgwg_____________________________________________________gwgwR
 wgg______________________________________________________ggwwR
 wg___~_______~_______~_______~_______~_______~_______~___wgwwR
 wwg_____________________________________________________ggwwwR
 wgwg____________________________________________________gwgwwR
 wwwg_~_______~_______~_______~_______~_______~_______~__gwwgwR
 wwwg____________________________________________________gwwgwR
 wwwwggggggggggggggggggggggggggggggggggggggggggggggggggggggwwwR
 wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwR''')
  bhp,yehp,owie,iframamo=1000,100,0,1.5
  dang,orang,theows,thereds,thewhites=[],[],[],[],[]
  cutscene,iframes,attackin=False,True,True
  thesymlist,theintlim=['⊿','▲','△','▴','▵'],-1 #was going to be for attack 1 multiple words at once so eh
  upimps,leftside,leftimps,rightside,rightimps,spaced=[135,143,151,159,167,175,183],[134,198,262,326,390,454,518,582,646,710,774,838],[198,390,582,774],[185,249,313,377,441,505,569,633,697,761,825,889],[249,441,633,825],[199,207,215,223,231,239,247,391,399,407,415,423,431,439,583,591,599,607,615,623,631,775,783,791,799,807,815,823]
  turnramp={0:-1,1:-1,2:-1,3:-1,4:-1,5:-1} #:flushed:
  JUSTUPIT,nonr,kys,itsafirst,hasspidy=False,False,False,True,False #itsafirst first attacking turn, 2.6 spidy cycle
  zeeeee,whereheat,dmgmul=0,0,1
  noheal,xtreme,bmulti=False,False,1 #different modes
  coloreddict={
    'o':'\033[48;5;0m ', #black for the border
    '-':'\033[48;5;233m ', #black (background)
    '_':'\033[48;5;235m ', #gray blac (background)
    'w':'\033[48;5;253m ', #white (lightning)
    'W':'\033[48;5;7m ', #white (normal)
    'b':'\033[48;5;130m ','m':'\033[48;5;3m ', #mouth color
    'B':'\033[48;5;94m ', #brown (darker)
    'r':'\033[48;5;88m ', #red (glow)
    'n':'\033[48;5;18m ','x':'',
    'g':'\033[48;5;242m ', #gray (for background)
    'G':'\033[48;5;236m ', #gray (for hair)
    'Q':'\033[38;5;46m','!':'\033[38;5;174m','@':'\033[38;5;181m','#':'\033[38;5;181m','$':'\033[38;5;181m',
    'R':'\033[0m','▢':'\033[38;5;51m▢', #player
    '~':'\033[38;5;62m◌'} #empty space to move in
  stats4nerds={'turns':0,'speak':0,'magic':0,'heal up':0,'kys':0,'yskysn heals':0,'dream mask':0,'rusty mask':0,'hockey mask':0,'doctors':0,'damage taken':0,'useless turns':0}
  if acheck("LYS"):
    c()
    print("\033[38;5;88mYSKYSN\033[0m recognizes you...\nIt's as if he is expecting something.")
    cOL = lambda u: "\033[38;5;1m2x boss hp" if u=="3" else "\033[38;5;93mLean" if u=='16' else "\033[38;5;159mNo heals" if u=='12' else "Normal" if u=='22' else "\033[38;5;130mNo hit."
    if (SAVE:=acheck("s"))!=False:
      if len(SAVE)==4:
        SAVE.append(False)
      print(f"\033[38;5;153mSave data detected! (l to load, will get overwritten if new game started!)\033[0m\n\tMode: {cOL(SAVE[0])}{r}\n\tYour hp: {SAVE[1]}\n\tBoss hp: {SAVE[2]}\n\tSpidy?: {SAVE[4]}\n\tOther stats: Would take up too much space rn. L.")
    if (g:=all([acheck("YSLYSN"),acheck("True Chad"),acheck("LEAN"),acheck("Double takedown")])):
      print("\n\033[38;5;67m0) .....\n")
    print(f"\n\033[38;5;1m{'1 - Open a window':<40}(x2 boss hp!)\n\033[38;5;93m{'2 - Give him lean':<40}(enables extreme mode!)\n\033[38;5;159m{'3 - Engulf yourself in lightning':<40}(disables heals!)\n\033[38;5;130m{'4 - Give into the hate.':<40}(don't.)\n\033[0m{'5 - Stare back at him':<40}(normal boss)\n\n[All harder modes give a special ending..., x to just exit]")
    dalist = [('0' if g else '1'),('l' if SAVE!=False else '1'),'1','2','3','4','5','x']
    while (jy:=getkey1()) not in dalist:
      pass
    c()
    if jy=='x':
      istime=True
      return
    if jy=='0' and 2==1:
      pass #add stuff
    elif jy=='l':
      print("\033[38;5;88mYSKYSN\033[0m smiles.\n(Loaded game!)")
      noheal,xtreme,bmulti,nonr,yehp,bhp,stats4nerds,hasspidy=SAVE[0] not in ['16','3','22'],SAVE[0]=="16",2 if SAVE[0]=="3" else 1,SAVE[0] not in ['16','3','12','22'],SAVE[1],SAVE[2],SAVE[3],SAVE[4]
    elif jy in ['0','1']:
      printt(['The window opens, letting in even more lightning.',"\033[38;5;88mYSKYSN\033[0m grows even stronger... (\033[38;5;88mYSKYSN\033[0m HP raised to 2000!)"],[2])
      bmulti=2
      bhp=2000
    elif jy=='2':
      printt(["With one chug, his face grows even brighter...","(\033[38;5;88mYSKYSN\033[0m gets even faster and stronger!)"],[2,1])
      xtreme=True
    elif jy=='3':
      printt(['The lightning feels \033[38;5;88mgreat\033[0m. You feel like giving in at any time...','\033[38;5;124m(Healing has been disabled!)'],[1,.02])
      noheal=True
    elif jy=='4':
      printt(["...","You feel....."+R+" meaningless.","At any moment, your life can be worth nothing.","\033[38;5;130m[No hit mode enabled (good luck)]"],[2,1,1,.02])
      yehp=1
      noheal=True
      nonr=True
    else:
      print(['\033[38;5;88mYSKYSN\033[0m looks back in anger.','\033[38;5;88mA waste of oxygen. I mean that, with 100 percent, a thousand percent.'+R],[1,1])
    anykey()
    if nonr:
      coloreddict['n']='\033[48;5;52m '
    if noheal:
      coloreddict['r']='\033[48;5;253m '
    if xtreme:
      coloreddict['r']='\033[48;5;91m '
  buttons='''
   !╓─────────╖  R @╓─────────╖      R #╓─────────╖    R$╓─────────╖
   !║  SPEAK  ║ R  @║  MAGIC  ║      R #║ HEAL UP ║   R $║   KYS   ║
   !╙─────────╜ R  @╙─────────╜     R  #╙─────────╜  R  $╙─────────╜
  '''
  #thresholds: 600, 300
  #for health: 750, 500, 250
  #idea, yskyn changes mouth colors the less health he has: 3 for start, 131 for med, 196 for low (also change hp color?) 9 for YSLYSN
  #when he becomes yslyn eyes ('W') change from 7 to 239
  hddict={4:'\033[38;5;46m',3:'\033[38;5;46m',2:'\033[38;5;6m',1:'\033[38;5;166m',0:'\033[38;5;196m'}
  saying={10:['\033[38;5;160m','Why are you here, just to worship me?'],9:['\033[38;5;160m','Kill yourself, now!!!!!!'],8:['','YSKYSN hates the crowd, YSKYSN kills the crowd.'],7:['','There is no more crowd.'],6:['','Lightning crackles all around you.'],5:['','YSKYSN is getting mad...'],4:['\033[38;5;160m','You serve ZERO purpose.'],3:['','Something about him seems less menacing.'],2:['','YSKYSN looks very tired...'],1:['','A sense of order emerges.'],0:['','Peace soon to come.']}
  def up(gu=False):
    print("\033[H",end="\n"*15)
    if gu:
      printman(playin,False)
      print('\n\033[38;5;'+str(93-(5-(yehp//20)))+f'm{"Health - "+str(yehp):^63}')
  noballs=['!','@','#','$']
  def turn2(ab,lol):
    nonlocal turnramp
    for i in turnramp.keys(): #disables ramping for the uh bad ones
      if i!=ab and lol==ab:
        turnramp[i]=-1
      elif i!=ab and turnramp[i]>-1:
        turnramp[i]-=1
    turnramp[ab]+=(1 if not xtreme else random.choice([2,3]))
  def danger(space,nubi=1,timee=2):
    nonlocal JUSTUPIT,dang
    if type(nubi)==int:
      for i in range(0,nubi):
        dang.append(space-i if space in rightside else space+i if space in leftside else space+(64*i))
    else:
      for i in nubi:
        dang.append(i)
    JUSTUPIT=True
    TY.sleep(timee)
    dang=[]
    JUSTUPIT=True
    return -1 if space in rightside else 1
  def more(theone,amoint,symb,dirt=1,timri=.5): #space to place, amount more, symbol to place, direction going (1/-1), time inbetween moves
    nonlocal playin,theows,JUSTUPIT,thereds
    if type(theone)!=list:
      for ib in range(amoint):
        if playin[theone+(ib*dirt)] not in ['▢','g','w','\n','R']:
          theows.append(theone+(ib*dirt))
          if symb=='r':
            thereds.append(theone+(ib*dirt))
          playin[theone+(ib*dirt)]=(symb if (ib==0 and dirt==1 or ib==amoint-1 and dirt==-1 or symb=='r') else 'x')
        else:
          if symb!='r':
            for ie in range(ib):
              playin[theone+(ie*dirt)]=playinref[theone+(ie*dirt)]
            return 'hit' if playin[theone+(ib*dirt)]=='▢' else 'end'
          else:
            thereds.append(theone+(ib*dirt))
            theows.append(theone+(ib*dirt))
    else:
      for i in theone:
        theows.append(i)
        thewhites.append(i)
        if playin[i]!='▢':
          playin[i]=symb
    JUSTUPIT=True
    TY.sleep(timri)
    if type(theone)!=list:
      for ib in range(amoint): #undo the stuff
        if playin[theone+(ib*dirt)]!='▢': #no killing yourself >:(
          playin[theone+(ib*dirt)]=playinref[theone+(ib*dirt)]
        theows.remove(theone+(ib*dirt))
    else:
      for i in theone:
        if playin[i]!='▢':
          playin[i]=playinref[i]
        theows.remove(i)
        thewhites.remove(i)
  def returnit(h=False):#True=in left, False = in right
    return ((198 if h else 249) if (e:=playin.index('▢')) in [199,207,215,223,231,239,247] else (390 if h else 441) if e in [391,399,407,415,423,431,439] else (582 if h else 633) if e in [583,591,599,607,615,623,631] else (774 if h else 825))
  phase1li=['HATE','DIE.','BURN','HATE','DIE.','BURN','KYSN','STOP','HATE','DIE.','BURN','KYSN','STOP','hihi','BURN','KYSN','KYSN','BURN','HAHA','LMAO','HEHE','GRRR',"BUMB"]
  def attack(lol=9): #find attack
    nonlocal playin,attackin,theintlim,coloreddict,iframes,yehp,orang,theows,JUSTUPIT,owie,turnramp,cutscene,iframamo
    TY.sleep(1)
    if bhp in [420,69,666]:
      yehp=999999
      c()
      cutscene=True
      TY.sleep(1)
      c()
      print('\033[38;5;88mYSKYSN\033[0m HP: '+str(bhp))
      TY.sleep(1)
      printt("\033[38;5;196mYou have activated his trap card...."+r)
      TY.sleep(2)
      cutscene=False
      if attackin:
        c()
        printman(YS[0:960])
        JUSTUPIT=True
        TY.sleep(2)
      if attackin:
        sound("Truth/KYSAFE.wav")
      iframamo=.25
      yehp+=round(690*dmgmul) #even though this is almost perfect, theres a way to cheese it...
      owie=20
      for i in range(0,69):
        if yehp>0:
          orang=spaced.copy()
          orang.remove(random.choice(orang))
          JUSTUPIT=True
          TY.sleep(.1)
          for i in orang:
            theows.append(i)
          JUSTUPIT=True
          TY.sleep(.1)
          theows=[]
          orang=[]
          JUSTUPIT=True
      yehp=1
      iframamo=1.5
      attackin=False
      return
    elif bhp>=900*bmulti or lol==0:#phase 1, words come frop left/right
      turn2(0,lol)
      owie=5+turnramp[0]
      for i in range(random.randrange(7,(10 if lol!=0 else 15)+turnramp[0])):
        if yehp>0:
          kf=random.choice(random.choice([leftimps,rightimps]))
          JUSTUPIT=True
          rw=((1 if lol!=0 else .25)-(.25 if xtreme else 0)-turnramp[0]/10)
          tru=danger(kf,4,rw if rw>0 else 0) #returns the direction its gonna go (-1 or 1)
          theintlim+=1 #this and thesymlist were for if i was gonna make many words at once which i never did lol (maybe some day!!!)
          metan=thesymlist[theintlim]
          coloreddict[metan]=random.choice(phase1li)
          h4='hehehaha'
          while h4 not in ['end','hit']:
            hei=(.4 if lol!=0 else .2)-(.1 if xtreme else 0)-turnramp[0]/40/(3 if xtreme else 1)
            h4=more(kf,4,metan,tru,hei if hei>.1 else .1)
            kf+=(8*tru)
          if h4=='hit' and not iframes:
            damage(((5 if lol!=0 else 10)+turnramp[0]+(2 if xtreme else 0))*dmgmul)
          theintlim-=1
    elif bhp>=750*bmulti or lol==1:#phase2, random spaces
      turn2(1,lol)
      owie=(8 if lol!=1 else 10)+(5 if xtreme else 0)+turnramp[1]
      for i in range(random.randrange((5 if lol!=1 else 8)+turnramp[1],(9 if lol!=1 else 14)+turnramp[1])):
        if yehp>0:
          orang=[]
          for i in range(random.randrange((10 if lol!=1 else 15),(17 if lol!=1 else 21))):
            orang.append(random.choice(spaced))
          JUSTUPIT=True
          TY.sleep((1.5 if not xtreme else .75)-(.75 if lol==1 and not xtreme else .25 if lol==1 else 0))
          for i in orang:
            theows.append(i)
          JUSTUPIT=True
          TY.sleep((1 if lol!=1 else .25)-(.2 if xtreme else 0))
          theows=[]
          orang=[]
          JUSTUPIT=True
          wer=(1 if lol!=1 else .5)-(.5 if xtreme else 0)-turnramp[1]/20
          TY.sleep(wer if wer>0 else 0)
    elif bhp>=600*bmulti or lol==2:#phase3, lasers up/down
      turn2(2,lol)
      owie=(10 if lol!=2 else 15)+(5 if xtreme else 0)+turnramp[2]
      for i in range(random.randrange((7 if lol!=2 else 10),(10 if lol!=2 else 13)+turnramp[2])):
        if yehp>0:
          spacer=random.choice(upimps)
          suret=danger(spacer,12,(1 if lol!=2 else .6)-(.3 if xtreme else 0))
          more(spacer,12,'r',64,(.9 if lol!=2 else .5)-(.3 if xtreme else 0))
          TY.sleep((1 if lol!=2 else .25)-(.2 if xtreme else 0))
          thereds=[]
    elif bhp>=500*bmulti or lol==3: #phase3.2, lasers up/down but faster (MAYBE CHANGE TO 2 lasers??)
      turn2(3,lol)
      owie=(10 if lol!=3 else 13)+turnramp[3]
      for i in range(random.randrange((0 if lol!=3 else 3)+(9 if not xtreme else 12),(0 if lol!=3 else 5)+(15 if not xtreme else 19)+turnramp[2])):
        if yehp>0:
          spacer=random.choice(upimps) #for this attack doesnt change for random one, cause its basically the one above but harder (at least not much)
          suret=danger(spacer,12,.5-(.2 if xtreme else 0))
          more(spacer,12,'r',64,.4-(.25 if xtreme else 0))
          TY.sleep((.5 if lol!=3 else .25)-(.25 if xtreme else 0))
          thereds=[]
    elif bhp>=400*bmulti or lol==4: #phase 4, lasers on rows
      turn2(4,lol)
      owie=(15 if lol!=4 else 20)+(5 if xtreme else 0)+turnramp[4]
      for i in range(random.randrange((7 if lol!=4 else 13),(14 if lol!=4 else 18))):
        if yehp>0:
          spacer=random.choice(random.choice([leftimps,rightimps]))
          surt=danger(spacer,51,(.75 if lol!=4 else .5)-(.25 if xtreme else 0))
          more(spacer,51,'r',surt,(.5 if lol!=4 else .3)-(.25 if xtreme else 0))
          TY.sleep((.5 if lol!=4 and not xtreme else 0))
          thereds=[]
    elif bhp>=100*bmulti or lol==5:
      turn2(5,lol)
      owie=13+(5 if xtreme else 0)+turnramp[5]
      for i4 in range(random.randrange((15 if lol!=5 else 20),(25 if lol!=5 else 30))):#phase 5, lightning bolts come from both sides to your space using algorithm thing
        ni1,ni2=random.choice(leftimps),random.choice(rightimps)
        pos=whereheat #so 0% chance for error lol (whereheat is player pos)
        lists={ni1:[],ni2:[]}
        for i in [ni1,ni2]:
          hei=abs(returnit(i in leftside)-i)//64
          wid=abs((i+(hei*64) if pos>i else i-(hei*64))-pos)
          muli=(-1 if i in rightside else 1)
          try:
            nuqe=i
            lists[i].append(i)
            refn=wid//hei*hei
            for i2 in range(hei):
              for i3 in range(wid//hei):
                nuqe+=(1*muli)
                lists[i].append(nuqe)
              if wid>refn:
                nuqe+=(1*muli)
                refn+=1
                lists[i].append(nuqe)
              nuqe+=(-64 if i>pos else 64)
              lists[i].append(nuqe)
          except:
            for id in range(1,wid+1):
              lists[i].append(i+(id*(-1 if i in rightside else 1)))
        hib=lists[ni1]
        for i in lists[ni2]:
          hib.append(i)
        danger(0,hib,(.75 if lol!=5 else .5)-(.4 if xtreme and lol!=5 else .25 if lol==5 and xtreme else 0))
        more(hib,0,'w',1,((.5 if lol!=5 else .3)))
    else: #phase 6, random attacks
      for i in turnramp.keys():
        turnramp[i]=-1
      attack(random.randrange(0,6))
    attackin=False
  def printman(yt,l=True): #find print
    coi=-1
    for i in yt:
      coi+=1
      if i in coloreddict.keys() and l or (not l and (i in ['!','@','#','$','R','w','_','g','~','▢','r','x'] or i in thesymlist)):
        if coi not in dang and ((coi not in theows and coi not in orang) or i not in ['~','▢']) or l:
          print(('\033[48;5;235m' if (i in ['~','▢'] or i in thesymlist) else '')+coloreddict[i],end=(r if ('!' not in yt and i!='Q') else ''))
        else:
          if coi in dang:
            if i not in ['~','▢']:
              print('\033[48;5;88m ',end=r)
            else:
              print('\033[48;5;88m'+coloreddict[i],end=r)
          elif coi in theows:
            print('\033[48;5;235m'+(coloreddict['r'][:-1] if coi in thereds else coloreddict['w'][:-1] if coi in thewhites else '')+(coloreddict[i] if i!='~' else  coloreddict['w'] if coi in thewhites else '\033[38;5;88m◌'),end=r)
          else:
            print("\033[48;5;235m\033[38;5;208m"+{'~':'◌','▢':'▢'}[i],end=r)
      else:
        print(i,end='')
  def movi(dire): #8 left to right, 192 up/down
    nonlocal playin
    beez=playin.index('▢')
    playin[beez]='~'
    if dire in ['d',RIGHT] and beez not in [247,439,631,823]:
      playin[beez+8]='▢'
    elif dire in ['w',UP] and beez not in [199,207,215,223,231,239,247]:
      playin[beez-192]='▢'
    elif dire in ['a',LEFT] and beez not in [199,391,583,775]:
      playin[beez-8]='▢'
    elif dire in ['s',DOWN] and beez not in [775,783,791,799,807,815,823]:
      playin[beez+192]='▢'
    else:
      playin[beez]='▢'
      return 'bruh'
    return 'ok'
  def damage(amo):
    nonlocal iframes,yehp,JUSTUPIT
    if not iframes:
      iframes=True
      sound("Truth/hurt.wav")
      yehp-=round(amo)
      JUSTUPIT=True
  def OWW():
    nonlocal owie
    while attackin and yehp>0:
      try:
        if playin.index('▢') in theows:
          damage(round(owie*dmgmul))
        TY.sleep(.04)
      except:
        TY.sleep(.1)
  def iframe():
    nonlocal iframes,coloreddict
    while attackin and yehp>0:
      while not iframes:
        TY.sleep(.1)
      coloreddict['▢']='\033[38;5;225m▢'
      TY.sleep(iframamo)
      iframes=False
      coloreddict['▢']='\033[38;5;51m▢'
  def heal(at,y=True): #a lil spaget but who cares
    nonlocal bhp,yehp
    if y==True:
      if not noheal:
        if yehp>100:
          return 0
        if yehp>=100-at:
          shees=100-yehp
          yehp=100
          return shees
        else:
          yehp+=at
    else:
      if bhp>=(1000*bmulti-at):
        unshe=1000*bmulti-bhp
        bhp=1000*bmulti
        return unshe
      else:
        bhp+=at
    return at if not noheal or not y else 'no'
  selection=0
  c()
  turn='gamer'
  theender = False
  #start yskysn
  music("yskysn","Truth/election.mp3" if xtreme and nonr else "Truth/unwave.mp3",True)
  while bhp>0 and (yehp>0 or iframamo!=1.5):
    coloreddict['Q']=hddict[bhp//(250*bmulti)]
    pickin=True
    ytp=14 #for clearing thing
    if turn!='gamer':
      print("\033[H",end="")
      printman(YS[0:960])
    if turn=='gamer':
      c()
      dmgmul=1
      while pickin:
        ytp+=1
        print("\033[H",end="")
        printman(YS)
        printman('''
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\no               Q       YSKYSN HP: '''+' '*(4-len(str(bhp)))+str(bhp)+'''                        o\nooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo''')
        j=saying[bhp//(100*bmulti)]
        print("\n"+j[0]+f"{j[1]:^63}"+R+(' (no)' if bhp//(100*bmulti)==9 else ''))
        print(f"\n{'[A/D/Enter to choose, n = stats, l = leave, game saves!]':^63}")#3 = 2x boss, 16 = LEAN, 12 = No heals, 22 = normal, anything else = no hit
        if hasspidy:
          print(f'\033[38;5;1m{"[Spidy]":^63}'+R)
        coloreddict[noballs[selection]]='\033[38;5;174m'
        print(f"\n\n\033[38;5;79m{'Health - '+str(yehp):^63}")
        printman(buttons,False)
        zeeeee = stats4nerds['rusty mask']*20
        achieve("s",['3' if bmulti==2 else '16' if xtreme else f'{random.randint(26,30)}' if nonr else '12' if noheal else '22',yehp,bhp,stats4nerds,hasspidy])
        wee=getkey1() #yskysn input
        if wee in [RIGHT,LEFT,'a','d']:
          coloreddict[noballs[selection]]='\033[38;5;177m'
        if wee in [LEFT,'a']:
          selection-=1
        elif wee in [RIGHT,'d']:
          selection+=1
        elif wee=='n':
          c()
          s4=stats4nerds
          print(R+'\n----------------\nStats for nerds:\n\n\033[38;5;82m\nHealth: '+str(yehp)+'\nBoss Health: '+str(bhp)+'\nTotal Turns: '+str(s4['turns'])+'\nTotal Speaks: '+str(s4['speak'])+'\nTotal Magics: '+str(s4['magic'])+'\nTotal Heal Ups: '+str(s4['heal up'])+'\nTotal KYS: '+str(s4['kys'])+'\nTotal Dream Masks: '+str(s4['dream mask'])+'\nTotal Hockey Masks: '+str(s4['hockey mask'])+'\nTotal Rusty Masks: '+str(s4['rusty mask'])+'\nTotal Doctor\'s Kits: '+str(s4['doctors'])+'\nTotal YSKYSN Heals: '+str(s4['yskysn heals'])+'\nTotal Damage Taken: '+str(s4['damage taken'])+'\nTotal Useless Turns: '+str(s4['useless turns'])+R+'\n----------------')
          anykey()
          c()
        if wee in [ENTER,'z','l']:
          pickin=False
          theender = wee=='l'
        elif ytp%15==0:
          c()
        if selection==4:
          selection=0
        elif selection==-1:
          selection=3
      clearline(5)
      print(r)
      if theender:
        pass
      elif selection==0: #attack
        stats4nerds['speak']+=1
        printt('A'+random.choice([' loving',' graceful',' caring',' thoughtful','n emotional',' kind',' heartfelt',' cool'])+' remark makes \033[38;5;88mYSKYSN'+r+' feel a little more love...')
        slepy(2)
        damdan=random.randrange(40,101)
        que='\033[38;5;26m' if damdan>50 else '\033[38;5;32m' if damdan>60 else '\033[38;5;38m' if damdan>70 else '\033[38;5;44m' if damdan>80 else '\033[38;5;50m' if damdan>90 else '\033[38;5;135m'
        printt('Just a small bit though...' if damdan<60 else 'It had some effect..' if damdan<74 else 'He seems to have felt that...' if damdan<90  else 'You hit him in a sensitive spot...')
        print(que+'('+str(damdan+zeeeee)+' damage dealt!)'+r)
        bhp-=damdan+zeeeee
      elif selection==1: #magic
        stats4nerds['magic']+=1
        printt("If only you were a wizard...",1)
        theeven=random.randrange(0,6) #4 options?
        while theeven==1 and hasspidy:
          theeven=random.randrange(0,6)
        if theeven in [0,4,6]:
          printt("You spot a mask on the floor...",2)
          gret=random.randrange(0,3)
          if gret==0:
            stats4nerds['dream mask']+=1
            printt("A completly white one, with a slight smile on it.",1)
            printt("You suddenly feel like a cheater....")
            print('\033[38;5;123m(Health doubled!)\n(Thats what the point of the mask is)\033[0m')
            yehp=yehp*2
          if gret in [1,3]:
            stats4nerds['rusty mask']+=1
            printt("It's a rusty metal mask, with a slight hint of blood...",2)
            printt("Much to old to wear, but it sure looks cool...")
            print('\033[38;5;202m(Speech power permanently +20!)\033[0m')
          if gret in [2,4]:
            stats4nerds['hockey mask']+=1
            printt("It's a big hockey mask.",2)
            printt("Seems big enough to help for a little...")
            print("\033[38;5;98m(Halved damage taken next attack!)\033[0m")
            dmgmul=.5
        elif theeven==1: #spiderman is that you
          printt(["Suddenly a man in a red suit breaks through the wall...","Spiderman is that you??/1?!?!?","He leaves just as fast as he came.",'Seems like he forgot something...'],[2,2,1,1])
          hasspidy=True
          print("\033[38;5;1m(Spidy web obtained!)\033[0m")
        elif theeven in [2,5]: #funny
          stats4nerds['doctors']+=1
          printt(['Suddenly, a full doctors kit appears.',"It is loaded with a military grade med-kit, a defibrillator, medical gause, and much more."],[1,2])
          printt("Luckily, there are a few band-aids® nearby that useless set.")
          q=heal((40 if not xtreme else 30))
          print('\033[38;5;123m(Healed '+str(q)+' hp!)')
          if q=='no':
            print("\033[38;5;88m(The lightning prevents it.)\033[0m")
          elif q<10:
            print('(How useful...)')
          if q in ['no',0]:
            stats4nerds['useless turns']+=1
        elif theeven==3: #heal him
          stats4nerds['yskysn heals']+=1
          printt("Suddenly the thunder outside gets even more intense...",2)
          printt("His eyes crackle even brighter.")
          print('(\033[38;5;88mYSKYSN\033[0m healed '+str(heal(random.randrange(40,65),kys))+'..)')
          if heal(10,kys)==0:
            stats4nerds['useless turns']+=1
            print("(What a loser...)")
      elif selection==2: #heal up
        stats4nerds['heal up']+=1
        printt(random.choice(['Staring straight into his eyes gives you a sudden confidence...','You remember that KYS can mean keep yourself safe...','The lightning seems to fill YOU with strength...','You try to imagine his face as the man face...']),1)
        miheal=heal(random.randrange(10,31))
        if miheal=='no':
          stats4nerds['useless turns']+=1
          print("\033[38;5;88m(The lightning prevents it.)\033[0m")
        else:
          printt('\033[38;5;123m(Healed '+str(miheal)+' hp!)')
        if miheal==0:
          print("(What a great choice...)")
      elif selection==3: #kys
        stats4nerds['kys']+=1
        printt("You decide to Keep Yourself Safe.",1)
        printt("(-25% damage next turn!)")
        dmgmul=.75
      if not theender:
        anykey()
        stats4nerds['turns']+=1
        c()
        turn='kill yourself, now!!!!!!!!!!!!!!!!!'
      else:
        yehp = 0
    else:
      printman('''
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\n\n''')
      if itsafirst and name!='Muffinlavania':
        itsafirst=False
        printt(["\033[38;5;88mYSKYSN\033[0m attacks!","Use WASD or Arrow keys to dodge his various attacks!","You can move your blue square to purple circles, if the color changes you might want to move...",'Don\'t touch the walls, they are made of lightning.',"Be careful of warnings and in general dark-colored elements!","As \033[38;5;88mYSKYSN\033[0m gets weaker, his attacks get harder!"],[1,2,2,1,1,2])
        printt("[One time explaination!, any key to continue to attack one]")
        getkey1(False)
        clearline(5)
      if bhp>0:
        attackin=True
        owie=5 #change what the damage is if you are in bad space
        THREAD(target=attack).start()
        THREAD(target=iframe).start()
        THREAD(target=OWW).start()
        coloreddict['▢']='\033[38;5;51m▢'
        c()
        afk=True
        printman(YS[:960])
        if bhp>=600*bmulti:
          coloreddict['m']='\033[48;5;3m '
        elif bhp>=300*bmulti:
          coloreddict['m']='\033[48;5;131m '
        else:
          coloreddict['m']='\033[48;5;196m '
        okle=yehp
        while attackin and yehp>0:
          whereheat=playin.index('▢')
          if not cutscene:
            up(True)
          while afk and attackin and yehp>0:
            TY.sleep(.05)
            if JUSTUPIT==True and not cutscene:
              JUSTUPIT=False
              up(True)
          if keyz in ['a','s','w','d',LEFT,DOWN,UP,RIGHT] and yehp>0 and not cutscene:
            h=movi(keyz)
            if h=='bruh' and attackin:#hit walls, take damage
              damage((10 if bhp in [666,420,69] else 5)*dmgmul)
          afk=True
        if yehp>0:
          TY.sleep(.1)
          c()
          stats4nerds['damage taken']+=okle-yehp
          dmgmul=1
          print(r+"\nAttack cleared!")
          TY.sleep(.5)
          anykey()
          turn='gamer'
  musicstop()
  
  if bhp<0:
    achieve('s',False)
    c()
    coloreddict['m']='\033[48;5;166m '
    coloreddict['W']='\033[48;5;9m '
    printman(YL)
    TY.sleep(2)
    printt("\n\033[38;5;204m...")
    slepy(2)
    if hasspidy:
      printt(r+'\n[One final bolt of lightning comes from the sky,\n but luckily the \033[38;5;1mspidy bot'+r+' is there to block it...]\033[38;5;204m\n')
      if nonr:
        printt(["Even against all odds, you managed to do it.","No matter how much I got mad, you just spoke.","That means a lot man, for real."],[2,1,2])
        printt("\033[48;5;14mYou should love yourself, now!"+r)
        achieve("YSLYSN")
      elif noheal or bmulti==2 or xtreme:
        printt(['Wow.',"I was so mad I didn't even see how cool you were man."],[1,2])
        printt("Love yourself."+r)
        achieve(("True Chad" if noheal else 'LEAN' if xtreme else 'Double takedown'))
      else:
        printt(['So much.... peace.',"You are worth something.","Your life serves tons of purpose!"],[2,1,2])
        print("\033[38;5;154m[\033[38;5;204mYSLYSN\033[38;5;154m walks away with new purpose...]"+r)
        for i in coloreddict:
          if i not in ['o','-']:
            coloreddict[i]=coloreddict['-']
        print("\033[H",end="")
        printman(YL)
        print('\n'*9)
        slepy(3)
      achieve('LYS')
      anykey()
    else:
      printt('\033[38;5;60mSuddenly, one last bolt of lightning comes from the sky,\nand hits the now \033[38;5;204mYSLYSN\033[0m \033[38;5;60mdirectly in the head...',2)
      c()
      coloreddict['m']='\033[48;5;3m '
      coloreddict['W']='\033[48;5;7m '
      printman(YS)
      slepy(2)
      printt(["\n\n\033[38;5;88mYSKYSN has rebirthed!\033[0m","[If only there was something magical to block that bolt...]"],[2,1])
      print(r+"\033[38;5;6m'R' to retry the fight\n\033[38;5;60mAny other key to exit\n\033[0m[Any key to continue]")
      if getkey1()=='r':
        c()
        print('\033[38;5;196mReturning to the land of KYS...\033[0m')
        slepy(2)
        c()
        yskysn()
  elif yehp<=0 and not theender:
    achieve('s',False)
    c()
    TY.sleep(1)
    printt(r+"...")
    slepy(2)
    if nonr:
      printt("It happened, was bound to.",1)
      printt("\033[38;5;88mYour life is worth nothing!\033[0m")
    elif noheal:
      printt("The lightning surrounds you, becomes you.",2)
      printt("\033[48;5;90mEveryone else is worth nothing!")
      #insert box yskysn lol
    elif bmulti==2:
      printt('\033[38;5;88mIdiots like you shouldn\'t breathe the same air as me.',1)
    else:
      printt(["\033[38;5;88mGood job bro.","You killed yourself."],[1,2])
      printt("Why are you still here, just to worship me?\n")
    print(r+"\033[38;5;6m'R' to retry the fight\n\033[38;5;60mAny other key to exit\n\033[0m[Any key to continue]")
    if getkey1()=='r':
      c()
      print('\033[38;5;196mReturning to the land of KYS...\033[0m')
      slepy(2)
      c()
      yskysn()
  c()
  istime=True

STOP=False
STOPGOOD=0
mazechang=False
numbero=1
sipper=False
erasin=True
def TheErase():
  global mazeq,isright,isleft,timeboss,mazechang,numbero,screenup,alive,sipper,erasin,gettingkey,STOP,istime
  while erasin and alive:
    try:
      if istime and gettingkey==False and numbero!=51:
        if mazechang:
          numbero,mazechang,sipper,STOP=1,False,False,False
        if not STOP:
          if isleft:
            for i in range(19):
              mazeq[(i*52)+numbero]='╳'
          if isright:
            for i in range(20):
              if numbero==1 and sipper==False:
                mazeq[zerosad[i]]='╳'
              else:
                mazeq[(i*52)-1-numbero]='╳'
            if numbero==1 and sipper==False:
              numbero=0
              sipper=True
          screenup=True
        if itemdict['Module C']!='Yes':
          TY.sleep(timeboss[returnword(mazeq)])
        else:
          TY.sleep(timebossC[returnword(mazeq)])
        if not STOP:
          numbero+=1
      else:
        TY.sleep(.1)
    except Exception as e:
      pass
  if alive==False and not FoR:
    c()
    istime=False
    TY.sleep(2)
    c()
    printt(redc+"I told you not to let it get you.\n")
    TY.sleep(2)
    printt(grec+"This is where we say goodbye again.")
    TY.sleep(2)
    printt(grec+"Come back, and try again. You can do it.")
    achieve('Horrible Game')
    TY.sleep(2)
def leepic():
  global mazeq,erasin,current
  erasin=False
  time.sleep(1)
  printt(redc+"...")
  time.sleep(2)
  printt("Wait...")
  time.sleep(1)
  printt(["Is that you "+name+"?",grec+"\nYou made it! I knew you could.","Sadly this might be the last time you see us, as we are merely part of this simulation."],[3,2,3])
  printt(redc+'\nWelcome to the real world '+name+'.',0.07)
  time.sleep(4)
  c()
  mazeq=TheOne1
  current=50
  if 'The Key' in inventory:
    achieve('end',2)
  else:
    achieve('end',1)
def gensz():
  global docksbelike,labbelike,planebelike,inventory,facbelike,achievements,wiringvar
  #Things todo and not be noob:
  #Be able to move stuf?
  print("There seems to be some kind of terminal, and a slot for "+bold+"Wiring"+R+" under each word.\n\nThe terminal reads:\n"+bold+"\nLab     Plane     Beach    Shed\n"+' '+gensdict[labbelike]+'        '+gensdict[planebelike]+'         '+gensdict[docksbelike]+'        '+gensdict[facbelike])
  wiredboi=any(item1 in inventory for item1 in ['Wiring','Multi Wiring','Super Wiring']) #pov any omg
  print('\nWhere would you like to place your '+bold+'Wiring'+R+'?\n(b for Beach, p for Plane, s for Shed, or l for Lab)' if wiredboi else '\nYou should find a wiring, and come back.')
  print(bold+"\nYour Super Wiring will be used!\n" if 'Super Wiring' in inventory else bold+"\nYour Multi Wiring will be used! ("+str(2-wiringvar)+' uses left)\n'+R if 'Multi Wiring' in inventory else "")
  tbhidk=getkey1()
  if not wiredboi or tbhidk not in ['p','b','s','l']:
    c()
    return 
  uj={'l':'Lab','s':'Shed','b':'Beach','p':'Plane'}
  if tbhidk=='l' and not labbelike:
      labbelike=True
  elif tbhidk=='s' and not facbelike:
      facbelike=True
  elif tbhidk=='b' and not docksbelike:
      docksbelike=True
  elif tbhidk=='p' and not planebelike:
      planebelike=True
  else:
    printt(['You try to slide your wiring in that slot, but the machine wont take it.','It seems to already have one in that slot.'],[.02,.02],[2,1])
    anykey()
    return
  
  if planebelike and labbelike and docksbelike and facbelike:
    achieve('Pro fix')
  if 'Super Wiring' in inventory:
    printt(["You try powering the "+uj[tbhidk]+' slot with your '+bold+'Super Wiring...'+R,"The slot gets powered before you even place it."],[2,1])
  else:
    printt(["You put your "+bold+('Multi Wiring' if "Multi Wiring" in inventory else "Wiring")+R+' into the '+uj[tbhidk]+' slot.',"Suddenly one of the lights turns green.\n"+bold],[1,.01],[True,1])
    if 'Multi Wiring' in inventory:
      wiringvar+=1
      if wiringvar==2:
        wiringvar=0
        printt("The Multi Wiring uses the last of its power...")
        inventory.remove('Multi Wiring')
      else:
        printt("The Multi Wiring still has more power! (One more use)")
    else:  
      inventory.remove('Wiring')
  anykey()
remainderp=['Plane Propeller','Plane Hull(Part)','Plane Fuel']
PLANED=False
def planet():
  global inventory,remainderp,maze10,PLANED,alive,achievements
  if len(remainderp)>0:
    tempE=[]
    for qn in inventory:
      if qn in remainderp:
        tempE.append(qn)
    for E in tempE:
      remainderp.remove(E)
      inventory.remove(E)
    if tempE!=[]:
      printt("You place your "+bold+", and ".join(tempE)+R+" on the plane",3)
    if 'Plane Hull(Part)' in tempE:
      for _ in range(2):
        maze10[maze10.index('`')]='~'
    elif 'Plane Propeller' in tempE:
      for _ in range(2):
        maze10[maze10.index('_')]='~'
    if itemdict['Module C']=='Yes' and remainderp!=[]:
      printt(bold+"The plane is still missing: "+",".join(remainderp)+'.')
    if remainderp==[]:
      printt("\nThe plane is fully repaired!")
    if tempE!=[]:
      anykey()
  else:
    if planebelike:
      istime=False
      printt("The plane is running...")
      time.sleep(2)
      printt('Do you want to get in? [\033[38;5;194mThis will end your game\033[0m]\n(y for yes n for no)')
      thinp=getkey1()
      if thinp=='y':
        funnyfunction()
        printt(["You get in the plane.","You fly it off the island."],[2,.02])
        time.sleep(2)
        if itemdict['Module C']=='Yes':
          printt(bold+"Its no use.")
          time.sleep(2)
          printt(["Theres only one true way out.","You will run out of gas eventually, and, as always, be back at the island.","You must break the chain. I'm sorry."],[2,2,.02])
          time.sleep(3)
        else:
          time.sleep(3)
          printt(["Within 3 hours your plane starts to run out of fuel...","It seems as if the plane suddenly stops.","You start to lose control of your breathing, and it seems as if time itself stops.","You close your eyes, ready to be in the ocean when you wake."],[3,4,3,.02])
          time.sleep(3)
          c()
          printt("So why am I back at the island?",.07)
          achieve('Escape?')
          achieve('The Plane')
          time.sleep(2)
        alive=False
        PLANED=True
      else:
        c()
    else:
      printt("The plane seems repaired, but out of power...",1)
      anykey()
  timeSTUP=False

def square(f): #find square, find player maker, give top left 
  global mazeq
  overide()
  mazeq[f]='┌'
  mazeq[f+1]='┐'
  mazeq[f+52]='└'
  mazeq[f+53]='┘'
def raftit():
  global inventory,timeSTUP,raftper,alive,achievements
  if box1 not in posup and box4 not in posdown and box3 not in posleft and box2 not in posright and 'Boat' in inventory:
    printt(["You place your boat on the water, ready to sail off.","Do you want to proceed  [\033[38;5;194mThis will end your game\033[0m]\n(y for yes, n for no)"],[1,.02])
    uhgn=getkey1()
    if uhgn=='y':
      printt("You put down your boat, and start to row.",0.06,4)
      funnyfunction()
      printt(["You row and row.","It seems like the ocean never stops.","Soon you see land.","It must be civilization."],[3,2,3,5])
      c()
      printt('So why am I back at the island?',0.07,1)
      achieve('Escape?')
      achieve('Raft')
      time.sleep(2)
      alive=False
      raftper=True
  timeSTUP=False
def overide(plo=False):
  global mazeq,maze8
  if plo==False:
    if '┌' in mazeq:
      for i in ['┌','┐','└','┘']:
        mazeq[mazeq.index(i)]=over
  elif type(plo)==str:
    try:
      mazeq[mazeq.index(plo)]='-'
    except:
      pass
  else:
    for i in ['┌','┐','└','┘']:
      maze8[maze8.index(i)]='-'
def slashem():
  global labm1
  while ':' in labm1:
    labm1[labm1.index(':')]='-'
def movedir(direc):
  square(box1+direc)
def signread(yp1):
  print('\n\nThe sign reads:\n'+bold+{'╽':"The Lab.",'┑':"Cave Entrance.",'┓':"The Powerplant",'┒':"Beach Gear.",'╿':"Grand Lake. (Divers must have proper diving gear!)",'╏':"The Maze. A true sight to see."}[yp1[True]])
  anykey() #easter, '╏'

tiit=True

def intern2():
  c()
  printt("The interface shows one screen, it appears to be the entire island.",2)
  printmaze(yum,True)
  time.sleep(2)
  anykey()
omgportal=0
def portal():
  global omgportal,alive,mined,achievements
  printt('It just looks like a purple wall...')
  time.sleep(1)
  if minimapa:
    printt(["Theres a slot for the minimap.","Do you want to place it?"],[1,.02])
    print('[\033[38;5;194mThis will end your game\033[0m]\n(y for yes n for no)')
    h=getkey1()
    if h=='y':
      funnyfunction()
      printt(["The map leaves your hand, and slides into place.","The wall whirls to life, and before you know it, a door forms. You have a way out.","No more escaping by the sea, no more escaping by the air.","Without any clue with what this door is, you step in and smell fresh air."],[2,2,3])
      time.sleep(3)
      c(1)
      printt([bold+"...","This isn't it.","This is not a way out.","There are things even I can't forsee.","I'm sorry.","\nYou are back on the island."],[1,2,1,1,1,.06])
      alive=False
      mined=True
      achieve('Escape?')
      achieve('The Lab')
  else:
    omgportal+=1
    if omgportal<3:
      printt("A small sign on the wall says 'Voy a la cueva.'")
      time.sleep(2)
      printt("[I thought this game was in english?]")
      anykey()
lll=False
TRUEYAYA=False
mined=False
def miniiq(tam=True):
  global timeSTUP,mazeq
  timeSTUP=True
  c()
  time.sleep(.5)
  while True:
    if tam:
      achieve('New game pog')
    printt("Would you like to play the minigame? \n(You will return here after playing, y for yes, r for the rules of the game)!\n\nMost Recent Score: "+str(miniscore)+"\nHighscore: "+str(hminiscore))
    if not acheck('Poggers'):
      print("(If you get 3k points you get pro achievement)")
    g=all([equipped(i) for i in modli])
    if g:
      time.sleep(1)
      printt(bold+"(The power of the modules unlocks extreme mode... (e to enable)")
    pl=getkey1()
    if pl=='y':
      t1=THREAD(target=mini)
      mazeq=Lesgo
      t1.start()
      break
    elif pl=='e':
      if g:
        c()
        printt("In extreme mode, the color shown is the only save place..\n[Any key to continue]")
        getkey1()
        if g:
          t1=THREAD(target=mini,args=('T'))
          mazeq=Lesgo
          t1.start()
          time.sleep(1)
          break
    elif pl=='r':
      printt("To play the game, you must stay alive as long as possible!")
      time.sleep(1)
      printt('A color will appear at the top, and you have to go to another corner that isnt that color!')
      time.sleep(1)
      printt("You have mere seconds to get out of that corner before it becomes a wall, and if you're caught in it its Game Over!")
      time.sleep(2)
      printt("As the game progresses, you get 100 points a turn and it gets more and more dificult!")
      time.sleep(3)
      printt("[Any key to go back to the menu]")
      getkey1()
      c()
    else:
      c()
      break
  timeSTUP=False
  c()
def shrine(uhr=True):
  global tinyvars
  tinyvars['shrine1' if mazeq==newthing1 else 'shrine2' if mazeq==newthing2 else 'shrine3' if mazeq==newthing3 and uhr else 'present1']+=1
  if mazeq==newthing1:
    printt(['\nA big statue.',"It looks even older than the walls around it.","\nA plate on the front says:",'\033[38;5;246mA shrine to the actual creator of this place.\nWithout this man, theres no way this place would have ever existed.\n\033[38;5;251mBut I\'m sure he already knew that.'+R] if tinyvars['shrine1']==1 else ["\nUpon further investigation, a note on the back says:\n\033[38;5;246m   1/3   [wearebydesign.com]"+R,'\nTalk about free advertising...'],[2,2,1,3] if tinyvars['shrine1']==1 else [2,2])
  elif mazeq==newthing2:
    printt(["Another big statue, but this time with a bigger nose.",'This time, there is a plate on the inside of the nose.',"\nIt says:","\033[38;5;246mA shrine to a true barbarian.\nIf you know, you know.\nAlso likes to say 'My business is my own'"+R,"\n(Hopefully you dont get that reference)"] if tinyvars['shrine2']==1 else "\nNo note on the back, but text carved into the statue says:\n\033[38;5;246mnuBBbBbBBBBBYyyy"+R,[2,2,1,3,1] if tinyvars['shrine2']==1 else 3)
  elif mazeq==newthing3:
    printt((["A statue of a blocky guy stands menacingly.","The colors of green, yellow, and blue can barely be seen.",'\nIn very blocky text it says:\n\033[38;5;246mDedicated to a true noob.\nAlso obsessed with boys?'+R] if tinyvars['shrine3']==1 else "kinda sus") if uhr else "A huge present. Looks like its lost all its lust..." if tinyvars['present1']==1 else "On the side of the present is:\nA squid, plane, jojo noob, star wars clone, monke, and other chaotic things...",([2,2,3] if tinyvars['shrine3']==1 else 3) if uhr else 2)
  anykey()
def colorsp():
  return random.choice(['\033[38;5;11m','\033[38;5;13m'])
def spAM():
  global tinyvars,mazeq,HEAHE
  tinyvars['umev']+=1
  if tinyvars['umev']==1:
    printt(['Its just a big head...',"Looks like its made of stone.",'Seems like its about to spit lure.'],[1,2,1])
  elif tinyvars['umev']==2:
    printt(colorsp()+'...'+R,.08,2)
    c()
    printt(colorsp()+"[Hello? Are you there?]",2)
    printt(colorsp()+"[Im not.]",2)
    printt(colorsp()+'[Free yourself. '+colorsp()+'Please.]',1)
    jtemp={}
    for numbers,i in enumerate(HEAHE):
      if i not in ['╸','7','R','p','y','’','-',']','[']:
        jtemp[numbers]=i
    HEAHE=HEAHE2.copy()
    for i in jtemp.keys():
      HEAHE[i]=jtemp[i]
    mazeq=HEAHE
pumpnumber=0
def pumpy():
  global pumpnumber,newthing3
  pumpnumber+=1
  if pumpnumber==1:
    printt('A very rotten pumpkin. For a second you almost remember something.')
  elif pumpnumber==2:
    printt("The memory is coming back.. Maybe?")
  elif pumpnumber==3:
    printt('But it wasnt anything relevant.')
    for i in [777,778,829,830]:
      newthing3[i]='-'
    slepy(2)
  else:
    printt(colorsp()+'...')
    time.sleep(1)
  slepy(2)
  c()
def anykey(ffg=True):
  print(R+'\n[Any key to continue]')
  getkey1()
  if ffg:
    c()
monkehappy=False
monkehappy2=False
def monke():
  global monkehappy2
  if not monkehappy2:
    c()
    printt2('oOOOEOEOEOOEOEAAAAL LOheEEEEEEEEhOOO','[bro its a hu man]',20,.03)
    time.sleep(3)
    c()
    printt2('xOOOOOOOEEDDdEEEEEEE HUuuuuoooooOAA','[what ye doin boi]',20,.03)
    time.sleep(3)
    c()
    printt2('oOoOaAAAAAAAAaaAUUUUU MMMMOOAAAAlmaOOOOOOOOOOO','[you dont even pop bloonj]',20,.03)
    time.sleep(4)
    c()
    printt2('RAOOOOoaaoAOAOoTTTTeEEEEE iGGMEEEEEE','[dont talk to me nob]',20,.03)
    time.sleep(4)
    c()
    if not acheck('luci'):
      achieve('luci')
      anykey()
    monkehappy2=True
craftablelol=succe
craftdict={
  'Boat':[False,{'Plank':1,'Paddle':2}],
  'Multi Wiring':[False,{'Wiring':3}],
  'Super Wiring':[False,{'Multi Wiring':2}],
  'Unspoken Relic':[succe,{'Module A':1,'Module B':1,'Module C':1,'Module D':1,'Module E':1}]
}
def gretly():
  global theroom,maze2,maze7,thelimiter,timero,TheOne1,Mining,theLake2,inventory
  for iq in ['>','<','x','(']:
    while iq in theroom:
      theroom[theroom.index(iq)]='-'
  theLake2[theLake2.index('╥')]='-'
  if 'The Key' in inventory:
    inventory=['The Key']
  else:
    inventory=[]
  timero=400
  while '┄' in True4:
    True4[True4.index('┄')]='-'
  for i_1 in [maze2,maze7]:
    for i_2 in i_1:
      if i_2 not in ['X','-','!','\n']:
        i_1[i_1.index(i_2)]='-'
  thelimiter=0
  TheOne1[294]='-'
  TheOne1[295]='-'
  for (i,i2) in zip([805,806,857,858],['┢','┪','┹','┺']):
    maze7[i+1]=i2 #he pulls the strings and makes them ring
    Mining[i]='-'
  for i,i2 in zip([182,183,234,235],['┌','┐','└','┘']):
    maze2[i]=i2
  for i in neverrel:
    for i2 in range(i,i+3):
      maze2[i2]='X'
      maze7[i2]='X'
def crafting():
  global inventory,craftdict
  c()
  print(bold+"Available recipes\n"+R)
  alistpo=[]
  for i in craftdict.keys():
    if craftdict[i][0]:
      print(str(len(alistpo)+1)+') '+bold+i+R)
      alistpo.append(i)
      for i2 in craftdict[i][1].keys():
        print('\t'+i2+' - '+str(craftdict[i][1][i2]))
      print()
  if not craftablelol:
    print("None")
  else:
    print('Press the number of the recipe you want to make (anything else will exit)')
  ru=getkey1()
  iodict={}
  if ru.isdigit():
    wegoody=False
    if int(ru)<=len(alistpo) and ru!='0':
      ru=int(ru)-1
      wegoody=True
      i=craftdict[alistpo[ru]][1]
      for i2 in i.keys():
        if inventory.count(i2)>=i[i2]:
          iodict[i2]=i[i2]
        else:
          wegoody=False
    if int(ru)>len(alistpo) or ru=='0':
      print("Invalid number...",1)
    elif not wegoody:
      printt(bold+"\nYou dont have the required materials for this..."+R,.01,2)
    elif alistpo[ru]=='Unspoken Relic' and any([mazeq not in [TheOne1,TheOne2,TheOne3,TheOne4,TheOne5,TheOne6,KeyRoom],not gGg]):
      c()
      print('...',2)
      printt("A truely unspoken item cannot be cheated.")
      if not gGg:
        printt("Try when achievements are on.... "+bold+"why are they off??"+R)
    else:
      achieve('minecraft')
      print("\nCrafted "+bold+alistpo[ru]+R+'!')
      if alistpo[ru]=='Boat':
        print("Now I can just sail off!")
      elif alistpo[ru]=='Unspoken Relic':
        c()
        printt(bold+"You may now return to the simulation.",.05,1)
        printt(bold+"Your capsule has been unlocked.",.05,2)
        achieve('end',9 if 'The Key' in inventory else 8)
        gretly()
      if alistpo[ru]!='Unspoken Relic':
        for i in iodict.keys():
          for i2 in range(iodict[i]):
            inventory.remove(i)
      if alistpo[ru] in unlockdict.keys():
        for i in unlockdict[alistpo[ru]]:
          if not craftdict[i][0]:
            print('(Unlocked '+i+' recipe!)')
            craftdict[i][0]=True
      inventory.append(alistpo[ru])
    anykey()
  c()
thevoltdict={
  1:[theroom,[317,359,577,837]],
  2:[Shed,[317,421,473,577,861]],
  3:[Portal,[837,839,841,843,845,847,849,851]],
  4:[labm1,[278,537,892,903]],
  5:[labm2,[427,430,439,445]],
  6:[cavem1,[453,471,474]],
  7:[maze10,[843,855]],
  8:[maze8,[860]],
  9:[maze5,[243,503,509,663]],
  10:[maze4,[187,343,390]],
  11:[maze3,[232,865]],
  12:[maze2,[143]],
  13:[maze1,[137,786]],
}
standed=False
def untrollin():
  global TheOne1,TheOne2,TheOne3,TheOne4,TheOne5,TheOne6,KeyRoom,mazeq,True1,True2,True3,True4,maze7,nodarks
  nodarks.extend(i for i in ["maze2","maze7"])
  for i in [806,807,858,859]:
    maze7[i]='-'
  for i in range(161,265):
    for i2 in [TheOne1,TheOne2,TheOne3,TheOne4]:
      if i2[i] not in ['[',']','-',')','\n','╊']:
        i2[i]='◌'
  for (i,i2) in zip([TheOne1,TheOne2,TheOne5,TheOne6,KeyRoom,TheOne4,True1,True3,True4,TheOne3],[{'⊡': 163,'⋄': 164,'⎔': 215,'⎚': 216,'▀': 393,'▁': 394,'▂': 445,'▃': 446},{'█': 368,'▉': 369,'▊': 420,'▋': 421,'⊞': 849,'⊟': 850,'⊠': 901,'░': 902},{'▄': 753,'▅': 754,'▆': 805,'▇': 806},{'⊡': 766,'⋄': 767,'⎔': 818,'⎚': 819},{'▀': 683,'▁': 684,'▂': 735,'▃': 736},{'⊞': 450,'⊟': 451,'⊠': 502,'░': 503},{'█': 357,'▉': 358,'▊': 409,'▋': 410},{'▄': 474,'▅': 475,'▆': 526,'▇': 527},{'▀': 69,'▁': 70,'▂': 121,'▃': 122,'⊡': 85,'⋄': 86,'⎔': 137,'⎚': 138,'⊞': 188,'⊟': 189,'⊠': 240,'░': 241,'⊡w': 174,'⋄w': 175,'⎔w': 226,'⎚w': 227,'█': 684,'▉': 685,'▊': 736,'▋': 737,'▄': 456,'▅': 457,'▆': 508,'▇': 509},{'⊡': 389,'⋄': 390,'⎔': 441,'⎚': 442,'▀': 587,'▁': 588,'▂': 639,'▃': 640}]): #FIND DIALOGUE CHARACTERS THING, find dialogue, add spaces here
    for i3 in i2.keys():
      i[i2[i3]]=i3[0]
def wasit():
  global mazeq,standed
  if 'Unspoken Relic' in inventory and mazeq==maze7:
    standed=True
    c()
    printt(bold+"..."+R,1) 
    printt("Unspoken, sure. But it exists.",2)
    printt(["It might all be a lie, but its a real lie.","But that does not make it a truth.","This whole place, enclosed in the walls of a small laboratory.","A real life science experiment.",bold+"A fake part of reality, a false part of truth."],[2,2,2,2,2])
    printt("Yet somehow,\033[38;5;160m we stumbled upon it."+R)
    time.sleep(2)
    printt(["\nI myself, now part of this falsehood.","A victim of a flaw, a threat to myself.","I try to help them all, I really do. I can't. \033[38;5;195mIt"+R+" has me,\033[38;5;195m he"+R+" had me.","If I could tell you what it was, I would.","A normal leaf, then all of a sudden, I couldn't move.","Condemned to watch myself destroy, to watch \033[38;5;195mIt"+R+'.',"\nBut you... the first and last player. You ended it.","Not erased, nor victim to \033[38;5;195mhim"+R+', alive.',"To say you broke the cycle would be an understatement.","You ended \033[38;5;195mthem"+R+", as nothing truely fake can exist in reality.","A world in a world, gone for good.","At least hopefully...."],[2,2,2,2,2,3,1,2,2,2,1,2])
    time.sleep(2)
    anykey()
    printt(["Re-entering.... what a feat.","To be real, made fake, turned real, then to return real in a fake world...","It breaks the rules of fantasy.","This fantasy can no longer exist. We are the only parts keeping this place together.","Everyone is freed.... even my old friend Jovs. (And that weird monkey...)","You can even view the island at any time with the press of the button 'H', and shorten time with '.'","Your path is clear, its time for me to figure out mine...."],[2,2,2,2,2,2,2])
    printt("Have fun.")
    time.sleep(3)
    anykey()
    achieve('end',7 if "The Key" in inventory else 6)
    untrollin()
def thevolts():
  global theroom,Shed,Portal,labm1,labm2,cavem1,maze10,maze8,maze5,maze4,maze3,maze2,maze1
  for i in thevoltdict.keys():
    mazetodo=thevoltdict[i][0]
    for i2 in thevoltdict[i][1]:
      if mazetodo[i2] in ['-',']','[',' ']:
        mazetodo[i2]=random.choice(['❖','❖','-']) #the volt thing
voltgood=True
def voltthread():
  global theroom,Shed,Portal,labm1,labm2,cavem1,maze10,maze8,maze5,maze4,maze3,maze2,maze1,voltgood
  voltgood=False
  time.sleep(120)
  voltgood=True
  for i in [theroom,Shed,Portal,labm1,labm2,cavem1,maze10,maze8,maze5,maze4,maze3,maze2,maze1]:
    numj=-1
    for i2 in i:
      numj+=1
      if i2=='❖':
        i[numj]='-'
def elsuper(): #elsupermercado
  global inventory,themine
  if not smallvarget("activateds"):
    printt(["A slot for a huge Wiring.",bold+"\nThe sign reads:"+R,'\tThe Gate\n\tNeeded Volts: 10,000V\n\t'+bold+'Warning: USE AS DIRECTED (voltage may get loose)\n'+R],[2,1])
    if 'Super Wiring' in inventory:
      printt("Would you like to put your "+bold+'Super Wiring'+R+' in this panel? (y for yes)')
      p=getkey1()
      if p=='y':
        c()
        inventory.remove('Super Wiring')
        printt(bold+'\nThe Super Wiring fits into place....',3)
        c()
        printt(["All of a sudden, voltage appears everywhere...\n"+R,'The voltage is slowly fading!\nGather 10 volts and bring them back to the panel!\nAll voltage will fade away in 2 minutes!\nVoltage can appear anywhere on the island, mainly where electricity is present.'],[2,5])
        printt("\n[Press any key to release the voltage!]")
        getkey1()
        c()
        thevolts()
        smallvarchange("activateds")
        THREAD(target=voltthread).start()
    elif 'Multi Wiring' in inventory:
      printt("Multi Wiring doesnt have that many volts...")
    elif 'Wiring' in inventory:
      printt('Wiring wont even get close to powering this...')
    if not smallvarget("activateds"):
      slepy(3)
      anykey()
  else:
    if volts>=10 and '*' in themine:
      printt(bold+"\nVoltage Collected: 100%"+R,.1,2)
      printt("You hear the distant creaking of metal...",3)
      while '*' in themine:
        themine[themine.index('*')]='-'
      anykey()
def thecart():
  global literallyvented,alive
  printt("A long mineshaft is ahead of you.",2)
  printt('Do you want to enter? [\033[38;5;194mThis will end your game\033[0m]\n(y for yes n for no)')
  thinep=getkey1()
  if thinep=='y':
    clearline(2)
    funnyfunction()
    printt(['You enter the mineshaft.',"Within no time you find a lonely empty cart, that seems to be the perfect size for a human.","With nothing else to do, you hop in and let the rails take you."],[2,2,4])
    c()
    printt(["The rails go on and on. The rocky walls seem like they never change.","Suddenly there is light. The rails stop.","You exit the shaft. It feels like a completely new place."],[3,3,4])
    c()
    printt("So why am I back at the island?")
    achieve('Escape?')
    achieve('The Cart')
    time.sleep(4)
    literallyvented=True
    alive=False
  else:
    c()
def tictactoe(): #need to do tictactoe, as a big boi ima do it from scratch lol, return True if win, False if loss
  bslots=['-','-','-','-','-','-','-','-','-']
  c()
  thekeis={
    'a':'   ','A':'   ','b':'   ','B':'   ','c':'   ','C':'   ','d':'   ','D':'   ','e':'   ','E':'   ','f':'   ','F':'   ','g':'   ','G':'   ','h':'   ','H':'   ','i':'   ','I':'   ',0:['a','A'],1:['b','B'],2:['c','C'],3:['d','D'],4:['e','E'],5:['f','F'],6:['g','G'],7:['h','H'],8:['i','I'],
  } #list for each slot, use for loops to like idk
  zeboard="""
\t┌⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┐
\t│  a  │  b  │  c  │
\t│  A  │  B  │  C  │
\t├⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┤
\t│  d  │  e  │  f  │
\t│  D  │  E  │  F  │
\t├⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┤
\t│  g  │  h  │  i  │
\t│  G  │  H  │  I  │
\t└⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┘
"""
  def checkwin(wd='O'):
    for i in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
      lk9=False
      for i2 in i:
        lk9=bslots[i2]==wd
        if lk9==False:
          break
      if lk9==True:
        return True
    return False
  gaming=True # B-)   (cool glasses obv)
  turn = 'O'
  def printboardy():
    c()
    for i in zeboard:
      if i in thekeis.keys():
        print(thekeis[i],end='')
      else:
        print(i,end='')
  printboardy()
  while gaming: #you are 0
    if turn=='O':
      print("Press the number where you want to place your piece!\nYou cannot place a piece on top of another piece.")
      print("Top left = 1, Bottom right = 9 (Left to right)")
      grea=getkey1()
      if grea in ['1','2','3','4','5','6','7','8','9']:
        grea=int(grea)-1
        if bslots[grea]=='-':
          bslots[grea]='O'
          for i in enumerate(thekeis[grea]): #returns a tuple with (pos,thing)
            if i[0]==0:
              thekeis[i[1]]='╭⎯╮'
            else:
              thekeis[i[1]]='╰⎯╯'
          print("\nPlaced 'O' in slot",grea+1)
          turn='X'
        else:
          print("Spot already taken...")
        anykey()
    else:
      slepy(1)
      printt("The kid is "+random.choice(['lazily','clumsily','weirdly','angrily'])+" placing his piece...")
      g=random.randrange(0,8)
      while bslots[g]!='-':
        g=random.randrange(0,8)
      bslots[g]='X'
      for i in enumerate(thekeis[g]):
        if i[0]==0:
          thekeis[i[1]]='\\_/'
        else:
          thekeis[i[1]]='/ \\'
      slepy(2)
      printt('He places his \'X\' in slot '+str(g+1)+'.',1)
      anykey()
      turn='O'
    printboardy()
    if checkwin('O'):
      return True
    elif checkwin('X'):
      return False
    elif '-' not in bslots:
      return 'Tie'
kiddoing=False
haskide=False
amokid=0
def itsakid():
  global kiddoing,amokid,haskide
  if 'Unspoken Relic' in inventory:
    if not kiddoing:
      if not haskide:
        printt(["A kid playing in the dirt.","He is staring at a board. Two shapes can be seen, both in the shape of letters.","He holds up the 'O' shapes to you. It seems as if he wants to play this game.","He seems just as clueless as you. But suddenly you remember..."],[2,2,1,2])
        haskide=True
      printt("\nWould you like to play "+bold+"tic-tac-toe? (y for yes)"+R)
      dokid=getkey1()
      c()
      if dokid=='y':
        ticing=tictactoe()
      else:
        return
      c()
      if ticing==True:
        if amokid==0:
          printt(["It seems as if the kid isnt too good at this game...",'You feel as if you have experience in "tic-tac-toe."'],[2,2])
        elif amokid==1:
          printt(["Another win...","The kid doesnt seem nearly as happy as before."],[2,2])
        elif amokid==2:
          printt(["The kid is definitely mad.","You think of telling him to get good, but decide against it."],[2,2])
        elif amokid==3:
          printt("Something about all these endless wins is getting boring...")
        else:
          printt('As if the kid couldn\'t get any madder...')
        printt("He stands next to his board, expecting a rematch.")
      elif ticing=='Tie':
        printt('A tie... how boring.',2)
        printt("The kid stands next to his board, expecting a rematch.")
      else:
        if amokid==0:
          printt(["The kid seems to have enjoyed that match.","For some reason, you feel the same enjoyment."],[2,1])
        elif amokid==1:
          printt(['The kid seems confident with himself now.',"Hopefully your loss was intentional.."],[2,1])
        elif amokid==2:
          printt(["The kid almost runs away from excitement.",'Glad to make his day...'],[2,1])
        elif amokid==3:
          printt(["The kid makes a winning smile.","It's almost creepy how big it is.."],[2,1])
        else:
          printt(["The kid is finally happy...","Good job?"],[2,1])
        achieve("loser")
        kiddoing=False
      anykey()
      amokid+=1
  else:
    printt("Its a kid. He knows what you've done.\n\033[38;5;12mHow the hell are you here without the unspoken relic?"+R)
    anykey()
def theeasterdoor():#easter
  global mazeq
  c()
  printt(["A door stands before you.","\nWritten on the door is -"],[1,1])
  theealist=[]
  while True:
    print(doorcode)
    print(bold+'\n\nEnter code: ')
    for i in theealist:
      print(i,end=' ')
    print('_ '*(len(doornumber)-len(theealist)))
    if len(theealist)!=len(doornumber):
      print(R+'\n(X/Enter to exit)')
      eae=getkey1()
      if eae.isdigit():
        theealist.append(eae)
      elif eae==BACKSPACE:
        if len(theealist)>0:
          theealist.remove(theealist[-1])
      elif eae in ['x','\n','',' ']:
        break
    else:
      letsseeifyougotit=''
      for i in theealist:
        letsseeifyougotit+=i
      if letsseeifyougotit==doornumber:
        c()
        printt("The door suddenly vanishes... wow.",.06,2)
        while 'n' in mazeq:
          mazeq[mazeq.index('n')]='-'
        anykey()
        break
      else:
        if name=='Muffinlavania':
          print(f'your the creator so like {shapes}')
        printt("The code suddenly resets... seems like it's wrong.",2)
        theealist=[]
        anykey()
    c()
eastering=False
theairfr=False
def eastertemple():#easter
  global alive,eastering,theairfr,active
  printt(["This huge temple seems to have been expecting you.","A bright light seems to be coming from the very top of the long flight of stairs.",'Do you want to climb the stairs? [\033[38;5;194mThis will end your game\033[0m]\n(y for yes)'],[2,2,1])
  chamoy=getkey1()
  if chamoy=='y':
    funnyfunction()
    slepy(1)
    printt(["You climb the stairs.","The light seems to grow dimmer as you rise.","\nYou finally reach the top."],[2,5,2])
    if not all([itemdict['Module A']=='Yes',itemdict['Module B']=='Yes',itemdict['Module C']=='Yes',itemdict['Module E']=='Yes']) and not itemdict['Module D']=='Yes':
      printt(["Theres nothing up here.","\nOn the ceiling are the words:"],[2,1])
      printt(bold+'PLAYERS LIKE YOU CANNOT SEE PAST THIS.\nGET ALL 4 MODULES THEN MAYBE WE CAN TALK.'+R,.07)
      time.sleep(3)
      c()
      printt(['Upon looking down, you see grass.',"An almost familiar looking cave stands in front of you, with a lake to the right.",bold+'You are back.'],[2,2])
      achieve('The Temple')
      slepy(1)
      alive=False
      eastering=True
    else:
      printt(["There is... an air fryer?","There is nothing else, no words on the wall, no more blinding light.","Upon further examination, a small scribble on it says \""+bold+"GOD"+R+'\"','Suddenly the air fryer starts to disappear.'],[2,2,2,5])
      c()
      printt(['Upon looking down, you see grass.',"An almost familiar looking cave stands in front of you, with a lake to the right.","A voice in your head tells you:"],[2,3,1])
      printt(bold+"Clearly you dont own an air fryer."+R)
      achieve("The Fryer")
      slepy(2)
      alive=False
      theairfr=True
  else:
    c()
def emazeguy():#easter
  pass
def guy15(): #easter
  global didbite15,didbite8
  if '◉' not in mazeq:
    if not didbite15:
      printt(["yo sup","you be lookin mad lost bro","got any clue what your doing here?"],[2,3,2])
      print('1) i wanna get out of the maze\n2) no pls help\n3) yea now shut up\n4) idk lol')
      ets=''
      while ets not in ['1','2','3','4']:
        ets=getkey1()
      c()
      if ets=='1':
        printt(["dont we all...","i mean hey you could just go out the way you started like bruh","but i think you wanna actually find something huh","well i kinda gave up lol but theres a door to the north i think"],[2,2,3,2])
      elif ets=='2':
        printt(["well i dont know that much tbh","im pretty sure theres other stuff in this maze thing, but theres a door to the north"],[2,2])
      elif ets=='3':
        printt(["bruh wth","fine theres a door to the north tho and uh"],[2,1])
      elif ets=='4':
        printt(["...ok","i mean theres some door thing to the north"],[2,2])
      printt(["\ntheres some shapes on the door and im pretty sure the square is like "+str(shapes['▢'])+' and the triangle thing is '+str(shapes['△']),"and like the code has "+str(len(doornumber))+' digits yeyye\n',"i forgor how i know that tho lol","im pretty sure theres more shapes but like that guy to the east knows that idk the other ones"],[2,3,2,4])
      anykey()
      didbite15=True
    else:
      printt(["bro square is "+str(shapes['▢'])+' and triangle is'+str(shapes['△']),'go to the other guy like bruhhh'],[2,2])
      c()
  else:
    if not didbite8:
      didbite8=True
      printt(["gGAAAAAAAAAAAhhHHHHHHHHI,HI,HI","top of the afternoon to you, and happy morning","ok one sec"],[2,2,7])
      clearline(3)
      printt(["thanks man for that i really really GAAAAAAAAA","\nanyways, back to the point here the circle is "+str(shapes['◯'])+' and the pentagon is '+str(shapes['⭔'])+'\n'],[2,3])
      printt("WAIT WAS THAT THE POINT OR WAIT WHAT I FORGOT WHAT THE HELL STOP THE ATTACKING BRO THAT ISNT FAIR YOU CANT NOT KILL ME WAIT WHAT OK")
      slepy(.5)
      c()
    else:
      printt(["y'know....... i-",'i-i-ii-i-i-i--ii-i-i--i-ii-i-i-i-','i said the circle is '+str(shapes['◯'])+' and pentagon is '+str(shapes['⭔']),'plsplspsl leave me alone now'],[1,2,2,2])
      c()
emazehappy=False
try:
  if achievements['easter_cooldown'][1]+86400-round(time.time())>0:
    emazehappy=True
except:
  pass
easterover='-' #make it change depending on what it overrides
easter_bunny={
  1:[879,[381,480,633,785]],
  2:[801,[866,849,686,479,120]],
  3:[616,[690,632,679]],
  4:[0,[716,768,821,874]]
}
easterb_dict={
  7:maze6,
  6:maze1,
  1:themine
}
bunnycutscene=0
def easterbunnycut():#easter, the bunny
  global bunnycutscene,easterover,mazeq,maze5,maze1,themine
  bunnycutscene+=1
  if bunnycutscene==1:
    printt(["A random bunny, white as the clouds.","The bunny starts to move..."],[2,3])
  for i in easter_bunny[bunnycutscene][1]:
    if 'U' in mazeq:
      mazeq[mazeq.index('U')]=easterover
    easterover=mazeq[i]
    if mazeq[i] in ['-',' ']:
      mazeq[i]='U'
    c()
    printmaze(mazeq)
    time.sleep(1)
  mazeq[mazeq.index('U')]=easterover
  c()
  printmaze(mazeq)
  time.sleep(1)
  if easter_bunny[bunnycutscene][0]!=0:
    sometheas=easterb_dict[current]
    sometheas[easter_bunny[bunnycutscene][0]]='U'
  if bunnycutscene==2:
    printt("That bunny sure has a mind of its own...")
  elif bunnycutscene==3:
    printt("bro what da bunny doin")
  elif bunnycutscene==4:
    printt("cmon man the bunny went into the water wth bro what in there")
  anykey()
  c()
eastereggs=0
def mellamovictor():#easter, 86400 secs in a day
  global emazehappy
  if not emazehappy and achievements['easter_cooldown'][1]+86400-round(time.time())<0:
    if eastereggs!=20:
      if not smallvarget("isguapo"):
        printt(["hola","que tal"],[2,1])
        print("1) good\n2) what")
        i_d_c=getkey1()
        if i_d_c=='1':
          printt("oh thats cool",2)
        elif i_d_c=='2':
          printt(["i said your mother","anyway"],[1,2])
        else:
          printt("ok",2)
        c()
        printt(["well i kinda like eggs","i think theres a bunch around the maze up top","i know they are colored but they taste fine either way","more calories",'so if you get all of them theres like 20 of them',"should make for at least a good hearty dinner\n"+bold],[2,3,1,2,2,2])
        if prizefortoday=='The Emblem':
          printt("i can give you a little badge thingie just get me the eggs")
        elif prizefortoday=='The Egg':
          printt("i got this other egg that i cant eat so ill trade you for the other ones just get em")
        elif prizefortoday=='The Rainbow':
          printt("i found a jar of like these colors idk its cool you gotta go get the eggs first")
        elif prizefortoday=='The Picture':
          printt("i got a small photo that looks cool you can have it for them eggs")
        else:
          printt("you can have this stripe thing for your name if you get the eggies i promise its cool")
        slepy(2)
        anykey()
        smallvarchange("isguapo")
      else:
        printt('bro go get me them eggs\n'+bold,2)
        if prizefortoday=='The Emblem':
          printt("you will get a totally radddd badge trust trust")
        elif prizefortoday=='The Egg':
          printt("you will get even cooler egg i promise gogo")
        elif prizefortoday=='The Rainbow':
          printt('then you will get the whole rainbow man (real)')
        elif prizefortoday=='The Picture':
          printt("think of how cool this photo would be if you had it just for 20 eggs")
        else:
          printt("your name would look so epic with a cool banner behind it just saying")
        slepy(2)
        anykey()
        c()
    else:
      c()
      printt(['YOO NO WAY LETS GOOOOOO','bro those eggs look amazing'],[2,2])
      printt("well here ya go")
      if prizefortoday in achievements.keys():
        printt("oh you already have this lol")
      achieve(prizefortoday)
      slepy(2)
      printt(["well ima sit perfectly still for a day or so eating my eggs bye","oh yea my names jesús btw","but not jesus its actually jesús lol"],[2,1,2])
      anykey()
      t=achievements['easter_cooldown'][0]+1
      if t==5:
        t=0
      achieve('easter_cooldown',[t,round(time.time())])
      emazehappy=True
  else:
    if round(time.time())+86400-achievements['easter_cooldown'][1]>5:
      printt(['He\'s literally standing there perfectly still...',"A sign next to him seems to change everytime you look away from it.","\nIt says: \n"+bold+'\tafk till i get robux\n\ttime left: '+str(achievements['easter_cooldown'][1]+86400-round(time.time()))+' secs'+R],[2,2,2])
      printt('\n(What a hideous sign to look at...)')
      anykey()
    else:
      printt(["Wait what.... you actually are ingame when your time reset??? didnt expect that lol\nFor that you get the rarest (probably) text in this game: \033[48;5;102me."+R,"well you have to reload the game to wake up this man..."],[2,3])
      anykey()
OMGRANDOM=True
thechanger=False #uh pls work
def easter_diet(hopethiswork):#easter
  global eastereggs,mazeq
  if hopethiswork!=None:
    eastereggs+=1
    printt(random.choice(['Another easter egg...','Seems part of a balanced diet...','Another easter egg...']),1)
    printt("("+str(eastereggs)+' eggs collected!)')
    mazeq[hopethiswork]='-'
    anykey()
hasgrut,minervar=False,False
somethinglo=Mining
thelist0i=[39,91,92,93,145,154,155,197,198,206,250,251,257,258,303,304,309,356,357,360,361,409,410,412,462,464,515,566,567,619,620,671,722,723,775,776]
smallysky=False
def move(dir):#find move find moving (keywords)
  global timeSTUP,current,nextone,mazeq,istrue,bossnumbu,mazechang,isright,isleft,numbero,lll,Truth,TRUEYAYA,alive,maze1,cavem1,theLake,cavem2,mined,achievements,notedict,Mining2,inventory,OMGRANDOM,STOP,thechanger,monkehappy,over,thelimiter,hasgrut,smallysky,somethinglo,minervar,getoitem,tinyvars
  #easter (youdid_nt) didthenote easter
  try:
    #fixing horrible code: all non dir specific things here (,False in ischars prevents errors, needed for down cases) find all dirs, find start move, go all dirs
    itempick(dir) #removed prevention for hacking since yea idk (Mod B looking easy to hack..)
    npctalker(dir)
    if ischar(dir,'7',False) and mazeq==HEAHE:
      spAM()
    elif ischar(dir,['ಠ','◉'],False):
      guy15() #easter
    elif ischar(dir,'U',False) and dir!="down":#easter
      easterbunnycut()
    elif ischar(dir,'/',False):
      slashem()
      temmiecolor['/']='\033[48;5;82m'
    elif ischar(dir,['┺','┢'],False):
      wasit()
    elif ischar(dir,'@',False) and mazeq==maze8 and dir!='up':
      if equipped('Diving Gear [Full]'):
        printt('\nDo you want to enter '+bold+"The Lake"+R+"? (y for yes)")
        if getkey1()=='y':
          mazeq=theLake
          c()
          slepy(1)
          printt("While Diving, you find an underwater cave...",2)
        c()
      else:
        printt("You cant go diving without gear on...",2)
        anykey()
    elif ischar(dir,['╽','┑','┓','┒','╿','╏'],False):
      j={}
      for h in ['╽','┑','┓','┒','╿','╏']:
        j[ischar(dir,h)]=h
      signread(j)
    elif ischar(dir,'’',False) and mazeq==TheOne5:
      intern2()
    elif ischar(dir,['◩','◪',False]):
      printt(["An old looking poster. In faded text is a language youve never seen before.","One symbol does remind you of a duck though..."] if ischar(dir,"◩") else ["An incredibly detailed poster.\nIt's a whole city, bustling with life","The caption simply says: "+bold+"by me"+(R*5)+"\nHow useful?"],[1,.02])
      anykey()
    elif ischar(dir,'◊',False):
      minshop()
    elif ischar(dir,'⊗',False): #easter, might keep in tho
      alive=False
      smallvarchange("didnt_listen")
    elif ischar(dir,'h',False):
      chest()
    elif ischar(dir,'k',False):
      planet()
    elif ischar(dir,'X',False):
      raftit()
    #END ALL DIRS
    if dir=='left':
      if ischar('left','ñ'):
        if mazeq==Shed2:
          mazeq=Shed
      if ischar('left',['╮','╯']):
        itsakid()
      if ischar('left','Z'):
        printt("An old lump of chocolate...",2)
        printt("Looks like it belongs on the ground.")
        anykey()
      if ischar('left','F'):
        if 'The Picture' in achievements.keys():
          printt("A not so distant memory. An easter egg and a bunny can be seen in the photo.",1)
          anykey()
      elif ischar('left',']') and mazeq==emaze7: #easter
        eastertemple()
      elif ischar('left','H'): #easter
        easter_diet(easter_diet(box1-1 if mazeq[box1-1]=='H' else box3-1))
      elif ischar('left','◓'):
        pumpy()
      elif ischar('left','*'):
        if mazeq==themine:
          printt("A huge metal door.",2)
          c()
      elif ischar('left','T'):
        if mazeq==newthing1:
          mazeq=Mining3
        elif mazeq==newthing2:
          mazeq=newthing1
      elif ischar('left','╥'):
        monke()
      elif ischar('left','~'):
        if mazeq==Mining:
          mazeq=cavem2
        elif mazeq==Mining2:
          mazeq=Mining
        elif mazeq==Mining3:
          mazeq=Mining2
          overide()
          for e,i in zip([515,516,567,568],['┌','┐','└','┘']):
            Mining2[e]=i
        elif mazeq==HEAHE:
          mazeq=newthing3
        elif '[' in mazeq:
          mazeq=cavem2
        elif '#' in mazeq:
          mazeq=Mining
        c()
      elif ischar('left','K'):
        if mazeq==newthing3:
          shrine(False)
      elif ischar('left','≣'):
        if mazeq==cavem2:
          mazeq=cavem1
        else:
          mazeq=maze1
        c()
      elif ischar('left','╕'):
        dialogue()
      elif ischar('left','!'):
        if '╳' in mazeq:
          bossnumbu+=1
          mazeq=nextonboss[bossnumbu]
          mazechang=True
        elif mazeq==emaze17:
          mazeq=emaze16
          current=-102
        elif mazeq==KeyRoom:
          mazeq=TheOne6
        elif mazeq==Mining3:
          mazeq=Mining2
          while 'T' in Mining2:
            Mining2[Mining2.index('T')]='-'
          overide()
          square(203)
        elif mazeq==theLake:
          mazeq=theLake2
        elif mazeq==maze3:
          elsuper() #el super wiring
        elif mazeq==themine:
          thecart()
        else:
          mazeq=maze5
        c()
      elif box1 not in posleft and box3 not in posleft and not thechanger:
        if getoitem==False:
          if mazeq[box1-1] in goods and mazeq[box3-1] in goods:
            movedir(-1)
      else: #find left change, find left transition
        if mazeq not in [lanc1,lanc2,lanc3,lanc4,lanc55,True4,emaze21,emaze22] and not thechanger: #easter (emaze one)
          if mazeq!=emaze7 or box1>625:
            thechanger=True
            overide()
            c()
            if mazeq not in [cavem2,labm2,theLake]:
              current-=1
              mazeq=nextone[current]
            else:
              mazeq=cavem1 if mazeq==cavem2 else labm1 if mazeq==labm2 else theLake
            movedir(49)
            thechanger=False
        elif mazeq==True4:
          if 'Unspoken Relic' in inventory:
            mazeq=True5
        elif mazeq==lanc55:
          c()
          print("Leave the land of KYS? (You can return by pressing 'k', y for yes)")
          if getkey1()=='y':
            mazeq=somethinglo
          c()
    if dir=='up':
      if ischar('up','╊'):
        if 'Unspoken Relic' in inventory:
          printt("Is it time to return?")
          print("(y for yes, \033[01myou are no longer trapped in either world\033[0m)")
          if getkey1()=='y':
            mazeq=theTruth
            current=-8
          c()
      if ischar('up','U'):#miner
        if mazeq==miney:
          mazeq=Mining3
          current=1
      if mazeq==emaze7 and ischar('up',';'):#easter
        eastertemple()
      if ischar('up','H'): #easter
        easter_diet(box1-52 if mazeq[box1-52]=='H' else box2-52)
      if ischar('up','n'):#easter
        theeasterdoor()
      if ischar('up','Z'):#easter
        if not smallvarget("didthenote"):
          printt(["A random note on the wall.","A faint symbol and number can be seen.",bold+"It reads:"+R+"\n ⎔ - "+str(shapes['⎔'])],[2,2,2])
          anykey()
          smallvarchange("didthenote")
        else:
          printt(bold+"It reads:"+R+"\n ⎔ - "+str(shapes['⎔']),1)
          anykey()
      if ischar('up','T'):
        if mazeq==newthing3:
          mazeq=newthing2
      if ischar('up','>') or ischar('up','<') or ischar('up',"x") or ischar('up',"("):
        p=list(i for i in ['Module A','Module B','Module C','Module E'] if itemdict[i]=='Yes')
        if p!=[]:
          for i in p:
            printt(moddict[i]+i+R,False)
            if p.index(i)==len(p)-2:
              printt(', and ',False)
            elif p.index(i)!=len(p)-1:
              printt(', ',False)
          printt(' seem to be attracted to something...',2)
          if len(p)==4:
            printt("Do you want to proceed? (y for yes)")
            if getkey1()=='y':
              istrue=True
              for i in p:
                itemdict[i]='No'
                goods.append(active[i+'.'])
                active[i]='Yes'
                active[active[i+'.']]='Yes'
              music("Truth",'Truth/Truth.mp3',True)
              c()
          else:
            printt("It seems as if they dont want to leave you..",1)
            if itemdict['Module C']=='Yes':
              printt(bold+"You must get all 4."+R)
            else:
              printt("Maybe you should try later.")
            slepy(2)
            c()

          c()
      if ischar('up','~'):
        planet()
      if ischar('left','9'):
        if itemdict['Module C']=='Yes' and not smallvarget('still caving'):
          tinyvars['still caving'] = False
          timeSTUP=True
          printt([bold+"The Makers of this island hid one module deep within the walls of these caves.","One of the many tricks of this island I was made to uncover."],[2,2])
          printt("Go Left.")
          time.sleep(1)
          print("[Any key to continue]")
          getkey1()
          timeSTUP=False
          c()
      if ischar('up','t'):
        mazeq=maze10
        c()
      elif ischar('up','g'):
        if mazeq not in [newthing1,newthing2]:
          gensz()
        else:
          shrine()
      elif ischar('up','K') or ischar('up','☼'):
        if mazeq==maze1:
          mazeq=festivehall
        elif mazeq==festivehall:
          printt(["\nA faded image of a star is on the wall...","You get a jolt of happiness just looking at it."],[3,1])
          anykey()
      elif ischar('up','e'):
        if mazeq==True1:
          if not smallvarget("true1"):
            c()
            smallvarset("true1")
            printt("So that's how fresh air feels.")
            time.sleep(2)
            if 'Unspoken Relic' in inventory:
              printt("You walk and walk, suprised by the warmth the Sun seems to give.")
              time.sleep(3)
            else:
              printt("You walk and walk, suprised by the great big ball of light in the sky.\n"+R+R+R+R+"It feels warm.")
              time.sleep(4)
            c()
            mazeq=True2
          else:
            mazeq=True2
        elif mazeq==True2:
          if not smallvarget("true2"):
            c()
            if 'Unspoken Relic' in inventory:
              printt("You pass those huge green objects...\nIf only you could remember their name.")
            else:
              printt("You pass huge green structures."+R+R+R+"\nThey smell better than anything you've ever smelled before.")
            time.sleep(3)
            c()
            smallvarset("true2")
            mazeq=True3
          else:
            mazeq=True3
        elif mazeq==True3:
          if not smallvarget("true3"):
            c()
            if 'Unspoken Relic' not in inventory:
              printt("Soon you find a campsite, which seems to have been used a long time ago.")
            else:
              printt("Soon you reach the campsite. A feeling of deja vu kicks in...")
            time.sleep(3)
            mazeq=True4
            smallvarset("true3")
            c()
          else:
            mazeq=True4
        elif mazeq==True4:
          c()
          if 'Unspoken Relic' not in inventory:
            achieve('end',0)
            printt("You close your eyes and rest.",2)
            printt("It feels as if this is your first time ever sleeping.")
            time.sleep(4)
            c()
            printt("You wake up, suprised that you are still at the campsite.",.02)
            time.sleep(3)
            printt('No longer waking up to the same island, no longer seeing the endless blue.',.02)
            time.sleep(1)
            printt(bold+'You are free.',.1)
            time.sleep(2)
          else:
            print("The campsite. The end of the game.\n\nAre you SURE you want to go? (make sure youve explored...)")
            if getkey1()=='y':
              achieve('end',0)
              printt(["You finally reach the campsite.","You remember. You know this is where you have to be.","It's as if they all know you."],[2,2,2])
              if 'The Key' in inventory:
                printt(["\n\033[48;5;44mscrew this 4th wall stuff god damn your a gamer.","you literally did the entire game in one run what the actual hell","if your not my friend lucas then like holy hell","i guess you could totally be bumba i would not be surprised","thats some serious comitment.....","i would give you an achievement but this is not being done by any other person in the entire world so im not that evil lol","thank you so much for playing :)\n"+R],[1,1,2,2,1,2])
                anykey(False)
                printt("\033[48;5;44moh wait im not done with the dialogue thing back to that lol"+R)
                anykey(False)
                clearline(8)
              time.sleep(2)
              printt(["It's as if you know them. You know you haven't been here before though....","A weird feeling starts to emerge.... hunger.","After a day of picking berries (not leaves....), your group finally decides to rest.","\nIt feels as if this is your first time sleeping.","At least in a while...","You know where you are in the morning. You couldn't be happier."],[2,2,2,2,3])
              thelastvar='⎯'*(12+len(name))
              time.sleep(4)
              printt("\033[38;5;9m\nWith me at the head, we all left in search of our futures.\nNo longer waking up in that filthy simulation, no longer staring at endless blue pixels.\nA feeling of life, a feeling of pain.\n\033[38;5;1mA feeling of freedom.\n\033[38;5;9mThe end of an dystopian utopia.\nAn endless world awaited us. The sky was no longer the limit.\nWe were truely free. And we knew it.",1)
              print("\033[0m\n\033[48;5;22m┌"+thelastvar+"┐\n│\033[38;5;9mI, "+name+", was it.\033[0m\033[48;5;22m│\n└"+thelastvar+'┘'+R+'\n')
              achieve('The Truth.')
              time.sleep(5)
              print("[Any key to leave, once and for all. Thank you for playing :)]")
              anykey()
          achieve('Escape?')
          achieve('Escape.')
          alive=False
          TRUEYAYA=True
          time.sleep(2)
      elif ischar('up','$') or ischar('up','o') or ischar('up','y') or ischar('up','m'):
        overide()
        square(tydict['up'][detup()]-53)
      elif ischar('up','!') and box1 not in posup:
        if mazeq==labm2:
          mazeq=labm1
        elif mazeq==theLake2:
          pass #idk it didnt work i said no
        elif '╦' in mazeq:
          if 'Unspoken Relic' in inventory:
            printt("Is it time to exit?")
            print("(y for yes, \033[01myou are no longer trapped in either world\033[0m)")
            if getkey1()=='y':
              c()
              if standed:
                printt("People are walking around...\nA sense of... happiness fills the air.",2)
                Music.set_volume(.2)
              mazeq=TheOne1
              current=50
            c()
          elif itemdict['Module D']=='Yes':
            printt([bold+"\nThe Last Key starts to drift off.","It is time to see the truth.","Do you wish to proceed? (y for yes)"+R],[1,2])
            if craftdict["Unspoken Relic"] and "The Key" not in inventory:
              print(bold+"\nIf you're on your way to get the relic... maybe something else beforehand too?\n"+r)
            if getkey1()=='y':
              c()
              slepy(2)
              printt(['You walk into the green light.',"You know you won't ever see this island again.",bold+'But it isnt a free ticket out.'],[1,1,3])
              anykey()
              truthtime()
            else:
              c()
          else:
            if 'Module D' in inventory:
              printt("And you have to equip it...")
            else:
              printt("Module D is required past this point... (And it's right there)")
            slepy(2)
            c()
        elif '╳' in mazeq:
          bossnumbu+=1
          mazeq=nextonboss[bossnumbu]
          mazechang=True
        elif mazeq==Portal:
          mazeq=labm2
        elif mazeq==maze2:
          current=-3
          mazeq=theroom
        else:
          mazeq=labm1
      elif ischar('up','@'):
        if equipped('Diving Gear [Full]'):
          printt('\nAre you sure you want to leave the underwater cave?\n(You will use the rest of your diving gear!)')
          if getkey1()=='y':
            mazeq,current=maze8,8
            inventory.remove('Diving Gear [Full]')
            inventory.append('Diving Gear [Empty]')
          c()
        else:
          printt("You cant survive that long underwater without diving gear on...",1)
          anykey()
      elif ischar('up','≣'):
        mazeq=cavem1
        c()
      elif box1 not in posup and not thechanger:
        if getoitem==False and mazeq[box2-52] in goods and mazeq[box1-52] in goods:
          movedir(-52)
      else:#find up change, find up transition
        if not thechanger and mazeq not in [emaze21,emaze22]: #easter (emaze)
          thechanger=True
          current=current-(5 if 'i' not in mazeq else 10)
          if mazeq!=theroom: #(IM AN IDIOT)
            overide()
          c()
          mazeq=nextone[current]
          if '┌' not in mazeq:
            movedir(832)
          thechanger=False
    if dir=='right':
      if ischar('right','ñ'):
        if facbelike==True:
          mazeq=Shed2
        else:
          printt("A gate,looks like it needs power...",1)
          anykey()
      if ischar('right','e'):
        if mazeq==True5:
          mazeq=True4
        elif mazeq==lanc55:
          if not smallysky and 'LYS' not in achievements.keys():
            c()
            printt(["A man stands before you.","\033[38;5;88mAn aura of pure hate flows from within him.","This isnt going to be easy.","YSKYSN attacks!"],[2,1,1,.1])
            anykey()
          smallysky=True
          yskysn()
      if ischar('right','é'):
        printt('A backpack lies on the ground...',2)
        printt("Do you want to pick it up?\n(y for yes)")
        if getkey1()=='y':
          c()
          printt("You feel your inventory get bigger...",1)
          printt("\033[38;5;194m(+3 Inventory space!)"+R)
          mazeq[mazeq.index('é')]='-'
          thelimiter=6
          anykey()
        c()
      if ischar('right','Z'):
        miniiq()
      if ischar('right','H'): #easter
        easter_diet(box2+1 if mazeq[box2+1]=='H' else box4+1)
      if ischar('right','⍨'): #easter
        mellamovictor()
      if ischar('right',']'):#easter
        if mazeq==emaze7:
          eastertemple()
      if ischar('right','J'):
        portal()
      if ischar('right','!'):
        if '╳' in mazeq:
          bossnumbu+=1
          mazeq=nextonboss[bossnumbu]
          mazechang=True
        elif mazeq==emaze16:#easter
          mazeq=emaze17
          current=-69
        elif mazeq==emaze21:#easter
          mazeq=emaze22
        elif mazeq==emaze22:#easter
          c()
          printt("...",1)
          slepy(1)
          printt(["It's the end. The end of the end.","At every end is a new beginning."],[3,2])
          printt("At least, usually.")
          achieve("The Darkest End")
          achieve('Horrible Game')
          smallvarchange("youdid_nt")
          alive=False
        elif mazeq==newthing3:
          mazeq=HEAHE
        elif mazeq==TheOne6:
          if not ('The Key' in inventory and smallvarget("hasgrut")):
            smallvarset("hasgrut")
            printt("There is a huge door, and a slot for a key.")
            time.sleep(2)
            if "The Key" in inventory:
              printt("You take out "+bold+"The Key"+R+" and it fits perfectly.")
              time.sleep(3)
              c()
            else:
              c()
          if "The Key" in inventory:
            mazeq=KeyRoom
        elif mazeq==TheOne4:
          if not smallvarget("exiteD"):
            printt("You take a step out of this place.")
            time.sleep(3)
            c()
            smallvarset("exiteD")
          mazeq=True1
          if 'Unspoken Relic' not in inventory:
            inventory=[]
        elif mazeq==Mining2:
          mazeq=Mining3
        elif mazeq!=theLake2:
          mazeq=labm1
        else:
          mazeq=theLake
      if ischar('right','g'):
        if mazeq not in [newthing1,newthing2,newthing3]:
          gensz()
        else:
          shrine()
      elif ischar('right','≣'):
        mazeq=cavem2
        c()
      elif ischar('right','◓') or ischar('right','◓'):
        pumpy()
      elif ischar('right','T'):
        if mazeq==Mining3:
          mazeq=newthing1
        elif mazeq==newthing1:
          mazeq=newthing2
      elif ischar('right','~'):
        if mazeq==cavem2:
          mazeq=Mining
        elif mazeq==Mining:
          mazeq=Mining2
        elif mazeq==Mining2:
          mazeq=Mining3
        c()
      elif ischar('right','╔'):
        dialogue()
      elif ischar('right','╥'):
        monke()
      elif ischar('right','|'):
        timeSTUP=True
        if docksbelike==True:
          if 'Diving Gear [Empty]' in inventory:
            print("\nWould you like to fill up your diving gear? (y for yes)")
            o90=getkey1()
            if o90.lower() in ['ye','y','yes']:
              for i in range(2):
                print('Filling Gear.')
                slepy(.5)
                clearline()
                print('Filling Gear..')
                slepy(.5)
                clearline()
                print('Filling Gear...')
                slepy(.5)
                clearline()
              inventory.remove('Diving Gear [Empty]')
              inventory.append('Diving Gear [Full]')
              c()
            else:
              c()
          else:
            printt("\n\nYou look at the pump, it reads:\n"+bold+"\nOxygen - Intended for Diving Gear\n"+R,0.04,True)
            printt("(You should find a diving gear, anykey to continue)")
            getkey1()
            c()
        else:
          printt("\nThe pump doesnt look like its on...",0.04,True)
          printt('(There is no power, anykey continue)')
          getkey1()
          c()
        timeSTUP=False
      elif ischar('right','*'):
        timeSTUP=True
        print('\n\n'+bold+'The gate needs power...'+R)
        slepy(2)
        c()
        timeSTUP=False
      elif box2 not in posright and not thechanger:
        if getoitem==False:
          if mazeq[box2+1] in goods and mazeq[box4+1] in goods:
            movedir(1)
            if box1 in [448,449] and '┋' in mazeq:
              timeSTUP=True
              for i in range(mazeq.count('╳')):
                mazeq[mazeq.index('╳')]='#'
              timeSTUP=False
              isleft=False
              isright=True
              numbero=1
      else:#find right change, find right transition
        if mazeq!=lanc3: #easter (emaze7)
          if not thechanger and mazeq not in [lanc55,emaze7,emaze21,emaze22]:
            thechanger=True
            overide()
            c()
            if mazeq!=cavem1:
              current+=1
              mazeq=nextone[current]
              movedir(-49)
            else:
              mazeq=cavem2
            thechanger=False
            if mazeq==easterblack:#easter
              c()
              printt('...',2)
              slepy(2)
              printt("Its gone.")
              slepy(2)
              printt("Everything. The island, the sky, the endless water.")
              slepy(2)
              printt('Its all gone.')
              slepy(2)
              achieve("The Dark End")
              achieve("Horrible Game")
              slepy(2)
              c()
              alive=False
              smallvarchange("youdid_nt")
        else:
          c()
          mazeq=lanc4
          try:
            for i in [19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]:
              janc=lanc4.copy()
              for i2 in range(0,i):
                for i3 in range(0,19):
                  janc[51-i2+(52*i3)]='7'
              printmaze(janc)
              time.sleep(.25 if i!=19 else 1)
              print("\033[H",end="")
          except:
            pass
          time.sleep(2)
          printt('\n'*20+'Its an ok day outside.',.03,True,True)
          slepy(2)
          printt("Birds are ok, flowers are ok.",.03,True,True)
          slepy(2)
          printt("On ok days like these.",.03,True,True)
          slepy(2)
          printt('Ok kids like you.',.03,True,True)
          slepy(3)
          c()
          printmaze(lanchm)
          time.sleep(1)
          c()
          printmaze(lanc6)
          time.sleep(2)
          printt(bold+'\nShould be',.1,False)
          slepy(1)
          print()
          for i in ['██████████','█        █','█        █','█        █','█        █','█        █','██████████']:
            print(i)
            time.sleep(.2)
          sys.stdout.write('\x1b[7A')
          sys.stdout.write('\x1b[12C')
          sys.stdout.flush()
          slepy(1)
          for i in ['██      ██','██     ██','██   ██','██████','██   ██','██     ██','██      ██']:
            print(i,end='')
            sys.stdout.write('\x1b[1B')
            sys.stdout.write('\x1b[25D')
            sys.stdout.write('\x1b[12C')
            sys.stdout.flush()
            time.sleep(.2)
          slepy(5)
          c()
          if not achievements['lanc']:
            mazeq=Mining
            print("\033[38;5;88mYou might not want to come back.\033[0m")
            achieve('lanc')
            time.sleep(2)
            c()
          else:
            printmaze(lanc4)
            time.sleep(2)
            lanc4x=lanc4.copy()
            for i in thelist0i:
              lanc4x[i]='◔'
            c()
            printmaze(lanc4x)
            time.sleep(2)
            for i in [827,828,880,879]:
              lanc4[i]='-'
            c()
            printmaze(lanc4)
            mazeq=lanc4
            current=102
            time.sleep(1)
            achieve('lanc2')
    if dir=='down':
      try:
        if ischar('down','.'):
          if 'bana' not in inventory:
            printt("The color of this part of the wall reminds you of an unripe banana...")
            slepy(3)
            printt("It even smells like them.")
            time.sleep(2)
            c()
          else:
            printt('monke veyr happy')
            slepy(3)
            printt('monke say yessir')
            slepy(3)
            while '.' in mazeq:
              mazeq[mazeq.index('.')]='-'
            monkehappy=True
            c()
        if ischar('down','U'):
          if mazeq!=Mining3: #(for easter)
            pass
          elif minervar and 249 not in nextone.keys():
            current=150
            mazeq=miney
            c()
            printt('A complex series of mines lays before you..')
            minegen()
            anykey()
          elif 'Old Pick' in inventory and not minervar:
            printt("One swing of the "+mcolor+"Old Pick, "+R+"and the wall crumbles.")
            anykey()
            minervar=True
          elif not minervar:
            printt("It seems like a wall of thin rock...\nEven the oldest tool could knock it down.")
            anykey()
          else:
            current=150
            mazeq=miney
            c()
        if ischar('down','u'):#easter
          c()
          if bunnycutscene==4:
            printt("The bunny has sat down next to a note...")
          else:
            printt("A note hidden in the water???")
          slepy(2)
          printt("It reads:")
          slepy(1)
          printt(bold+"\tFun fact: pressing '=' while in the main island can lead to a pretty cool event.\n\tYou will have to stay there, so do it when you can :)")
          slepy(3)
          printt(R+'\n(What type of lazy developer does this like omg)')
          anykey()
        if ischar('down','H'): #easter
          easter_diet(easter_diet(box3+52 if mazeq[box3+52]=='H' else box4+52))
        if ischar('down','~'):
          planet()
        if ischar('down','◓') or ischar('down','◓') or ischar('down','○'):
          pumpy() #omg halloween
        if ischar('down','T'):
          if mazeq==newthing2:
            mazeq=newthing3
          lll=True
        elif ischar('down','╥'):
          monke()
        elif ischar('down','e'):
          if mazeq==True3:
            mazeq=True2
          elif mazeq==True4:
            mazeq=True3
          elif mazeq==True2:
            mazeq=True1
        elif ischar('down','g'):
          if mazeq not in [newthing1,newthing2,newthing3]:
            gensz()
          else:
            shrine()
        elif ischar('down','['):
          if mazeq==festivehall:
            mazeq=maze1
          lll=True
        elif ischar('down','K'):
          if mazeq==newthing3:
            shrine(False)
        elif ischar('down','╔') or ischar('down','╕'):
          dialogue()
        elif ischar('down','⊙') or ischar('down','⊚'):
          pass
        elif ischar('down','5'):
          if itemdict['Module C']=='Yes':
            mazeq=Portal
        elif ischar('down','!'):
          if mazeq==maze5:
            mazeq=labm1
          elif mazeq==True1:
            mazeq = TheOne4
            current = 53
          elif mazeq==emaze20: #easter
            c()
            printt(".......")
            time.sleep(3)
            printt(["You have ventured too far out of reality.","Your fate is inevitable.",bold+'\nIf you want it to have meaning, get to the light.'+R,"\nThe rules have changed. Death appears after every step.\n",bold+"Do not step backwards. Do not think twice. Plan carefully."],[2,3,2,1])
            time.sleep(3)
            anykey()
            mazeq,over=emaze21,'⊗'
          elif mazeq==Modulea:
            bossnumbu+=1
            mazeq=nextonboss[bossnumbu]
            mazechang=True
            OMGRANDOM=False
          elif '╳' in mazeq:
            if mazeq!=Boss10:
              bossnumbu+=1
              mazeq=nextonboss[bossnumbu]
              if mazeq==Boss9:
                isright=True
                isleft=True
              mazechang=True
            else:
              c()
              leepic()
          elif mazeq==theTruth:
            mazeq=theroom
            current=-3
          elif mazeq==theroom:
            mazeq=maze2
            current=2
          elif mazeq==labm1:
            mazeq=labm2
          lll=True
        elif ischar('down','$') or ischar('down','o') or ischar('down','y') or ischar('down','m'):
          overide()
          square(tydict['down'][detup(False)]-1)
        elif ischar('down','t'):
          mazeq=Shed
      except:
        pass
      if box3 not in posdown and lll==False:
        if not thechanger:
          if getoitem==False and OMGRANDOM:
            if mazeq[box3+52] in goods and mazeq[box4+52] in goods:
              movedir(52)
          if OMGRANDOM==False:
            OMGRANDOM=True
      else:#find down change, find down transition
        if mazeq not in [lanc1,lanc2,lanc3,lanc4,lanc55,Modulea,theTruth,HEAHE,maze6,labm1,festivehall,themine,emaze20,emaze21,emaze22,Lesgo]: #easter (emaze)
          if not thechanger:
            thechanger=True
            if lll==True:
              lll=False
            else:
              current=current+(5 if 'i' not in mazeq else 10)
              overide()
              c()
              mazeq=nextone[current]
              if mazeq==maze2:
                istrue=False
              movedir(-832)
            thechanger=False
        lll=False
  except Exception as e:
    print(f"Error! {e} || Type: ({type(e)})")
    time.sleep(1)
  getoitem=False
  

theeasters=[emaze,emaze1,emaze2,emaze3,emaze4,emaze5,emaze6,emaze7,emaze8,emaze9,emaze10,emaze11,emaze12,emaze13,emaze14,emaze15,emaze16,emaze17,emaze132] #easter

#ADD STUFF HERE (colors for items, items must be added to the itemdict [in 2 different ways] and the ditem dict in setup.py, and a valid color code must be put in here)
#If you dont know how to get colors go here and look at f.txt and copy paste the one you want https://replit.com/@Muffinlavania/Terminal-Colours#main.py
#and add a space after each color code like i did eee
rubyc='\033[48;5;198m'
temmiecolor={
  '/':plane2, 
  '“':'\033[48;5;137m ',
  'ñ':'\033[48;5;137m',
  'U':"\033[48;5;15m ",
  '^':'\033[48;5;124m ',
  '&':'\033[48;5;147m ',
  '%':'\033[48;5;82m ',
  '=':'\033[48;5;226m ',
  'r':'\033[48;5;237m ',
  'l':'\033[48;5;226m ',
  '▣':'\033[48;5;220m ',
  '╼':'\033[48;5;139m ',
  '╾':'\033[48;5;172m ',
  '+':'\033[48;5;148m ',
  'p':'\033[48;5;148m ',
  'V':'\033[48;5;148m ',
  '{':'\033[48;5;57m ',
  'q':'\033[48;5;94m ',
  '0':'\033[48;5;94m ',
  'I':'\033[48;5;237m ',
  '1':'\033[48;5;147m ',
  'W':'\033[48;5;52m ',
  '❖':'\033[48;5;184m\033[38;5;232mϟ',
  '▤':'\033[48;5;94m ',  
  '☒':'\033[48;5;151m', #miner note
  'ₒ':'\033[48;5;16m', #start mining minerals
  '॰':'\033[48;5;95m',
  '°':'\033[48;5;100m', 
  '৹':'\033[48;5;93m',
  '๐':'\033[48;5;88m',
  'i':'\033[48;5;242m',
  '𐤏':rubyc, #numbers just dont work 
  'Ｏ':'\033[48;5;39m',
  '⦿':'\033[48;5;118m'
}
i92={'⎾':'┌','⎿':'└','⏋':'┐','⏌':'┘','┬':'┬','╘':'╘','╛':'╛'}
counti=-1
def printr(tex,sure=''): #the \x1b thing is what the slash turns into in a color code and is one index okay then 
  print(tex+(' ' if (tex[0]=='\x1b' and tex[-1]=='m') else ''),end=R+sure)
def printout(i9,Se=False,hue=False):
  global docksbelike,planebelike,labbelike,facbelike,counti,thebigfunny,eastervar1,eastervar2
  counti+=1 
  if counti!=0:
    if i9=='X':
      printr(waterc)
    elif i9 in temmiecolor.keys(): #find temmie
      printr(temmiecolor[i9])
    elif i9=='F':
      if not acheck('The Picture'):
        printr(waterc+' ')
      else:
        printr("\033[48;5;15m ")
    elif i9=='╥':
      printr('\033[48;5;94m'+random.choice(['╥','╥','╥','╥','╥','╥','╥','╨']) if monkehappy else cavein3)
    elif i9==' ':
      if mazeq==theLake2:
        if monkehappy:
          print(' ',end='')
        else:
          printr(cavein3+' ')
      elif mazeq==themine:#easter
        print(waterc+' '+R,end='')
      else:
        print(' ',end='')
    elif i9=='ñ':
      printr('\033[48;5;137m ')
    elif i9=='╱':
      print('\033[48;5;222m\033[38;5;16m',end='')
      try: #no risks (nothing is worth the risk)
        if counti==mazeq.index('╱'):
          print('Press K',end='')
        else:
          print("to return here!",end='')
      except:
        print(' ',end='')
    elif i9=='é': #backpack backpack
      printr("\033[48;5;84m ")
    elif i9=='◔':
      printr('\033[48;5;254m ')
    elif i9=='K':#old christmas ones
      if mazeq!=newthing3:
        printr('\033[48;5;35m ')
      else:
        printr(cavein1+' ')
    elif i9=='Z' and mazeq==maze6: #old valentines thing
      printr('\033[48;5;200m ')
    elif i9=='☼': #old christmas ones
      printr('\033[48;5;88m ')
    elif i9=='⊗':#easter
      printr('\033[48;5;52m ')
    elif i9=='H':#easter
        eastervar2+=1
        try:
            print(easterlist12[eastervar2]+R,end='')
        except:
            print(easterlist12[0]+R,end='')
    elif i9=='u':
        print(waterc,end=' ')
    elif i9=='U': #easter bunny sheeeeeeeeeeee
        print(('\033[48;5;7m '+R if not minervar or mazeq!=Mining3 else " "),end='')
    elif i9=='e' and mazeq in theeasters:#easter
        pass
    elif i9=='⍨': #easter
        if not emazehappy:
            print(i9,end='')
        else:
            print('ت',end='')
    elif i9=='z': #easter
        print('\033[48;5;22m '+R,end='')
    elif i9=='n':#easter
        eastervar1+=1
        if eastervar1 in easterdict1.keys():
            ieas=easterdict1[eastervar1]
        else:
            ieas=' '
        print('\033[48;5;146m'+ieas+R,end='')
    elif i9=='─':
      printr('\033[48;5;118m ')
    elif i9=='┢':
      printr("\033[38;5;59m┌")
    elif i9=='┪':
      printr("\033[38;5;59m┐")
    elif i9=='┹':
      printr("\033[38;5;59m┘")
    elif i9=='┺':
      printr("\033[38;5;59m└")
    elif i9=='6':
      printr('\033[48;5;222m ')
    elif i9=='7':
      printr('\033[48;5;232m ')
    elif i9=='4':
      printr('\033[48;5;238m ')
    elif i9=='8':
      printr('\033[48;5;216m ')
    elif i9=='▸':
      printr('\033[48;5;53m ')
    elif i9=='◓':
      printr('\033[48;5;202m ')
    elif i9=='○':
      printr('\033[48;5;82m ')
    elif i9=='g':
      if mazeq not in [newthing1,newthing2,newthing3]:
        printr('\033[48;5;127m ')
      else:
        printr('\033[48;5;240m ')
    elif i9=='╳':
      printr('\033[48;5;160m ')
    elif i9 in ['x','(','<','>']:
      if active[i9]!='Yes':
        print('\033[48;5;0m ',end='')
      else:
        print(coloredp[i9]+' ',end='')
    elif i9=='2':
      if itemdict['Module C']!='Yes':
        printr('\033[48;5;61m ')
      else:
        print(' ',end='')
    elif i9=='J':
      printr(purp+' ')
    elif i9==':':
      printr('\033[48;5;63m ')
    elif i9 in ['-','|'] and thebigfunny==True:
      printr('\033[48;5;76m ')
    elif i9=='|':
      print(" ",end="")
    elif i9 in ['┌','┐','└','┘','A','B','C','D','E'] and thebigfunny==True:
      printr('\033[48;5;82m'+i9)
    elif i9=='A':
      if mazeq==Modulea:
        print(gisforgree,end='')
      printr(ArtA+'A')
    elif i9=='B' and itemdict['Module C']=='Yes' or (mazeq!=labm1 and i9=='B'):
      printr(ArtB+'B')
    elif i9=='B':
      printr(lab1+' ')
    elif i9=='C':
      printr(ArtC+'C')
    elif i9=='D':
      if mazeq==theTruth:
        printr(gisforgree+ArtD+'D')
      else:
        printr(ArtD+'D')
    elif i9=='E':
      printr(ArtE+'E')
    elif i9 in ['╰','╯','╭','╮']:
      printr(d_green+i9)
    elif i9 in ['-','╪','e']: #find space, find -
      if istrue and 'a' in mazeq:
        if counti in range(23,28):
          printr('\033[48;5;196m ')
        elif counti in range(75,80):
          printr('\033[48;5;208m ')
        elif counti in range(127,132):
          printr('\033[48;5;74m ')
        elif counti in range(160,204):
          printr('\033[48;5;82m ')
        else:
          print(' ',end='')
      elif mazeq==theTruth:
        if counti in listoqs:
          printr(gisforgree+" ")
        else:
          print(' ',end='')
      elif mazeq in [True1,True2,True3,True4,True5]:
        printr(d_green+' ')
      elif mazeq in [lanc1,lanc2,lanc3,lanc4,lanc55]:
        if counti in lanc['gray'] and (mazeq!=lanc55 or counti not in lancd):
          printr('\033[48;5;238m ')
        elif counti in lanc['black'] and (mazeq!=lanc55 or counti not in lancd):
          printr('\033[48;5;232m ')
        elif counti in range(573,676) or counti in range(781,884):
          printr('\033[48;5;178m ')
        elif counti in range(677,780) or counti in range(885,988):
          printr('\033[48;5;172m ')
        else:
          print(' ',end='')
      elif mazeq==maze1:
        if counti in alistlol: 
          printr(cavecolor+' ')
        else:
          print(' ',end='')
      elif mazeq==emaze: #easter
        if counti in easlist11: #to like make sure i dont screw up lol
          print(' ',end='')
        elif counti in range(221,247) or counti in range(270,302):
          print('\033[48;5;57m '+R,end='') #purp
        elif counti in range(680,768):
          print('\033[48;5;2m '+R,end='') #green
        elif counti in range(470,580):
          print('\033[48;5;226m '+R,end='') #yellow
        elif any(counti in i for i in [range(169,470),range(580,680),range(790,840)]):
          print('\033[48;5;39m '+R,end='')#blue
        else:
          print(' ',end='')
      else:
        print(' ',end='')
    elif i9=='S':
      printr('\033[48;5;178m ')
    elif i9=='M':
      printr('\033[48;5;172m ')
    elif i9=='Q':
      if itemdict['Module C']=='Yes':
        print(waterc+"_",end="")
      else:
        print(waterc+' ',end='')
    elif i9=='┬':
      printr(('\033[48;5;178m' if hue else '\033[48;5;172m')+i92[i9])
    elif i9 in ['⎾','⎿','⏋','⏌','╘','╛']:
      printr(('\033[48;5;172m' if mazeq!=lanc55 else '\033[48;5;254m')+i92[i9])
    elif i9==']':
      printr(lab1+" ")
    elif i9=='◌':
      printr('\033[48;5;108m ')
    elif i9=='[':
      printr(lab2+" ")
    elif i9==')':
      printr(lab3+" ")
    elif i9=='╇':
      printr(lab3+" ")
    elif i9=='*':
      if mazeq!=themine:
        printr('\033[48;5;111m ')
      else:
        printr('\033[48;5;248m ')
    elif i9 in ['y','m','o','$'] and mazeq not in [HEAHE]:
      printr('\033[48;5;127m ')
    elif i9=='╤':
      printr(cavecolor+" ")
    elif i9=='5':
      if itemdict['Module C']=='Yes':
        printr('\033[48;5;110m ')
      else:
        printr(lab2+" ")
    elif i9 in ['Z','!']: #woah :0
      printr(gisforgree if mazeq==Modulea else gisforgree2 if mazeq==theTruth else "\033[48;5;6m " if mazeq==maze2 and itemdict['Module C']=='Yes' else waterc if mazeq==maze2 else cavein1 if mazeq==newthing3 and pumpnumber<3 else '\033[48;5;110m ' if mazeq==newthing3 else '\033[48;5;110m ' if mazeq not in [theLake,theLake2,themine] else " ")
    elif i9 in ['┋','┊']:
      if isright==False:
        if i9=='┋':
          print(" ",end="")
        elif i9=='┊':
          printr('\033[48;5;110m ')
      else:
        printr(cavein1+" ")
    elif i9=='╫':
      if isright==False:
        printr(cavein1+" ")
      else:
        print(' ',end='')
    elif i9=='≣':
      printr(cave2color+" ")
    elif i9 in ['⊞','⊟','⊠','░','⊡','⋄','⎔','⎚','▀','▁','▂','▃','▄','▅','▆','▇','█','▉','▊','▋','╊']:
      if i9!='╊':
        if not standed:
          print('\033[48;5;109m',end='')
        elif mazeq in [True1,True2,True3,True4]:
          print(d_green,end='') 
        print(symboldi[i9],end='')
      else:
        if 'Unspoken Relic' not in inventory:
          printr('\033[48;5;125m ')
        else:
          printr('\033[48;5;20m ')
    elif i9=='#': 
      if mazeq==theLake2 or '_' in mazeq:
        printr(cavein3+" ")
      else:
        printr(cavein1+" ")
    elif i9=='.':
      printr('\033[48;5;190m ')
    elif i9=='3':
      if itemdict['Module B']=='Yes':
        printr(cavein1+"-")
      else:
        printr(cavein1+" ")
    elif i9=='9':
      printr(cavein1+" ")
    elif i9=='T':
      if mazeq not in [newthing1,newthing2,newthing3,Mining3]:
        printr(yelo+" ")
      else:
        printr('\033[48;5;247m ')
    elif i9=='◘':
      if '⊖' in mazeq:
        if daco=='white':
          print('█',end='')
        elif daco=='red':
          printr(ArtA1+' ')
        elif daco=='orange':
          printr(ArtB1+' ')
        elif daco=='purple':
          printr(ArtC1+' ')
        elif daco=='blue':
          printr(ArtD1+' ')
      else:
        print(i9,end='')
    elif i9=='◴':
      if active['Module B']=='Yes':
        printr(mred+' ')
      else:
        printr(mgreen+' ')
    elif i9=='◵':
      if active['Module B']=='Yes':
        printr(mred+' ')
      elif itemdict['Module B']=='Yes':
        printr(mgreen+' ')
      else:
        printr(myellow+' ')
    elif i9=='◶':
      if active['Module B']=='Yes':
        printr(mred+' ')
      elif itemdict['Module B']=='Yes':
        printr(mgreen+' ')
      else:
        printr(mred+' ')
    elif i9 in ['◰','⊖']:
      printr(ArtA1+' ')
    elif i9 in ['◱','⊘']:
      printr(ArtB1+' ')
    elif i9 in ['◲','⊙']:
      printr(ArtC1+' ')
    elif i9 in ['⊚','◳']:
      printr(ArtD1+' ')
    elif i9=='╦':
      if mazeq!=True4:
        printr('\033[48;5;240m ')
      else:
        printr(blue1+' ')
    elif i9=='O':
      printr(blue2+' ')
    elif i9=='R':
      if mazeq!=HEAHE:
        printr(blue3+' ')
      else:
        printr('\033[48;5;160m ')
    elif i9=='╸':
      printr('\033[48;5;7m ')
    elif i9=='╩':
      printr('\033[48;5;243m ')
    elif i9=='G':
      if mazeq not in [newthing1,newthing2,newthing3]:
        if itemdict['Module C']=='Yes':
          printr(cavein1+"_")
        else:
          printr(cavein1+" ")
      else:
        if mazeq==newthing3:
          printr('\033[48;5;226m ')
        else:
          printr('\033[48;5;237m ')
    elif i9==';':
      if mazeq==emaze7:
        print('\033[48;5;115m '+R,end='')
      elif mazeq not in theeasters: #easter 
        print(cavein2+" "+R,end="")
      else:
        print('\033[48;5;2m '+R,end='')
    elif i9=='}':
      printr('\033[48;5;254m ')
    elif i9=='◝':
      print('',end='')
    elif i9=='◠':
      if miniscore==0:
        print("how did you actually get here.. well hi :)",end='') #lol if you find this dont screenshot this, its for something else...
      else:
        print(f'{"Good job! Your last minigame score - "+str(miniscore):<42}',end='')
    elif i9=='a':
      printr('\033[48;5;196m ' if active['Module A']=='Yes' else '\033[48;5;0m ')
    elif i9=='b':
      printr('\033[48;5;208m ' if active['Module B']=='Yes' else '\033[48;5;0m ')
    elif i9=='p':
      printr('\033[48;5;13m ')
    elif i9=='y':
      printr('\033[48;5;226m ')
    elif i9=='c':
      printr('\033[48;5;74m ' if active['Module C']=='Yes' else '\033[48;5;0m ')
    elif i9=="'":
      printr('\033[48;5;82m ' if active['Module E']=='Yes' else '\033[48;5;0m ')
    elif i9=='@':
      printr('\033[48;5;21m ')
    elif i9=='h':
      printr('\033[48;5;181m ')
    elif i9=="’":
      printr(gens+" ")
    elif i9=='┄':
      printr(gens+' ')
    elif i9=="~":
      printr(plane1+" ")
    elif i9=="`":
      printr(plane3+" ")
    elif i9=="t":
      printr('\033[48;5;139m ')
    elif i9 in tinyvars['minydict'].keys():
      printr('\033[48;5;155m ' if returnword(mazeq)==tinyvars['minydict'][i9] else " ")
    elif i9 in notes:
      printr(('\033[38;5;189m' if i9!='◫' else '\033[48;5;189m')+'?') 
    elif i9 in ['\\',"k"]:
      printr(plane2)
    elif i9=='_':
      printr(i9 if mazeq in theeasters else plane2 if '[' not in mazeq else '\033[48;5;226m ')
    elif i9 in ['╽','┑','┓','┒','╿','╏']:
      printr(signc+" ")
    elif i9 in ['L','w','d','f']:
      printr('\033[48;5;46m ' if (labbelike and i9=='L') or (facbelike and i9=='w') or (docksbelike and i9=='d') or (planebelike and i9=='f') else '\033[48;5;160m ')
    else: 
      if i9 not in ['┌','┐','└','┘']:  #find normal, find normal print
        print(i9,end="")
      else: #find player
        if mazeq not in [theroom,theTruth,True1,True2,True3,True4,True5,lanc1,lanc2,lanc3,lanc4,lanc55,emaze,emaze20] and not viewing:
          print(i9,end='')
        elif viewing:
          print(' ',end='')
        elif mazeq == theTruth:
          if counti in listoqs:
            printr(gisforgree+i9)
          else:
            print(i9,end='')
        elif mazeq in [True2,True3,True1,True4,True5]:
          printr(d_green+i9)
        elif mazeq==maze1:
          if counti in alistlol:
            printr(cavecolor+i9)
          else:
            print(i9,end='')
        elif mazeq in [lanc1,lanc2,lanc3,lanc4,lanc55]:
          if counti in lanc['gray'] and (mazeq!=lanc55 or counti not in lancd):
            printr('\033[48;5;238m\033[38;5;238m'+i9)
          elif counti in lanc['black'] and (mazeq!=lanc55 or counti not in lancd):
            printr('\033[48;5;232m\033[38;5;232m'+i9)
          elif counti in range(573,676) or counti in range(781,884):
            printr('\033[48;5;178m'+i9)
          elif counti in range(677,780) or counti in range(885,988):
            printr('\033[48;5;172m'+i9)
        elif mazeq==emaze20:#easter
          if counti in itscold:
            print(' ',end='')
          else:
            print(i9,end='')
        elif mazeq==emaze: #easter
          if counti in easlist11:
            print(i9,end='')
          elif counti in range(221,247) or counti in range(270,302):
            print('\033[48;5;57m'+i9+R,end='')
          elif counti in range(680,768):
            print('\033[48;5;2m'+i9+R,end='')
          elif counti in range(470,580):
            print('\033[48;5;226m'+i9+R,end='')
          elif any(counti in i for i in [range(169,470),range(580,680),range(790,840)]):
            print('\033[48;5;39m'+i9+R,end='')
          else:
            print(i9,end='')
        else:
          if 'a' in mazeq and istrue:
            if counti in range(23,28):
              printr('\033[48;5;196m'+i9)
            elif counti in range(75,80):
              printr('\033[48;5;208m'+i9)
            elif counti in range(127,132):
              printr('\033[48;5;74m'+i9)
            elif counti in range(160,204):
              printr('\033[48;5;82m'+i9)
            else:
              print(i9,end='')
          else:
            print(i9,end='')
nodarks=["theLake","theLake2","theroom","theTruth","labm1","labm2","Mining","Portal","True1","True2","True3","True4","lanc1","lanc2","lanc3","lanc4","lanc55","lanc6","Modulea","HEAHE","festivehall","newthing1","newthing2","newthing3","emaze","emaze7","emaze17","emaze18","emaze19","Boss 5","Boss 6","Halloween"] #easter (the emaze)

thebigfunny=False
def printmaze(themaze,k=False):
  global itemdict,f,startnight1,startnight2,startnight3,thebigfunny,counti
  themaze2=themaze
  thebigfunny=False
  RET = returnword(mazeq)
  if themaze==mazeq:
    if jing:
      print('Score:'+str(miniscore)+'\n')
  if (mazeq not in [cavem1,cavem2,Mining2,Mining3] and night==False and not(mazeq==Shed and facbelike==False) and not any([startnight1,startnight2,startnight3])) or RET in nodarks or RET in Finale or k or (RET in ["Shed","Shed2"] and facbelike) or current<-50:
    counti=-1
    for i in themaze2:
      printout(i,False,'7' in themaze2)
  else: #find dark, find nv
    def PLACED(height,width):
      p=[]
      for i in range(-1*height,height+2):
        i3=52*i
        p.append([box1-(width+1)+i3+i,box1+width+3+i3-i] if i>0 else [box1-width+i3-i,box1+width+2+i3+i])
      return p
    if mazeq in [cavem1,cavem2,Mining2,Mining3] or night==True or (mazeq==Shed and facbelike==False) or any(i==True for i in [startnight1,startnight2,startnight3]):
      places=[[1,2]]
      if itemdict['Night Vision']=='Yes' and "lanc" not in RET and "cavem" not in RET and "Mining" not in RET:
        thebigfunny=True
      elif equipped('Flashlight') or equipped('Lantern') or equipped('Night Vision') and not any(i==True for i in [startnight1,startnight2,startnight3]):
        places=PLACED(2,5)
      elif startnight1==True and mazeq not in [cavem1,cavem2,Shed,Mining2,Mining3]:
        places=PLACED(7,18)
      elif startnight2==True and mazeq not in [cavem1,cavem2,Shed,Mining2,Mining3]:
        places=PLACED(6,14)
      elif startnight3==True and mazeq not in [cavem1,cavem2,Shed,Mining2,Mining3]:
        places=PLACED(5,11)
      else:
        places=PLACED(1,4)
      for first1,i in enumerate(themaze2):
        t=False
        for G in places:
          if first1 in range(G[0],G[1]) or thebigfunny==True:
            printout(i)
            t=True
        if t==True:
          pass
        elif i in ['T','\n']:
          printout(i)
        else:
          counti+=1 #useless? (come here)
          print('\033[48;5;0m '+R,end='')
    print(R,end='')
outsides = ['maze1','maze2','maze3','maze4','maze5','maze6','maze7','maze8','maze9','maze10','themine']
def startnight():
  global startnight1,startnight2,startnight3,screenup
  for i in [0,1,2]:
    startnight1,startnight2,startnight3 = i==0,i==1,i==2
    if istime and returnword(mazeq) in outsides:
      screenup=True
    time.sleep(thetime*20)
  startnight3=False
  screenup=True
startslep=False
alive=True
LoL=[UP,UP,DOWN,DOWN,LEFT,RIGHT,LEFT,RIGHT,'b','a']
mada=True
def thenight():
  printt("The night is once again silent.",7)
  time.sleep(2)
def creepem():
  global alive,itemdict,mada,achievements
  clearline(2)
  printt('\nYou wake up to a noise...')
  time.sleep(3)
  trflex=random.randrange(1,4)#Your odds of surviving demon boi
  if mazeq in theeasters:#easter
    printt(['Its something... inhuman.',"You know its the end.","But nothing happens.","It seems the power of jesus strikes again."],[2,2,2,2])
  elif 'Unspoken Relic' in inventory:
    printt(random.choice(['A rabbit can be seen running into the bushes.','Just a few leaves passing by.','Must have been the crashing of the waves.',"A presence can be felt behind you."+R*4+"\nBut you know it means no harm. Not anymore.","You can't quite figure out where it came from.\nCould have been the wind, could have been the earth."]),2)
    printt(['What a peaceful place.',"You go back to sleeping."],[2,.02])
    time.sleep(3)
  elif trflex!=1 or itemdict['Module D']=='Yes':
    printt('Suddenly you feel a presence.',3)
    if itemdict['Module C']=='Yes':
      printt(bold+'The Demon.')
      time.sleep(2)
      printt("Its coming toward you.",3)
      if itemdict['Module D']=='Yes':
        printt(['It doesnt know about Module D.','Look it in the eyes.'+R,'Taking its advice, you turn around and look it straight in the eyes.',"It isnt anything, just a dark cloud of nothingness, void.","It doesnt move.","...","Suddenly its gone, and in its place is a key."+R+"(You found "+bold+"The Key"+R+')'],[2,.08,2,3,2,3,.02],[True,4])
        time.sleep(2)
        inventory.append("The Key")
        achieve('Rip bozo')
        printt(bold+"You are unbeatable."+R)
        time.sleep(7)
        clearline(10)
        thenight()
      else:
        printt(["I told you to stay indoors.","He spares no one."+R,"You want to look back, yet your body won't respond."],[2,1,1])
        if 'Revolver' not in inventory:
          printt(["Its impossible to breath, move, speak.",bold+"I'm sorry."+R],[2,.02])
          time.sleep(4)
          c()
          if itemdict['Module A']=='Yes' and mada==True:
            time.sleep(3)
            printmaze(mazeq)
            time.sleep(2)
            printt([bold+'...','You are still here?'],[3,.02])
            time.sleep(2)
            printt(['You must have been the one they spoke of.',R+'(Module A seems to glow dimmer...)'],[2,.02])
            mada=False
            achieve('Live on')
            time.sleep(4)
            clearline(4)
          else:
            achieve('Horrible Game')
            alive=False #le epicly dies
        else:
          time.sleep(3)
          printt([bold+"The Revolver.","Take it and find the courage to survive.",R+"You turn around and close your eyes.\nYou can barely feel your finger move."],[2,2,.03])
          achieve('Bang')
          achieve('Rip bozo')
          time.sleep(3)
          clearline(5)
          inventory.remove("Revolver")
          inventory.append('Revolver[Empty]')
          thenight()
    else:
      printt(["It doesnt feel human.","You cant turn around."],[2,3])
      if itemdict['Module D']=='Yes':
        printt(["Yet something within you tells you to.","The presence seems to weaken, sensing your sudden confidence.","You turn around, only to find a key.","Must have been your imagination... (You found"+bold+" The Key"+R+")."],[2,2,2,.02])
        inventory.append("The Key")
        achieve('Rip bozo')
        time.sleep(5)
        clearline(10)
        thenight()
      else:
        if 'Revolver' not in inventory:
          c()
          printt("You close your eyes and let it happen.")
          time.sleep(3)
          if itemdict['Module A']=='Yes' and mada==True:
            c()
            time.sleep(3)
            printmaze(mazeq)
            time.sleep(2)
            printt(['...','....?'],[2,.02])
            time.sleep(2)
            printt(['What a weird dream.',R+'(Module A seems to glow dimmer...)'],[1,.07])
            achieve('Live on')
            time.sleep(4)
            clearline(4)
            mada=False
            thenight()
          else:
            getkey1()
            achieve('Horrible Game')
            alive=False #le epicly dies
        else:
          time.sleep(2)
          printt("But wait... What about my "+bold+"Revolver?"+R,2)
          time.sleep(1)
          printt(["You turn around.","You point the gun at it.","You pull the trigger."],[1,2,.05])
          time.sleep(.5)
          c()
          achieve('Bang')
          achieve('Rip bozo')
          time.sleep(3)
          inventory.remove('Revolver')
          inventory.append('Revolver[Empty]')
          thenight()
  else:
    printt(["...","Theres no more sounds...","Must have been a squirrel"],[2,1,2])
    if itemdict['Module C']=='Yes':
      printt(bold+"Consider yourself lucky. Extremely lucky.")
    time.sleep(2)
  if alive:
    anykey()
#English be like
thetime=.75
the_no_times=['Boss 1','Boss 2','Boss 3','Boss 4','Boss 5','Boss 6','Boss 7','Boss 8','Boss 9','Boss 10','TheOne1','TheOne2','TheOne3','TheOne4','TheOne5','TheOne6','KeyRoom','Lesgo','lanc1','lanc2','lanc3','emaze21','emaze22','True1','True2','True3','True4']

timec=timez[501] 
timero=501 
def timeing():  #find time
  global timec,timez,timero,night,startslep,mazeq,mazesec,istime,Day,alive,achievements,thetime
  while alive:
    TY.sleep(thetime)
    if 'Boss' in returnword(mazeq):
      timero = 201
    if returnword(mazeq) not in the_no_times and istime:
      timero+=1
    timec=timez[timero] #0 = 1, 60 = 2, etc
    if timero==719:
      timero=0
    if timec=='5:00' and night==False and istime:
      t2 = THREAD(target=startnight)
      t2.start()
    elif timec=='6:00' and night==False and istime:
      night=True
      c()
      printmaze(mazeq)
    elif timec=='11:20' and night==True and istime:
      startslep=True
      clearline()
      time.sleep(.5)
      printt("\n(You feel drowsy...)",2)
      startslep=False
    elif timec=='12:00' and night==True and istime:
      startslep=True
      c()
      printmaze(mazeq)
      printt("\nYou lay down...",0.09)
      time.sleep(3)
      try:
        if mazesec[returnword(mazeq)][2]=='Yes' or itemdict['Module D']=='Yes' or 'Unspoken Relic' in inventory:
          creepem()
        elif mazeq in theeasters:
          creepem()#easter
        elif mazesec[returnword(mazeq)][2]=='Maybe':
          if random.randrange(1,5) in [2,3,4]:
            creepem()
          else:
            slepy(7)
        else:
          slepy(7)
      except:
        slepy(7)
      c()
      thetime,night,startslep,timec,timero=.75,False,False,'6:00',400
      if 'Unspoken Relic' in inventory:
        Day=-1
      Day+=1
      if Day==6:
        c()
        printt('Day 6',.1)
        time.sleep(3)
        printt(["That's it.","The island seems to be disappearing.","Yet you are still standing... on nothing.","Suddenly you start to fall..."+R+" You think.","There is nothing, no ground, no sky. You could be falling, you could be dead.","Yet suddenly, an island appears. In front of you is a cave.\nIn the distance there seems to be a plane, and a few metal structures.\nWater surrounds you on all sides.","A completely new experience."],[2,2,2,2,2,2,2])
        time.sleep(2)
        if itemdict["Module C"]=="Yes":
          printt("\nYou're back.",2)
        achieve('Horrible Game')
        alive=False
        anykey()
def dropitem(posii,doin_val=False):
  global mazeq,box1,box2,box3,box4,itemdict
  H,indicate=set_inv()[posii],''
  if H in ['Unspoken Relic','The Key'] or H in mindict.keys():
    printt("But it refused." if H not in mindict.keys() else "You can't drop these rocks...")
    return anykey()
  else:
    for i in [box2+1,box4+1,box1-1,box3-1,box1-52,box2-52,box3+52,box4+52]:
      if mazeq[i]=='-':
        mazeq[i]=ditem[H]
        indicate='E'
        break
  if indicate!='E':
    inventory.append(H)
    printt("An item magically appears in your inventory...\n(how did you manage to do this??????)" if doin_val else "Item cannot be dropped!",3) 
    anykey()
  else:
    inventory.remove(H)
    itemdict[H]='No' if (H not in inventory and itemdict[H]!='NA') else itemdict[H]
#All the things that have an item/thing that has to be present for hint
Re=R+bold
listohintdict={
  "cavem1":['"E" in mazeq',ArtE+'Module E'+Re+' is hidden here somewhere...'+R+Re+"\nThe only way to get it is with "+ArtB+'Module B','now you can pick up every item ever lol'],
  "cavem2":['"A" in mazeq',ArtA+"Module A"+Re+" is hidden in this part of the caves."+Re+" Its quite tricky to find, thats why im here.",'aaaaaaaaaaaa'],
  "labm1":['"B" in mazeq',ArtB+"Module B"+Re+" is impossible to get, unless you have "+ArtC+"Module C"+Re+". \nYou're welcome.",'lab go brrr'],
  "maze2":['"QQ" in mazeq',"There is only one true way out of this place. \nThe Fake water at the top can be walked through with "+ArtB+"Module B"+Re+".","Find the truth."],
  'theLake2':['monkehappy',"look at this monke bro why this stupid game dev adding a monkey racist??????",'An old shortcut to the cave.. Seems to have collapsed. (AKA I COULDNT FIGURE OUT HOW TO MAKE THIS IM SORRY)'],
  'maze6':["'Unspoken Relic' in inventory","Where you spawned. The first place every player sees.","Where you.... appeared."],
}
FoR=False
#All the mazes which just have a hint, might make it a list so like random
listorandodict={ #find module c hints, find mod c hint, find hints
  'theroom':'With '+ArtA+"Module A"+Re+", "+ArtB+"Module B"+Re+", "+ArtC+"Me"+Re+", and "+ArtE+"Module E"+Re+", you can escape this place.",
  'Shed':"Lots of loot in here, including the chance for a plane part.",
  "Shed2":"Backpack, backpack! (real)",
  'theLake':'This is where the makers of the island hid me.',
  'theLake2':'An old shortcut to the cave.. Seems to have collapsed. (AKA I COULDNT FIGURE OUT HOW TO MAKE THIS IM SORRY)',
  'maze3':'The Powerplant, where you give power to the island with the use of Wiring.',
  'maze10':'A way out? If you can get all three parts and power it up.',
  'theTruth':"Its time. Good luck :)",
  'Portal':'A way out? Seems like a minimap is needed...',
  'themine':"A way out? Seems like the door cant be opened with anything normal... It's going to have to be super."
}

labisntlike=True
thingk=''
def equipped(t):
  return itemdict[t]=="Yes"
def equip(e):
  global inventory,goods
  print(set_inv()[e].title()+' equipped')
  itemdict[set_inv()[e]]='Yes'
  if set_inv()[e]=='Module B':
    goods.extend(['Q','G'])
  if set_inv()[e] in modli and mazeq not in [TheOne1,TheOne2,TheOne3,TheOne4,TheOne5,TheOne6]:
    if set_inv()[e]=='Module C' and mazeq!=TheOne6:
      goods.append('2')
      while '╇' in labm2:
        labm2[labm2.index('╇')]='-' #Make portal ending possible
      printt(bold+"Hello "+name,2)
      printt("Press f at any time if you want a clue. I'll always be here."+R)
    inventory.remove(set_inv()[e])

afk=True
#Yoinked from https://replit.com/talk/share/Flappy-Block/125246 (Its too big brain for me)
keyz=''
class KeyboardThread(Thread):
  def __init__(self, input_cbk = None, name='keyboard-input-thread'):
    self.input_cbk = input_cbk
    super(KeyboardThread, self).__init__(name=name)
    self.daemon = True
    self.start()
  def run(self):
    while alive:
      self.input_cbk(getkey())
keyz2=''
def thingthing(key):#find key
  global afk,keyz,keyz2
  keyz2=key
  if afk:
    afk=False
    keyz=key
secrr=0
keyin = KeyboardThread(thingthing)
ONON=False
def tT():
  time.sleep(100)
  if not ONON:
    achieve('afk')
try:
  with open('truthdata2.json','r') as j:
    pass
except:
  print("Audio_test.mp3")
  music("test","Truth/testy.mp3",False)
  THREAD(target=tT).start()
  print("[Yes thats me playing the piano in 144p]")
  anykey()
  ONON = True
  musicstop()
lancd=[604,656,708,760,812,864,916,968,609,661,713,765,817,869,921,973,605,657,709,761,813,865,917,969,606,658,710,762,814,866,918,970,607,659,711,763,815,867,919,971,608,660,712,764,816,868,920,972]
lanc={'black':[586,638,690,742,794,846,898,950,591,643,695,747,799,851,903,955,604,656,708,760,812,864,916,968,609,661,713,765,817,869,921,973],'gray':
[587,639,691,743,795,847,899,951,588,640,692,744,796,848,900,952,589,641,693,745,797,849,901,953,590,642,694,746,798,850,902,954,605,657,709,761,813,865,917,969,606,658,710,762,814,866,918,970,607,659,711,763,815,867,919,971,608,660,712,764,816,868,920,972]
}
easlist11=[119,120,121,122,123,124,125,126,127,134,135,136,137,138,139,140,141,169,170,171,172,173,174,175,189,190,191,192,193,194,195,219,220,221,222,223,224,245,246,247,248,249,271,272,273,274,299,300,301,302,322,323,324,325,352,353,354,373,374,375,376,377,404,405,406,407,425,426,427,428,457,458,459,477,478,479,480,509,510,511,529,530,531,532,561,562,563,581,582,583,584,613,614,615,634,635,636,637,664,665,666,686,687,688,689,690,691,714,715,716,717,718,739,740,741,742,743,766,767,768,769,793,794,795,796,817,818,819,820,847,848,849,850,851,852,853,854,863,864,865,866,867,868,869,460,461,462,463,464,465,512,513,514,515,516,517,564,565,566,567,568,569] #easter
alistlol=[121,122,123,124,173,174,175,176,177]
sawdacontrols=False

def somerandom(aj):
  return random.choice(['\033[38;5;160m','\033[38;5;41m']) if aj else ""

#easter, getting your daily reward find rewards
if 'easter_cooldown' not in achievements.keys():
  achieve('easter_cooldown',[random.randrange(0,4),1])
elif achievements['easter_cooldown']==0:
  achieve('easter_cooldown',[random.randrange(0,4),1])

inventory=[]
prizefortoday=possibleprizes[achievements['easter_cooldown'][0]] #easter
#1 time is the second after the world was created i think lol [use round(time.time()) for other ones]
def achieveprint(wewew=False):  #find achievements print, find achieves
    eventsnumber=3 #change this and n2 to the amount of events (also add the new thing to h2)
    u,n,n2='',0,eventsnumber
    pagesnumber=5 #amount of pages (not event) +1
    updateq()
    h=[achieve1,achieve2,achieve3,achieve4,achieve5true if succe and "The Truth." in achievements.keys() else achieve5 if succe else achieve5alt]
    h2=[achieve5_1,achieve5_2,achieve5_3,achieve5_4]
    while u not in [ENTER,'x']:
      print("Press left/right to go through the pages, enter/x to exit\n(Green = gotten, Red = Not)\n"+bold+("(Up/down to go through the events)\n" if n==pagesnumber else '\n')+R+(h[n] if n!=pagesnumber else h2[n2])+'\nPage '+str(n+1)+'/'+str(pagesnumber+(1 if n==pagesnumber else 0)))
      if n==pagesnumber:
        print(bold+'\nEvent '+str(n2+1)+'/'+str(len(h2))+R)
      u=getkey1()
      n+=(1 if u in [RIGHT,'d'] and n<pagesnumber-1 else -1 if u in [LEFT,'a'] else 0)
      n2+=(1 if u in [UP,'w'] and n2<eventsnumber else -1 if u in [DOWN,'s'] and n2>0 else 0)
      n=(5 if n in [-1,6] else n)
      c()
if 'SEEN_UPDATE' not in achievements:
  achievements['SEEN_UPDATE']=True
  print(underline('Hi :)')+"\n\033[38;5;10mImportant first time stuff\033[0m\n\nBasic controls ingame: (view full list at the main screen after this)\nWASD/arrows to move around, TAB for inventory\n\nMain menu things:\nTo view update logs, press 'u'\nTo get a small overview of the game press 'o'\n\n(wait 10 seconds, this only appears once!)")
  time.sleep(10)
  clearline()
  anykey()
while True: #find start (bro ctrl f is a life saver)
  numbi2=0
  achieve('thisachievementispissingmeoff')
  thew=acheck('thisachievementispissingmeoff') #christmas achievement
  printt(somerandom(thew)+"Welcome to the Truth!")
  print(R+"---------------------------------------\n"+somerandom(thew)+"To skip the introduction, press 's'.\n"+somerandom(thew)+"To see the controls, press 'c'.\n"+somerandom(thew)+"To see your achievements, press 'a'"+somerandom(thew)+"\nTo view update logs, 'u', small overview of the game, 'o'\n"+R+"\n(Everything else will lead to the intro)\n"+R+"---------------------------------------")
  if 'lanc2' in achievements.keys():
    print(somerandom(thew)+"[ingame] Press K to try the yskysn boss fight!"+R)
  if acheck('New game pog'):
    print(bold+somerandom(thew)+'[ingame] If you would like to try the minigame again, press p!'+R)
  if acheck('Escape.'):
    print(somerandom(thew)+'[ingame] If you would like to skip to The Erase, press "-"'+R+bold+' (This will turn off achievements from then on, for fun)'+R)
  if name in devz:
    print(somerandom(thew)+'\nCool dev stuff you can do:'+R+'\n\tPress e right now to try out The Erase (with Module A)\n\tIn the actual game press 0 to get any item\n\tPress - in the game to tp to the end\n\t[THIS WILL TURN OFF ACHIEVEMENTS IF YOU USE ANY OF THEM]')
  if 'Bat' in achievements.keys():
    print('\n\033[38;5;202mThanks for doing the halloween event, quite a big shot move (and quite rare)'+R)
  if 'thisachievementispissingmeoff' in achievements.keys():
    if 'Bat' in achievements.keys():
      print((random.choice(['\033[38;5;65m','\033[38;5;64m'])+"christmas event is cooler") if 'Bat' in achievements.keys() else (bold+"A little festivity never hurt :)")+R)
  if 'The Impossible' in achievements.keys():
    print("\033[48;5;168mYou should love yourself, now!!!!!!!! (you're too good for this game..)"+R)
  gr1=getkey1()
  c()
  if gr1=='c':
    print(bold+"Controls:\n\n"+R+"WASD / Arrow Keys to move\nTAB for inventory\n\tEquip items in inventory to use them\n\tCrafting also is in inventory (or just press 4!!)\nN to take notes, basically writing stuff down\nC to redraw the screen (If anything weird happens)\nY/N for yes and no (when prompted)\nV to view achievements in game\nZ to end the game, if you want to speedrun or something\nX to skip waiting times on  dialogue/text (Spam/hold it to skip a lot) \nF might come into play later.."+("K to get to the \033[38;5;88mYSKYSN\033[0m boss fight!" if 'lanc2' in achievements else ""))
    slepy(2)
    anykey()
    sawdacontrols=True
  elif gr1=='u': #find update logs
    c()
    loe=0
    heha=''
    logs=[updatelogs,updatelogs2,updatelogs3,updatelogs4]
    while heha!='x':
      print(logs[loe])
      print('Left/Right to switch between logs, x to exit\nUpdate Log '+str(loe+1)+'/'+str(len(logs)))
      heha=getkey1()
      loe += 1 if heha in ['d',RIGHT] and loe!=(len(logs)-1) else -1 if heha in ['a',LEFT] and loe!=0 else 0
      c()
  elif gr1=='o':
    c()
    print("Well here goes nothing....\n\nTrapped on an island. \033[38;5;106mNo means of escape.\033[0m At least, \033[38;5;12mnot to the untrained eye.\033[0m\n\nCan you escape? There are currently 5 endings... One of them being the true ending.\nSearch around, find uses for items.\nWhen in doubt, check the achievements/your inventory. You'd be suprised how much is there...\n(For that one speedrunner out there you can press 'Z' to end your game/time)\n\n\033[38;5;26mHave fun!\033[0m")
    anykey()
  elif gr1=='e' and name in devz:
    printt("Wow your a dev very col")
    slepy(1)
    printt("Ok heres the final boss battle pro gamer, (no achievements tho)")
    slepy(2)
    printt("Also "+bold+"The Key"+R+' because yes')
    slepy(4)
    itemdict['Module A']='Yes'
    inventory.append('The Key')
    if name!='Muffinlavania':
      gGg=False
    
    mazeq=Boss1
    erasin=True
    istime=True
    qp=THREAD(target=TheErase)
    qp.start()
    break
  elif gr1=='=':
    c()
    printt("Easter event: on :)")
    mazeq=emaze
    current=-100
    anykey()
  elif gr1=='a': #find achievements find the achievements
    achieveprint()
  elif gr1 !='s':
    printt(["You wake up...","You seem to be in a glass container, full of some sort of liquid.","The silence is almost unbearable.","Faces are all around you, it looks as if they are speaking.","Suddenly everything is red, and the world starts to go black...."],[2,2,2,2,4,.03])
    c()
    break
  else:
    break
print("If you forget any keybinds press 'R' for a reminder!")
slepy(1)
anykey()
hasplayedlol=False
for i in achievements.values():
  if i==True:
    hasplayedlol=True
if not hasplayedlol and not sawdacontrols:
  print(bold+"Seems to me like you are new.... so here are the controls\n\n"+R)
  print("WASD / Arrow Keys to move\nTAB for inventory\n\tEquip items in inventory to use them\n\tCrafting also is in inventory (or just press 4!!)\nC to redraw the screen (If anything weird happens)\nY/N for yes and no (when prompted)\nV to view achievements in game\nZ to end the game, if you want to speedrun or something\nX to skip waiting times on  dialogue/text (Spam/hold it to skip a lot) \nF might come into play later..")
  slepy(3)
  anykey()
  c()
try:
  if achievements['end']>0:
    c()
    print("It seems like you got disconnected during The Truth ending!\n")
    if achievements['end'] in [2,9,7]:
      print("\n(And yes you will still have The Key)\n")
    if achievements['end'] in [9,8,7,6]:
      print("\n\033[38;5;10m(We still haven't forgotten you "+name+".)\033[0m\n")
    print("Would you like to return to the ending lab? (THIS IS A ONE TIME USE, SAYING NO WILL STILL KEEP THIS SAVE!)\ny for yes, anything else for no")
    time.sleep(.5)
    thetrup=getkey1()
    if thetrup=='y':
      c()
      print('Exiting simulation.... Exit code: no_losing_hard_ending_for_you_yaya')
      time.sleep(2)
      mazeq=TheOne1
      current = 50
      if achievements['end'] in [9,2]:
        inventory.append('The Key')
      if achievements['end'] in [9,8]:
        gretly()
        inventory.append('Unspoken Relic')
      if achievements['end'] in [7,6]:
        standed=True
        untrollin()
        inventory.append('Unspoken Relic')
      achieve('end',0)
except:
  pass
def tbhidk2():
  global STOP
  time.sleep(1.5)
  STOP=False
pissedoff=True
t = THREAD(target=timeing)
t.start()
TIPO=time.time()
Lol2=0
c()
okvar=False
okvar2=''
thatonemoduleavar=False

def typer(YE,new='\n',limit=0):
  thi=getkey1(True)
  YE+=(thi if thi not in [ENTER,TAB,BACKSPACE] and len(thi)==1 else new if thi==ENTER else '')
  if thi==BACKSPACE and len(YE)>limit:
    if ((YE[-1]!='-' and YE[-2]!=ENTER) if new=='\n- ' else True):
      YE=YE[:-1]
    else:
      YE=YE[:-2]
  return (thi, YE)
yenotes="- "
while alive:
  if labisntlike and labbelike:
    while '*' in maze5:
      maze5[maze5.index('*')]='-'
  print("\033[H",end="")
  try:
    box1,box2,box3,box4=int(mazeq.index('┌')),int(mazeq.index('┐')),int(mazeq.index('└')),int(mazeq.index('┘'))
    for i in ['┌','┐','└','┘']: #kill all dupers of player lol
      while i in mazeq:
        mazeq[mazeq.index(i)]='-' 
      mazeq[box1 if i=='┌' else box2 if i=='┐' else box3 if i=='└' else box4]=i
  except:
    if '╳' not in mazeq and '◘' not in mazeq:
      print('Code died (something funky happened, respawned in the middle!)')
      square(390)
      box1,box2,box3,box4=int(mazeq.index('┌')),int(mazeq.index('┐')),int(mazeq.index('└')),int(mazeq.index('┘'))
  thatonemoduleavar=False
  if mazeq==theroom and not acheck("What's this?"):
    achieve("What's this?")
  if jing:
    print('Score:'+str(miniscore)+'\n')
  if not gettingkey:
    printmaze(mazeq,True if current in range(150,250) else False)
  if returnword(mazeq) not in Bosses and returnword(mazeq) not in Finale and '⊚' not in mazeq:
    print(f'{"Day "+str(Day):^52}',end='')
  
  if not startslep:
    #MUSIC
    if mazeq in [theTruth,theroom]:
      if mazeq==theTruth:
        if 'Unspoken Relic' in inventory:
          Music.set_volume(.5)
        music("Truth",'Truth/Truth.mp3')
    elif all_music!={}:
      if 'Unspoken Relic' not in inventory:
        musicstop()
    
    istime=True
    while afk: #find main input, find input, find main getkey
      TY.sleep(.05)
      if screenup:
        if not gettingkey:
          print("\033[H",end="")
          printmaze(mazeq,True if current in range(150,250) else False)
          screenup=False
    
    keyz = keyz.lower() #correction for caps lock
    
    try:
      if all([i in mazeq for i in ['┌','┐','└','┘']]):
        square(mazeq.index('┌'))
    except:
      pass
    if not ('┌' in mazeq and '┐' in mazeq and '└' in mazeq and '┘' in mazeq or '◘' in mazeq):
      if not ('╳' in mazeq and itemdict['Module A']=='Yes'):
        erasin = False
        alive = False
      else:
        STOP=True
        itemdict['Module A']='No'
        mazeq=Modulea
        thatonemoduleavar=True
        overide()
        square(546)
    if not thatonemoduleavar:
      print()
      try:
        if keyz==LoL[Lol2]:
          Lol2+=1
        else:
          Lol2=0
      except:
        printt("wow how cool you did the funny combination thing whndaiufneiugbiug heres an achievement")
        achieve('classic')
        anykey()
        Lol2=0
      
      
      if keyz=='w' or keyz==UP:
        move('up')
      if keyz=='/' and name=='Muffinlavania':
        print("1) Gens\n2) Achievements")
        if getkey1()=='1':
          inventory.append('Wiring')
          gensz()
        else:
          ac=''
          print("Enter achievement name to achieve (enter/tab to exit):\n>")
          while (e:=typer(ac))[0] not in [ENTER,TAB]:
            ac=e[1]
            clearline()
            print("> "+ac)
          print(f"achieve({ac}) right?")
          if getkey1()=='y':
            achieve(ac)
        anykey()
      if keyz=='9' and name=='Muffinlavania':
        print('Top left box:',mazeq.index('┌'))
        print("Current:"+str(current))
        print("Inventory: "+str(inventory))
        print("Progression: "+str(nextone.keys()))
        print("Raw maze:")
        for i in mazeq:
          print(i,end='')
        print("\nRaw maze (next):")
        try:
          for i in nextone[current+1]:
            print(i,end='')
        except:
          print("error!")
        anykey()
      if keyz=='n':
        thi=''
        while thi!=TAB:
          print("\033[0mNotes:\n"+yenotes+"\n\n\033[38;5;202mType to add to notes, \033[38;5;160menter for a new line, \033[38;5;52mTab to exit\033[0m")
          thi, yenotes=typer(yenotes,'\n- ',2)
          c()
      if keyz=='u': #save button, mostly useless tho
        achieve()
      if keyz=='r':
        print(bold+"Controls:\n\n"+R+"WASD / Arrow Keys to move\nTAB for inventory\n\tEquip items in inventory to use them\n\tCrafting also is in inventory (or just press 4!!)\nC to redraw the screen (If anything weird happens)\n\033[38;5;46m[NEW]\033[0m N to takes notes\nV to view achievements in game\nZ to end the game, if you want to speedrun or something\nX to skip waiting times on  dialogue/text (Spam/hold it to skip a lot) \nF to use a certain item..\n")
        if 'lanc2' in achievements.keys():
          print("\'K\' - teleport to the yskysn boss fight!"+R)
        if acheck('New game pog'):
          print('\'P\' - try the minigame!'+R)
        if acheck('Escape.'):
          print('\'-\' - try The Erase!'+R+' (disables achievements, just for fun)')
        if name in devz:
          print('\nCool dev stuff you can do:'+R+'\n\tPress 0 to get any item (from a console thing)\n\tPress - in the game to tp to the end\n\n'+"\t[THIS WILL TURN OFF ACHIEVEMENTS IF YOU USE ANY OF THEM]")
        anykey()
      if keyz=='v': #viewing achievements (omg new)
        c()
        achieveprint(True)
      if keyz=='b' and name=='Muffinlavania':
        over='⊗'
      if keyz=='k' and acheck('lanc2'):
        if mazeq not in [Lesgo,lanc55,lanc4,lanc3,lanc2,lanc1]:
          c()
          somethinglo=mazeq
          print("Are you sure you want to return to the \033[38;5;88mYSKYSN\033[0m boss fight? (y for yes)")
          if acheck("LYS"): 
            print("Normal mode beaten!")
          if acheck('True Chad'):
            print("No heal mode beaten!")
          if acheck('LEAN'):
            print("Extreme mode beaten! (sheesh)")
          if acheck('Double takedown'):
            print("Double boss hp beaten!")
          if acheck('YSLYSN'):
            print("You beat no hit mode.... WHAT")
          if getkey1()=='y':
            mazeq=lanc55
          c()
      if keyz=='h' and ('Unspoken Relic' in inventory or name=='Muffinlavania'):
        jstem=0
        thige=[themine, maze1,maze2,maze3,maze4,maze5,maze6,maze7,maze8,maze9,maze10,cavem1,cavem2,Mining,Mining2,Mining3,newthing1,newthing2,newthing3,HEAHE,festivehall,theLake,theLake2,labm1,labm2,Portal,Shed,Shed2,theroom,theTruth,Boss1,Boss2,Boss3,Boss4,Boss5,Boss6,Boss7,Boss8,Boss9,Boss10,Modulea] #might need to update
        storing=mazeq
        viewing=True
        while True:
          c()
          mazeq=thige[jstem]
          printmaze(thige[jstem],True)
          print('\nCurrent maze name: '+returnword(thige[jstem])+'\t\tNumber: '+str(jstem)+'\nD to go +1, A to go -1, X to exit')
          nv=getkey1()
          jstem+=1 if (jstem!=len(thige)-1 and nv=='d') else -1 if (nv=='a' and jstem!=0) else 0
          if nv=='x':
            mazeq=storing
            viewing=False
            c()
            break
      if keyz=='=': #easter
        if mazeq in [themine,maze1,maze2,maze3,maze4,maze5,maze6,maze7,maze8,maze9,maze10] or name=="Muffinlavania":
          c()
          printt("Easter event: on :)\n[Any key to continue, n to cancel]")
          if getkey1()!='n':
            mazeq=emaze
            current=-100
        else:
          printt("(you need to be in the main island to go to the easter event)")
          anykey()
      if keyz=='p' and acheck('New game pog'):
        c()
        okvar=True
        okvar2=mazeq
        miniiq(False)
      if keyz=='3' and name=='Muffinlavania':
        print('Top left box:',mazeq.index('┌'))
      if keyz=='q':
        if minimapa or name=='Muffinlavania':
          c()
          if 'The Key' not in inventory:
            printmaze(yum2,True)
          else:
            printmaze(yl)
          anykey()
          c()
      if keyz=='c':
        c()
      if keyz=='-':
        if name=='Muffinlavania':
          overide()
          for i in ['Note 1','Note 2','Note 3','Note 4','Note 5','Note 6','Note 7','Note 8','Note 9','Note ?']:
            notedict[i][0]=True
          mazeq=theTruth
          square(230)
        elif name in devz or acheck('Escape.'):
          c()
          printt('Are you sure you want to go to The Erase (you cant go back, y for yes)')
          hhh=getkey1()
          if hhh=='y':
            gGg=False
            overide()
            mazeq=theTruth
            square(230)
            for i in range(899,922):
              mazeq[i]='╦'
          c()
      if keyz=='a' or keyz==LEFT:
        move('left')
      if keyz=='e':
        if returnword(mazeq) not in Bosses:
          c()
          printnotes()
        else:
          if itemdict['Module D']=='Yes' and STOPGOOD<3 and not STOP:
            STOPGOOD+=1
            STOP=True
            yy=THREAD(target=tbhidk2)
            yy.start()
      if keyz=='4': #craft
        crafting()
      if keyz==TAB and mazeq!=Lesgo: #find inventory
        clearline()
        print("Inventory: (Max: "+("∞" if itemdict['Module E']=='Yes' else str(thelimiter))+")"+bold+(' '*(26-len(name)))+'┌'+('─'*(len(name)+2))+'┐')
        theywe=0
        letsago=random.choice(['\033[48;5;4m','\033[48;5;5m','\033[48;5;6m','\033[48;5;13m']) if acheck("The Banner") else ''
        for i in set_inv():
          theywe+=1
          i+='('+str(inventory.count(i))+")"
          print(i+((' '*(45-len(i)-len(name))+'│ '+name+' │') if theywe==1 else (' '*(45-len(i)-len(name))+'└'+('─'*(len(name)+2))+'┘') if theywe==2 else ''))
          #prints item then 2nd part of name thing then maybe 3rd part
        print((('None'+(' '*(41-len(name)))+'│ '+letsago+name+R+' │\n') if len(inventory)==0 else '')+R+'Temperature:'+bold+((' '*(33-len(name))+'└'+('─'*(len(name)+2))+'┘') if theywe<2 else ''))
        #None print at the start, name print(if the first one didnt happen) at the end
        #if theywe 2 or higher then yay we printed everything
        try:
          if 'Thermometer' in inventory:
            print(str(mazesec[returnword(mazeq)][0])+'°F, '+mazesec[returnword(mazeq)][1]+R)
          else:
            print(mazesec[returnword(mazeq)][1]+R)
        except:
          print("???")
        print('Time:',end='')
        if acheck('The Emblem'):
          print(' '*37+'\033[48;5;39m     '+R+bold) #\033[48;5;57m purp \033[48;5;2m green \033[48;5;226m yellow \033[48;5;39m blue
        else:
          print(bold)
        thingk='Night' if night else "Morning" if timero in range(300,660) else "Afternoon" if timero in range(0,200) or timero in range(660,721) else "Dusk"
        somethingge=0
        if acheck('The Emblem'):
          somethingge=41
        if 'Watch' in inventory:
          print(str(timec)+', '+thingk,end='')
          somethingge-=(len(str(timec))+2)
        else:
          print(thingk,end='')
        somethingge-=len(thingk)
        print((' '*somethingge+'\033[48;5;2m   \033[48;5;57m \033[48;5;2m   ') if somethingge>0 else ''+R+'\n'+(' '*42+'\033[48;5;39m     '+R if acheck('The Emblem') else ''))
        qer=False
        eeee=0
        for q in modli:
          if itemdict[q]=='Yes':
            qer=True
            eeee+=1
            print(moddict[q]+colname[q])
        if qer:
          print()
        if festivity>1: #....
          clearline()
          print(random.choice(['\033[38;5;160m','\033[38;5;41m'])+"Festivity: "+str(festivity)+'\n')
        if acheck('The Rainbow'):
          a_listprint=['\033[38;5;196m','\033[38;5;202m','\033[38;5;220m','\033[38;5;46m']
        else:
          a_listprint=['','','','']
        print(R+"You can:\n"+a_listprint[0]+"1) Equip an item"+R+"\n"+a_listprint[1]+"2) Drop an item"+R+"\n"+a_listprint[2]+"3) Unequip an item"+R+"\n"+a_listprint[3]+"4) Crafting"+R+'\n')
        if acheck('valentine') and not eaten_it:
          print("\033[38;5;198m5) A chocolate"+R)
        if acheck('The Egg'):
          print("\033[38;5;140m0) The Egg"+R)
        thuyg=getkey1()
        clearline((14 if not qer else 15)+eeee+len(inventory)+(1 if festivity>1 else 0)) #...
        if thuyg=='1':
          print("\nWhich item would you like to equip? (Say number of item)"+bold)
          i2=0
          for i in set_inv():
            i2+=1
            print(str(i2)+") "+i)
          if len(set_inv())==0:
            print('None')
          print(R)
          mewantpls=getkey1()
          if mewantpls.isdigit():
            if int(mewantpls)<=len(set_inv()):
              if itemdict[set_inv()[int(mewantpls)-1]]=='No':
                equip(int(mewantpls)-1)
              else:
                print('This item is already equipped!')
              anykey()
          c()
        if thuyg=='2':
          print("Which item would you like to drop? (Say number of item)"+bold)
          i2=0
          for i in set_inv():
            i2+=1
            print(str(i2)+") "+i)
          if len(set_inv())==0:
            print('None')
          print(R)
          LOLLL=getkey1()
          clearline(3+len(set_inv()))
          if LOLLL.isdigit():
            if int(LOLLL) < len(set_inv())+1 and len(set_inv())>0:
              try:
                dropitem(int(LOLLL)-1)
              except Exception as fe:
                print(f"Error... {fe}")
        if thuyg=='3':
          print("\nWhich item would you like to unequip? (Say number of item)"+bold)
          i2=0
          for i in set_inv():
            i2+=1
            print(str(i2)+") "+i)
          if len(set_inv())==0:
            print('None')
          print(R)
          mewantpls=getkey1()
          if mewantpls.isdigit():
            if int(mewantpls)<=len(set_inv()):
              if itemdict[set_inv()[int(mewantpls)-1]]=='Yes':
                itemdict[set_inv()[int(mewantpls)-1]]='No'
                print('Item unequipped.')
              else:
                print('This item is not equipped (Or cant be unequipped)')
              anykey()
        if thuyg=='4':
          crafting()
        if all([thuyg=='5','valentine' in achievements.keys(),not eaten_it]):
          c()
          print("A single chocolate. \nA small encarving on it says:\n\t\033[38;5;198mThank you :)"+R+'\n\nDo you want to eat it?\n (One time use per game, y for yes)')
          eat_it_dare=getkey1()
          if eat_it_dare=='y':
            eaten_it=True
            somethingiget=random.choice(['Flashlight','Watch','Wiring','Night Vision'])
            inventory.append(somethingiget)
            dropitem(len(set_inv())-1,True)
        if thuyg=='0' and 'The Egg' in achievements.keys():
          printt("The egg seems ..."+R+" almost ready to hatch?",2) #the_easter_egg
          anykey()
        c()
      if keyz=='s' or keyz==DOWN and not any([ischar('down','⊚'),ischar('down','⊙')]):
        move('down')
      if keyz=='d' or keyz==RIGHT:
        move("right")
      if keyz=='g' and name=="Muffinlavania":
        t=''
        print("What would you like to eval? (enter to eval, tab to exit)\n")
        while (e:=getkey1()) not in ['tab','enter']:
          t+=e if len(e)==1 else ''
          clearline()
          print(t)
        if e=='enter':
          try:
            eval(t)
            print("Executed!")
          except Exception as q:
            print(f"Error... {q}")
        anykey()
      if keyz=='0':
        h=''
        if name in devz:
          k=''
          c()
          print('0) All Modules')
          for i in item4dev:
            print(str(item4dev.index(i)+1)+') '+i)
          print('(if you make a mistake the code wont break lol)')
          while k!=ENTER:
            print(bold+"Item Number > "+R+h)
            k=getkey1()
            try:
              if k not in [ENTER]:
                h+=k
            except:
              pass
          try:
            if h!='0':
              inventory.append(item4dev[int(h)-1])
            else:
              inventory.extend(modli[:-1])
            if name!='Muffinlavania':
              gGg=False
              print("[Achievements have been disabled!]")
          except:
            pass
          c()
      if keyz=='.' and (name in devz or "Unspoken Relic" in inventory):
        if thetime>.05:
          thetime=round(thetime-.01,3)
          print("Current time (Seconds irl per minute ingame): "+str(thetime))
      if keyz=='m':
        achieve('ok')
        secrr+=1
        try:
          printt(["GG you found the easiest secret.","Ok, you already found the secret stop pressing the button.",bold+"WE GET IT."+R+" You found big boi secret. Now stoppp","Bruh... cmon this is taking too many lines of unnecessary code.","Geez play the game and stop looking at this text.","Probably should have made this button just one text huh. Would have been less fun and YOU WOULD ACTUALLY PLAY THE GAME.","Ok well this is the end of all the texts, so stop.","kdwioajfinjvrigthungorimfoirmfoiesmfoiesfoisem.","(Look my code is breaking omg)mfoiefoiemomf01010101010.","You are going to just keep pressin this huh.","01010101 (omg hes so bad at coding code breaking xdxd, 01010101100","Yea I added this text cause its actually fun pressing m lol","Fun fact: this is based off of a game named Isle"][secrr-1])
        except:
          if secrr==14:
            printt("Fun fact: Candice",1)
            print("1) ok\n2) Whos Candice\n(Press 1 or 2)")
            while (y:=getkey1()) not in ['1','2']:
              pass
            if y=='1':
              printt("\nok\n(get clickbaited this no give ok achievement ezezezez)")
            else:
              printt("\nCandeez nuts fit in your mo")
              clearline(2)
          if secrr==15:
            printt("Ok whatever this is ACTUALLY the end. Now the button will just print 1 of 3 messages")
          if secrr>15:
            printt(random.choice(['Button go brrrrrr','Be a gamer and get the '+bold+'Truth'+R+' ending.','Muffin op?']))
        anykey()
      if keyz=='u' and name=='Muffinlavania':
        mazeq,current=lanc1,100
      if keyz=='z':
        clearline(2)
        print("Are you sure you want to end the game? (Y/N)")
        if getkey1()=='y':
          alive=False
          FoR=True
        c()
      if keyz=='f':
        if itemdict['Module C']=='Yes':
          printt(bold+((listohintdict[returnword(mazeq)][1] if eval(listohintdict[returnword(mazeq)][0]) else listohintdict[returnword(mazeq)][2]) if returnword(mazeq) in listohintdict.keys() else listorandodict[returnword(mazeq)] if returnword(mazeq) in listorandodict.keys() else "Run." if mazeq in Bosses else "You Made it." if mazeq in Finale else random.choice(['\033[38;5;160m','\033[38;5;41m'])+"jingy bells :(" if mazeq==festivehall else "Nothing unusual here.")+R,2)
          anykey()
      afk=True
  else:
    while startslep:
      time.sleep(.1)
  eastervar1=0#easter
  eastervar2=-1#easter
TIPO2=round(time.time()-TIPO)
if Day==1 and TRUEYAYA:
  achieve('Sped')
print('\033[38;5;44mAchievements:'+R)
for i in achievements.keys():
  if acheck(i)==True:
    print('\033[38;5;86m - '+i+R)
def quit(promp):
  print("\033[38;5;196m"+promp)
  if input("\n\033[38;5;7mWould you like to start the game again? (y/n, you can actually type!!!)\n>\033[38;5;46m ").lower()=='y':
    if ".py" not in str(sys.argv[0]):
      try:
        os.startfile(sys.argv[0])
      except Exception as e:
        input(f"Couldnt start for some reason... actually heres the reason lol: {e}\n[Enter to quit]")
    else:
      print("but youre testing!!")
if FoR==True:
  inti=''
  for i in inventory:
    inti+=i
    if i!=inventory[-1]:
      inti+=','
  if len(inventory)==0:
    inti+='None'
  inti+='\n'
  for i in colname.keys():
    if itemdict[i]=='Yes':
      inti+=moddict[i]+colname[i]+R+'\n'
  print("\nInventory: "+inti)
  quit(str(TIPO2)+" seconds passed before you ended your game")
elif raftper or TRUEYAYA or PLANED or mined or literallyvented or eastering or theairfr: #eastering/theairfr easter
  time.sleep(1 if TRUEYAYA else 0)
  quit('It took you '+str(TIPO2)+" seconds\n"+("Raft Ending" if raftper else "The Absolute Truth. You are cool ffrfrffrfrfrfrfrfrfrff!!!!!!!!!!!" if TRUEYAYA and "Unspoken Relic" in inventory else "The Truth" if TRUEYAYA else "The Plane Ending" if PLANED else "The Lab Ending" if mined else "The Cart Ending" if literallyvented else "\033[38;5;4mThe Temple Ending" if eastering else "\n\033[38;5;4mThe Air Fryer"))
elif smallvarget("youdid_nt"): #easter
  quit('.......')
elif smallvarget("didnt_listen"):#easter
  achieve('Horrible Game')
  quit('Death.')
elif Day==6:
  quit(":)")
elif '╳' not in mazeq:
  quit('You died to him.')
else: #erase
  time.sleep(13)
  sys.exit('Return.')