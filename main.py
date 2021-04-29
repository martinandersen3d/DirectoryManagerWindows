#!/usr/bin/env python3

# Ctrl+ c:   copy path
# Ctrl+ v:   vscode
# Ctrl+ e:   explorer
# Ctrl+ t:   terminal
# Ctrl+ p:   powershell

import tkinter as tk
from generateList import generateList

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.folderTupleList = ()

        # app = tk.Tk()
        # set window width and height
        mywidth = 900
        myheight = 550

        # get screen height and width
        scrwdth = int( self.winfo_screenwidth() )
        scrhgt = int(self.winfo_screenheight())

        # write formula for center screen
        xLeft = int( (scrwdth/2) - (mywidth/2))
        yTop = int((scrhgt/2) - (myheight/2))

        # set geometry 
        self.geometry(str(mywidth) + "x" + str(myheight) + "+" + str(xLeft) + "+" + str(yTop))
        self.title("📁 Folder Bookmarks")

        # TEXTFIELD ---------------------------------
        self.entry = tk.Entry(self, width=140, borderwidth=8, relief=tk.FLAT)

        self.entry.pack()
        self.entry.bind('<KeyRelease>', self.on_entry_keyrelease)
        self.entry.bind('<<EntryFocus>>', self.on_entry_focus)
        self.scrollbar = tk.Scrollbar(self, orient="vertical")

        # LISTBOX --------------------------------
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox = tk.Listbox(self, width=126, height=27, borderwidth=8, relief=tk.FLAT, yscrollcommand=self.scrollbar.set)

        self.listbox.pack()
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.bind('<KeyRelease>', self.on_listbox_keyrelease)
        #listbox.bind('<Double-Button-1>', on_select)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        self.listbox.bind('<<ListboxFocused>>', self.on_listbox_focus)


        # BUTTONS --------------------------------------
        self.button1 =  tk.Button(self, text="Explorer", underline=0, command=self.on_button1_click)
        self.button1.pack(side=tk.LEFT)
        self.button2 =  tk.Button(self, text="Terminal", underline=0, command=self.on_button1_click)
        self.button2.pack(side=tk.LEFT)
        self.button3 =  tk.Button(self, text="VsCode", underline=0, command=self.on_button1_click)
        self.button3.pack(side=tk.LEFT)
        self.button4 =  tk.Button(self, text="Copy Path", underline=0, command=self.on_button1_click)
        self.button4.pack(side=tk.LEFT)
        self.button5 =  tk.Button(self, text="PowerShell", underline=0, command=self.on_button1_click)
        self.button5.pack(side=tk.LEFT)
        self.lbl =  tk.Label(self, text="           Use Ctrl+key or Enter to open in File Manager", fg="#aaa")
        self.lbl.pack(side=tk.LEFT)
        self.reloadList()
        self.bind_all('<Control-Key-E>', self.on_shared_keyrelease)
        self.bind_all('<Control-Key-A>', self.on_shared_keyrelease)
        self.bind_all('<Control-Key-C>', self.on_shared_keyrelease)
        self.bind_all('<Control-Key-T>', self.on_shared_keyrelease)
        self.bind_all('<Control-Key-P>', self.on_shared_keyrelease)
    
    def reloadList(self):
        self.folderTupleList=generateList()
        self.listbox_update(self.folderTupleList)
        # listbox.focus_set()
        self.listbox.select_set(0,0)
        self.listbox.activate(0)
        self.entry.focus_set()
        
        
    
    def on_entry_keyrelease(self, event):
        
        # get text from entry
        value = event.widget.get()
        value = value.strip().lower()
        print(event.keysym)
        
        # get data from folderTupleList
        if value == '':
            data = self.folderTupleList
        else:
            data = []
            for item in self.folderTupleList:
                if value in item.lower():
                    data.append(item)                

        # update data in listbox
        self.listbox_update(data)
        
        # If listbox is not emtpy and key is down, then focus the list
        end_index = self.listbox.index("end")
        if end_index != 0 and event.keysym == 'Down':
            if end_index == 1:
                self.listbox.focus_set()
                self.listbox.select_set(0,0)
                self.listbox.activate(0)
                self.listbox.focus_set()

            if end_index > 1:
                self.listbox.focus_set()
                self.listbox.select_set(1,1)
                self.listbox.activate(1)
                self.listbox.focus_set()
            
        if end_index != 0 and event.keysym == 'Up':
            # listbox.focus_set()
            # listbox.select_set(0)
            self.listbox.select_set(0,0)
            # listbox.activate(0)
            # listbox.focus_set()
            
        if end_index != 0 and event.keysym != 'Up'  and event.keysym != 'Down':
            # listbox.focus_set()
            # listbox.select_set(0)
            self.listbox.select_set(0,0)
            # listbox.activate(0)
            # listbox.focus_set()
            
        self.on_shared_keyrelease(event)

    def on_listbox_keyrelease(self, event):
        
        # get text from entry
        print(event.keysym)
        print(event.widget.curselection()[0])
        if event.keysym == 'Up' and event.widget.curselection()[0] == 0 or event.keysym == 'BackSpace':
            self.entry.focus_set()
            self.listbox.selection_clear(0, tk.END),
            self.listbox.select_set(0,0)

        self.on_shared_keyrelease(event)

    def on_shared_keyrelease(self, event):
        print('ctrl')
        if event.keysym == 'Escape':
            self.destroy()
        
    def listbox_update(self, data):
        # delete previous data
        self.listbox.delete(0, 'end')
        
        # sorting data 
        data = sorted(data, key=str.lower)

        # put new data
        for item in data:
            self.listbox.insert('end', item)


    def on_select(self, event):
        # display element selected on list
        print('(event) previous:', event.widget.get('active'))
        print('(event)  current:', event.widget.get(event.widget.curselection()))
        print('---')

    def on_listbox_focus(self, event):
            self.listbox.select_set(0,0)
            self.listbox.activate(0)
            self.listbox.focus_set()

    def on_entry_focus(self, event):
            self.listbox.select_set(0,0)
            self.listbox.activate(0)
            self.listbox.focus_set()

    def on_button1_click(self, event):
            pass
        
if __name__ == "__main__":
    app = App()
    app.mainloop()


# //------------------------------------




# --- main ---

# folderTupleList = ('apple', 'banana', 'Cranberry', 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry'  )

# app = tk.Tk()
# # set window width and height
# mywidth = 900
# myheight = 550

# # get screen height and width
# scrwdth = int( app.winfo_screenwidth() )
# scrhgt = int(app.winfo_screenheight())

# # write formula for center screen
# xLeft = int( (scrwdth/2) - (mywidth/2))
# yTop = int((scrhgt/2) - (myheight/2))

# # set geometry 
# app.geometry(str(mywidth) + "x" + str(myheight) + "+" + str(xLeft) + "+" + str(yTop))
# app.title("📁 Folder Bookmarks")

# # TEXTFIELD ---------------------------------
# entry = tk.Entry(app, width=140, borderwidth=8, relief=tk.FLAT)

# entry.pack()
# entry.bind('<KeyRelease>', on_entry_keyrelease)
# entry.bind('<<EntryFocus>>', on_entry_focus)
# scrollbar = tk.Scrollbar(app, orient="vertical")

# # LISTBOX --------------------------------
# scrollbar = tk.Scrollbar(app)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# listbox = tk.Listbox(app, width=126, height=27, borderwidth=8, relief=tk.FLAT, yscrollcommand=scrollbar.set)

# listbox.pack()
# scrollbar.config(command=listbox.yview)
# listbox.bind('<KeyRelease>', on_listbox_keyrelease)
# #listbox.bind('<Double-Button-1>', on_select)
# listbox.bind('<<ListboxSelect>>', on_select)
# listbox.bind('<<ListboxFocused>>', on_listbox_focus)
# listbox_update(folderTupleList)
# # listbox.focus_set()
# listbox.select_set(0,0)
# listbox.activate(0)
# entry.focus_set()

# # BUTTONS --------------------------------------
# button1 =  tk.Button(app, text="Explorer", underline=0, command=on_button1_click)
# button1.pack(side=tk.LEFT)
# button2 =  tk.Button(app, text="Terminal", underline=0, command=on_button1_click)
# button2.pack(side=tk.LEFT)
# button3 =  tk.Button(app, text="VsCode", underline=0, command=on_button1_click)
# button3.pack(side=tk.LEFT)
# button4 =  tk.Button(app, text="Copy Path", underline=0, command=on_button1_click)
# button4.pack(side=tk.LEFT)
# button5 =  tk.Button(app, text="PowerShell", underline=0, command=on_button1_click)
# button5.pack(side=tk.LEFT)
# lbl =  tk.Label(app, text="           Use Ctrl+key or Enter to open in File Manager", fg="#aaa")
# lbl.pack(side=tk.LEFT)
# app.mainloop()