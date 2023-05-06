# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

import tkinter as Tk
from tkinter import LEFT
import psycopg2
from datetime import datetime
from tkinter import END
import winsound
import sys, os

def log_step(step, fp="logging.txt"):
    with open(fp, "a") as f:
        f.write(f"{step}\n")
log_step("Udał się import bibliotek w main")        

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
load_dotenv(resource_path(".env"))
log_step("Udało się otworzyć env w main")
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PORT = os.getenv('DB_PORT')
DB_PASSWORD = os.getenv('DB_PASSWORD')


log_step("Udało się odczytać parametry logowania")
log_step(f"{DB_NAME} {DB_HOST} {DB_USER} {DB_PORT} {DB_PASSWORD}")

#conn=None
conn = psycopg2.connect(
    host=DB_HOST,
    dbname=DB_NAME,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
)
log_step("Udało się conn w main")


def show_window(login):
    
    def last_post():
        sql= '''SELECT * FROM "Posty" '''
        cur = conn.cursor()
        cur.execute(sql)
        posty = cur.fetchall()
        cur.close()
        return posty[-1:-4:-1]
    log_step("Udało się wczytać posty w main")            
    
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
    log_step("Udało się wysłać posta ")
    
    main = Tk.Tk()
    main.geometry("550x550") 
    main.title('Postownia')
    main.config(bg='#0f54d4')
    main.iconbitmap(resource_path(r'2824438_academic_clip_exam_note_paper_icon.ico'))
    log_step("Udało się wczytać ikone i tytuł")
    def task():
        posty=last_post()
        if posty[0][3] != post1["text"]:
            winsound.PlaySound(resource_path(r"C:\Users\sebix\ZajeciaEdun\POST-APLICATION-WITH-DB\MessageSaund.wav"),
                               winsound.SND_FILENAME)
            
        user1.config(text=f"{posty[0][2]}, {posty[0][1]}, {posty[0][0]}")
        post1.config(text=f"{posty[0][3]}")
        user2.config(text=f"{posty[1][2]}, {posty[1][1]}, {posty[1][0]}")
        post2.config(text=f"{posty[1][3]}")
        user3.config(text=f"{posty[2][2]}, {posty[2][1]}, {posty[2][0]}")
        post3.config(text=f"{posty[2][3]}")
        main.after(1000, task)
        log_step("Udało się wczytać dźwięk")
    
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
    
    post1 = Tk.Label(posty, text="", bg='#a6a6a6', borderwidth=4, relief="groove", highlightbackground="black", anchor="nw", font=('Arial', 10))
    post1.place(relx=0.01, rely=0.12, relwidth=0.97, relheight=0.2)
    
    #Post2
    
    user2 = Tk.Label(posty, text="2022-04-09, 10:02:00, Owner =", bg='#a6a6a6', anchor="w", borderwidth=4, relief="groove", highlightbackground="black" )
    user2.place(relx=0.01, rely=0.34, relwidth=0.97, relheight=0.09)
    
    post2 = Tk.Label(posty, text="", bg='#a6a6a6', borderwidth=4, relief="groove", highlightbackground="black", anchor="nw", font=('Arial', 10))
    post2.place(relx=0.01, rely=0.44, relwidth=0.97, relheight=0.2)
    
    #Post3
    
    user3 = Tk.Label(posty, text="2022-04-09, 10:02:00, Owner =", bg='#a6a6a6', anchor="w", borderwidth=4, relief="groove", highlightbackground="black" )
    user3.place(relx=0.01, rely=0.66, relwidth=0.97, relheight=0.09)
    
    post3 = Tk.Label(posty, text="", bg='#a6a6a6', borderwidth=4, relief="groove", highlightbackground="black", anchor="nw", font=('Arial', 10))
    post3.place(relx=0.01, rely=0.76, relwidth=0.97, relheight=0.2)
    
    
    
    main.after(1000, task)
    log_step("Udało się utworzyć gui")
    main.mainloop()
#show_window("Owner")