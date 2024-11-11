import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função para calcular a integral indefinida (aproximação numérica usando o Método dos Trapézios)
def calcular_integral_indefinida(funcao, a, b, n=1000):
    try:
        x = np.linspace(a, b, n)
        h = (b - a) / (n - 1)
        y = funcao(x)
        integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])  # Método dos trapézios
        return integral
    except Exception as e:
        return None

# Função para calcular a integral definida usando o Método das Somas de Riemann
def calcular_integral_riemann(expressao, a, b, n=1000):
    try:
        funcao = lambda x: eval(expressao)
        x = np.linspace(a, b, n)
        y = funcao(x)
        h = (b - a) / n
        area = h * np.sum(y[:-1])  # Soma pela esquerda
        return area, None
    except Exception as e:
        return None, str(e)

# Função para calcular a área entre duas funções usando a soma de Riemann
def calcular_area_entre_funcoes(expressao1, expressao2, a, b, n=1000):
    try:
        funcao1 = lambda x: eval(expressao1)
        funcao2 = lambda x: eval(expressao2)
        x = np.linspace(a, b, n)
        y1 = funcao1(x)
        y2 = funcao2(x)
        h = (b - a) / n
        area = h * np.sum(np.abs(y1[:-1] - y2[:-1]))  # módulo da diferença
        return area, None
    except Exception as e:
        return None, str(e)

# Função para plotar as funções e a região entre elas
def plotar_grafico_duas_funcoes(funcao1, funcao2, a, b):
    try:
        x = np.linspace(a - 1, b + 1, 400)  # Ampliar o intervalo para visualizar melhor
        y1 = funcao1(x)
        y2 = funcao2(x)
        
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Função 1')
        ax.plot(x, y2, label='Função 2', linestyle='--')
        
        # Sombrear a área entre as funções no intervalo [a, b]
        ax.fill_between(x, y1, y2, where=(x >= a) & (x <= b), alpha=0.3, label='Área entre as funções')
        ax.axvline(x=a, color='red', linestyle='--', label='Limite Inferior (a)')
        ax.axvline(x=b, color='green', linestyle='--', label='Limite Superior (b)')
        
        ax.set_title("Gráfico das Funções e Área entre Elas")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()
        ax.grid()
        
        return fig
    except Exception as e:
        print(f"Erro ao plotar o gráfico: {e}")
        return None

# Função principal para manipulação da interface
def calcular():
    expressao = entry_expressao.get()
    expressao2 = entry_expressao2.get()  # Segunda função para cálculo da área entre funções
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = int(entry_n.get()) if entry_n.get() else 1000  # Número de retângulos para a soma de Riemann
        
        # Função para calcular a integral indefinida (aproximação numérica)
        funcao1 = lambda x: eval(expressao)
        integral_indefinida = calcular_integral_indefinida(funcao1, a, b, n)
        
        # Pergunta ao usuário se deseja calcular a integral definida
        resposta_definida = messagebox.askyesno("Integral Definida", "Deseja calcular a integral definida?")
        if resposta_definida:
            # Calcular a integral definida da primeira função no intervalo [a, b]
            resultado_definida, erro = calcular_integral_riemann(expressao, a, b, n)
            if erro:
                resultado_label.config(text=f"Erro ao calcular integral definida: {erro}")
                return
        
        # Se houver uma segunda função, calcular a área entre as duas funções
        if expressao2:
            resultado_area, erro = calcular_area_entre_funcoes(expressao, expressao2, a, b, n)
            if erro:
                resultado_label.config(text=f"Erro ao calcular área entre as funções: {erro}")
                return
        
        # Exibir resultados formatados
        resultado_text = f"Integral indefinida aproximada (Método numérico): {integral_indefinida}\n\n"
        
        if resposta_definida:
            resultado_text += f"Integral definida no intervalo [{a}, {b}]: {resultado_definida}\n\n"
        
        if expressao2:
            resultado_text += f"Área entre as funções (Soma de Riemann com {n} retângulos): {resultado_area:.4f}"
        
        resultado_label.config(text=resultado_text, font=('Courier', 10))
        
        # Plotar o gráfico das duas funções
        funcao1 = lambda x: eval(expressao)
        funcao2 = lambda x: eval(expressao2)
        fig = plotar_grafico_duas_funcoes(funcao1, funcao2, a, b)
        if fig is not None:
            # Exibir o gráfico
            for widget in frame_grafico.winfo_children():
                widget.destroy()  # Limpa o gráfico anterior
            canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
            canvas.draw()
            canvas.get_tk_widget().pack()
        
    except ValueError:
        resultado_label.config(text="Erro: Por favor, insira valores numéricos válidos para os limites.")

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Calculadora de Integral e Área entre Funções")

ttk.Label(root, text="Digite a expressão da função f(x):").grid(column=0, row=0)
entry_expressao = ttk.Entry(root, width=40)
entry_expressao.grid(column=1, row=0)

ttk.Label(root, text="Digite a expressão da função g(x):").grid(column=0, row=1)
entry_expressao2 = ttk.Entry(root, width=40)
entry_expressao2.grid(column=1, row=1)

ttk.Label(root, text="Limite inferior (a):").grid(column=0, row=2)
entry_a = ttk.Entry(root, width=10)
entry_a.grid(column=1, row=2)

ttk.Label(root, text="Limite superior (b):").grid(column=0, row=3)
entry_b = ttk.Entry(root, width=10)
entry_b.grid(column=1, row=3)

ttk.Label(root, text="Número de retângulos (n) para a soma de Riemann:").grid(column=0, row=4)
entry_n = ttk.Entry(root, width=10)
entry_n.grid(column=1, row=4)

ttk.Button(root, text="Calcular", command=calcular).grid(column=0, row=5, columnspan=2)

resultado_label = ttk.Label(root, text="Resultado: ", justify='left')
resultado_label.grid(column=0, row=6, columnspan=2)

# Frame para o gráfico
frame_grafico = ttk.Frame(root)
frame_grafico.grid(column=0, row=7, columnspan=2)

root.mainloop()
