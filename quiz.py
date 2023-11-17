import customtkinter
from tkinter import *
import tkinter as tk8
from fun_trans import *

stage = 0
cont = 0
fim = 0
pontos = 0
def quiz():
    print(cont)

    gabarito = {'questao 1': 2, 'questao 2':  2, 'questao 3': 4, 'questao 4': 1, 'questao 5': 2}
    gabarito_usu = []

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    tela = customtkinter.CTk()
    tela.geometry("900x500")
    tela.title("CO2 Por consumo de combustível")
    tela.iconbitmap("")
    tela.resizable(False, False)



    #frame
    frame = customtkinter.CTkFrame(master=tela, width=600, height=600, fg_color="white")
    frame.pack(side=RIGHT)


    frameCnt = 12
    frames = [PhotoImage(file='imagens/terrinha.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]




    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label_gif.configure(image=frame)
        tela.after(100, update, ind)

    label_gif = Label(tela)
    label_gif.place(x=430, y=110)
    tela.after(0, update, 0)




    def get_certas():
        global pontos
        label_numero.place_forget()
        label_pergunta.place_forget()
        radio.place_forget()
        radio2.place_forget()
        radio3.place_forget()
        radio4.place_forget()
        bar.place_forget()
        botao_proximo.place_forget()
        label_titulo.place_forget()
        lista_certas = []
        lista_erradas = []
        if gabarito_usu[0] == "2":
            pontos +=1
            lista_certas.append("1")
        else:
            lista_erradas.append("1")
        if gabarito_usu[1] == "2":
            pontos +=1
            lista_certas.append("2")
        else:
            lista_erradas.append("2")
        if gabarito_usu[2] == "4":
            pontos +=1
            lista_certas.append("3")
        else:
            lista_erradas.append("3")
        if gabarito_usu[3] == "1":
            pontos +=1
            lista_certas.append("4")
        else:
            lista_erradas.append("4")
        if gabarito_usu[4] == "2":
            pontos +=1
            lista_certas.append("5")
        else:
            lista_erradas.append("5")
        
        if len(lista_certas) == 0:
            lista_certas.append("Nenhuma!")
        if len(lista_erradas) == 0:
            lista_erradas.append("Nenhuma!")
        label_acertos = tk.Label(tela, text="Questões certas: ", background="#e5e2d2", foreground="#1a1a1a", font=("Arial", 17), justify="left")
        label_acertos.place(x=315, y=230)

        label_erradas = tk.Label(tela, text="Questões erradas: ", background="#e5e2d2", foreground="#1a1a1a", font=("Arial", 17), justify="left")
        label_erradas.place(x=315, y=325)

        label_pontuacao_certas = Label(tela, text=lista_certas, background="white", foreground="#1a1a1a", font=("Arial", 18), justify="left")
        label_pontuacao_certas.place(x=350, y=275)

        label_certa = Label(tela, text="✓",font=("Arial", 18, "bold"), foreground="green", bg="white")
        label_certa.place(x=315, y=275)

        label_pontuacao_erradas = Label(tela, text=lista_erradas, background="white", foreground="#1a1a1a", font=("Arial", 18), justify="left")
        label_pontuacao_erradas.place(x=350, y=385)
        
        label_erro = Label(tela, text="X",font=("Arial", 18, "bold"), foreground="red", bg="white")
        label_erro.place(x=315, y=385)

        botao_voltar = customtkinter.CTkButton(tela, text="X", fg_color="green", hover_color="green", border_width=2, border_color="white", width=40, height=15, font=("Arial", 20, "bold"), text_color="white", corner_radius=0, command=close_all)
        botao_voltar.place(x=3, y=1.5)

        #grid_pontuação
        label_pontos_msg = Label(tela, text="Sua pontuação: ",font=("Arial", 20, "bold"), foreground="white", bg="#1a1a1a")
        label_pontos_msg.place(x=45, y=150)
        label_pontos = Label(tela, text=f"{pontos}/5",font=("Arial", 50, "bold"), foreground="white", bg="#1a1a1a")
        label_pontos.place(x=90, y=230)
        if pontos == 5:
            print(pontos)
            label_msg_acertos["text"] = "Parabéns! Você está no caminho certo na jornada para\nreduzir a emissão de carbono. Acertou todas as questões,\ndemonstrando um comprometimento em aprender e fazer a\ndiferença no combate às mudanças climáticas. \nContinue assim!"
            label_msg_acertos.place(x=315, y=80)
            label_msg_acertos2["text"] = "UM GÊNIO?"
            label_msg_acertos2.place(x=480, y=20)
            label_acertos.place(x=315, y=230)
        elif pontos == 3 or pontos == 4:
            print(pontos)
            label_msg_acertos["text"] = "Parabéns! Você demonstrou um bom conhecimento sobre a\nemissão de carbono ao acertar mais da metade das questões.\n Seu comprometimento em aprender e contribuir para um\nplaneta mais sustentável é admirável. Continue a sua\njornada de aprendizado e ação"
            label_msg_acertos.place(x=310, y=100)
            label_msg_acertos2["text"] = "PESSOA ECOLÓGICA!"
            label_msg_acertos2.place(x=390, y=20)
            label_acertos.place(x=315, y=230)
        elif pontos == 2 or pontos == 1:
            label_msg_acertos["text"] = "Parabéns pelo seu esforço! Embora você não tenha acertado\ntodas as questões, cada tentativa é um passo em direção a\num futuro mais sustentável. Continue aprendendo e se\nenvolvendo na luta contra a emissão de carbono."
            label_msg_acertos.place(x=310, y=100)
            label_msg_acertos2["text"] = "APRENDER SEMPRE!"
            label_msg_acertos2.place(x=390, y=20)
            label_acertos.place(x=315, y=230)
        elif pontos == 0:
            label_msg_acertos["text"] = "Não desanime! O conhecimento é construído através da\nexperiência, e mesmo que você tenha errado todas\nas questões, a participação já é um passo na direção certa.\nContinue aprendendo e explorando informações sobre\nemissão de carbono. Com o tempo, você também\npoderá fazer a diferença!"
            label_msg_acertos.place(x=310, y=70)
            label_msg_acertos2["text"] = "ESTÁ TUDO BEM!"
            label_msg_acertos2.place(x=420, y=10)
            label_acertos.place(x=315, y=230)


        
            


    #texto na tela
    texto = "                                         QUIZ                                        "
    rotulo = tk.Label(tela, text=texto, font=("Arial", 18, "bold"), bg="green", fg="white")
    rotulo.place(x=0, y=0)
    rotulo.pack()


    def close_all():
        tela.destroy()



    label_titulo = tk.Label(tela, text="RESPONDA 5 PERGUNTAS E\nDESCUBRA QUAL SEU NÍVEL\nDE CONHECIMENTO SOBRE\nEMISSÃO DE CARBONO", bg="#1a1a1a", foreground="white", font=("Arial", 14, "bold"), justify="center")
    label_titulo.place(x=6, y=80)


    label_erradas = tk.Label(tela, text="Questões erradas: ", background="#e5e2d2", foreground="#1a1a1a", font=("Arial", 17), justify="left")


    label_msg_acertos = tk.Label(tela, text="", background="#e5e2d2", foreground="green", font=("Arial", 15, "bold"), justify="left")

    label_msg_acertos2 = tk.Label(tela, text="", background="white", foreground="green", font=("Arial", 30, "bold"), justify="center")


    label_numero = tk.Label(tela, text="1º QUESTÃO:",font=("Arial", 15, "bold"), foreground="#1a1a1a")


    label_pergunta = tk.Label(tela, text="Qual é o nome do processo pelo qual a quantidade total\nde carbono é mantida na Terra, com trocas constantes entre\na atmosfera, os oceanos, a biosfera e a litosfera?", background="white", foreground="#1a1a1a", font=("Arial", 14), justify="left")


    radios = StringVar()
    radio = Radiobutton(text="a) Ciclo da Água", bg="white", font=15, value=1, variable=radios, background="#e5e2d2")


    radio2 = Radiobutton(text="b) Ciclo do Carbono", bg="white", font=15, value=2, variable=radios, background="#e5e2d2")


    radio3 = Radiobutton(text="c) Ciclo do Nitrogênio", bg="white", font=15, value=3, variable=radios, background="#e5e2d2")


    radio4 = Radiobutton(text="d) Ciclo do Enxofre", bg="white", font=15, value=4, variable=radios, background="#e5e2d2")


    bar = customtkinter.CTkProgressBar(master=tela, orientation='horizontal', mode='determinate', determinate_speed=2, progress_color="green", width=500)
    bar.set(0.2)



    #grid_pontuação
    label_pontos_msg = Label(tela, text="Sua pontuação: ",font=("Arial", 20, "bold"), foreground="white", bg="#1a1a1a")

    label_pontos = Label(tela, text=f"{pontos}/5",font=("Arial", 50, "bold"), foreground="white", bg="#1a1a1a")





    def comecar():
        label_gif.place_forget()
        botao_comecar.place_forget()

        label_numero.place(x=340, y=70)

        label_pergunta.place(x=340, y=150)

        radio.place(x=340, y=250)

        radio2.place(x=340, y=290)

        radio3.place(x=340, y=330)

        radio4.place(x=340, y=370)

        bar.place(x=350, y=450)

        botao_proximo.place(x=750, y=370)
    

        




    def get():
        choosen = radios.get()
        gabarito_usu.append(choosen)

    def proximo():
        global pontos
        global cont
        global fim
        get()
        cont += 1
        if cont == 1:
            label_numero.place(x=340, y=70)
            label_numero["text"] = "2º QUESTÃO:"

            label_pergunta.place(x=340, y=150)
            label_pergunta["text"] = "Qual é o principal fator responsável pelo aumento das\nconcentrações de dióxido de carbono (CO2) na atmosfera\nnas últimas décadas?"

            radio.place(x=340, y=250)
            radio["text"] = "a) Atividades vulcânicas"

            radio2.place(x=340, y=290)
            radio2["text"] = "b) Uso de combustíveis fósseis"

            radio3.place(x=340, y=330)
            radio3["text"] = "c) Emissões de metano (CH4)"

            radio4.place(x=340, y=370)
            radio4["text"] = "d) Queimadas florestais"
            
            bar.place(x=350, y=450)
            bar.set(0.4)
            #if get_cont != 1:
            #    get()
            #    get_cont += 1
        elif cont == 2:
            label_numero.place(x=340, y=70)
            label_numero["text"] = "3º QUESTÃO:"

            label_pergunta.place(x=340, y=150)
            label_pergunta["text"] = "Qual setor é responsável pelas maiores emissões de carbono\nna maioria dos países?"

            radio.place(x=340, y=250)
            radio["text"] = "a) Transporte"

            radio2.place(x=340, y=290)
            radio2["text"] = "b) Agricultura"

            radio3.place(x=340, y=330)
            radio3["text"] = "c) Indústria"

            radio4.place(x=340, y=370)
            radio4["text"] = "d) Energias"
            
            bar.place(x=350, y=450)
            bar.set(0.6)
        elif cont == 3:
            label_numero.place(x=340, y=70)
            label_numero["text"] = "4º QUESTÃO:"

            label_pergunta.place(x=340, y=150)
            label_pergunta["text"] = "O Protocolo de Quioto é um acordo internacional destinado\na reduzir as emissões de gases de efeito estufa.\nEm que ano entrou em vigor?"

            radio.place(x=340, y=250)
            radio["text"] = "a) 1997"

            radio2.place(x=340, y=290)
            radio2["text"] = "b) 2000"

            radio3.place(x=340, y=330)
            radio3["text"] = "c) 2005"

            radio4.place(x=340, y=370)
            radio4["text"] = "d) 2010"
            
            bar.place(x=350, y=450)
            bar.set(0.8)
        elif cont == 4:
            label_numero.place(x=340, y=70)
            label_numero["text"] = "5º QUESTÃO:"

            label_pergunta.place(x=340, y=150)
            label_pergunta["text"] = 'Qual é o conceito de "neutralidade de carbono"?'

            radio.place(x=340, y=250)
            radio["text"] = "a) Não emitir carbono de forma alguma"

            radio2.place(x=340, y=290)
            radio2["text"] = "b) Compensar todas as emissões de carbono com a remoção equivalente"

            radio3.place(x=340, y=330)
            radio3["text"] = "c) Utilizar energia renovável para todas as atividades"

            radio4.place(x=340, y=370)
            radio4["text"] = "d) Diminuir a produção de carbono em 50%"
            
            bar.place(x=350, y=450)
            bar.set(1)
            fim = 1
        elif fim == 1:
            get_certas()



    botao_comecar = customtkinter.CTkButton(tela, text="COMEÇAR", fg_color="green", hover_color="#1a1a1a", border_width=2, border_color="white", width=120, height=50, font=("Arial", 20, "bold"), text_color="white", anchor="center", command=comecar)
    botao_comecar.place(x=85.5, y=270)


    botao_proximo = customtkinter.CTkButton(tela, text="Próxima  >", fg_color="#e5e2d2", hover_color="white", border_width=4, border_color="black", width=120, height=50, font=("Arial", 20, "bold"), text_color="#1a1a1a", anchor="center", command=proximo)


    tela.mainloop()
