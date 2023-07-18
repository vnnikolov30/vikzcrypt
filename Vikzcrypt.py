from tkinter import *
from tkinter import messagebox

import base64
import pygame
import time

PASSWORD = "123"



# MUSIC AND SOUNDS
pygame.mixer.init()
decrypt_sound = pygame.mixer.Sound("resources/decrypt1.wav")
decrypt_sound.set_volume(0.6)
encrypt_sound = pygame.mixer.Sound("resources/encrypt1.wav")
encrypt_sound.set_volume(1.0)
reset_sound = pygame.mixer.Sound("resources/reset.wav")
reset_sound.set_volume(0.5)
pygame.mixer.music.load("resources/theme.mp3")
pygame.mixer.music.play(-1)
secret_sound = pygame.mixer.Sound("resources/secret_sound.wav")
secret_sound.set_volume(0.3)

def encrypt():
    stop = None
    text = text1.get(1.0,"end-1c")
    if len(text) == 0:
        messagebox.showerror("no message", "No message found! ☹")
        stop = True
    else:
        stop = False

    password = pwd.get()
    if not stop:
        if password == PASSWORD:
            encrypt_sound.play()
            screen1 = Toplevel(screen)
            screen1.title("encryption")
            screen1.geometry("400x200")
            screen1.configure(bg="#000000")

            message = text1.get(1.0, END)
            encode_message = message.encode("ascii")
            base64_bytes = base64.b64encode(encode_message)
            encrypt = base64_bytes.decode("ascii")
            Label(screen1, text="DONE ☭", font="arial", fg="white", bg="#000000").place(x=10, y=0)
            text2 = Text(screen1, font="Helvetica 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(END, encrypt)
            text1.delete(1.0, END)
        elif password == "":
            messagebox.showerror("missing password", "You forgot the password ☹")
        elif password != PASSWORD:
            messagebox.showerror("wrong password", "Invalid Password ☹")


def decrypt():
    stop = None
    text = text1.get(1.0,"end-1c")
    if len(text) == 0:
        messagebox.showerror("no message", "No message found! ☹")
        stop = True
    else:
        stop = False

    password = pwd.get()
    if not stop:
        if password == PASSWORD:
            decrypt_sound.play()
            screen2 = Toplevel(screen)
            screen2.title("decryption")
            screen2.geometry("400x200")
            screen2.configure(bg="#00bd56")

            message = text1.get(1.0, END)
            decode_message = message.encode("ascii")
            base64_bytes = base64.b64decode(decode_message)
            decrypt = base64_bytes.decode("ascii")

            Label(screen2, text="DONE ☭", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
            text2 = Text(screen2, font="Helvetica 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text1.delete(1.0, END)

            text2.insert(END, decrypt)
        elif password == "":
            messagebox.showerror("missing password", "You forgot the password ☹")
        elif password != PASSWORD:
            messagebox.showerror("wrong passowrd", "Invalid Password ☹")


def main_screen():
    global screen
    global pwd
    global text1
    reset_counter = 0
    screen = Tk()
    screen.geometry("380x398")
    screen.resizable(width=False, height=False)
    # set icon
    img = PhotoImage(file="resources/icon.png")
    screen.iconphoto(False, img)

    # set window bg

    bg = PhotoImage(file="resources/image.png")
    my_label = Label(screen, image=bg)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)


    screen.title("Vikzcrypt")

    def reset():
        nonlocal reset_counter
        reset_counter += 1
        print(reset_counter)
        reset_sound.play()
        pwd.set("")
        text1.delete(1.0, "end")
        if reset_counter == 10:
            reset_secret()
    
    def reset_secret():
        pygame.mixer.music.stop()
        secret_sound.play()
        time.sleep(4)
        pygame.mixer.music.play(-1)

        easter_egg_window = Toplevel(screen) 
        easter_egg_window.title("THE GLORIOUS LEADER HAS GRACED YOU WITH HIS PRESENCE")
        # easter_egg_window.geometry("400x200")
        image_path = "resources/Untitled.png"
        image = PhotoImage(file=image_path)

        image_label = Label(easter_egg_window, image=image)
        image_label.pack()
        image_label.image = image
        nonlocal reset_counter 
        reset_counter = 0
    # TEXT FIELD
    Label(text="👽 Gimmie Text 👽 ", bg="white", relief=RIDGE, bd=5, font=("helvetica", 13)).place(x=10, y=10)

    # TEXT INPUT
    text1 = Text(font="Arial 10", bg="white", relief=RIDGE, bd=10)
    text1.place(x=10, y=50, width=355, height=100)
    
    

    # PASS FIELD
    Label(text="🖖 Gimmie Pass 🖖 ", fg="black", relief=RIDGE, bd=5, font=("helvetica", 13)).place(x=10, y=155)
    # PASS INPUT
    pwd = StringVar()
    Entry(textvariable=pwd, width=20, relief=RIDGE, bd=5, font=("arial", 17), show="☭").place(x=10, y=195)

    Button(text="ENCRYPT", height="2", width=23, bg="#000000", fg="white", bd=5, relief=RAISED,
           command=encrypt, ).place(x=10, y=250)

    Button(text="DECRYPT", height="2", width=23, bg="#FFFFFF", fg="black", bd=5, relief=RAISED,
           command=decrypt, ).place(x=200, y=250)
    
    Button(text="RESET", height="2", width=49, bg="#1089ff", fg="white", bd=10, relief=RAISED, command=reset).place( x=10,y=300)
    screen.mainloop()


main_screen()
