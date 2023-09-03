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
notes = {'Fis0': 184.997, 'G0': 192.471, 'Gis0': 200.2475, 'Pes0': 208.3385, 'P0': 216.756, 'Pis0': 225.5135, 'I0': 234.625, 'Q0': 244.105, 'Qis0': 253.9675, 'Ås0': 264.2285, 'Å0': 274.904, 'Åis0': 286.0115, 'L0': 297.567, 'Mes0': 309.59, 'M0': 322.098, 'Mis0': 335.112, 'Fes0': 348.6515, 'Lauta0': 362.7385, 'Fis1': 369.994, 'G1': 384.942, 'Gis1': 400.495, 'Pes1': 416.677, 'P1': 433.512, 'Pis1': 451.027, 'I1': 469.25, 'Q1': 488.21, 'Qis1': 507.935, 'Ås1': 528.457, 'Å1': 549.808, 'Åis1': 572.023, 'L1': 595.134, 'Mes1': 619.18, 'M1': 644.196, 'Mis1': 670.224, 'Fes1': 697.303, 'Lauta1': 725.477, 'Fis2': 739.988}

# Settings of the keys
Whites = ['Fis0', 'Gis0', 'Pes0', 'Pis0', 'Qis0', 'Ås0', 'Åis0', 'Mes0', 'Mis0', 'Fes0', 'Fis1', 'Gis1', 'Pes1', 'Pis1', 'Qis1', 'Ås1', 'Åis1', 'Mes1', 'Mis1', 'Fes1', 'Fis2']
WhitesDisplay = ['Fis', 'Gis', 'Pes', 'Pis', 'Qis', 'Ås', 'Åis', 'Mes', 'Mis', 'Fes', 'Fis', 'Gis', 'Pes', 'Pis', 'Qis', 'Ås', 'Åis', 'Mes', 'Mis', 'Fes', 'Fis']

Blacks = ['G0', 'P0', 'I0', 'Q0', 'Å0', 'L0', 'M0', 'Lauta0', 'G1', 'P1', 'I1', 'Q1', 'Å1', 'L1', 'M1', 'Lauta1', 'G2']
BlackPos = [0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,18,20]
BlackSticky = ['NE','NE','NE','NW','NE','NE','NE','NE','NE','NE','NE','NW','NE','NE','NE','NE','NE']
BlacksDisplay=['G', 'P', 'I', 'Q', 'Å', 'L', 'M', '-', 'G', 'P', 'I', 'Q', 'Å', 'L', 'M', '-', 'G']

Version = "1.1"

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
    # root.iconphoto(False, tk.PhotoImage(file='resources/icon.png'))

    root.geometry(f'{WIDTH}x{HEIGHT}')
    root.resizable(False,False)

    j = 0
    for i in Whites:
        root.grid_columnconfigure(index=j,weight=1)
        
        exec(f'{i} = tk.Button(root,height=20,width=10,\
        background=WKEY,activebackground=WKEYACTIVE,\
        text="{WhitesDisplay[j]}", fg="black", anchor="s")')                # Creating the button

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
        text="{BlacksDisplay[j]}", fg="white", anchor="s")')     # Creating the button itself

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