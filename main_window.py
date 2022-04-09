# -*- coding: utf-8 -*-
import tkinter as Tk
import psycopg2
from datetime import datetime

conn = psycopg2.connect("dbname=postgres user=postgres password=Elorado123*")




    


def show_window(login):
    
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
    
    
    main = Tk.Tk()
    main.geometry("550x550") 
    main.title('Postownia')
    main.config(bg='#0f54d4')
    main.iconbitmap(r'C:\Users\szymo\Desktop\Szymon\AplikacjaPY\2824438_academic_clip_exam_note_paper_icon.ico')
    
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
    
    
    posty = Tk.Label(main, text="",bg='#a6a6a6', font=('Arial', 12, "bold"))
    posty.place(relx=0.50, rely=0.08, relwidth=0.48, relheight=0.9)
    
    
    
    
    
    
    main.mainloop()
    