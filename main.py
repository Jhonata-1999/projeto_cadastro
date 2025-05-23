from config import criar_janela
from login import abrir_tela_login

# Criar janela principal
app = criar_janela()

# Exibir tela de login ao iniciar
abrir_tela_login(app)

# Iniciar aplicação
app.mainloop()