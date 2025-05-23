import sqlite3
import customtkinter as ctk

#configurar aparencia
ctk.set_appearance_mode('dark')

#criar janela principal
def criar_janela():
    app = ctk.CTk()
    app.title("Sistema de Login e Cadastro")
    app.geometry("800x600")
    return app
