from tkinter import *
from database import *
Menu=Tk()
Menu.geometry("500x500")

def v():
    View=Tk()
    View.geometry("500x500")

    l1=Label(View,text="CARDS",height=5,width=20)
    l2=Label(View,text="Delete",height=2,width=70)
    l3=Label(View,text="Deck:")
    l4=Label(View,text="Question:",height=2)
    le=Label(View)

    deck=StringVar(View)
    que=StringVar(View)
    e1=Entry(View,textvariable=deck)
    e2=Entry(View,textvariable=que)

    lb=Listbox(View,width=70)
    print(list_decks())
    for i in list_decks():
        print(get_cards(i))
        j=0
        while j<len(get_cards(i)):
            lb.insert(j,"Deck: "+i+"     Question: "+get_cards(i)[j][2]+"     Answer: "+get_cards(i)[j][3]+"     Days Left: "+str(get_cards(i)[j][0]))
            j+=1

    b2=Button(View,text='Back To Menu',command=View.destroy,width=15)
    b1=Button(View,text='Delete',command=lambda:delete_card(deck.get(),que.get()),width=20)

    l1.grid(row=0,column=1)
    lb.grid(row=1,column=1)
    l2.grid(row=2,column=1)
    l3.grid(row=3,column=1)
    e1.grid(row=4,column=1)
    l4.grid(row=5,column=1)
    e2.grid(row=6,column=1)
    b1.grid(row=7,column=1)
    le.grid(row=8)
    b2.grid(row=9,column=1)
    View.mainloop()
    
def s(deck):
    Solve=Tk()
    Solve.geometry("500x500") 
    
    current_EF = get_daily_cards(deck)[0][0][1]
    current_intv = get_daily_cards(deck)[0][0][0]

    def n():
        Solve.destroy() 
        s(deck)

    def ans(inter):
        l5.grid(row=2,column=1)
        l3.grid(row=2,column=2)
        b7.grid(row=5,column=4)
        choice = inter
        new_intv = intervals(current_intv,current_EF)
        newEF = new_EF_calculation(current_EF,choice)
        print(get_daily_cards(deck)[0][0][2])
        update_card(deck,get_daily_cards(deck)[0][0][2],new_intv,newEF)

    l1=Label(Solve,text="SOLVE",width=10,height=5)
    l4=Label(Solve,text="Question:")
    l5=Label(Solve,text="Answer:")
    l2=Label(Solve,text=get_daily_cards(deck)[0][0][2],width=10,height=2)
    l3=Label(Solve,text=get_daily_cards(deck)[0][0][3],width=10,height=2)
    le=Label(Solve,width=10)
    b2=Button(Solve,text="Incorrect",command=lambda:ans(1),width=10,height=2)
    b3=Button(Solve,text="Easy",command=lambda:ans(4),width=10,height=2)
    b4=Button(Solve,text="Moderate",command=lambda:ans(3),width=10,height=2)
    b5=Button(Solve,text="Difficult",command=lambda:ans(2),width=10,height=2)
    b6=Button(Solve,text="Back to Menu",command=Solve.destroy,width=10,height=2)
    b7=Button(Solve,text="Next Card",command=n,width=10,height=2)

    l1.grid(row=0,column=2)
    l4.grid(row=1,column=1)
    l2.grid(row=1,column=2)

    if get_daily_cards(deck)[1] == '':
        b4.grid(row=3,column=2)
        b6.grid(row=5,column=1)
    else:
        le.grid(row=3,column=0)
        b2.grid(row=3,column=1) 
        b3.grid(row=3,column=2) 
        b4.grid(row=3,column=3) 
        b5.grid(row=3,column=4)
        le.grid(row=4)
        b6.grid(row=5,column=1)
    Solve.mainloop()

def d():
    Deck=Tk()
    Deck.geometry("500x500")
    def b():
        Deck.destroy()
        s(decks.get())

    decks=StringVar(Deck)
    e1=Entry(Deck,textvariable=decks)
    b1=Button(Deck,text="Go",command=b,width=10)
    l1=Label(Deck,text='Enter a Deck Name:',height=5,width=70)

    l1.grid(row=0,column=0)
    e1.grid(row=1,column=0)
    b1.grid(row=2,column=0)
    Deck.mainloop()
    
def a():
    Add=Tk()
    Add.geometry("500x500")
    
    def add():
        insert_new_card(deck.get(),question.get(),answer.get())
        question.set("")
        answer.set("")

    l1=Label(Add,text="Add Cards",width=20,height=5)
    l2=Label(Add,text="Deck:",height=2)
    l3=Label(Add,text="Question:",height=2)
    l4=Label(Add,text="Answer:",height=2)
    le=Label(Add,width=20)
                    
    question=StringVar(Add)
    answer=StringVar(Add)
    deck=StringVar(Add)
    e1=Entry(Add,textvariable=deck)
    e2=Entry(Add,textvariable=question)
    e3=Entry(Add,textvariable=answer)

    b1=Button(Add,text="Add",command=add,width=10)
    b2=Button(Add,text="Back",command=Add.destroy,width=10)

    l1.grid(row=0,column=2)
    le.grid(row=1,column=0)
    l2.grid(row=1,column=1)
    l3.grid(row=2,column=1)
    l4.grid(row=3,column=1)
    
    e1.grid(row=1,column=2)
    e2.grid(row=2,column=2)
    e3.grid(row=3,column=2)
    le.grid(row=4,column=0)
    b1.grid(row=5,column=2)
    b2.grid(row=5,column=1,sticky='e')
    Add.mainloop()
    
l=Label(Menu,text="MENU",height=5,width=70)
b1=Button(Menu,text='View Cards',command=v,width=50,height=5)
b2=Button(Menu,text='Solve Cards',command=d,width=50,height=5)
b3=Button(Menu,text='Add Card',command=a,width=50,height=5)
b4=Button(Menu,text="Exit",command=Menu.destroy,height=2,width=10)
l.grid(row=1,column=1)
b1.grid(row=2,column=1)
b2.grid(row=3,column=1)
b3.grid(row=4,column=1)
b4.grid(row=5,column=1)
Menu.mainloop()
