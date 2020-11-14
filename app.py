

import wmi
from tkinter import *
from tkinter import ttk


class Process:
    def __init__(self,root):
        self.root=root
        self.root.title("Process")
        self.root.geometry("400x493")
        self.root.iconbitmap("logo50.ico")
        self.root.resizable(0,0)




#===============================frame======================
        
        mainframe=Frame(self.root,width=400,height=493,bd=3,relief="ridge")
        mainframe.place(x=0,y=0)

        scol=Scrollbar(mainframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')


        processess=ttk.Treeview(mainframe,columns=("Process ID","Process Name"),height=23,yscrollcommand=scol.set)
        processess.heading("Process ID",text="Process ID")
        processess.heading("Process Name",text="Process Name")
        processess['show']="headings"
        processess.column("Process ID",width=155,minwidth=10)
        processess.column("Process Name",width=218,minwidth=40)
        processess.place(x=0,y=0)
        scol.config(command=processess.yview)

        c=wmi.WMI()

        for process in c.win32_process():
            self.root.update()
            processess.insert('','end',values=(process.processID,process.NAME))
            

if __name__ == "__main__":
    root=Tk()
    app=Process(root)
    root.mainloop()  