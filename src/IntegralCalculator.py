from scipy.integrate import quad
import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import sympy as sp

# Função para calcular a integral de uma expressão fornecida pelo usuário
def calcular_integral(expressao, a, b):
    try:
        # Define 'x' como uma variável simbólica
        x = sp.symbols('x')
        
        # Transforma a string da expressão em uma função simbólica
        funcao_simb = sp.sympify(expressao)
        
        # Converte a função simbólica em uma função numérica para integração
        funcao_num = sp.lambdify(x, funcao_simb, 'numpy')
        
        # Calcula a integral numérica no intervalo [a, b]
        resultado, erro = quad(funcao_num, a, b)
        return resultado, erro, funcao_num
    except Exception as e:
        return None, None, str(e)

def plotar_grafico(funcao, a, b):
    try:
        # Define o intervalo de -6 a 6 para o eixo x
        x = np.linspace(-6, 6, 400)
        y = funcao(x)
        
        plt.figure()
        plt.plot(x, y, label='Função')
        
        # Verifica se os limites de integração estão dentro da faixa de -6 a 6
        if -6 <= a <= 6 and -6 <= b <= 6:
            plt.fill_between(x, y, where=(x >= a) & (x <= b), alpha=0.3, label='Área sob a curva')
            plt.axvline(x=a, color='red', linestyle='--', label='Limite Inferior (a)')
            plt.axvline(x=b, color='green', linestyle='--', label='Limite Superior (b)')
        
        plt.title("Gráfico da Função e Área sob a Curva")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.ylim([min(y) - 1, max(y) + 1])  # Ajusta dinamicamente os limites do eixo y
        plt.xlim([-6, 6])  # Define os limites do eixo x de -6 a 6
        plt.legend()
        plt.grid()
        plt.show()
    except Exception as e:
        print(f"Erro ao plotar o gráfico: {e}")

# Interface gráfica com Tkinter
def calcular():
    expressao = entry_expressao.get()  # Pega a expressão da entrada
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        
        # Calcular a integral
        resultado, erro, funcao = calcular_integral(expressao, a, b)
        
        if resultado is not None and funcao != str(funcao):
            # Exibir o resultado
            resultado_label.config(text=f"Resultado da integral: {resultado:.4f} (Erro: {erro:.4f})")
            
            # Plotar o gráfico da função
            plotar_grafico(funcao, a, b)
        else:
            resultado_label.config(text=f"Erro: {funcao}")
    
    except ValueError:
        resultado_label.config(text="Erro: Por favor, insira valores numéricos válidos para os limites.")

# Criação da janela principal do Tkinter
root = tk.Tk()
root.title("Integral")

ttk.Label(root, text="Digite a expressão da função:").grid(column=0, row=0)
entry_expressao = ttk.Entry(root, width=40)
entry_expressao.grid(column=1, row=0)

ttk.Label(root, text="Limite inferior (a):").grid(column=0, row=1)
entry_a = ttk.Entry(root, width=10)
entry_a.grid(column=1, row=1)

ttk.Label(root, text="Limite superior (b):").grid(column=0, row=2)
entry_b = ttk.Entry(root, width=10)
entry_b.grid(column=1, row=2)

ttk.Button(root, text="Calcular Integral", command=calcular).grid(column=0, row=3, columnspan=2)

resultado_label = ttk.Label(root, text="Resultado: ")
resultado_label.grid(column=0, row=4, columnspan=2)

root.mainloop()