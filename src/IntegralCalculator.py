import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import sympy as sp
from scipy.integrate import quad
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função para calcular a integral usando o Método das Somas de Riemann
def calcular_integral_riemann(expressao, a, b, n=1000):
    try:
        # Define a função em termos de "x"
        funcao = lambda x: eval(expressao)
        
        # Divide o intervalo [a, b] em "n" subintervalos
        x = np.linspace(a, b, n)
        y = funcao(x)
        
        # Calcula a área dos retângulos (Soma de Riemann pela esquerda)
        h = (b - a) / n
        area = h * np.sum(y[:-1])
        
        return area, None
    except Exception as e:
        return None, str(e)

# Função para calcular a integral usando bibliotecas prontas (scipy)
def calcular_integral_pronta(expressao, a, b):
    try:
        # Define 'x' como uma variável simbólica
        x = sp.symbols('x')
        
        # Transforma a string da expressão em uma função simbólica
        funcao_simb = sp.sympify(expressao)
        
        # Converte a função simbólica em uma função numérica para integração
        funcao_num = sp.lambdify(x, funcao_simb, 'numpy')
        
        # Calcula a integral definida numérica no intervalo [a, b]
        resultado_definida, erro = quad(funcao_num, a, b)
        
        return resultado_definida, erro
    except Exception as e:
        return None, None

# Função para calcular a integral indefinida e formatar a função original
def calcular_integral_indefinida(expressao):
    try:
        # Define 'x' como uma variável simbólica
        x = sp.symbols('x')
        
        # Transforma a string da expressão em uma função simbólica
        funcao_simb = sp.sympify(expressao)
        
        # Calcula a integral indefinida da função simbólica
        integral_indefinida = sp.integrate(funcao_simb, x) + sp.Symbol('C')
        
        return funcao_simb, integral_indefinida
    except Exception as e:
        return None, None

# Função para plotar o gráfico da função
def plotar_grafico(funcao, a, b):
    try:
        # Define o intervalo de -6 a 6 para o eixo x
        x = np.linspace(-6, 6, 400)
        y = funcao(x)
        
        fig, ax = plt.subplots()
        ax.plot(x, y, label='Função')
        
        # Verifica se os limites de integração estão dentro da faixa de -6 a 6
        if -6 <= a <= 6 and -6 <= b <= 6:
            ax.fill_between(x, y, where=(x >= a) & (x <= b), alpha=0.3, label='Área sob a curva')
            ax.axvline(x=a, color='red', linestyle='--', label='Limite Inferior (a)')
            ax.axvline(x=b, color='green', linestyle='--', label='Limite Superior (b)')
        
        ax.set_title("Gráfico da Função e Área sob a Curva")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_ylim([min(y) - 1, max(y) + 1])  # Ajusta dinamicamente os limites do eixo y
        ax.set_xlim([-6, 6])  # Define os limites do eixo x de -6 a 6
        ax.legend()
        ax.grid()
        
        return fig
    except Exception as e:
        print(f"Erro ao plotar o gráfico: {e}")
        return None

# Interface gráfica com Tkinter
def calcular():
    expressao = entry_expressao.get()  # Pega a expressão da entrada
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        
        # Calcular a integral usando Somas de Riemann
        resultado_riemann, erro_riemann = calcular_integral_riemann(expressao, a, b)
        
        # Calcular a integral usando bibliotecas prontas (scipy)
        resultado_pronta, erro_pronta = calcular_integral_pronta(expressao, a, b)
        
        # Calcular a integral indefinida e formatar a função original
        funcao_simb, integral_indefinida = calcular_integral_indefinida(expressao)
        
        if resultado_riemann is not None and resultado_pronta is not None and funcao_simb is not None:
            # Calcular o erro entre o método das Somas de Riemann e a integral pronta
            erro = abs(resultado_pronta - resultado_riemann)
            
            # Formatar a função original e a integral indefinida de forma legível
            funcao_formatada = sp.pretty(funcao_simb, use_unicode=True)
            integral_indefinida_formatada = sp.pretty(integral_indefinida, use_unicode=True)
            
            # Exibir os resultados formatados
            resultado_text = (
                f"Função original: \n{funcao_formatada}\n\n"
                f"Resultado da integral definida utilizando Somas de Riemann no intervalo [{a}, {b}]: {resultado_riemann:.7f}\n"
                f"Resultado da integral definida utilizando a biblioteca Sympy no intervalo [{a}, {b}]: {resultado_pronta:.7f}\n"
                f"Erro da integral por somas de Riemann (diferença entre os métodos): {erro:.7f}\n\n"
                f"Integral indefinida: \n{integral_indefinida_formatada}"
            )
            resultado_label.config(text=resultado_text, font=('Courier', 10))
            
            # Converter a expressão em uma função numérica para plotagem
            funcao = lambda x: eval(expressao)
            
            # Plotar o gráfico da função
            fig = plotar_grafico(funcao, a, b)
            if fig is not None:
                canvas = FigureCanvasTkAgg(fig, master=root)
                canvas.draw()
                canvas.get_tk_widget().grid(column=0, row=5, columnspan=2)
        else:
            resultado_label.config(text=f"Erro: {erro_riemann if resultado_riemann is None else erro_pronta}")
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

resultado_label = ttk.Label(root, text="Resultado: ", justify='left')
resultado_label.grid(column=0, row=4, columnspan=2)

root.mainloop()
