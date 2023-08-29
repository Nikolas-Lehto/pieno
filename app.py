import tkinter as tk

WIDTH=      1100
HEIGHT=     450
WKEY=       'white'
WKEYACTIVE= 'lightgrey'
BKEY=       'black'
BKEYACTIVE= 'darkgray'

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
        exec(f'def {i}():\n    print("{i} has been played")')
        exec(f'{i} = tk.Button(root,height=20,width=10,background=WKEY,activebackground=WKEYACTIVE,command={i})')
        exec(f'{i}.grid(column={j}, row=0)')
        j+=1
    j = 0
    for i in Blacks:
        exec(f'def {i}():\n  print("{i} has been played")')
        exec(f'{i} = tk.Button(root,height=15,width=2,background=BKEY,activebackground=BKEYACTIVE,command={i})')
        exec(f'{i}.grid(column={BlackPos[j]},row=0,sticky="{BlackSticky[j]}")')
        j+=1
    title_label = tk.Label(text='\nThe first ever 17,5 TET piano made by Nikolas "Koodarimpi" Lehto in 2023.', font=('monospace'))
    title_label.grid(row=4,column=0,columnspan=10)
    root.mainloop()

if __name__ == "__main__":
    main()