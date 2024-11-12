import tkinter as tk
from tkinter import ttk
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from fractions import Fraction

# Função para calcular a integral indefinida manualmente (exemplos limitados para integrais polinomiais)
def calcular_integral_indefinida_manual(expressao):
    try:
        # Substituir espaços e garantir que a notação de potência esteja correta
        expressao = expressao.replace(' ', '')

        # Regex para extrair coeficientes e expoentes
        termos = re.findall(r'([+-]?\d*\.?\d*)\*?x\^?(\d*)|([+-]?\d+\.?\d*)', expressao)
        integral_termos = []

        # Verificar se todos os termos estão no formato correto
        for termo in termos:
            coef_str, exp_str, constante_str = termo
            if coef_str:  # Termo com x
                # Caso o coeficiente esteja ausente, definir como 1 ou -1 dependendo do sinal
                coef = Fraction(1) if coef_str in ('', '+') else Fraction(-1) if coef_str == '-' else Fraction(coef_str)
                exp = int(exp_str) if exp_str else 1  # O expoente é 1 se não for especificado

                # Realizar a integração: aumento do expoente e divisão do coeficiente
                novo_exp = exp + 1
                novo_coef = coef / novo_exp  # Converter coeficiente para fração

                # Representar o termo da integral indefinida
                if novo_exp == 1:
                    integral_termos.append(f"{novo_coef}*x")
                else:
                    integral_termos.append(f"{novo_coef}*x^{novo_exp}")
            elif constante_str:  # Termo constante
                constante = Fraction(constante_str)
                integral_termos.append(f"{constante}*x")

        # Unir os termos da integral com o formato adequado e adicionar +C
        integral = ' + '.join(integral_termos).replace('+ -', '- ') + ' + C'
        return integral, None
    except Exception as e:
        return None, str(e)

# Função para calcular a integral definida manualmente utilizando Somas de Riemann (pela esquerda)
def calcular_integral_riemann(expressao, a, b, n=1000):
    try:
        # Substituir espaços e garantir que a notação de potência esteja correta
        expressao = expressao.replace('^', '**').replace(' ', '')
        funcao = lambda x: eval(expressao)
        
        x = np.linspace(a, b, n+1)[:-1]  # Pegar os pontos à esquerda dos subintervalos
        h = (b - a) / n
        soma = np.sum(funcao(x) * h)  # Soma de Riemann à esquerda
        return soma, None
    except Exception as e:
        return None, str(e)

# Função para calcular a integral definida utilizando a regra de integração (simples para polinômios)
def calcular_integral_definida_manual(expressao, a, b):
    try:
        integral_indefinida, erro = calcular_integral_indefinida_manual(expressao)
        if erro:
            return None, erro

        # Substituir '^' por '**' para realizar a avaliação da expressão
        integral_indefinida = integral_indefinida.replace('^', '**').replace(' + C', '')

        # Calcular a integral definida usando a integral indefinida
        valor_a = eval(integral_indefinida.replace('x', f'({a})'))
        valor_b = eval(integral_indefinida.replace('x', f'({b})'))
        integral_definida = valor_b - valor_a
        return integral_definida, None
    except Exception as e:
        return None, str(e)

# Função principal para manipulação da interface
def calcular():
    expressao = entry_expressao.get()
    expressao2 = entry_expressao2.get()  # Segunda função para cálculo da área entre funções
    n = int(entry_n.get()) if entry_n.get() else 1000  # Número de retângulos para a soma de Riemann (padrão 1000)
    try:
        # Converter valores de a e b para float diretamente
        try:
            a = float(entry_a.get().strip())
            b = float(entry_b.get().strip())
        except ValueError:
            resultado_label.config(text="Erro: Por favor, insira valores numéricos válidos para os limites.")
            return
        
        # Validar se os limites a e b são diferentes
        if a == b:
            resultado_label.config(text="Resultado: 0 (Limite inferior e superior iguais)")
            return
        
        # Calcular a integral indefinida da primeira função manualmente
        integral_indefinida1, erro1 = calcular_integral_indefinida_manual(expressao)
        if erro1:
            resultado_label.config(text=f"Erro ao calcular integral indefinida da primeira função: {erro1}")
            return
        
        # Calcular a integral definida da primeira função usando a integral indefinida
        integral_definida1_manual, erro_definida_manual = calcular_integral_definida_manual(expressao, a, b)
        if erro_definida_manual:
            resultado_label.config(text=f"Erro ao calcular integral definida da primeira função: {erro_definida_manual}")
            return
        
        # Calcular a integral definida da primeira função usando Somas de Riemann (pela esquerda)
        integral_definida1_riemann, erro_riemann = calcular_integral_riemann(expressao, a, b, n)
        if erro_riemann:
            resultado_label.config(text=f"Erro ao calcular integral pela soma de Riemann da primeira função: {erro_riemann}")
            return
        
        # Calcular a integral indefinida da segunda função, se houver
        if expressao2:
            integral_indefinida2, erro2 = calcular_integral_indefinida_manual(expressao2)
            if erro2:
                resultado_label.config(text=f"Erro ao calcular integral indefinida da segunda função: {erro2}")
                return
        else:
            integral_indefinida2 = None

        # Calcular a integral definida da segunda função, se houver
        if integral_indefinida2:
            integral_definida2_manual, erro_definida2_manual = calcular_integral_definida_manual(expressao2, a, b)
            if erro_definida2_manual:
                resultado_label.config(text=f"Erro ao calcular integral definida da segunda função: {erro_definida2_manual}")
                return
            
            integral_definida2_riemann, erro_riemann2 = calcular_integral_riemann(expressao2, a, b, n)
            if erro_riemann2:
                resultado_label.config(text=f"Erro ao calcular integral pela soma de Riemann da segunda função: {erro_riemann2}")
                return
            
            # Área entre as duas funções (valor absoluto da diferença)
            area_entre_funcoes_manual = abs(integral_definida1_manual - integral_definida2_manual)
            area_entre_funcoes_riemann = abs(integral_definida1_riemann - integral_definida2_riemann)
        else:
            area_entre_funcoes_manual = None
            area_entre_funcoes_riemann = None
        
        # Exibir resultados formatados
        integral_indefinida1_formatada = integral_indefinida1.replace('**', '^')
        resultado_text = f"Integral indefinida da primeira função: \n∫ f(x) dx = {integral_indefinida1_formatada}\n\n"
        resultado_text += f"Integral definida da primeira função no intervalo [{a}, {b}] (Manual): {integral_definida1_manual}\n"
        resultado_text += f"Integral definida da primeira função no intervalo [{a}, {b}] (Somas de Riemann): {integral_definida1_riemann}\n"
        resultado_text += f"Diferença entre Riemann e Manual: {abs(integral_definida1_manual - integral_definida1_riemann)}\n\n"
        
        if integral_indefinida2:
            integral_indefinida2_formatada = integral_indefinida2.replace('**', '^')
            resultado_text += f"Integral indefinida da segunda função: \n∫ g(x) dx = {integral_indefinida2_formatada}\n\n"
            resultado_text += f"Integral definida da segunda função no intervalo [{a}, {b}] (Manual): {integral_definida2_manual}\n"
            resultado_text += f"Integral definida da segunda função no intervalo [{a}, {b}] (Somas de Riemann): {integral_definida2_riemann}\n"
            resultado_text += f"Diferença entre Riemann e Manual: {abs(integral_definida2_manual - integral_definida2_riemann)}\n\n"
            resultado_text += f"Área entre as duas funções no intervalo [{a}, {b}] (Manual): {area_entre_funcoes_manual}\n"
            resultado_text += f"Área entre as duas funções no intervalo [{a}, {b}] (Somas de Riemann): {area_entre_funcoes_riemann}\n\n"
        
        resultado_label.config(text=resultado_text, font=('Courier', 10))

        # Plotar o gráfico das funções e da área entre elas
        fig, ax = plt.subplots()
        x_vals = np.linspace(-6, 6, 400)
        funcao1 = lambda x: eval(expressao.replace('^', '**'))
        y_vals1 = funcao1(x_vals)
        ax.plot(x_vals, y_vals1, label='f(x)', color='blue')

        if expressao2:
            funcao2 = lambda x: eval(expressao2.replace('^', '**'))
            y_vals2 = funcao2(x_vals)
            ax.plot(x_vals, y_vals2, label='g(x)', color='red', linestyle='--')
            # Sombrear a área entre as funções no intervalo [a, b]
            x_fill = np.linspace(a, b, 400)
            y_fill1 = funcao1(x_fill)
            y_fill2 = funcao2(x_fill)
            ax.fill_between(x_fill, y_fill1, y_fill2, where=(y_fill1 > y_fill2), interpolate=True, alpha=0.3, color='purple', label='Área entre f(x) e g(x)')
            ax.fill_between(x_fill, y_fill2, y_fill1, where=(y_fill2 > y_fill1), interpolate=True, alpha=0.3, color='purple')
        
        ax.set_xlim(-6, 6)
        ax.set_ylim(-10, 10)
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.set_title('Gráfico das Funções e Área Entre Elas')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()
        ax.grid(True)

        # Mostrar o gráfico na interface Tkinter
        for widget in frame_grafico.winfo_children():
            widget.destroy()  # Limpar gráfico anterior
        canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except Exception as e:
        resultado_label.config(text=f"Erro inesperado: {e}")

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("Calculadora de Integral e Área entre Funções")

# Campos de entrada e botões
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

ttk.Label(root, text="Número de retângulos (n) para Somas de Riemann:").grid(column=0, row=4)
entry_n = ttk.Entry(root, width=10)
entry_n.grid(column=1, row=4)

ttk.Button(root, text="Calcular", command=calcular).grid(column=0, row=5, columnspan=2)

resultado_label = ttk.Label(root, text="Resultado: ", justify='left')
resultado_label.grid(column=0, row=6, columnspan=2)

# Frame para o gráfico
frame_grafico = ttk.Frame(root)
frame_grafico.grid(column=0, row=7, columnspan=2)

root.mainloop()
