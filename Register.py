# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
import psycopg2
import tkinter as Tk
import sys
import random
from emailsender import sendemail
from kod import potwierdzanie_kodu




def register_win():
    
    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


    def przyciskReg():
        load_dotenv(resource_path(".env"))
        DB_NAME = os.getenv('DB_NAME')
        DB_HOST = os.getenv('DB_HOST')
        DB_USER = os.getenv('DB_USER')
        DB_PORT = os.getenv('DB_PORT')
        DB_PASSWORD = os.getenv('DB_PASSWORD')
        nazwa = okienko_wpisz_Nazwe.get()
        mail = okienko_wpisz_maila.get()
        haslo = okienko_wpisz_haslo.get()
        phaslo =okienko_wpisz_Phaslo.get()
        
        if haslo != phaslo:
            okienko_wpisz_Phaslo.config(bg='red')
            return
    
        conn = psycopg2.connect(f"port={DB_PORT} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST}")
        sql= '''SELECT * FROM "Users" '''
        cur = conn.cursor()
        cur.execute(sql)
        wynik = cur.fetchall()
        cur.close()
        for a in wynik:
            if a[0] == nazwa:
                okienko_wpisz_Nazwe.config(bg='red')
                return
            if a[1] == mail:
                okienko_wpisz_maila.config(bg='red')
                return
            
        znaki = list('1234567890qwertyuiopasdfghjklzxcvbnm')
        code = ''.join([random.choice(znaki) for _ in range(6)])
            
        sql= f'''INSERT INTO Public."Users" values ('{nazwa}','{mail}','{haslo}','{code}')'''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        sendemail(mail,code)
        potwierdzanie_kodu(nazwa,code)
        main.destroy()
    
    
        
        
    #Główne konto
    main = Tk.Tk()
    main.geometry("350x550") 
    main.title('Rejestracja')
    main.iconbitmap(resource_path(r'2824438_academic_clip_exam_note_paper_icon.ico'))
    main.config(bg='#0f54d4')
    #Napis Rejestracja
    
    napis_rejestracja = Tk.Label(main, text="REJESTRACJA", bg='#0f54d4', font=('Arial', 12, "bold"))
    napis_rejestracja.place(relx=0.125, rely=0.03, relwidth=0.75, relheight=0.05)
    #Rejestracja
    
    napis_rejestracja = Tk.Label(main, text="Nazwa Użytkowanika:", bg='#0f54d4', font=('Arial', 12, "bold"))
    napis_rejestracja.place(relx=0.125, rely=0.1, relwidth=0.75, relheight=0.05)
    
    okienko_wpisz_Nazwe = Tk.Entry(main, bg='#a6a6a6')
    okienko_wpisz_Nazwe.place(relx=0.125, rely=0.15, relwidth=0.75, relheight=0.05)
    
    #Mail
    
    napis_Mail = Tk.Label(main, text="Mail:", bg='#0f54d4', font=('Arial', 12, "bold"))
    napis_Mail.place(relx=0.125, rely=0.23, relwidth=0.75, relheight=0.05)
    
    okienko_wpisz_maila = Tk.Entry(main, bg='#a6a6a6')
    okienko_wpisz_maila.place(relx=0.125, rely=0.28, relwidth=0.75, relheight=0.05)
    
    #Haslo
    
    napis_haslo = Tk.Label(main, text="Hasło:", bg='#0f54d4', font=('Arial', 12, "bold"))
    napis_haslo.place(relx=0.125, rely=0.35, relwidth=0.75, relheight=0.05)
    
    okienko_wpisz_haslo = Tk.Entry(main, bg='#a6a6a6', show="*")
    okienko_wpisz_haslo.place(relx=0.125, rely=0.4, relwidth=0.75, relheight=0.05)
    
    #Powtoz haslo
    
    napis_hasloP = Tk.Label(main, text="Powtórz Hasło:", bg='#0f54d4', font=('Arial', 12, "bold"))
    napis_hasloP.place(relx=0.125, rely=0.48, relwidth=0.75, relheight=0.05)
    
    okienko_wpisz_Phaslo = Tk.Entry(main, bg='#a6a6a6', show="*")
    okienko_wpisz_Phaslo.place(relx=0.125, rely=0.53, relwidth=0.75, relheight=0.05)
    
    #CheckBox
    #c1 = Tk.Checkbutton(main, text='Zapoznałem się z REGULAMINEM', onvalue=1, offvalue=0,bg='#0f54d4')
    #c1.place(relx=0.125, rely=0.6, relwidth=0.75, relheight=0.05)
    
    #Przycisk_Rejestracja
    Rejestracja_Button = Tk.Button(main, text='ZAREJETRUJ',bg='#a6a6a6', font=('Arial', 14, "bold"), command=przyciskReg)
    Rejestracja_Button.place(relx=0.125, rely=0.7, relwidth=0.75, relheight=0.05)
    
    
    
    main.mainloop()