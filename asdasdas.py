# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import sqlite3

class ChatApp:
    def __init__(self, master):
        self.master = master
        master.title("Chat App")

        self.db_conn = sqlite3.connect("chatapp.db")
        self.db_cursor = self.db_conn.cursor()
        self.create_tables()

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.login_frame = tk.Frame(master)
        self.register_frame = tk.Frame(master)
        self.chat_frame = tk.Frame(master)

        self.login_frame.pack()
        self.register_frame.pack_forget()
        self.chat_frame.pack_forget()

        self.show_login_frame()

    def create_tables(self):
        self.db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT
            )
        """)
        self.db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS groups (
                groupname TEXT PRIMARY KEY
            )
        """)
        self.db_cursor.execute("""
            CREATE TABLE IF NOT EXISTS group_members (
                groupname TEXT,
                username TEXT,
                FOREIGN KEY (groupname) REFERENCES groups (groupname),
                FOREIGN KEY (username) REFERENCES users (username)
            )
        """)
        self.db_conn.commit()

    def show_login_frame(self):
        self.login_frame.pack()
        self.register_frame.pack_forget()
        self.chat_frame.pack_forget()

        tk.Label(self.login_frame, text="Username").grid(row=0, column=0)
        tk.Entry(self.login_frame, textvariable=self.username).grid(row=0, column=1)
        tk.Label(self.login_frame, text="Password").grid(row=1, column=0)
        tk.Entry(self.login_frame, textvariable=self.password, show="*").grid(row=1, column=1)
        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, column=0)
        tk.Button(self.login_frame, text="Register", command=self.show_register_frame).grid(row=2, column=1)

    def show_register_frame(self):
        self.login_frame.pack_forget()
        self.register_frame.pack()
        self.chat_frame.pack_forget()

        tk.Label(self.register_frame, text="Username").grid(row=0, column=0)
        tk.Entry(self.register_frame, textvariable=self.username).grid(row=0, column=1)
        tk.Label(self.register_frame, text="Password").grid(row=1, column=0)
        tk.Entry(self.register_frame, textvariable=self.password, show="*").grid(row=1, column=1)
        tk.Button(self.register_frame, text="Register", command=self.register).grid(row=2, column=0)
        tk.Button(self.register_frame, text="Back", command=self.show_login_frame).grid(row=2, column=1)

    def show_chat_frame(self):
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()
        self.chat_frame.pack()

        self.groups = self.get_groups()

        tk.Label(self.chat_frame, text="Chat App", font=("Arial", 18)).grid(row=0, column=0, columnspan=2)
        tk.Label(self.chat_frame, text="Logged in as: " + self.username.get()).grid(row=1, column=0)
        tk.Button(self.chat_frame, text="Logout", command=self.logout
