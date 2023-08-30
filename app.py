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
import playsound

# A dictionary of all the 17.5 TET notes on the first and the second nonus
notes = {'Fis1': 369.994, 'G1': 384.942, 'Gis1': 400.495, 'Pes1': 416.677, 'P1': 433.512, 'Pis1': 451.027, 'I1': 469.25, 'Q1': 488.21, 'Qis1': 507.935, 'Ås1': 528.457, 'Å1': 549.808, 'Åis1': 572.023, 'L1': 595.134, 'Mes1': 619.18, 'M1': 644.196, 'Mis1': 670.224, 'Fes1': 697.303, '–1': 725.477, 'Fis2': 739.988, 'G2': 769.884, 'Gis2': 800.99, 'Pes2': 833.354, 'P2': 867.024, 'Pis2': 902.054, 'I2': 938.5, 'Q2': 976.42, 'Qis2': 1015.87, 'Ås2': 1056.914, 'Å2': 1099.616, 'Åis2': 1144.046, 'L2': 1190.268, 'Mes2': 1238.36, 'M2': 1288.392, 'Mis2': 1340.448, 'Fes2': 1394.606, '–2': 1450.954, 'Fis3': 1479.976}

# TODO: Add the rest of the keys

# Settings of the keys
Whites = ['Fis','Gis','Pes','Pis','Qis','Ås','Åis','Mes','Mis','Fes']
Blacks = ['G','P','I','Q','Å','L','M','Lauta']
BlackPos = [0,2,3,4,5,6,7,9]
BlackSticky = ['NE','NE','NE','NW','NE','NE','NE','NE',]

def main():
    root = tk.Tk()
    root.geometry(f'{WIDTH}x{HEIGHT}')
    root.resizable(False,False)

    j = 0
    for i in Whites:
        root.grid_columnconfigure(index=j,weight=1)
        exec(f'{i} = playsound.Sound({notes[i]})')          # Creating a sound for every note
        exec(f'def {i}_start():\n  {i}.start()')            # A function to start the created sound
        exec(f'def {i}_stop():\n  {i}.stop()')              # A function to stop that sound
        exec(f'{i} = tk.Button(root,height=20,width=10,\
        background=WKEY,activebackground=WKEYACTIVE')       # Creating the button itself
        exec(f'{i}.bind("<ButtonPress-1>,{i}_start")')      # Binding the start function
        exec(f'{i}.bind("<ButtonRelease-1>,{i}_stop")')     # Binding the stop function
        exec(f'{i}.grid(column={j}, row=0)')                # Mapping the button to the grid
        j+=1

    j = 0
    for i in Blacks:
        exec(f'def {i}_start():\n  {i}.start()')            # Creating a sound for every note
        exec(f'def {i}_stop():\n  {i}.stop()')              # A function to start the created sound
        exec(f'{i} = playsound.Sound({notes[i]})')          # A function to stop that sound
        exec(f'{i} = tk.Button(root,height=15,width=2,\
        background=BKEY,activebackground=BKEYACTIVE')       # Creating the button itself
        exec(f'{i}.bind("<ButtonPress-1>,{i}_start")')      # Binding the start function
        exec(f'{i}.bind("<ButtonRelease-1>,{i}_stop")')     # Binding the stop function
        exec(f'{i}.grid(column={BlackPos[j]}, \
        row=0,sticky="{BlackSticky[j]}")')                  # Mapping the button to the grid
        j+=1


    title = tk.Label(text='"Pieno"', font=('monospace',20))
    title.grid(row=1,column=0,columnspan=10,pady=10)

    title_label = tk.Label(text='The first ever 17,5 TET piano made by Nikolas "Koodarimpi" Lehto in 2023.', font=('monospace'))    
    title_label.grid(row=4,column=0,columnspan=10)


    root.mainloop()

if __name__ == "__main__":
    main()