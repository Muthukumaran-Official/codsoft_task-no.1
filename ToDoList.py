from tkinter import *
from tkinter import messagebox
import pickle

#creating the layout and designs for the UI!!!
window=Tk()

window.title("TO DO LIST")
window.maxsize(500,600)
window.minsize(400,500)
window.geometry("400x500")
window.config(bg="#1f2833")

#defining required functions here!!!!

def add_task():
    task=entrybox.get()
    if task!="":
        listbox.insert(END,task)
        entrybox.delete(0,END)   
    else:
         messagebox.showwarning(title="warning",message="must enter a task!!")

def del_task():
    try:
        selectedItem = listbox.curselection()[0]
        listbox.delete(selectedItem)
    except:
        messagebox.showwarning(title="warning",message="must select a task to delete")

def load_task():
    try:
        tasks=pickle.load(open("tasks.dat","rb"))
        listbox.delete(0,END)
        for task in tasks:
            listbox.insert(END,task)
    except:
        messagebox.showwarning(title="warning",message="no file found!!!")
def save_task():
    tasks=listbox.get(0,listbox.size())
    pickle.dump(tasks, open ("tasks.dat", "wb")) 

#creating GUI

Framebox=Frame(window,bg="#1f2833")
Framebox.pack()

emptylabel=Label(Framebox,bg="#1f2833")
emptylabel.pack()
listbox=Listbox(Framebox,height=10,width=53,bg="pink",fg="black")
listbox.pack(side=LEFT)

scroll_bar=Scrollbar(Framebox,width=15)
scroll_bar.pack(side=RIGHT,fill=Y)
listbox.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=listbox.yview)
entrybox=Entry(window,width=56,bg="light blue",fg="black")
entrybox.pack(pady=20)

Framebox2=Frame(window,bg="#45a29e")
Framebox2.pack()

addbutton=Button(Framebox2,text="Add Task",width=20,command=add_task)
addbutton.grid(row=0,column=0,padx=10,pady=10)

delbutton=Button(Framebox2,text="Delete Task",width=20,command=del_task)
delbutton.grid(row=0,column=1,padx=10,pady=10)

loadbutton=Button(Framebox2,text="Load Task",width=20,command=load_task)
loadbutton.grid(row=1,column=0,padx=10,pady=10)

savebutton=Button(Framebox2,text="Save Task",width=20,command=save_task)
savebutton.grid(row=1,column=1,padx=10,pady=10)

window.mainloop()