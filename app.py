#!venv/bin/python3



#--------------------------------Settings-------------------------------|
WIDTH=      1100        # Width of the window                           | 
HEIGHT=     450         # Height of the window                          |
WKEY=       'white'     # Color of the deactivated "white" keys         |
WKEYACTIVE= 'lightgrey' # Color of the activated "white" keys           |
BKEY=       'black'     # Color of the deactivated "black" keys         |
BKEYACTIVE= 'darkgray'  # Color of the activated "black" keys           |
#-----------------------------------------------------------------------|






import tkinter as tk
from src import playsound as ps
import time

# A dictionary of all the 17.5 TET notes on the first and the second nonus
notes = {'Fis1': 369.994, 'G1': 384.942, 'Gis1': 400.495, 'Pes1': 416.677, 'P1': 433.512, 'Pis1': 451.027, 'I1': 469.25, 'Q1': 488.21, 'Qis1': 507.935, 'Ås1': 528.457, 'Å1': 549.808, 'Åis1': 572.023, 'L1': 595.134, 'Mes1': 619.18, 'M1': 644.196, 'Mis1': 670.224, 'Fes1': 697.303, 'Lauta1': 725.477, 'Fis2': 739.988, 'G2': 769.884, 'Gis2': 800.99, 'Pes2': 833.354, 'P2': 867.024, 'Pis2': 902.054, 'I2': 938.5, 'Q2': 976.42, 'Qis2': 1015.87, 'Ås2': 1056.914, 'Å2': 1099.616, 'Åis2': 1144.046, 'L2': 1190.268, 'Mes2': 1238.36, 'M2': 1288.392, 'Mis2': 1340.448, 'Fes2': 1394.606, 'Lauta2': 1450.954, 'Fis3': 1479.976, "G3": 1539.768}

# Settings of the keys
Whites = ['Fis1','Gis1','Pes1','Pis1','Qis1','Ås1','Åis1','Mes1','Mis1','Fes1','Fis2','Gis2','Pes2','Pis2','Qis2','Ås2','Åis2','Mes2','Mis2','Fes2','Fis3']
Blacks = ['G1','P1','I1','Q1','Å1','L1','M1','Lauta1','G2','P2','I2','Q2','Å2','L2','M2','Lauta2','G3']
BlackPos = [0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,18,20]
BlackSticky = ['NE','NE','NE','NW','NE','NE','NE','NE','NE','NE','NE','NW','NE','NE','NE','NE','NE']

Display = ['G1','P1','I1','Q1','Å1','L1','M1','-1','G2','P2','I2','Q2','Å2','L2','M2','-2','G3']

Version = "alpha-0.5"

CurrentlyPlaying = dict()

def play(note):
    global CurrentlyPlaying
    note.strip('.!')[1]
    # print(f'DEBUG: Playing {note}...')
    exec(f'playing_{note} = ps.Sound(notes["{note}"])')
    exec(f"CurrentlyPlaying[note] = playing_{note}")
    exec(f'playing_{note}.start()')
def stop(note):
    global CurrentlyPlaying
    note.strip('.!')[1]
    CurrentlyPlayingNote = CurrentlyPlaying[note]
    # print(f'DEBUG: Stopping {note}...')
    CurrentlyPlayingNote.stop()

def main():
    print(f'Pieno {Version}')

    root = tk.Tk()

    root.title(f'Pieno {Version}')
    root.iconphoto(False, tk.PhotoImage(file='resources/icon.png'))

    root.geometry(f'{WIDTH}x{HEIGHT}')
    root.resizable(False,False)

    j = 0
    for i in Whites:
        root.grid_columnconfigure(index=j,weight=1)
        
        exec(f'{i} = tk.Button(root,height=20,width=10,\
        background=WKEY,activebackground=WKEYACTIVE,\
        text="{i}", fg="black", anchor="s")')                # Creating the button

        exec(f'{i}.bind("<ButtonPress-1>",\
        lambda gulag:play("{i}"))')                        # Binding the start function
        exec(f'{i}.bind("<ButtonRelease-1>",\
        lambda gulag:stop("{i}"))')                        # Binding the stop function
        
        exec(f'{i}.grid(column={j}, row=0)')               # Mapping the button to the grid
        j+=1

    j = 0
    for i in Blacks:
        exec(f'{i} = tk.Button(root,height=15,width=1,\
        background=BKEY,activebackground=BKEYACTIVE, \
        text="{Display[j]}", fg="white", anchor="s")')     # Creating the button itself

        exec(f'{i}.bind("<ButtonPress-1>",\
        lambda gulag:play("{i}"))')                        # Binding the start function
        exec(f'{i}.bind("<ButtonRelease-1>",\
        lambda gulag:stop("{i}"))')                        # Binding the stop function

        exec(f'{i}.grid(column={BlackPos[j]}, \
        row=0,sticky="{BlackSticky[j]}")')                 # Mapping the button to the grid
        j+=1
    # Lauta1.bind("<ButtonPress-1>",lambda note={i}:play(note))
    title = tk.Label(text='Pieno', font=('monospace',20),fg="darkgray")
    title.grid(row=1,column=0,columnspan=20,pady=10)

    title_label = tk.Label(text='The first ever 17,5 TNSET piano made by Nikolas "Koodarimpi" Lehto in 2023.', font=('monospace'),fg="darkgray")    
    title_label.grid(row=4,column=0,columnspan=20)


    root.mainloop()

if __name__ == "__main__":
    main()