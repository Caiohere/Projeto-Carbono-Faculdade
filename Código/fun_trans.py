import customtkinter 
from tkinter import *
import tkinter as tk




def func_comb(ent, esc, label, label2, label3, label4, label5):

    #pegar as informações do usuário
    dados1 = ent.get()
    dados2 = esc.get()
    dados1 = int(dados1)

    #números para o calculo de gasolina
    gasolina = 0.82
    dens_gasolina = 0.75
    gasol_to_co2 = 3.7

    #número para calculo de diesel
    diesel_to_co2 = 2.97


    def calculo_diesel(km_l):
        total_comb = round(dados1 / km_l, 2)
        print("Combustivel total:",total_comb)

        total_carb = total_comb * diesel_to_co2
        print("Carbono total:",round(total_carb))
        result = round(total_carb / 1000, 2)

        anual_result = round(result * 12, 1)
        budget_reais = round(result * 12, 3) * 35
        trees = round(anual_result * 7)

        label["text"] = f"{result}kg de CO2"
        label2["text"] = f"{anual_result}(t)"
        label3["text"] = f"{anual_result} credito(s)"
        label4["text"] = f"Total de R${round(budget_reais, 4)}"
        label5["text"] = f"{trees}"


    def calculo_gasol(km_l):
        total_comb = round(dados1 / km_l, 2)
        print(total_comb)

        total_carb = total_comb * gasolina * dens_gasolina * gasol_to_co2
        print(round(total_carb, 2))
        result = round(total_carb / 1000, 3)

        anual_result = round(result * 12, 2)
        budget_reais = round(result * 12, 3) * 35
        trees = round(anual_result * 7)

        label["text"] = f"{result}kg de CO2"
        label2["text"] = f"{anual_result}(t)"
        label3["text"] = f"{anual_result} credito(s)"
        label4["text"] = f"Total de R${round(budget_reais, 4)}"
        label5["text"] = f"{trees}"


    if dados2 == 'Carro a gasolina (até 1.4)':
        km_l = 11
        calculo_gasol(11)

    elif dados2 == 'Carro a gasolina (1.5 até 2.0)':
        km_l = 9.5
        calculo_gasol(9.5)
    elif dados2 == 'Carro a gasolina (acima de 2.0)':
        km_l = 7.5
        calculo_gasol(7.5)
    elif dados2 == 'Ônibus comum (diesel)':
        calculo_diesel(2.5)
    elif dados2 == 'Ônibus articulado (diesel)':
        calculo_diesel(1.5)
    else:
        print("lets groove")





def func_gas(ent1, ent2, btn1, msg, msg2, msg3, msg4, msg5):
    resp = ent1.get()
    resp = int(resp)
    resp2 = ent2.get()
    resp2 = int(resp2)
    if btn1 == "botijao":
        calc_b_m = (resp * 40)/1000
        calc_b_a = (resp*40)/1000 *12
        credit_real =  (calc_b_a *12) * 35
        if calc_b_a <  0.170:
            tree = 0
        tree = round(calc_b_a * 7)
        msg["text"] = f"{calc_b_m:.3f}kg de CO2"
        msg2["text"] = f"{calc_b_a:.3f}(t)"
        msg3["text"] = f"{calc_b_a:.2f} credito(s)"
        msg4["text"] = f"Total de R${credit_real:.2f}"
        msg5["text"] = f"{tree}"
        print(calc_b_a, 1)
    else:
        print(btn1, 3)
    if btn1 == "gas":
        calc_b_m = (resp2 * 20)/1000
        calc_b_a = (resp2*20)/1000 *12
        credit_real =  (calc_b_a *12) * 35
        if calc_b_a <  0.170:
            tree = 0
        tree = round(calc_b_a * 7)
        msg["text"] = f"{calc_b_m:.3f}kg de CO2"
        msg2["text"] = f"{calc_b_a:.3f}(t)"
        msg3["text"] = f"{calc_b_a:.2f} credito(s)"
        msg4["text"] = f"Total de R${credit_real:.2f}"
        msg5["text"] = f"{tree}"
        print(calc_b_a, 1)
    else:
        print(btn1, 4)






def func_ele(ent1, ent2, btn1, msg, msg2, msg3, msg4, msg5):
    resp = ent1.get()
    resp = int(resp)
    resp2 = ent2.get()
    resp2 = int(resp2)
    if btn1 == 'kw':
        calc_k_m = (resp * 0.0817)/1000
        calc_k_a = (resp*0.0817)/1000 *12
        credit_real =  (calc_k_a *12) * 35
        if calc_k_a <  0.170:
            tree = 0
        tree = round(calc_k_a * 7)
        msg["text"] = f"{calc_k_m:.3f}kg de CO2"
        msg2["text"] = f"{calc_k_a:.3f}(t)"
        msg3["text"] = f"{calc_k_a:.2f} credito(s)"
        msg4["text"] = f"Total de R${credit_real:.2f}"
        msg5["text"] = f"{tree}"
    elif btn1 == 'conta':
        calc_b_m = (resp * 0.14)/1000
        calc_b_a = (resp*0.14)/1000 *12
        credit_real =  (calc_b_a *12) * 35
        if calc_b_a <  0.170:
            tree = 0
        tree = round(calc_b_a * 7)
        price_tree  = tree * 28.50
        msg["text"] = f"{calc_b_m:.3f}kg de CO2"
        msg2["text"] = f"{calc_b_a:.3f}(t)"
        msg3["text"] = f"{calc_b_a:.2f} credito(s)"
        msg4["text"] = f"Total de R${credit_real:.2f}"
        msg5["text"] = f"{tree}"


def back(current_window, main_window):
    current_window.destroy()
    main_window()



def tela_princ():
    from segundatela import tela_comb
    from terceiratela import tela_ele
    from quartatela import tela_gas
    from quiz import quiz

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
    label_titulo = tk.Label(janela, text="ESCOLHA A OPÇÃO A QUAL DESEJA\n🢃", bg="white", foreground="#1a1a1a", font=("Arial", 14, "bold"))
    label_titulo.place(x=485, y=60)

    label_titulo = tk.Label(janela, text="Carbono Consciente", bg="#1a1a1a", foreground="white", font=("Arial", 13, "bold"))
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
    janela, text="      QUIZ - Teste seu conhecimento sobre carbono      ",
    fg_color="green", hover_color="#1a1a1a", 
    border_width=2, border_color="black", width=80, height=45, 
    font=("Arial", 12, "bold"), 
    text_color="white", command=open_quiz)
    botao3.place(x=500, y=450)


    janela.mainloop()

