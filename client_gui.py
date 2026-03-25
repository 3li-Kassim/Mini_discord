import tkinter as tk
from tkinter import simpledialog

class MyGUI:

    def __init__(self,incoming_msgs,sock):
        BG_COLOR = "#17202A"
        TEXT_COLOR = "#EAECEE"
        def delete_message(event= None):
           self.entry.delete(0,"end")
        def add_message(event = None):
            self.message = "Message"
            self.entry.insert(0,self.message)
        
        self.incoming_msgs = incoming_msgs    
        self.sock = sock
           
        self.root = tk.Tk()
        self.root.geometry("650x700")
        self.root.title("Mini Discord")
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.username= None
        while self.username is None:
            self.username= simpledialog.askstring("Input","Enter your name",parent =self.root)

        self.root.lift()       
        
        self.label_frame = tk.Frame(self.root)
        self.root.grid_columnconfigure(0,weight=1)
        self.label_frame.grid(row=0, column=0)
        self.label = tk.Label(self.label_frame, bg = BG_COLOR, fg = TEXT_COLOR ,text = "Discord", font = ('Arial', 18), pady = 10, width = 20 , height= 1)
        self.label.grid(row = 0, column=0,sticky="n")

        self.text_frame = tk.Frame(self.root)
        self.text_frame.grid(row=1, column=0, sticky="nsew")
        self.text = tk.Text(self.text_frame, bg =BG_COLOR, fg = TEXT_COLOR, font= ('Arial', 16), width = 60)
        self.text.grid(row=0, column=0, sticky="nsew")

        self.scroll = tk.Scrollbar(self.text_frame, command = self.text.yview)
        self.scroll.grid(row=0, column=1, sticky="ns")
        self.text.config(yscrollcommand=self.scroll.set) 
        self.text_frame.grid_rowconfigure(0, weight=1)
        self.text_frame.grid_columnconfigure(0, weight=1) 

        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.grid(row = 2,column=0)
        self.entry_frame.grid_columnconfigure(0,weight=1)
        self.entry = tk.Entry(self.entry_frame,bg = "#2C3E50",fg = TEXT_COLOR,font= ('Arial', 16),width=55)
        self.entry.grid(row = 0, column = 0)
        self.message = "Message"
        self.entry.insert(0,self.message)
        self.entry.bind("<FocusOut>",add_message)
        self.entry.bind("<FocusIn>",delete_message)

        self.button = tk.Button(self.entry_frame, text ="Send",bg= "#ABB2B9", font = ('Arial', 14), command = self.show_message)
        self.button.grid(row = 0, column= 1 )
        self.entry.bind("<Return>",self.show_message)
        
        self.text.config(state="disabled")
        self.check_message()
        
        self.root.mainloop()
    def check_message(self):
        if self.incoming_msgs.empty():
            pass
        else:
            msg = self.incoming_msgs.get()
            self.text.config(state="normal")
            self.text.insert("end",msg+ "\n")
            self.text.config(state="disabled")
            
                
        self.root.after(10,self.check_message)    
               
    def show_message(self,event = None):
        message = self.entry.get()
        send = self.username+": " + message
        if message == "":
            return
        else:
            self.text.config(state="normal")
            self.text.insert("end",send + "\n")
            self.text.config(state="disabled")
            self.entry.delete(0,"end")
            self.sock.sendall(send.encode())

            
            