import tkinter as tk 
from tkinter import LabelFrame, Button, Label, PhotoImage
import random

def usuario_joga_pedra(escolha_computador):
    if escolha_computador == 'Papel':
        mensagem = f"""
                Sua escolha: Pedra 
                Escolha do computador: {escolha_computador}
                Papel cobre Pedra
                COMPUTADOR GANHOU!
                   """
    elif escolha_computador == 'Tesoura':
        mensagem = f"""
                Sua escolha: Pedra 
                Escolha do computador: {escolha_computador}
                Pedra quebra Tesoura
                VOCÊ GANHOU!
                   """
    elif escolha_computador == 'Lagarto':
        mensagem = f"""
                Sua escolha: Pedra 
                Escolha do computador: {escolha_computador}
                Pedra esmaga lagarto
                VOCÊ GANHOU!
                   """
    elif escolha_computador == 'Spock':
        mensagem = f"""
                Sua escolha: Pedra 
                Escolha do computador: {escolha_computador}
                Spock vaporiza Pedra
                COMPUTADOR GANHOU!
                   """   

    resultado.config(text=mensagem)


def usuario_joga_papel(escolha_computador):
    if escolha_computador == 'Pedra':
        mensagem = f"""
                Sua escolha: Papel 
                Escolha do computador: {escolha_computador}
                Papel cobre Pedra
                VOCÊ GANHOU!
                   """
    elif escolha_computador == 'Tesoura':
        mensagem = f"""
                Sua escolha: Papel 
                Escolha do computador: {escolha_computador}
                Tesoura corta Papel
                COMPUTADOR GANHOU!
                   """
    elif escolha_computador == 'Lagarto':
        mensagem = f"""
                Sua escolha: Papel 
                Escolha do computador: {escolha_computador}
                Lagarto come Papel
                COMPUTADOR GANHOU!
                   """
    elif escolha_computador == 'Spock':
        mensagem = f"""
                Sua escolha: Papel 
                Escolha do computador: {escolha_computador}
                Papel refuta Spock
                VOCÊ GANHOU!
                   """   

    resultado.config(text=mensagem)


def usuario_joga_tesoura(escolha_computador):
    if escolha_computador == 'Papel':
        mensagem = f"""
                Sua escolha: Tesoura 
                Escolha do computador: {escolha_computador}
                Tesoura corta Papel
                VOCÊ GANHOU!
                   """
    elif escolha_computador == 'Pedra':
        mensagem = f"""
                Sua escolha: Tesoura 
                Escolha do computador: {escolha_computador}
                Pedra quebra Tesoura
                COMPUTADOR GANHOU!
                   """
    elif escolha_computador == 'Lagarto':
        mensagem = f"""
                Sua escolha: Tesoura 
                Escolha do computador: {escolha_computador}
                Tesoura decapita Lagarto
                VOCÊ GANHOU!
                   """
    elif escolha_computador == 'Spock':
        mensagem = f"""
                Sua escolha: Tesoura
                Escolha do computador: {escolha_computador}
                Spock esmaga Tesoura
                COMPUTADOR GANHOU!
                   """   

    resultado.config(text=mensagem)


def usuario_joga_lagarto(escolha_computador):
    if escolha_computador == 'Papel':
        mensagem = f"""
                Sua escolha: Lagarto 
                Escolha do computador: {escolha_computador}
                Lagarto come papel
                VOCÊ GANHOU!
                   """
    elif escolha_computador == 'Tesoura':
        mensagem = f"""
                Sua escolha: Lagarto
                Escolha do computador: {escolha_computador}
                Tesoura decapita Lagarto
                COMPUTADOR GANHOU!
                   """
    elif escolha_computador == 'Pedra':
        mensagem = f"""
                Sua escolha: Lagarto 
                Escolha do computador: {escolha_computador}
                Pedra esmaga lagarto
                COMPUTADOR GANHOU!
                   """
    elif escolha_computador == 'Spock':
        mensagem = f"""
                Sua escolha: Lagarto
                Escolha do computador: {escolha_computador}
                Lagarto envenena Spock
                VOCÊ GANHOU!
                   """   

    resultado.config(text=mensagem)


def usuario_joga_spock(escolha_computador):
    if escolha_computador == 'Papel':
        mensagem = f"""
                Sua escolha: Spock 
                Escolha do computador: {escolha_computador}
                Papel refuta Spock
                COMPUTADOR GANHOU!
                   """
    elif escolha_computador == 'Tesoura':
        mensagem = f"""
                Sua escolha: Spock 
                Escolha do computador: {escolha_computador}
                Spock esmaga tesoura
                VOCÊ GANHOU!
                   """
    elif escolha_computador == 'Lagarto':
        mensagem = f"""
                Sua escolha: Spock 
                Escolha do computador: {escolha_computador}
                Lagarto envenena Spock
                COMPUTADOR GANHOU!
                   """
    elif escolha_computador == 'Pedra':
        mensagem = f"""
                Sua escolha: Spock 
                Escolha do computador: {escolha_computador}
                Spock vaporiza Pedra
                VOCÊ GANHOU!
                   """   

    resultado.config(text=mensagem)

def jokenpo(escolha_usuario):
    escolha_computador = random.choice(['Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock'])

    
    if escolha_usuario == escolha_computador:
        mensagem = f"""
        Sua escolha: {escolha_usuario} 
        Escolha do computador: {escolha_computador}
        EMPATE!
                   """
        resultado.config(text=mensagem)
                    
    elif escolha_usuario == 'Pedra':
        usuario_joga_pedra(escolha_computador)
    elif escolha_usuario == 'Papel':
        usuario_joga_papel(escolha_computador)
    elif escolha_usuario == 'Tesoura':
        usuario_joga_tesoura(escolha_computador)
    elif escolha_usuario == 'Lagarto':
        usuario_joga_lagarto(escolha_computador)
    elif escolha_usuario == 'Spock':
        usuario_joga_spock(escolha_computador)


janela = tk.Tk()
frame = LabelFrame(janela, text="Qual você escolhe?", padx=10, pady=10)
frame.pack()

icone_pedra = PhotoImage(file='png/pedra.png')
icone_papel = PhotoImage(file='png/papel.png')
icone_tesoura = PhotoImage(file='png/tesoura.png')
icone_lagarto = PhotoImage(file='png/lagarto.png')
icone_spock = PhotoImage(file='png/spock.png')

Button(frame, text='Pedra', command=lambda:jokenpo('Pedra'), image=icone_pedra, compound=tk.LEFT).grid(column=1, row=1)
Button(frame, text='Papel', command=lambda:jokenpo('Papel'), image=icone_papel, compound=tk.LEFT).grid(column=2, row=1)
Button(frame, text='Tesoura', command=lambda:jokenpo('Tesoura'), image=icone_tesoura, compound=tk.LEFT).grid(column=3, row=1)
Button(frame, text='Lagarto', command=lambda:jokenpo('Lagarto'), image=icone_lagarto, compound=tk.LEFT).grid(column=4, row=1)
Button(frame, text='Spock', command=lambda:jokenpo('Spock'), image=icone_spock, compound=tk.LEFT).grid(column=5, row=1)

resultado = Label(frame, pady=10, padx=10, justify=tk.LEFT)
resultado.grid(column=1, row=2, columnspan=4)

janela.title('Pedra, Papel, Tesoura, Lagarto e Spock')
janela.geometry("500x200+700+200")
janela.mainloop()