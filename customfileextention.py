import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
# from PIL import Image, ImageTk

filepath = ""

def browse():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a text file",
                                          filetypes=(("Text Files", "*.txt*"), ("All Files", "*.*"))
                                          )
    extention = os.path.splitext(filename)[1].lower()
    if extention != ".txt":
        popuperror()
    else:
        outputtext.configure(text=filename)
        filepath = filename

def preview():
    with open(filepath, "r") as file:
        content = file.read()
        ###

def popuperror():
    popup = tk.Tk()
    popupscreenwidth = popup.winfo_screenwidth() # sets popup in center of screen
    popupscreenheight = popup.winfo_screenheight()
    popupcenterx = int(popupscreenwidth/2 - 100)
    popupcentery = int(popupscreenheight/2 - 40)
    popup.geometry(f"{200}x{80}+{popupcenterx}+{popupcentery}")
    popup['bg'] = "darkred"
    popup.attributes("-topmost", 1)
    popup.overrideredirect(True)
    tk.Label(popup, 
             text="Unacceptable file type.\nOnly use \".txt\" files.",
             font=("Comic Sans MS", 12),
             bg="darkred",
             padx="20",
             pady="20",
             fg="white",
             ).pack()
    popup.after(1000, popup.destroy)
    popup.mainloop()

invalidfileformats = ("jpg", "png", "gif", "bmp", "tiff", "psd", "mp4", "mkv", "avi", "mov", "mpg", "vob", "mp3", "aac", "wav", "flac", "ogg", "mka", "wma",
                      "m4a", "pdf", "doc", "xls", "ppt", "docx", "odt", "zip", "rar", "7z", "tar", "iso", "mdb", "accde", "frm", "sqlite", "exe", "dll", 
                      "so", "class", "jpeg")


root = tk.Tk()
root.title('Custom File Extentions!')
windowwidth = 700
windowheight = 400
root['bg'] = "lightgreen"
root.resizable(False, False)
root.attributes("-topmost", 1)
#img = Image.open("icon.png") # tried to make custom icon, try later
#photo = ImageTk.PhotoImage(img)
#root.wm_iconphoto(True, photo)

customext = tk.StringVar() # activates variable "customext" in entry field

screenwidth = root.winfo_screenwidth() # places window in center of screen
screenheight = root.winfo_screenheight()
centerx = int(screenwidth/2 - windowwidth/2)
centery = int(screenheight/2 - windowheight/2)
root.geometry(f"{windowwidth}x{windowheight}+{centerx}+{centery}")

# stuff appearing on screen ↓↓↓

tk.Label(root,
         text="Create your own custom\nfile extentions!", 
         bg="lightgreen", 
         padx="20",
         pady="10",
         font=("Comic Sans MS", 20),
         justify="left",
         ).pack(anchor="w")
tk.Label(root, 
         text="Select your text file with the button below",
         bg="lightgreen",
         padx="30",
         pady="10",
         font=("Comic Sans MS", 10)
         ).pack(anchor="w")
tk.Button(root,
          text="Select a text file...",
          activebackground="darkgreen",
          activeforeground="white",
          font=("Comic Sans MS", 15),
          bg="green",
          padx="20",
          pady="15",
          relief="flat",
          overrelief="raised",
          command=browse,
          ).place(x=40, y=160)
outputtext = tk.Label(root,
                      text="",
                      bg="lightgreen",
                      font=("Comic Sans MS", 7),
                      )
outputtext.place(x=30, y=250)
tk.Label(root,
         text="Enter your custom file format here:",
         bg="lightgreen",
         font=("Comic Sans MS", 10),
         ).place(x=30, y=270)
tk.Label(root,
         text=".",
         bg="lightgreen",
         font=("Comic Sans MS", 9)
         ).place(x=50, y=295)
tk.Entry(root,
         textvariable=customext,
         justify="left",
         ).place(x=60, y=295)
tk.Button(root,
          text="Convert",
          bg="green",
          font=("Comic Sans MS", 15),
          activebackground="darkgreen",
          activeforeground="white",
          padx="5",
          pady="5",
          relief="flat",
          overrelief="raised",
          ).place(x=30, y=325)
tk.Button(root,
          text="Preview text",
          command=preview,
          bg="green",
          font=("Comic Sans MS", 15),
          activebackground="darkgreen",
          activeforeground="white",
          padx="5",
          pady="5",
          relief="flat",
          overrelief="raised",
          ).place(x=140, y=325)
tk.LabelFrame(root,
              text="",
              bg="cyan",
              width="330",
              height="360",
              ).place(x=350, y=20)


root.mainloop()
