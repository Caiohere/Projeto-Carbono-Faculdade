import customtkinter 
from tkinter import *
import tkinter as tk
from segundatela import tela_comb
from terceiratela import tela_ele
from quartatela import tela_gas
from quiz import quiz


#funçoes
def tela_princ():
    
    #fontes,cores
    fonte = ("Arial", 18, "bold")
    fonte1 = ("Arial", 10, )
    cor_defundo = "white"
    cor_defundo1 = "green"
    cor_defundo2 = "black"
    cor_texto = "white"
    cor_texto1 = "blue"

    #janela principal
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    janela = customtkinter.CTk()
    janela.geometry("900x500")
    janela.title("Cálculadora de CO₂")
    janela.iconbitmap("")
    janela.resizable(False, False)

    #texto na tela
    texto = "                                               CÁLCULADORA DE CO2                                         "
    rotulo = tk.Label(janela, text=texto, font=fonte, bg=cor_defundo1, fg=cor_texto)
    rotulo.place(x=-1, y=0)
    rotulo.pack()

    #trabalhando com a imagem da tela
    img = PhotoImage(file="icones interface/Design_sem_nome__5_-removebg-preview.png")
    label_img = customtkinter.CTkLabel(master=janela, image=img, text="")
    label_img.place(x=40, y=100)

    #frame
    frame = customtkinter.CTkFrame(master=janela, width=500, height=600, fg_color=cor_defundo,)
    frame.pack(side=RIGHT)

    #barra divisoria 
    label = tk.Label(janela, text="_" * 10000,bg="white" , font=("Arial", 15))
    label.place(x=400, y=100)

    # texto  no frame
    label_titulo = tk.Label(janela, text="ESCOLHA A OPÇÃO A QUAL DESEJA\n🢃", 
    bg="white", foreground="#1a1a1a", font=("Arial", 14, "bold"))
    label_titulo.place(x=485, y=60)

    label_titulo = tk.Label(janela, text="Carbono Consciente", 
    bg="#1a1a1a", foreground="white", font=("Arial", 13, "bold"))
    label_titulo.place(x=10, y=460)


    def open_tela1():
        janela.destroy()
        tela_comb()

    def open_tela2():
        janela.destroy()
        tela_ele()

    def open_tela3():
        janela.destroy()
        tela_gas()

    def open_quiz():
        janela.destroy()
        quiz()

    #botao1
    botao = customtkinter.CTkButton(
    janela, text="    Emissão de CO2 por consumo de combustível      ", 
    fg_color="green", hover_color="#1a1a1a", border_width=2,
    border_color="black",
    width=80, height=50, font=("Arial", 12, "bold"),
    text_color="white", command=open_tela1)
    botao.place(x=500, y=150)

    #botao2
    botao2 = customtkinter.CTkButton(
    janela, text="  Emissão de CO2 por consumo de energia elétrica  ", 
    fg_color="green", hover_color="#1a1a1a", border_width=2, 
    border_color="black", width=80, height=50, font=("Arial", 12, "bold"), 
    text_color="white", command= open_tela2)
    botao2.place(x=500, y=250)

    #botao3
    botao3 = customtkinter.CTkButton(
    janela, text="   Emissão de CO2 por consumo de gás de cozinha   ", 
    fg_color="green", hover_color="#1a1a1a", 
    border_width=2, border_color="black", width=80, height=50, 
    font=("Arial", 12, "bold"), 
    text_color="white", command= open_tela3)
    botao3.place(x=500, y=350)

    #botao4
    botao3 = customtkinter.CTkButton(
    janela, text="     QUIZ - Teste seu conhecimento sobre carbono      ",
    fg_color="green", hover_color="#1a1a1a", 
    border_width=2, border_color="black", width=80, height=45, 
    font=("Arial", 12, "bold"), 
    text_color="white", command=open_quiz)
    botao3.place(x=500, y=450)

    janela.mainloop()

tela_princ()