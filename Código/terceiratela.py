import customtkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from fun_trans import *


def tela_ele():
    #fontes,cores
    fonte = ("Arial", 18, "bold")
    fonte1 = ("Arial", 10, )
    cor_defundo = "white"
    cor_defundo1 = "green"
    cor_defundo2 = "black"
    cor_texto = "white"
    cor_texto1 = "blue"

    #janela2principal
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    terceira_janela = customtkinter.CTk()
    terceira_janela.geometry("900x500")
    terceira_janela.title("CO2 Por consumo de Energia elétrica")
    terceira_janela.iconbitmap("")
    terceira_janela.resizable(False, False)

    #frame
    frame = customtkinter.CTkFrame(master=terceira_janela, width=600, height=600, fg_color=cor_defundo)
    frame.pack(side=RIGHT)

    #texto na tela
    texto = "                                         Cálcule                                        "
    rotulo = tk.Label(terceira_janela, text=texto, font=fonte, bg=cor_defundo1, fg=cor_texto)
    rotulo.place(x=-1, y=0)
    rotulo.pack()


    def open_back():
            back(terceira_janela , tela_princ)

    botao_voltar = customtkinter.CTkButton(terceira_janela, text="<", fg_color="green", hover_color="green", border_width=2, border_color="white", width=40, height=15, font=("Arial", 20, "bold"), text_color="white", corner_radius=0, command=open_back)
    botao_voltar.place(x=3, y=1.5)




    def selected_kw():
        global pressed_btn
        label_kw.place(x=20, y=240)
        entrada1.place(x=20, y=270)
        label_conta.place_forget()
        entrada2.place_forget()
        pressed_btn = "kw"
        return pressed_btn


    def selected_conta():
        global pressed_btn
        label_conta.place(x=20, y=240)
        entrada2.place(x=20, y=270)
        label_kw.place_forget()
        entrada1.place_forget()
        pressed_btn = "conta"
        return pressed_btn



    # estilo personalizado para o ComboBox
    combo_style = ttk.Style()
    combo_style.configure('Custom.TCombobox', padding=( 30, 2))


    #Entrada do usuario
    entrada1 = tk.Entry(terceira_janela, bg="white", width=35)
    entrada1.insert(END, 0)


    entrada2 = tk.Entry(terceira_janela, bg="white", width=35)
    entrada2.insert(END, 0)




    btn_kw = customtkinter.CTkButton(terceira_janela, text="Kwh/M", fg_color= "#1a1a1a", hover_color="green",border_width=2, border_color="white", width=40, height=25, font=("Arial", 20, "bold"), text_color="white", command=selected_kw)
    btn_kw.place(x=20, y=190)

    btn_conta = customtkinter.CTkButton(terceira_janela, text="Conta de energia", fg_color="#1a1a1a", hover_color="green", border_width=2, border_color="white", width=40, height=25, font=("Arial", 20, "bold"), text_color="white", command=selected_conta)
    btn_conta.place(x=110, y=190)




    #rotulo
    label_kw = tk.Label(terceira_janela, text="informe a baixo o Kwh/Mês", bg="#1a1a1a",foreground="white", font=("Arial", 10, "bold"))


    label_titulo = tk.Label(terceira_janela, text="EMISSÕES DE CO2 POR\nCONSUMO DE ENERGIA \nELÉTRICA", bg="#1a1a1a", foreground="white", font=("Arial", 14, "bold"))
    label_titulo.place(x=30, y=80)

    label_conta = tk.Label(terceira_janela, text="Valor da conta R$", bg="#1a1a1a",foreground="white", font=("Arial", 10, "bold"))


    #imagens
    img = PhotoImage(file="imagens/ico-arvore.png")
    img_label = Label(terceira_janela, image=img, borderwidth=0)
    img_label.place(x=700, y=326)

    img2 = PhotoImage(file="imagens/co2_image.png")
    img_label2 = Label(terceira_janela, image=img2, borderwidth=0)
    img_label2.place(x=390, y=340)

    #mensagem das imagens
    label_tree = tk.Label(terceira_janela, text="ARVORES/ANO ", bg="white", foreground="#1a1a1a", font=("Arial", 15), borderwidth=0)
    label_tree.place(x=690, y=440)
    label_tree_num = tk.Label(terceira_janela, text="0", bg="white", foreground="#1a1a1a", font=("Arial", 15), borderwidth=0)
    label_tree_num.place(x=755, y=460)

    label_carb_ano = tk.Label(terceira_janela, text="CARBONO/ANO\n ", bg="white", foreground="#1a1a1a", font=("Arial", 15), borderwidth=0)
    label_carb_ano.place(x=375, y=440)
    label_carb_ano_num = tk.Label(terceira_janela, text="0(t)", bg="white", foreground="#1a1a1a", font=("Arial", 15), borderwidth=0)
    label_carb_ano_num.place(x=425, y=460)


    # etiquetas ( label )
    label_carb_mes = tk.Label(terceira_janela, text="POR MÊS VAI EMITIR:",font=("Arial", 12), foreground="#1a1a1a")
    label_carb_mes.place(x=510, y=40)   
    label_carb_mes_num = tk.Label(terceira_janela, text="0kg de CO2", background="white", foreground="#1a1a1a", font=("Arial", 14))
    label_carb_mes_num.place(x=540, y=70)

    label_cred = tk.Label(terceira_janela, text="CRÉDITO(S) DE CARBONO PARA EQUIVALÊNCIA:",font=("Arial", 12), foreground="#1a1a1a")
    label_cred.place(x=410, y=120)
    label_cred_num = tk.Label(terceira_janela, text="0 crédito(s)", background="white", foreground="#1a1a1a", font=("Arial", 14))
    label_cred_num.place(x=540, y=150)

    label_cred_reais = tk.Label(terceira_janela, text="Total de R$0", background="white", foreground="#1a1a1a", font=("Arial", 14))
    label_cred_reais.place(x=520, y=180)

    #barra divisoria 
    label = tk.Label(terceira_janela, text="_" * 10000,bg="white" , font=("Arial", 15))
    label.place(x=300, y=270)

    def open_btn_energia():
        func_ele(entrada1, entrada2, pressed_btn, label_carb_mes_num, label_carb_ano_num, label_cred_num, label_cred_reais, label_tree_num)

    #Botao1
    botao = customtkinter.CTkButton(terceira_janela, text="Adicionar ao cálculo", fg_color="green", hover_color="#1a1a1a", border_width=2, border_color="white", width=80, height=50, font=("Arial", 20, "bold"), text_color="white", command=open_btn_energia)
    botao.place(x=45, y=410)

    terceira_janela.mainloop()

