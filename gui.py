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
    #lb=Listbox(View
    b2=Button(View,text='Back:',command=View.destroy,height=2)
    b1=Button(View,text='Delete:',command=lambda:delete_card(deck.get(),que.get()),height=2)

    l1.place(x=250,y=0)

    l2.place(x=250,y=120)
    l3.place(x=150,y=150)
    e1.place(x=200,y=150)
    l4.place(x=150,y=190)
    e2.place(x=200,y=190)
    b1.place(x=250,y=240)
    b2.place(x=250,y=270)
    View.mainloop()
    
def s(deck):
    Solve=Tk()
    while True:
        l1=Label(Solve,text="SOLVE")
        l2=Label(Solve,text=get_cards(deck))
        b1=Button(Solve,text="Again",command=lambda:ans(10))
        b2=Button(Solve,text="Incorrect",command=lambda:ans(10))
        b3=Button(Solve,text="Easy",command=lambda:ans(10))
        b4=Button(Solve,text="Moderate",command=lambda:ans(10))
        b5=Button(Solve,text="Difficult",command=lambda:ans(10))
        b6=Button(Solve,text="Back to Menu",command=Solve.destroy)
        b7=Button(Solve,text="Next Card")
    
        l2=Label(Solve,text="answer")
        def ans(inter):
            l2.place(x=3,y=
    3)
            b7.place(x=5,y=
    4)
            print(inter)
        l1.place(x=0,y=
3)
        b1.place(x=1,y=
1)
        b2.place(x=1,y=
2) 
        b3.place(x=1,y=
3) 
        b4.place(x=1,y=
4) 
        b5.place(x=1,y=
5)
        b6.place(x=5,y=
2)
        Solve.mainloop()

def d():
    Deck=Tk()
    l1=Label(Deck,text="Choose a Deck:")
    b1=Button(Deck,text="Math",command=lambda:s("Math"))
    b2=Button(Deck,text="Chemistry",command=lambda:s("Chemistry"))
    b3=Button(Deck,text="Law",command=lambda:s("Law"))
    b4=Button(Deck,text="Biology",command=lambda:s("Biology"))

    l1.place(x=0,y=3)
    b1.place(x=1,y=2)
    b2.place(x=1,y=4)
    b3.place(x=2,y=2)
    b4.place(x=2,y=4)
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
                    
    b1=Button(Add,text="Add",command=insert_new_card(deck.get(), question.get(), answer.get()))
    b2=Button(Add,text="Back",command=Add.destroy)
                    
    l1.place(x=0,y=3)
    l2.place(x=1,y=0)
    l3.place(x=2,y=0)
    l4.place(x=3,y=0)
    
    e1.place(x=1,y=3)
    e2.place(x=2,y=3)
    e3.place(x=3,y=3)
    
    b1.place(x=4,y=5)
    b2.place(x=4,y=1)
    Add.mainloop()
    
l=Label(Menu,text="MENU",height=5)
b1=Button(Menu,text='View Cards',command=v,height=5,width=25)
b2=Button(Menu,text='Solve Cards',command=d,height=5,width=25)
b3=Button(Menu,text='Add Card',command=a,height=5,width=25)
l.pack()
b1.pack()
b2.pack()
b3.pack()
Menu.mainloop()

