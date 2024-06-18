from tkinter import *
import openpyxl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def claculate_ci():
    wBook = openpyxl.load_workbook("Practice1.xlsx")
    b=wBook["Sheet1"]
    p=player.get()
    y1 = y2017.get()
    y2 = y2018.get()
    y3 = y2019.get()
    y4 = y2020.get()
    data=[p,y1,y2,y3,y4]
    b.append(data)

    wBook.save("Practice1.xlsx")
    print('All Data Inserted Successfully')
def graph():
    e1=pd.read_excel("Practice1.xlsx","Sheet1")
    X=np.arange(len(e1['player']))
    plt.figure(figsize=(10,6))
    width=0.15
    plt.bar(x=e1['player'],height=e1[2017],width=width,label='2017',color="red")
    plt.bar(X+0.20, height=e1[2018], width=width, color="green",label='2018')
    plt.bar(X+0.40, height=e1[2019], width=width, color="pink",label='2019')
    plt.bar(X+0.60, height=e1[2020], width=width, color="yellow",label='2020')
    plt.legend()
    plt.title('Players Run Bar Chart')
    plt.xlabel('Players')
    plt.ylabel('Runs')
    plt.savefig('Players runs.png')
    plt.show()
root=Tk()
root.configure(background='light blue')
root.geometry("400x250")
root.title("Compound Inter")

label1 = Label(root,text="Player :").grid(row = 1,column = 0)
label2=Label(root,text="2017 :").grid(row=2,column=0)
label3=Label(root,text="2018:").grid(row=3,column=0)
label4=Label(root,text="2019:").grid(row=4,column=0)
label5=Label(root,text="2020:").grid(row=5,column=0)
player=Entry(root)
y2017=Entry(root)
y2018=Entry(root)
y2019=Entry(root)
y2020=Entry(root)
player.grid(row=1,column=1)
y2017.grid(row=2,column=1)
y2018.grid(row=3,column=1)
y2019.grid(row=4,column=1)
y2020.grid(row=5,column=1)
button1=Button(root,text="Submit",command=claculate_ci).grid(row=6,column=1,pady=10)
button2=Button(root,text="Display Graph",command=graph).grid(row=7,column=1,pady=10)
root.mainloop()