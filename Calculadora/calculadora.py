from tkinter import *

root = Tk()
root.title("Calculadora")
root.configure(bg="black")
cor_botao = "black"
cor_letra = "white"

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=70, padx=10, pady=10)

def botao_clicar(numero):
    anterior = e.get()

    e.delete(0, END)
    e.insert(0, anterior + numero)

def botao_limpar_tudo():
    e.delete(0, END)

def botao_limpar_ultimo_caracter():
    valor = e.get()
    if valor:
        tamanho = len(valor)
        e.delete(tamanho-1, END)

def calcular_valor():
    try:
        segundo_numero = e.get()
        e.delete(0, END)
        
        if math == "+":
            e.insert(0, p_num + int(segundo_numero))
        elif math == "-":
            e.insert(0, p_num - int(segundo_numero))
        elif math == "/":
            e.insert(0, p_num / int(segundo_numero))
        else:
            e.insert(0, p_num * int(segundo_numero))
    except:
        e.insert(0, " ")

def tipo_operador(simbolo):
    primeiro_numero = e.get()
    global p_num
    global math 
    math = simbolo 
    try:
        p_num = int(primeiro_numero)
        e.delete(0, END)
    except:
        e.delete(0, END)
    
botao_1 = Button(root, text="1", padx=20, pady=20, font=5, bg=cor_botao, fg=cor_letra, command=lambda: botao_clicar('1'))
botao_2 = Button(root, text="2", padx=20, pady=20, font=5, bg=cor_botao, fg=cor_letra, command=lambda: botao_clicar('2'))
botao_3 = Button(root, text="3", padx=20, pady=20, font=5, bg=cor_botao, fg=cor_letra, command=lambda: botao_clicar('3'))
botao_4 = Button(root, text="4", padx=20, pady=20, font=5, bg=cor_botao, fg=cor_letra, command=lambda: botao_clicar('4'))
botao_5 = Button(root, text="5", padx=20, pady=20, font=5, bg=cor_botao, fg=cor_letra, command=lambda: botao_clicar('5'))
botao_6 = Button(root, text="6", padx=20, pady=20, font=5, bg=cor_botao, fg=cor_letra, command=lambda: botao_clicar('6'))
botao_7 = Button(root, text="7", padx=20, pady=20, font=5, bg=cor_botao, fg=cor_letra, command=lambda: botao_clicar('7'))
botao_8 = Button(root, text="8", padx=20, pady=20, font=5, bg=cor_botao, fg=cor_letra, command=lambda: botao_clicar('8'))
botao_9 = Button(root, text="9", padx=20, pady=20, font=5, bg=cor_botao, fg=cor_letra, command=lambda: botao_clicar('9'))
botao_0 = Button(root, text="0", padx=51, pady=20, font=5, bg=cor_botao, fg=cor_letra, command=lambda: botao_clicar('0'))
botao_soma = Button(root, text="+", padx=19, pady=55, font=5, bg=cor_botao, fg=cor_letra, command=lambda: tipo_operador("+"))
botao_sub = Button(root, text="-", padx=21, pady=20, font=5, bg=cor_botao, fg=cor_letra, command=lambda: tipo_operador("-"))
botao_mul = Button(root, text="x", padx=21, pady=20, font=2, bg=cor_botao, fg=cor_letra, command=lambda: tipo_operador("*"))
botao_div = Button(root, text="/", padx=22, pady=20, font=5, bg=cor_botao, fg=cor_letra, command=lambda: tipo_operador("/"))
botao_del = Button(root, text="AC", padx=14, pady=20, font=2, bg=cor_botao, fg=cor_letra, command=botao_limpar_tudo)
botao_igual = Button(root, text="=", padx=19, pady=55, font=5, bg=cor_botao, fg=cor_letra, command=calcular_valor)
botao_ponto = Button(root, text="C", padx=19, pady=20, font=10, bg=cor_botao, fg=cor_letra, command=botao_limpar_ultimo_caracter)

botao_1.grid(row=4, column=0)
botao_2.grid(row=4, column=1)
botao_3.grid(row=4, column=2)

botao_4.grid(row=3, column=0)
botao_5.grid(row=3, column=1)
botao_6.grid(row=3, column=2)

botao_7.grid(row=2, column=0)
botao_8.grid(row=2, column=1)
botao_9.grid(row=2, column=2)

botao_del.grid(row=1, column=0)
botao_div.grid(row=1, column=1)
botao_mul.grid(row=1, column=2)
botao_sub.grid(row=1, column=3)

botao_soma.grid(row=2, column=3, rowspan=2)
botao_igual.grid(row=4, column=3, rowspan=2)

botao_0.grid(row=5, column=0, columnspan=2)
botao_ponto.grid(row=5, column=2)

root.mainloop()
