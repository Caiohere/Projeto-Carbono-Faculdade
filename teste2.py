import customtkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

stage = 0

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
label_gif.place(x=420, y=100)
tela.after(0, update, 0)


#texto na tela
texto = "                                         QUIZ                                        "
rotulo = tk.Label(tela, text=texto, font=("Arial", 18, "bold"), bg="green", fg="white")
rotulo.place(x=0, y=0)
rotulo.pack()


label_titulo = tk.Label(tela, text="RESPONDA 5 PERGUNTAS E\nDESCUBRA QUAL SEU NÍVEL\nDE CONHECIMENTO\nSOBRE EMISSÃO\n DE CARBONO", bg="#1a1a1a", foreground="white", font=("Arial", 14, "bold"), justify="center")
label_titulo.place(x=6, y=80)


def grid_perguntas(num_quest=0, text= '', rd1= '', rd2='', rd3='', rd4='', num_bar=1, dele=0):
    global radios, radio, radio2, radio3, radio4, label_numero, label_pergunta, bar
    label_numero = tk.Label(tela, text=f"{num_quest}º QUESTÃO:",font=("Arial", 15, "bold"), foreground="#1a1a1a")
    label_numero.place(x=340, y=70)

    label_pergunta = tk.Label(tela, text=text, background="white", foreground="#1a1a1a", font=("Arial", 14), justify="left")
    label_pergunta.place(x=340, y=150)

    radios = StringVar()
    radio = Radiobutton(text=rd1, bg="white", font=15, value=1, variable=radios, background="#e5e2d2")
    radio.place(x=340, y=250)

    radio2 = Radiobutton(text=rd2, bg="white", font=15, value=2, variable=radios, background="#e5e2d2")
    radio2.place(x=340, y=290)

    radio3 = Radiobutton(text=rd3, bg="white", font=15, value=3, variable=radios, background="#e5e2d2")
    radio3.place(x=340, y=330)

    radio4 = Radiobutton(text=rd4, bg="white", font=15, value=4, variable=radios, background="#e5e2d2")
    radio4.place(x=340, y=370)

    bar = customtkinter.CTkProgressBar(master=tela, orientation='horizontal', mode='determinate', determinate_speed=2, progress_color="green")
    bar.place(x=50, y=400)
    bar.set(num_bar)
    if dele == 1:
        label_numero.place_forget()
        label_pergunta.place_forget()
        radio.place_forget()
        radio2.place_forget()
        radio3.place_forget()
        radio4.place_forget()
        bar.place_forget()





def comecar():
    label_gif.place_forget()
    botao_comecar.place_forget()
    grid_perguntas(num_quest=1, text="Qual é o nome do processo pelo qual a quantidade total\nde carbono é mantida na Terra, com trocas constantes entre\na atmosfera, os oceanos, a biosfera e a litosfera?", rd1="a) Ciclo da Água", rd2="b) Ciclo do Carbono", rd3="c) Ciclo do Nitrogênio", rd4="d) Ciclo do Enxofre", num_bar=0.2, dele=0)
    botao_proximo.place(x=700, y=420)


stage = 0
certas = 0
gabarito = [2, 2, 4, 1, 2]
gabarito_usu = []

def proximo():
    global certas
    global stage
    if stage == 0:
        pass
    else:
        stage += 1
    choosen = radios.get()
    gabarito_usu.append(choosen)
    stage += 1
    print("gabarito do usuario: ", gabarito_usu)
    print("estagio:", stage)
    if stage == 1:
        grid_perguntas(num_quest=2, text="Qual é o principal fator responsável pelo aumento das concentrações de dióxido de carbono (CO2) na atmosfera nas últimas décadas?", rd1="a) Atividades vulcânicas", rd2="b) Uso de combustíveis fósseis", rd3="c) Emissões de metano (CH4)", rd4="d) Queimadas florestais", num_bar=0.4, dele=0)
        choosen = radios.get()
        if choosen != "":
            gabarito_usu.append(choosen)
        print("gabarito do usuario: ", gabarito_usu)
    elif stage == 3:
        grid_perguntas(num_quest=3, text="Qual setor é responsável pelas maiores emissões de carbono na maioria dos países?", rd1="a) Transporte", rd2="b) Agricultura", rd3="c) Indústria", rd4="d) Energia", num_bar=0.6, dele=0)
        choosen = radios.get()
        if choosen != "":
            gabarito_usu.append(choosen)
        print("gabarito do usuario: ", gabarito_usu)
    elif stage == 5:
        grid_perguntas(num_quest=4, text="O Protocolo de Quioto é um acordo internacional destinado a reduzir as emissões de gases de efeito estufa. Em que ano entrou em vigor?", rd1="a) 1997", rd2="b) 2000", rd3="c) 2005", rd4="d) 2010", num_bar=0.8, dele=0)
        choosen = radios.get()
        if choosen != "":
            gabarito_usu.append(choosen)
    elif stage == 7:
        grid_perguntas(num_quest=5, text='Qual é o conceito de "neutralidade de carbono"?', rd1="a) Não emitir carbono de forma alguma", rd2="b) Compensar todas as emissões de carbono com a remoção equivalente", rd3="c) Utilizar energia renovável para todas as atividades", rd4="d) Diminuir a produção de carbono em 50%", num_bar=1, dele=0)
        choosen = radios.get()
        if choosen != "":
            gabarito_usu.append(choosen)
    elif stage > 7:
        grid_perguntas(dele=1)

botao_comecar = customtkinter.CTkButton(tela, text="COMEÇAR", fg_color="green", hover_color="#1a1a1a", border_width=2, border_color="white", width=120, height=50, font=("Arial", 20, "bold"), text_color="white", anchor="center", command=comecar)
botao_comecar.place(x=85.5, y=270)


botao_proximo = customtkinter.CTkButton(tela, text="Próxima  >", fg_color="#e5e2d2", hover_color="white", border_width=4, border_color="black", width=120, height=50, font=("Arial", 20, "bold"), text_color="#1a1a1a", anchor="center", command=proximo)


tela.mainloop()