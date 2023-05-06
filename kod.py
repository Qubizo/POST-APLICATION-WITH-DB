# -*- coding: utf-8 -*-
import tkinter as Tk
import sys
import os
import psycopg2


def potwierdzanie_kodu(login,code):
    



    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
    
    def  czy_kod_dobry(code,login):
        DB_NAME = os.getenv('DB_NAME')
        DB_HOST = os.getenv('DB_HOST')
        DB_USER = os.getenv('DB_USER')
        DB_PORT = os.getenv('DB_PORT')
        DB_PASSWORD = os.getenv('DB_PASSWORD')
        conn = psycopg2.connect(f"port={DB_PORT} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST}")
        kod_u = okienko_wpisz_Nazwe.get()
        if code == kod_u:
            sql =  f""" update "Users" set kod_p = 'true' where login = '{login}' """
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            cur.close()
            main.destroy()
    
    
    #Główne konto
    main = Tk.Tk()
    main.geometry("350x350") 
    main.title('KOD')
    main.iconbitmap(resource_path(r'2824438_academic_clip_exam_note_paper_icon.ico'))
    main.config(bg='#0f54d4')
    #Kod
    napis_kod = Tk.Label(main, text="Wpisz kod:", bg='#0f54d4', font=('Arial', 12, "bold"))
    napis_kod.place(relx=0.125, rely=0.2, relwidth=0.75, relheight=0.05)
    #Napis Kod
    napis_rejestracja = Tk.Label(main, text="KOD POTWIERDZAJACY", bg='#0f54d4', font=('Arial', 12, "bold"))
    napis_rejestracja.place(relx=0.125, rely=0.1, relwidth=0.75, relheight=0.05)
    #Wpisz kod
    okienko_wpisz_Nazwe = Tk.Entry(main, bg='#a6a6a6')
    okienko_wpisz_Nazwe.place(relx=0.125, rely=0.4, relwidth=0.75, relheight=0.06)
    
    #Przycisk_Rejestracja
    Rejestracja_Button = Tk.Button(main, text='POTWIERDZ',bg='#a6a6a6', font=('Arial', 14, "bold"), command=lambda:czy_kod_dobry(code, login))
    Rejestracja_Button.place(relx=0.125, rely=0.5, relwidth=0.75, relheight=0.06)
    
    main.mainloop()
