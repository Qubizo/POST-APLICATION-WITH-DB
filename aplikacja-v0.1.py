# -*- coding: utf-8 -*-

import psycopg2
import tkinter as Tk
from PIL import ImageTk, Image

conn = psycopg2.connect("dbname=postgres user=postgres password=Elorado123*")

def login():
    login = okienko_wpisz_Login.get()
    print(login)
    mail = okienko_wpisz_Mail.get()
    print(mail)
    haslo = okienko_wpisz_haslo.get()
    print(haslo)
    sql= '''SELECT * FROM "Users" '''
    cur = conn.cursor()
    cur.execute(sql)
    wynik = cur.fetchall()
    cur.close()
    okienko_wpisz_Login.delete(0, 'end')
    okienko_wpisz_Mail.delete(0, 'end')
    okienko_wpisz_haslo.delete(0, 'end')
    
    for record in wynik:
        if login == record[0] and haslo == record[2] and mail == record[1]:
            print("zalogowano")
            
            break
            
            

    
    
    
    
#Glowne-Okno

main = Tk.Tk()
main.geometry("350x550") 
main.title('Logowanie')
main.iconbitmap(r'C:\Users\szymo\Desktop\Szymon\AplikacjaPY\2824438_academic_clip_exam_note_paper_icon.ico')
main.config(bg='#0f54d4')

#Login

napis_Login = Tk.Label(main, text="Login:", bg='#0f54d4', font=('Arial', 12, "bold"))
napis_Login.place(relx=0.125, rely=0.05, relwidth=0.75, relheight=0.05)

okienko_wpisz_Login = Tk.Entry(main, bg='#a6a6a6')
okienko_wpisz_Login.place(relx=0.125, rely=0.1, relwidth=0.75, relheight=0.05)

#Mail

napis_mail = Tk.Label(main, text="Podaj mail-a:",bg='#0f54d4', font=('Arial', 12, "bold"))
napis_mail.place(relx=0.125, rely=0.15, relwidth=0.75, relheight=0.05)

okienko_wpisz_Mail = Tk.Entry(main,bg='#a6a6a6',)
okienko_wpisz_Mail.place(relx=0.125, rely=0.2, relwidth=0.75, relheight=0.05)

#Hasło

napis_haslo = Tk.Label(main, text="Podaj hasło:",bg='#0f54d4', font=('Arial', 12, "bold"))
napis_haslo.place(relx=0.125, rely=0.25, relwidth=0.75, relheight=0.05)

okienko_wpisz_haslo = Tk.Entry(main,bg='#a6a6a6',show="*")
okienko_wpisz_haslo.place(relx=0.125, rely=0.3, relwidth=0.75, relheight=0.05)

#Zaloguj

submit = Tk.Button(main, text="Zaloguj", command=login)
submit.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.05)

#Zdjęcie



img = (Image.open("mewaa.jpg"))


resized_image= img.resize((325,215), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

label = Tk.Label(main, image = new_image, bg= '#0f54d4')
label.place(relx=0, rely=0.5, relwidth=1)





main.mainloop()