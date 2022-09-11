import os.path
import tkinter.filedialog
from tkinter import *
from tkinter.messagebox import showinfo

import os
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, END)

def openFile():
    global file
    file = tkinter.filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Ducuments", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()
def saveFile():
    global file
    if file == None:
        file = tkinter.filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")])
        if file == "":
            file = None

        else:
            #Save file as
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save file as
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()
def quitApp():
    root.destroy()

def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad by Chandan Vishwakarma.")

def notepad():
    pass

if __name__ == '__main__':

    root = Tk()
    root.geometry("644x550")
    root.title("Untitled - Notepad with CWH")
    # Add text area
    textarea = Text(root)
    textarea.pack(fill=BOTH,expand=True)
    file = None

    #create Menubar

    menubar = Menu(root)
    #$$$$$$$$$ File Menu starts $$$$$$$$$$
    filemenu = Menu(menubar, tearoff=0)

    #to open new file
    filemenu.add_command(label="New", command=newFile)
    #to open existing file
    filemenu.add_command(label="Open", command=openFile)
    #To save current file
    filemenu.add_command(label="Save", command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=quitApp)
    menubar.add_cascade(label="File", menu=filemenu)
    #$$$$$$$$$$ File Menu Ends $$$$$$$$$$$

     #$$$$$$$$$$ Edit Menu starts $$$$$$$$$$$
    editMenu = Menu(menubar, tearoff=0)
    #to give a feature of cut
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)

    menubar.add_cascade(label="Edit",menu=editMenu)
    #$$$$$$$$$$ Edit Menu Ends $$$$$$$$$$$

    #help menu starts
    helpMenu = Menu(menubar, tearoff=0)
    helpMenu.add_command(label="About Notepad", command=about)
    menubar.add_cascade(label="Help",menu=helpMenu)


    #help menu ends

    
    root.config(menu=menubar)

    #Adding scrollbar
    scrolbar= Scrollbar(textarea)
    scrolbar.pack(side=RIGHT, fill=Y)
    scrolbar.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrolbar.set)



    root.mainloop()
