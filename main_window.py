# -*- coding: utf-8 -*-
import tkinter as Tk
from tkinter import LEFT
import psycopg2
from datetime import datetime
from tkinter import END
import winsound
conn = psycopg2.connect("dbname=POST-APLICATION-WITH-DB user=postgres password=Elorado123*")



def show_window(login):
    
    def last_post():
        sql= '''SELECT * FROM "Posty" '''
        cur = conn.cursor()
        cur.execute(sql)
        posty = cur.fetchall()
        cur.close()
        return posty[-1:-4:-1]
            
    
    def submit_post(login=login):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%Y-%m-%d")
        tresc = okienko_dodaj_post.get("1.0", "end-1c")
        print("Czas =", current_time)    
        print("Data =", current_date)    
        sql= f'''INSERT INTO "Posty" values ('{login}', '{current_time}', '{current_date}', '{tresc}')'''
        print(sql)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        okienko_dodaj_post.delete('1.0', END)
        posty=last_post()
        user1.config(text=f"{posty[0][2]}, {posty[0][1]}, {posty[0][0]}")
        post1.config(text=f"{posty[0][3]}")
        user2.config(text=f"{posty[1][2]}, {posty[1][1]}, {posty[1][0]}")
        post2.config(text=f"{posty[1][3]}")
        user3.config(text=f"{posty[2][2]}, {posty[2][1]}, {posty[2][0]}")
        post3.config(text=f"{posty[2][3]}")

    
    main = Tk.Tk()
    main.geometry("550x550") 
    main.title('Postownia')
    main.config(bg='#0f54d4')
    main.iconbitmap(r'2824438_academic_clip_exam_note_paper_icon.ico')
    
    def task():
        posty=last_post()
        if posty[0][3] != post1["text"]:
            winsound.PlaySound(r"C:\Users\sebix\ZajeciaEdun\POST-APLICATION-WITH-DB\MessageSaund.wav",
                               winsound.SND_FILENAME)
            
        user1.config(text=f"{posty[0][2]}, {posty[0][1]}, {posty[0][0]}")
        post1.config(text=f"{posty[0][3]}")
        user2.config(text=f"{posty[1][2]}, {posty[1][1]}, {posty[1][0]}")
        post2.config(text=f"{posty[1][3]}")
        user3.config(text=f"{posty[2][2]}, {posty[2][1]}, {posty[2][0]}")
        post3.config(text=f"{posty[2][3]}")
        main.after(1000, task)
    
    
    #dodajposta
    napis_dodajpost = Tk.Label(main, text="Dodaj post:", bg='#0f54d4', font=('Arial', 12, "bold"))
    napis_dodajpost.place(relx=0.02, rely=0.03, relwidth=0.45, relheight=0.05)
    
    okienko_dodaj_post = Tk.Text(main, bg='gray')
    okienko_dodaj_post.place(relx=0.02, rely=0.08, relwidth=0.45, relheight=0.25)
    
    #Wyslij Post
    
    submit = Tk.Button(main, text="Wyslij",bg='#a6a6a6',command=submit_post)
    submit.place(relx=0.02, rely=0.35, relwidth=0.45, relheight=0.05)
    
    #MiejsceNaPosty
    
    ostatnieposty = Tk.Label(main, text="Ostatnie Posty",bg='#0f54d4', font=('Arial', 12, "bold"))
    ostatnieposty.place(relx=0.50, rely=0.03, relwidth=0.48, relheight=0.05)
    
    
    posty = Tk.Frame(main,bg='#a6a6a6')
    posty.place(relx=0.50, rely=0.08, relwidth=0.48, relheight=0.9)
    
    #Post1
    
    user1 = Tk.Label(posty, text="2022-04-09, 10:02:00, Owner =", bg='#a6a6a6', anchor="w", borderwidth=4, relief="groove", highlightbackground="black" )
    user1.place(relx=0.01, rely=0.02, relwidth=0.97, relheight=0.09)
    
    post1 = Tk.Label(posty, text="Lorem ipsum, polskafdhfdkjsbfsdkjf", bg='#a6a6a6', borderwidth=4, relief="groove", highlightbackground="black", anchor="nw", font=('Arial', 10))
    post1.place(relx=0.01, rely=0.12, relwidth=0.97, relheight=0.2)
    
    #Post2
    
    user2 = Tk.Label(posty, text="2022-04-09, 10:02:00, Owner =", bg='#a6a6a6', anchor="w", borderwidth=4, relief="groove", highlightbackground="black" )
    user2.place(relx=0.01, rely=0.34, relwidth=0.97, relheight=0.09)
    
    post2 = Tk.Label(posty, text="Lorem ipsum, polskafdhfdkjsbfsdkjf", bg='#a6a6a6', borderwidth=4, relief="groove", highlightbackground="black", anchor="nw", font=('Arial', 10))
    post2.place(relx=0.01, rely=0.44, relwidth=0.97, relheight=0.2)
    
    #Post3
    
    user3 = Tk.Label(posty, text="2022-04-09, 10:02:00, Owner =", bg='#a6a6a6', anchor="w", borderwidth=4, relief="groove", highlightbackground="black" )
    user3.place(relx=0.01, rely=0.66, relwidth=0.97, relheight=0.09)
    
    post3 = Tk.Label(posty, text="Lorem ipsum, polskafdhfdkjsbfsdkjf", bg='#a6a6a6', borderwidth=4, relief="groove", highlightbackground="black", anchor="nw", font=('Arial', 10))
    post3.place(relx=0.01, rely=0.76, relwidth=0.97, relheight=0.2)
    
    
    
    main.after(1000, task)
    main.mainloop()
#show_window("Owner")