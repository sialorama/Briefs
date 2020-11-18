from tkinter import Tk, Frame, Label, IntVar, Checkbutton, Button, Toplevel, ttk
from algo import Binomotron
from query import Query

class graphique:

    def __init__(self):
        self.window = Tk()
        self.window.title("My Application")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
        self.window.config(background='#41B77F')
        self.people = Query.get_apprenants(self)
        self.main_windows()

    # def compute(self, number_in_group, ):
    #     crew = Binomotron(number_in_group)
    #     crew = crew()
    #     self.group_window(crew)
    #     #Query().add_crew(crew)

    
    def main_windows(self):
        frameLeft = Frame(self.window, padx=50, pady=50)
        frameCenter = Frame(self.window, padx=50, pady=50)
        frameRight = Frame(self.window, padx=50, pady=25)
        Label(self.window, text="Binômotron", font=("Courier", 16, "italic")).grid()

        frameLeft.grid(row=1, column=0)
        frameCenter.grid(row=1, column=1)
        frameRight.grid(row=1, column=2)

        for i in self.people:
            Label(frameLeft, text=i).pack()

        number_in_group = IntVar()
        Checkbutton(frameCenter, text='Groupe 2',variable=number_in_group, onvalue=2, offvalue=0).pack()
        Checkbutton(frameCenter, text='Groupe 3',variable=number_in_group, onvalue=3, offvalue=0).pack()
        Checkbutton(frameCenter, text='Groupe 4',variable=number_in_group, onvalue=4, offvalue=0).pack()
        Checkbutton(frameCenter, text='Groupe 5',variable=number_in_group, onvalue=5, offvalue=0).pack()

        Button(frameRight, text="press me", command=lambda:  self.compute(number_in_group.get())).pack()
        self.window.mainloop()


    def group_window(self, crew):
        new_windows = Toplevel(self.window)


        
        treev = ttk.Treeview(new_windows, selectmode ='browse') 
        treev.pack(side ='right') 
         
        verscrlbar = ttk.Scrollbar(new_windows, orient ="vertical", command = treev.yview) 
        verscrlbar.pack(side ='right', fill ='x') 
        
        treev.configure(xscrollcommand = verscrlbar.set)  
        treev["columns"] = ("1", "2", "3") 
        treev['show'] = 'headings'
          
        treev.column("1", width = 100, anchor ='c') 
        treev.column("2", width = 100, anchor ='c') 
        treev.column("3", width = 250, anchor ='c') 
         
        treev.heading("1", text ="Index") 
        treev.heading("2", text ="Group") 
        treev.heading("3", text ="People in group") 
        for i in range(len(crew.keys())):
            treev.insert("", "end", text="L1", values=(i, "Group"+str(i+1), crew["group " + str(i+1)]))


app = graphique()
app.window.mainloop()