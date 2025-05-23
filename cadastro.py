import sqlite3
import customtkinter as ctk

# TELA DE CADASTRO
#criar funcionalidades
def abrir_tela_cadastro(app):
    frame_cadastro = ctk.CTkFrame(app)
    frame_cadastro.pack(expand=True, fill="both")

    label_nome = ctk.CTkLabel(frame_cadastro, text="Nome")
    label_nome.pack(pady=10)
    campo_nome = ctk.CTkEntry(frame_cadastro, placeholder_text="Digite seu nome")
    campo_nome.pack(pady=10)

    label_email = ctk.CTkLabel(frame_cadastro, text="Email")
    label_email.pack(pady=10)
    campo_email = ctk.CTkEntry(frame_cadastro, placeholder_text="Digite seu email")
    campo_email.pack(pady=10)

    botao_cadastro = ctk.CTkButton(frame_cadastro, text="Cadastrar", command=lambda: print("Usuário cadastrado!"))
    botao_cadastro.pack(pady=10)

    botao_tela_login = ctk.CTkButton(frame_cadastro, text="Voltar para Login", command=lambda: frame_cadastro.pack_forget())
    botao_tela_login.pack(pady=10)