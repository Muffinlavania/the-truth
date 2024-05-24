# The Truth
- A game I have been working on for years now...
- Entirely in the console, pretty bad code (getting better every update!!!) but actually almost fun
- You play as a box, and explore your new home, an island that wont let you leave...
(unless you find the real ending)

Has:
- 5 different endings
- Not a single use of pygame even though this would probably be sick in it
- A kinda huge map, with darkness and stuff
- NPCS, Invemtory/Crafting, Items, interactables like the powerplant etc.
- An easter event (yes i added events, theres definitely not reminants of other ones in there...)
- Bosses...

This is mainly so I remember it exists, the code for Windows/Mac/Other stuff is here, as well as the already made exe for windows (idk how to make it for other OS)

# To play on mac (or windows if you want to compile yourself)
## If you want music (as of right now doesnt work without it!!): 
- download [this folder of songs](https://drive.google.com/drive/folders/1bpNWlxozLGk5Ks6vH8DcmFtmvU1f9MPO) (MAKE SURE ITS THE FOLDER, Truth)
- put this folder in the same path as the next step,
  
## To set up the exe from the source code you will need: (YOU NEEEEEEEEEEEEEEEEEEED THE MUSIC RN!!!)
- [Python/pip](https://www.python.org/downloads/) (pip3 for mac/linux/whatever)
- run `pip/pip3 install pyinstaller` in your console
- (make sure you are in the current path as the source code before next step, probably downloads)
### WINDOWS
- **if you do have the music**: run `pyinstaller -F --add-data "Truth/*.wav;Truth/" --add-data "Truth/*.mp3;Truth/" TheTruth.py`
### Mac/other stuff
- **if you do have the music**: run `pyinstaller -F --add-data "Truth/*.wav:Truth/" --add-data "Truth/*.mp3:Truth/" TheTruth.py`
Screenshots from the game:

![image](https://user-images.githubusercontent.com/93288617/221372251-66f4fa82-1453-4361-9f32-89a4d3c5c90c.png) ![image](https://user-images.githubusercontent.com/93288617/221372265-7713e076-4fdb-48ba-803b-974c85897f46.png) ![image](https://user-images.githubusercontent.com/93288617/221372310-d5366a0d-4675-4c8a-a352-f6f647013b5e.png) ![image](https://user-images.githubusercontent.com/93288617/221372339-6ef899ea-b3ed-4dd5-8881-401fbb664143.png) ![image](https://user-images.githubusercontent.com/93288617/221372369-7328c5c5-74c9-48bf-8a6c-9044c5e7c60e.png) ![image](https://user-images.githubusercontent.com/93288617/221372425-41d16eb9-ba6f-47b0-af98-b1b332089ddc.png)


### (*K*eep *Y*ourself *S*afe boss)
![image](https://user-images.githubusercontent.com/93288617/221372797-a8a89a5b-8b2c-4838-90af-41261f9549c0.png)


## Can you find the truth?
![image](https://user-images.githubusercontent.com/93288617/221373135-e510a29b-e841-4a3b-9eb2-1f62136ae665.png)

