import sqlite3
import customtkinter as ctk
from cadastro import abrir_tela_cadastro

def abrir_tela_login(app):
    frame_login = ctk.CTkFrame(app)
    frame_login.pack(expand=True, fill="both")

    label_usuario = ctk.CTkLabel(frame_login, text="Usuário")
    label_usuario.pack(pady=10)
    campo_usuario = ctk.CTkEntry(frame_login, placeholder_text="Digite seu usuário")
    campo_usuario.pack(pady=10)

    label_senha = ctk.CTkLabel(frame_login, text="Senha")
    label_senha.pack(pady=10)
    campo_senha = ctk.CTkEntry(frame_login, placeholder_text="Digite sua senha", show="*")
    campo_senha.pack(pady=10)

    botao_login = ctk.CTkButton(frame_login, text="Login", command=lambda: print("Login realizado!"))
    botao_login.pack(pady=10)

    botao_cadastro = ctk.CTkButton(frame_login, text="Ir para Cadastro", command=lambda: abrir_tela_cadastro(app))
    botao_cadastro.pack(pady=10)

