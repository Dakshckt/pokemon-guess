import tkinter as tk
import tkinter.messagebox
import tkinter.ttk
from tkinter.ttk import *
from PIL import Image , ImageTk
from data import select_pokemon

"""
    CAN DISPLAY THE NAME OF THE POKEMON AS IT IS STORED IN POKEMON VARIABLE IN THE PROGRAM
"""

base = tk.Tk()
base.geometry("350x500")
base.title("Who's This Pokemon")
base.configure(bg="#CDEAF4")

pokemon = file = "select_pokemon()"
cl_image = ""
tk_image = ""
guess = ""

def clear():
    for widget in base.winfo_children():
        widget.destroy()

def check():
    color_pokemon()
    pokemon_color = Label(base , image=cl_image)
    pokemon_color.place(x=50 , y=20)

    value = guess.get()

    if pokemon.lower() == value.lower():
        output = Label(base , text=f"Your are Right It's {pokemon}..!!!")
    else:
        output = Label(base , text=f"Your are Wrong Answer is {pokemon}")
    output.place(x=83 , y=420)

    btn = Button(base , text="Restart" , command=main)
    btn.place(x=130 , y=380)

def color_pokemon():
    global cl_image
    image = Image.open(file)
    image = image.resize((250 , 250))
    cl_image = ImageTk.PhotoImage(image)

def black_pokemon():
    global tk_image
    img = Image.open(file).convert("RGBA")  
    img = img.resize((250 , 250))
    bg = Image.new("RGBA", img.size, (255, 255, 255, 0)) 
    black_image = Image.new("RGBA", img.size, (0, 0, 0, 255))  
    silhouette = Image.composite(black_image, bg, img.split()[3]) 
    tk_image = ImageTk.PhotoImage(silhouette)

def main():
    global guess , pokemon , file

    pokemon , file = select_pokemon()

    clear()
    black_pokemon()

    pokemon_black = Label(base , image=tk_image)
    pokemon_black.place(x=50 , y=20)

    guess = Entry(base ,width=30)
    guess.place(x=80 , y=320)

    check_button = Button(base , text="Submit" , command=check)
    check_button.place(x=130 , y = 350)

    

if __name__ == "__main__":
    # tkinter.messagebox.showinfo("Information","Not advance thus recheck Spellings") NOT WORKING
    main()



base.mainloop()