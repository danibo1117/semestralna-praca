import tkinter as tk
from tkinter import ttk
from pacient import Pacient
from Backend import loadFromJson, saveToJson
import time
import random
from tkinter import messagebox
import matplotlib.pyplot as plt

#janos

root = tk.Tk()
root.configure(bg = "#333333")

def ID_generator():
    Time = time.time()
    cislo = random.randint(100000,1000000)
    return str(Time) + str(cislo)
    

def remove_from_trv():
    for pacient in trv.get_children():
        trv.delete(pacient)

def vyber_id():
    pacient_vyber = trv.selection()[0]
    return pacient_vyber

def najdi_id_pacient():
    pacienti = loadFromJson()
    vybrane_id = vyber_id()
    for pacient in pacienti:
        if pacient.id == vybrane_id:
            label0_text.config(text = str(pacient.id))

            label1_entry.delete(0, tk.END)
            label1_entry.insert(0, str(pacient.meno))
            
            label2_entry.delete(0, tk.END)
            label2_entry.insert(0, str(pacient.priezvisko))
            
            label3_entry.delete(0, tk.END)
            label3_entry.insert(0, str(pacient.datumnarod))
            
            label4_entry.delete(0, tk.END)
            label4_entry.insert(0, str(pacient.posledna_navs))
            
            label5_entry.delete(0, tk.END)
            label5_entry.insert(0, str(pacient.diagnoza))
            
            label6_entry.delete(0, tk.END)
            label6_entry.insert(0, str(pacient.predpis_liek))
            
            
def update_edit_pacient():
    pacienti = loadFromJson()
    for pacient in pacienti:

        if pacient.id == label0_text.cget("text"):
            pacient.id = label0_text.cget("text")
            pacient.meno = label1_entry.get()
            pacient.priezvisko = label2_entry.get()
            pacient.datumnarod = label3_entry.get()
            pacient.posledna__navs =label4_entry.get()
            pacient.diagnoza = label5_entry.get()
            pacient.predpis_liek = label6_entry.get()
        
        saveToJson(pacienti)

    load_trv_with_json()
    
    

def add_new_patient():

    pacienti = loadFromJson()
        
    
    meno1 = label1_entry.get()
    priezvisko1 = label2_entry.get()
    datumn1= label3_entry.get()
    datumvy1=label4_entry.get()
    diagnoza1 = label5_entry.get()
    lieky1 = label6_entry.get()

    if len(meno1) == 0 or len(priezvisko1) == 0 or len(datumn1) == 0 or len(datumvy1) == 0 or len(diagnoza1) == 0 or len(lieky1) == 0:
        box = messagebox.showinfo( " ","Jednotlivé polia musia byť vyplnené")
        return
    


    

    def check_date(datum):
        
        nums = datum.split(".")
        try:
            den = int(nums[0])
            mesiac = int(nums[1])
            rok = int(nums[2])
        except:
            messagebox.showerror(" ", "Nesprávny dátum")
            return False
        
        if den < 1 or den > 31:
            messagebox.showerror(" ","Nesprávny datum")
            return False
        if mesiac > 12 or mesiac < 1:
            messagebox.showerror(" ", "Nesprávny dátum")
            return False
        if rok < 1900 or rok > 2025:
            messagebox.showerror(" ","Nesprávny dátum")
            return False
        
        return True

    if check_date(datumn1) == False or check_date(datumvy1) == False:
        return

    pacient = Pacient(ID_generator(), meno1, priezvisko1, datumn1, datumvy1, diagnoza1, lieky1)
    pacienti.append(pacient)
    
    saveToJson(pacienti)

    load_trv_with_json()
     


def load_trv_with_json():
    pacienti = loadFromJson()
    rowIndex = 1
    remove_from_trv()
    for pacient in pacienti:
        Id = pacient.id
        meno = pacient.meno
        priezvisko = pacient.priezvisko
        datumna = pacient.datumnarod
        datumvy = pacient.posledna_navs
        diagnoza = pacient.diagnoza 
        predpis = pacient.predpis_liek
        trv.insert("",index= "end", iid=Id,text="", values=(Id, meno, priezvisko, datumna, datumvy, diagnoza, predpis))
        rowIndex += 1

def delete_field():
    data = loadFromJson()
    a = trv.selection()
    
    for id in a:
        for pacient in data:
            if id == pacient.id:
                data.remove(pacient)


    saveToJson(data)
    load_trv_with_json()



def graf_datum_narod():
    pacienti = loadFromJson()
    datum_narod = {"1940-1960": 0 , "1960-1980" : 0, "1980-2000": 0, "2000-2024": 0}
    


    for pacient in pacienti:
        rok = pacient.getYear()
        if rok in range(1940,1960):
            datum_narod["1940-1960"] += 1
        if rok in range(1960, 1980):
            datum_narod["1960-1980"]+=1
        if rok in range(1980, 2000):
            datum_narod["1980-2000"]+=1
        if rok in range(2000, 2024):
            datum_narod["2000-2024"]+=1
        

    
    positions = datum_narod.keys()
    roky = datum_narod.values()

    plt.bar(positions, roky)
    plt.xlabel("Rok narodenia")
    plt.ylabel("Počet pacientov")
    plt.show()


    

label0 = ttk.Label(root, text= "Id:",background = "#333333", font = ("Ariel", 12,),foreground="white", anchor="w", justify="left", )
label0_text = ttk.Label(root, text= ID_generator() )

label1 = ttk.Label(root, text= "Meno:",background = "#333333", font = ("Ariel", 12,),foreground="white", anchor="w", justify="left")
label1_entry = ttk.Entry(root)

label2 = ttk.Label(root, text= "Priezvisko:",background = "#333333", font = ("Ariel", 12),foreground="white",  anchor="w")
label2_entry = ttk.Entry(root)

label3 = ttk.Label(root, text= "Dátum narod.:\n(DD.MM.YYYY)",background = "#333333", font = ("Ariel", 12),foreground="white",  anchor="w")
label3_entry = ttk.Entry(root)

label4 =ttk.Label(root, text= "Dátum vyšetrenia:\n(DD.MM.YYYY)",background = "#333333", font = ("Ariel", 12), foreground="white", justify="left")
label4_entry = ttk.Entry(root)

label5 = ttk.Label(root, text= "Diagnóza:",background = "#333333", font = ("Ariel", 12),foreground="white", justify="left")
label5_entry = ttk.Entry(root)

label6 = ttk.Label(root, text= "Predpísané lieky:",background = "#333333", font = ("Ariel", 12),foreground="white",  justify="left")
label6_entry = ttk.Entry(root)

nahrat_button = tk.Button(root, text="Nahrať", command=add_new_patient)
delete_button = tk.Button(root, text = "Vymazať", command = delete_field )
graf_button = tk.Button(root, text="Graf", command = graf_datum_narod)
edit_button = tk.Button(root, text="Uprav", command = najdi_id_pacient)
update_button = tk.Button(root, text="Update", command = update_edit_pacient)


label0.grid(row = 0, column = 0, sticky="w",pady = 20)
label0_text.grid(row =0 , column = 1,pady = 20)

label1.grid(row = 1, column = 0, sticky="w",pady = 10)
label1_entry.grid(row = 1 , column = 1,pady = 10)

label2.grid(row = 2, column = 0, sticky="w")
label2_entry.grid(row = 2, column = 1,pady = 10)

label3.grid(row = 3, column = 0,sticky="w",pady = 20)
label3_entry.grid(row = 3, column = 1, pady = 20)

label4.grid(row = 4, column = 0, sticky="w")
label4_entry.grid(row = 4, column = 1)

label5.grid(row = 5, column = 0, sticky="w",pady = 20)
label5_entry.grid(row = 5, column = 1, pady = 20)

label6.grid(row = 6, column = 0, sticky="w")
label6_entry.grid(row = 6, column = 1, pady = 20)

nahrat_button.grid(row=7, column =0, pady = 20, sticky="ew")
delete_button.grid(row=7, column =1, pady = 20, sticky="ew")
graf_button.grid(row=9, column = 0, columnspan = 2, pady = 20, sticky="ew")
edit_button.grid(row=8, column = 1,pady = 20, sticky="ew")
update_button.grid(row=8, column = 0,pady = 20, sticky="ew")

trv_frame = tk.Frame(root, padx=30, pady=30, bg = "#333333")
trv_frame.grid(row=0, column = 2, rowspan=10)

scroll = ttk.Scrollbar(trv_frame, orient="vertical")
scroll.pack(side = "right", fill = "y")

trv = ttk.Treeview(trv_frame, columns=(1,2,3,4,5,6,7),show="headings", height="25",yscrollcommand=scroll.set)
trv.pack()


trv.heading(1,text="ID", anchor = "center")
trv.heading(2,text="Meno", anchor = "center")
trv.heading(3,text="Priezvisko", anchor = "center")
trv.heading(4,text="Dátum narodenia", anchor = "center")
trv.heading(5,text="Dátum vyšetrenia", anchor = "center")
trv.heading(6,text="Diagnóza", anchor = "center")
trv.heading(7,text="Predpísané lieky", anchor = "center")   

trv.column(1, width = 150)
trv.column(2, width = 150)
trv.column(3, width = 150)
trv.column(4, width = 150)
trv.column(5, width = 150)
trv.column(6, width = 150)
trv.column(7, width = 150)


            



load_trv_with_json()
root.mainloop()

