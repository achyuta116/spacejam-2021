from tkinter import *
from database import *
Menu=Tk()
Menu.geometry("500x500")

def v():
    View=Tk()
    View.geometry("500x500")
    l1=Label(View,text="CARDS")
    l2=Label(View,text="Delete")
    l3=Label(View,text="Deck")
    l4=Label(View,text="Question")
    deck=StringVar(View)
    que=StringVar(View)
    e1=Entry(View,textvariable=deck)
    e2=Entry(View,textvariable=que)
    lb=Listbox(View,width=500)
    print(list_decks())
    for i in list_decks():
        print(get_cards(i))
        j=0
        while j<len(get_cards(i)):
            lb.insert(j,"Question: "+get_cards(i)[j][3]+" Answer: "+get_cards(i)[j][4]+" Days Left: "+str(get_cards(i)[j][0]))
            j+=1
    b2=Button(View,text='Back:',command=View.destroy)
    b1=Button(View,text='Delete:',command=lambda:delete_card(deck.get(),que.get()))
    l1.grid(row=0,column=5)
    lb.grid(row=1,column=5)
    l2.grid(row=2,column=10)
    l3.grid(row=3,column=0)
    e1.grid(row=3,column=10)
    l4.grid(row=4,column=0)
    e2.grid(row=4,column=5)
    b1.grid(row=5,column=5)
    b2.grid(row=6,column=5)
    View.mainloop()
    
def s(deck):
    Solve=Tk()  

    def n():
        Solve.destroy()
        s(deck)
    def ans(inter):
        l3.grid(row=3,column=3)
        b7.grid(row=5,column=4)
    print(get_daily_cards(deck))
    l1=Label(Solve,text="SOLVE")
    l2=Label(Solve,text=get_daily_cards(deck)[0][0][3])
    b2=Button(Solve,text="Incorrect",command=lambda:ans(1))
    b3=Button(Solve,text="Easy",command=lambda:ans(4))
    b4=Button(Solve,text="Moderate",command=lambda:ans(3))
    b5=Button(Solve,text="Difficult",command=lambda:ans(2))
    b6=Button(Solve,text="Back to Menu",command=Solve.destroy)
    b7=Button(Solve,text="Next Card",command=n)
    l3=Label(Solve,text=get_daily_cards(deck)[0][0][4])
    
    l1.grid(row=0,column=3)
    b1.grid(row=1,column=1)
    b2.grid(row=1,column=2) 
    b3.grid(row=1,column=3) 
    b4.grid(row=1,column=4) 
    b5.grid(row=1,column=5)
    b6.grid(row=5,column=2)
    Solve.mainloop()

def d():
    Deck=Tk()
    Deck.geometry("500x500")
    def b():
        Deck.destroy()
        s(decks.get())

    decks=StringVar(Deck)
    e1=Entry(Deck,textvariable=decks)
    b1=Button(Deck,text="Go",command=b)
    l1=Label(Deck,text='Enter a Deck Name',height=5)

    l1.grid(row=0,column=0)
    e1.grid(row=1,column=0)
    b1.grid(row=2,column=0)
    Deck.mainloop()
    
def a():
    Add=Tk()
    
    l1=Label(Add,text="ADD")
    l2=Label(Add,text="Deck:")
    l3=Label(Add,text="Question:")
    l4=Label(Add,text="Answer:")
                    
    question=StringVar(Add)
    answer=StringVar(Add)
    deck=StringVar(Add)
    e1=Entry(Add,textvariable=deck)
    e2=Entry(Add,textvariable=question)
    e3=Entry(Add,textvariable=answer)
    
    def add():
        insert_new_card(deck.get(),question.get(),answer.get())
        question.set("")
        answer.set("")
    
    b1=Button(Add,text="Add",command=add)
    b2=Button(Add,text="Back",command=Add.destroy)

    l1.grid(row=0,column=3)
    l2.grid(row=1,column=0)
    l3.grid(row=2,column=0)
    l4.grid(row=3,column=0)
    
    e1.grid(row=1,column=3)
    e2.grid(row=2,column=3)
    e3.grid(row=3,column=3)
    
    b1.grid(row=4,column=5)
    b2.grid(row=4,column=1)
    Add.mainloop()
    
l=Label(Menu,text="MENU",height=5)
b1=Button(Menu,text='View Cards',command=v,width=25,height=5)
b2=Button(Menu,text='Solve Cards',command=d,width=25,height=5)
b3=Button(Menu,text='Add Card',command=a,width=25,height=5)
b4=Button(Menu,text="Exit",command=Menu.destroy,height=2,width=10)
l.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
Menu.mainloop()
