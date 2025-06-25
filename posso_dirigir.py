import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.title("Verificação de habilitação")
janela.geometry("800x400")


def verificar_habilitacao():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
   
    if not nome or not idade:
        messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
        return

    try:
        idade = int(idade)
    except ValueError:
        messagebox.showwarning("Erro","A idade precisa ser um número inteiro.")
        return
 
    if idade >= 18:
        resultado_label.configure(text=f"{nome}, você está apto(a) a dirigir!", text_color="green")
    else:
        resultado_label.configure(text=f"{nome}, você NÃO está apto(a) a dirigir.", text_color="red")

# Executa a função
label_nome = ctk.CTkLabel(janela, text="Digite seu nome:")
label_nome.pack(pady=20)

entrada_nome = ctk.CTkEntry(janela, width=200)
entrada_nome.pack(pady=20)

label_idade = ctk.CTkLabel(janela, text="Digite sua idade:")
label_idade.pack(pady=20)

entrada_idade = ctk.CTkEntry(janela, width=200)
entrada_idade.pack(pady=20)

def Verificar_habilitacao():
 nome = entrada_nome.get()
 idade = entrada_idade.get()
 resultado_label.configure(text="")

botao_verificar = ctk.CTkButton(janela, text="Verificar Habilitação", command=verificar_habilitacao)
botao_verificar.pack(pady=10)


resultado_label = ctk.CTkLabel(janela, text="")
resultado_label.configure(text="")
resultado_label.pack(pady=10)
janela.mainloop()
