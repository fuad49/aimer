import smallS as SmallS
import Mytts as mytts
import Save as saveit
import Translate as translate
import tkinter as tk
import sys
import os


from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,filedialog

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

aText = ''
url=''
output_path="C:/Users/"

def PerfromSummarization():
   global aText
   print("Here mate")
   myUrl = url_entry.get()
   aText = SmallS.ReturnArticle(myUrl)
   canvas.itemconfig(tagOrId=sText, text=aText)
   canvas.itemconfig(tagOrId=tText, text=SmallS.ReturnTitle())


def PlaySoundTTS():
    mytts.PlayNarration(aText)

def SaveFile():
    finalText = f'Title :: {SmallS.ReturnTitle()}\n\n\n{aText}'
    if name_entry.get() == "":
        saveit.saveit(SmallS.ReturnTitle() + lang_entry.get(),finalText,path_entry.get())
    elif name_entry.get() != "":
        saveit.saveit(name_entry.get(),finalText,path_entry.get())


def TranslateIt():
   global aText
    #translate.TranslateIt(aText, 'bn')
   trSText = translate.TranslateIt(aText, lang_entry.get())
   aText = trSText
   trtText = translate.TranslateIt(SmallS.ReturnTitle(), lang_entry.get())
   canvas.itemconfig(tagOrId=sText, text=trSText)
   canvas.itemconfig(tagOrId=tText, text=trtText)

def select_path():
    global output_path

    output_path = filedialog.askdirectory(initialdir=r'C:/Users/')
    path_entry.delete(0, tk.END)
    path_entry.insert(0, output_path)



ASSETS_PATH = resource_path(Path(__file__).parent.resolve() / "assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def fade_in(window, alpha):
    if alpha < 1:
        window.attributes('-alpha', alpha)
        alpha += 0.01  
        window.after(10, fade_in, window, alpha)  
    else:
        window.attributes('-alpha', 1)

def fade_out(window, alpha):
    if alpha > 0:
        window.attributes('-alpha', alpha)
        alpha -= 0.01
        window.after(10, fade_out, window, alpha)
    else:
        window.attributes('-alpha', 0)
        window.destroy()
def destroySplash():
    fade_out(splash_root,1)

splash_root = Tk()
splash_root.geometry("250x250+0+0")
splash_root.attributes('-alpha', 0)
screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

x = int((screen_width - splash_root.winfo_reqwidth()) / 2)
y = int((screen_height - splash_root.winfo_reqheight()) / 2)

splash_root.geometry(f"+{x}+{y}")
splash_root.overrideredirect(True)
scanvas = Canvas(
    splash_root,
    bg = "#FFFFFF",
    height = 250,
    width = 250,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

scanvas.place(x = 0, y = 0)
sImageBG = PhotoImage(file=resource_path("assets\\Slogo.png"))
BGSIMAGe = scanvas.create_image(
    125.0,
    125.0,
    image=sImageBG
)
fade_in(splash_root, 0)

splash_root.after(3000,destroySplash)
splash_root.mainloop()

window = Tk()

window.geometry("1200x650")
window.title("@imer")
window.iconbitmap(resource_path("assets\\logo.ico"))
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 650,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=resource_path("assets\\image_1.png"))
image_1 = canvas.create_image(
    600.0,
    337.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    0.0,
    1200.0,
    34.0,
    fill="#032155",
    outline="")

canvas.create_text(
    21.0,
    7.0,
    anchor="nw",
    text="@imer",
    fill="#FFFFFF",
    font=("Inter ExtraBold", 17 * -1)
)

image_image_2 = PhotoImage(file=resource_path("assets\\image_2.png"))
image_2 = canvas.create_image(
    81.0,
    76.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(file=resource_path("assets\\entry_1.png"))
entry_bg_1 = canvas.create_image(
    654.8878784179688,
    76.0,
    image=entry_image_1
)
url_entry = Entry(
    bd=0,
    bg="#46B5CD",
    fg="#000716",
    highlightthickness=0
)
url_entry.place(
    x=142.0,
    y=57.0,
    width=1025.7757568359375,
    height=36.0
)

image_image_3 = PhotoImage(file=resource_path("assets\\image_3.png"))
image_3 = canvas.create_image(
    603.0,
    332.0,
    image=image_image_3
)

image_image_4 = PhotoImage(file=resource_path("assets\\image_4.png"))
image_4 = canvas.create_image(
    603.0,
    366.0,
    image=image_image_4
)

image_image_5 = PhotoImage(file=resource_path("assets\\image_5.png"))
image_5 = canvas.create_image(
    603.0,
    209.0,
    image=image_image_5
)

entry_image_2 = PhotoImage(file=resource_path("assets\\entry_2.png"))
entry_bg_2 = canvas.create_image(
    260.0,
    577.0,
    image=entry_image_2
)
name_entry = Entry(
    bd=0,
    bg="#689BB2",
    fg="#000716",
    highlightthickness=0
)
name_entry.place(
    x=36.0,
    y=561.0,
    width=448.0,
    height=30.0
)

entry_image_3 = PhotoImage(file=resource_path("assets\\entry_3.png"))
entry_bg_3 = canvas.create_image(
    260.0,
    539.0,
    image=entry_image_3
)
path_entry = Entry(
    bd=0,
    bg="#689BB2",
    fg="#000716",
    highlightthickness=0
)
path_entry.place(
    x=36.0,
    y=523.0,
    width=448.0,
    height=30.0
)

entry_image_4 = PhotoImage(file=resource_path("assets\\entry_4.png"))
entry_bg_4 = canvas.create_image(
    1109.5,
    530.0,
    image=entry_image_4
)
lang_entry = Entry(
    bd=0,
    bg="#689BB2",
    fg="#000716",
    highlightthickness=0
)
lang_entry.place(
    x=1064.0,
    y=516.0,
    width=91.0,
    height=26.0
)

canvas.create_text(
    63.0,
    169.0,
    anchor="nw",
    text="Title",
    fill="#064C8A",
    font=("Inter ExtraBold", 20 * -1)
)

canvas.create_text(
    63.0,
    225.0,
    anchor="nw",
    text="summary",
    fill="#054988",
    font=("Inter ExtraBold", 20 * -1)
)

sText=canvas.create_text(
    68.0,
    260.0,
    width=1086,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Inter Medium", 13 * -1)
)

SummaryBTN_image = PhotoImage(file=resource_path("assets\\button_1.png"))
SummaryBTN = Button(
    image=SummaryBTN_image,
    borderwidth=0,
    highlightthickness=0,
    command=PerfromSummarization,
    relief="flat"
)
SummaryBTN.place(
    x=1013.9999389648438,
    y=113.0,
    width=158.00006103515625,
    height=31.0
)

saveBTN_Image = PhotoImage(file=resource_path("assets\\button_2.png"))
saveBTN = Button(
    image=saveBTN_Image,
    borderwidth=0,
    highlightthickness=0,
    command=SaveFile,
    relief="flat"
)
saveBTN.place(
    x=412.0,
    y=599.0,
    width=79.0,
    height=20.0
)

ReadAloudBTM_Image = PhotoImage(file=resource_path("assets\\button_3.png"))
readAloudBTN = Button(
    image=ReadAloudBTM_Image,
    borderwidth=0,
    highlightthickness=0,
    command=PlaySoundTTS,
    relief="flat"
)
readAloudBTN.place(
    x=1050.0,
    y=588.0,
    width=121.0,
    height=25.0
)

translateBTN_image = PhotoImage(file=resource_path("assets\\button_4.png"))
translateBTN = Button(
    image=translateBTN_image,
    borderwidth=0,
    highlightthickness=0,
    command=TranslateIt,
    relief="flat"
)
translateBTN.place(
    x=1050.0,
    y=552.0,
    width=121.0,
    height=28.0
)

tText=canvas.create_text(
    63.0,
    198.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Inter Medium", 15 * -1)
)

pathBTN_Image = PhotoImage(file=resource_path("assets\\button_5.png"))
pathBTN = Button(
    image=pathBTN_Image,
    borderwidth=0,
    highlightthickness=0,
    command=select_path,
    relief="flat"
)
pathBTN.place(
    x=494.0,
    y=520.0,
    width=37.0,
    height=37.0
)
window.resizable(False, False)
window.mainloop()
