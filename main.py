#!/usr/bin/env python3

# Ctrl+ c:   copy path
# Ctrl+ v:   vscode
# Ctrl+ e:   explorer
# Ctrl+ t:   terminal
# Ctrl+ p:   powershell


import tkinter as tk

def on_entry_keyrelease(event):
    
    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()
    print(event.keysym)
       
    # get data from test_list
    if value == '':
        data = test_list
    else:
        data = []
        for item in test_list:
            if value in item.lower():
                data.append(item)                

    # update data in listbox
    listbox_update(data)
    
    # If listbox is not emtpy and key is down, then focus the list
    end_index = listbox.index("end")
    if end_index != 0 and event.keysym == 'Down':
        if end_index == 1:
            listbox.focus_set()
            listbox.select_set(0,0)
            listbox.activate(0)
            listbox.focus_set()

        if end_index > 1:
            listbox.focus_set()
            listbox.select_set(1,1)
            listbox.activate(1)
            listbox.focus_set()
        
    if end_index != 0 and event.keysym == 'Up':
        # listbox.focus_set()
        # listbox.select_set(0)
        listbox.select_set(0,0)
        # listbox.activate(0)
        # listbox.focus_set()
        
    if end_index != 0 and event.keysym != 'Up'  and event.keysym != 'Down':
        # listbox.focus_set()
        # listbox.select_set(0)
        listbox.select_set(0,0)
        # listbox.activate(0)
        # listbox.focus_set()

def on_listbox_keyrelease(event):
    
    # get text from entry
    print(event.keysym)
    print(event.widget.curselection()[0])
    if event.keysym == 'Up' and event.widget.curselection()[0] == 0:
        print('JACKPOT')
        entry.focus_set()
        listbox.select_set(0,0)
    
    
def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')
    
    # sorting data 
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox.insert('end', item)


def on_select(event):
    # display element selected on list
    print('(event) previous:', event.widget.get('active'))
    print('(event)  current:', event.widget.get(event.widget.curselection()))
    print('---')

def on_listbox_focus(event):
        listbox.select_set(0,0)
        listbox.activate(0)
        listbox.focus_set()

def on_entry_focus(event):
        listbox.select_set(0,0)
        listbox.activate(0)
        listbox.focus_set()

def on_button1_click(event):
        pass


# --- main ---

test_list = ('apple', 'banana', 'Cranberry', 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' , 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry'  )

app = tk.Tk()
# set window width and height
mywidth = 900
myheight = 500

# get screen height and width
scrwdth = int( app.winfo_screenwidth() )
scrhgt = int(app.winfo_screenheight())

# write formula for center screen
xLeft = int( (scrwdth/2) - (mywidth/2))
yTop = int((scrhgt/2) - (myheight/2))

# set geometry 
app.geometry(str(mywidth) + "x" + str(myheight) + "+" + str(xLeft) + "+" + str(yTop))
app.title("📁 Folder Bookmarks")

# TEXTFIELD ---------------------------------
entry = tk.Entry(app, width=140, borderwidth=8, relief=tk.FLAT)

entry.pack()
entry.bind('<KeyRelease>', on_entry_keyrelease)
entry.bind('<<EntryFocus>>', on_entry_focus)
scrollbar = tk.Scrollbar(app, orient="vertical")

# LISTBOX --------------------------------
scrollbar = tk.Scrollbar(app)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(app, width=126, height=25, borderwidth=8, relief=tk.FLAT, yscrollcommand=scrollbar.set)

listbox.pack()
scrollbar.config(command=listbox.yview)
listbox.bind('<KeyRelease>', on_listbox_keyrelease)
#listbox.bind('<Double-Button-1>', on_select)
listbox.bind('<<ListboxSelect>>', on_select)
listbox.bind('<<ListboxFocused>>', on_listbox_focus)
listbox_update(test_list)
# listbox.focus_set()
listbox.select_set(0,0)
listbox.activate(0)
entry.focus_set()

# BUTTONS --------------------------------------
button1 =  tk.Button(app, text="Explorer", underline=0, command=on_button1_click)
button1.pack(side=tk.LEFT)
button2 =  tk.Button(app, text="Terminal", underline=0, command=on_button1_click)
button2.pack(side=tk.LEFT)
button3 =  tk.Button(app, text="VsCode", underline=0, command=on_button1_click)
button3.pack(side=tk.LEFT)
button4 =  tk.Button(app, text="Copy Path", underline=0, command=on_button1_click)
button4.pack(side=tk.LEFT)
button5 =  tk.Button(app, text="PowerShell", underline=0, command=on_button1_click)
button5.pack(side=tk.LEFT)
lbl =  tk.Label(app, text="           Use Ctrl+key or Enter to open in File Manager", fg="#aaa")
lbl.pack(side=tk.LEFT)
app.mainloop()