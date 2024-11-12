# README - Calculadora de Integrais e Área entre Funções

## Descrição
Este projeto é uma calculadora de integrais que permite ao usuário calcular tanto integrais definidas quanto indefinidas de funções matemáticas. Além disso, a ferramenta permite o cálculo da área entre duas funções em um intervalo especificado pelo usuário. Utilizando uma interface gráfica desenvolvida com Tkinter, o usuário pode inserir expressões matemáticas e limites de integração, visualizando os resultados e o gráfico das funções e suas áreas.

Este projeto faz uso das bibliotecas `re`, `numpy`, `matplotlib` e `tkinter` para realizar os cálculos e visualizar os resultados, tornando o processo de integração acessível e intuitivo.

## Funcionalidades
- **Cálculo de integrais indefinidas**: Calcula a integral indefinida de uma função polinomial inserida pelo usuário.
- **Cálculo de integrais definidas**: Calcula a integral definida da função em um intervalo [a, b] especificado pelo usuário, utilizando duas abordagens:
  - Utilizando a integral indefinida.
  - Utilizando a Somas de Riemann (pela esquerda).
- **Cálculo da área entre duas funções**: Permite o cálculo da área entre duas funções no intervalo especificado.
- **Gráfico das funções**: Plota o gráfico das funções no intervalo [-6, 6], mostrando também a área entre as duas funções.
- **Interface intuitiva**: Desenvolvida utilizando Tkinter para facilitar a interação do usuário.

## Requisitos
- Python 3.8+
- Bibliotecas Python:
  - `re`
  - `numpy`
  - `matplotlib`
  - `tkinter`

## Instalação e Como Executar
### Passo a Passo para Executar em um Ambiente Virtual
Recomenda-se rodar o projeto em um ambiente virtual para garantir que todas as dependências sejam instaladas corretamente e que não haja conflitos com outras bibliotecas instaladas no sistema.

1. **Clone este repositório** para o seu computador local:
   ```bash
   git clone https://github.com/MarcosLaine/IntegralCalculator.git
   cd IntegralCalculator
   ```

2. **Crie um ambiente virtual**. No diretório do projeto, execute:
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências necessárias** utilizando o arquivo `requirements.txt`. Caso ele não esteja presente, instale as bibliotecas manualmente:
   ```bash
   pip install re numpy matplotlib tkinter
   ```

5. **Execute o arquivo principal do projeto**:
   ```bash
   python IntegralCalculator.py
   ```

### Rodando o Projeto Sem Ambiente Virtual
Se preferir rodar sem ambiente virtual, certifique-se de que você tem as bibliotecas necessárias instaladas globalmente. Utilize o comando:
```bash
pip install re numpy matplotlib tkinter
```
Após a instalação das dependências, execute o projeto com:
```bash
python IntegralCalculator.py
```

## Como Utilizar
1. **Digite a expressão da função f(x)**: No campo indicado, insira a expressão da primeira função. Por exemplo: `3*x^2 + 2*x - 5`.
2. **Digite a expressão da função g(x)** (opcional): Se desejar calcular a área entre duas funções, insira a segunda expressão.
3. **Limite inferior (a)**: Insira o valor do limite inferior do intervalo de integração.
4. **Limite superior (b)**: Insira o valor do limite superior do intervalo de integração.
5. **Número de retângulos (n)** (opcional): Informe o número de retângulos para as somas de Riemann (valor padrão é 1000).
6. **Clique em "Calcular"**: O resultado das integrais e o gráfico serão exibidos na interface.

## Exemplo de Uso
Imagine que você quer calcular a integral da função `f(x) = 3*x^2 + 2*x - 5` no intervalo de `a = 0` até `b = 4`. Além disso, você deseja calcular a área entre esta função e a função `g(x) = x^3 - 4` no mesmo intervalo.

Passo a passo:
1. Digite `3*x^2 + 2*x - 5` no campo para a expressão de `f(x)`.
2. Digite `x^3 - 4` no campo para a expressão de `g(x)`.
3. Insira `0` como limite inferior e `4` como limite superior.
4. Clique em "Calcular".

A interface exibirá os resultados das integrais indefinida e definida das duas funções, além da área entre elas. O gráfico das funções será plotado, mostrando a área sombreada entre `f(x)` e `g(x)`.

## Dependências e Tecnologias Utilizadas
- **Tkinter**: Utilizado para construir a interface gráfica do usuário.
- **Matplotlib**: Utilizado para plotar os gráficos das funções e da área entre elas.
- **Numpy**: Utilizado para criar os pontos e realizar cálculos numéricos.
- **Re**: Utilizado para manipulação de expressões regulares.

## Detalhes de Implementação
- A integral **indefinida** é calculada manualmente utilizando expressões polinomiais, sendo limitada a uma quantidade restrita de tipos de funções.
- A integral **definida** é calculada através de duas abordagens:
  1. **Manual**: Utilizando a integral indefinida e aplicando os limites de integração.
  2. **Somas de Riemann**: Utilizando Somas de Riemann pela esquerda para aproximação numérica.
- O gráfico permite visualizar a função plotada no intervalo entre `-6` e `6`, com as áreas de interesse destacadas para facilitar a análise.

## Erros Comuns e Soluções
1. **Erro ao inserir uma expressão**: Certifique-se de usar `x` como a variável e usar `^` para potência. Expressões devem ser inseridas no formato, por exemplo, `3*x^2 + 2*x - 5`.
2. **Erro de valor para os limites**: Certifique-se de que os limites de integração `a` e `b` são diferentes. Se `a == b`, o resultado da integral será `0`.

## Autores
- João Pedro Gomes Machado
- Marcos Paulo Da Silva Laine
- Matheus Rossi
- Vitor Artur

Este projeto foi desenvolvido como parte de uma atividade de programação com foco em cálculos matemáticos e visualização gráfica, visando proporcionar uma experiência didática e intuitiva no estudo de integrais.

Sinta-se à vontade para contribuir com melhorias, sugere alteracões ou relatar problemas encontrados ao utilizar o projeto!


# README - Integral Calculator and Area Between Functions

## Description
This project is an integral calculator that allows users to calculate both definite and indefinite integrals of mathematical functions. Additionally, the tool allows the calculation of the area between two functions in a user-specified interval. Using a graphical interface developed with Tkinter, users can input mathematical expressions and integration limits, and visualize the results and the graph of the functions and their areas.

This project makes use of the libraries `re`, `numpy`, `matplotlib`, and `tkinter` to perform the calculations and visualize the results, making the integration process accessible and intuitive.

## Features
- **Indefinite Integral Calculation**: Calculates the indefinite integral of a polynomial function input by the user.
- **Definite Integral Calculation**: Calculates the definite integral of a function in an interval [a, b] specified by the user, using two approaches:
  - Using the indefinite integral.
  - Using Riemann Sums (left endpoint).
- **Area Between Two Functions Calculation**: Allows the calculation of the area between two functions in the specified interval.
- **Graph of Functions**: Plots the graph of the functions in the range [-6, 6], also showing the area between the two functions.
- **Intuitive Interface**: Developed using Tkinter to facilitate user interaction.

## Requirements
- Python 3.8+
- Python Libraries:
  - `re`
  - `numpy`
  - `matplotlib`
  - `tkinter`

## Installation and How to Run
### Step by Step to Run in a Virtual Environment
It is recommended to run the project in a virtual environment to ensure that all dependencies are installed correctly and to avoid conflicts with other libraries installed in the system.

1. **Clone this repository** to your local computer:
   ```bash
   git clone https://github.com/MarcosLaine/IntegralCalculator.git
   cd IntegralCalculator
   ```

2. **Create a virtual environment**. In the project directory, run:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

4. **Install the necessary dependencies** using the `requirements.txt` file. If it is not present, install the libraries manually:
   ```bash
   pip install re numpy matplotlib tkinter
   ```

5. **Run the main project file**:
   ```bash
   python IntegralCalculator.py
   ```

### Running the Project Without a Virtual Environment
If you prefer to run without a virtual environment, make sure you have the necessary libraries installed globally. Use the command:
```bash
pip install re numpy matplotlib tkinter
```
After installing the dependencies, run the project with:
```bash
python IntegralCalculator.py
```

## How to Use
1. **Enter the expression for the function f(x)**: In the indicated field, enter the expression for the first function. For example: `3*x^2 + 2*x - 5`.
2. **Enter the expression for the function g(x)** (optional): If you want to calculate the area between two functions, enter the second expression.
3. **Lower limit (a)**: Enter the value of the lower limit of the integration interval.
4. **Upper limit (b)**: Enter the value of the upper limit of the integration interval.
5. **Number of rectangles (n)** (optional): Specify the number of rectangles for Riemann sums (default value is 1000).
6. **Click on "Calculate"**: The results of the integrals and the graph will be displayed in the interface.

## Usage Example
Imagine you want to calculate the integral of the function `f(x) = 3*x^2 + 2*x - 5` in the interval from `a = 0` to `b = 4`. Additionally, you want to calculate the area between this function and the function `g(x) = x^3 - 4` in the same interval.

Step by step:
1. Enter `3*x^2 + 2*x - 5` in the field for the expression of `f(x)`.
2. Enter `x^3 - 4` in the field for the expression of `g(x)`.
3. Enter `0` as the lower limit and `4` as the upper limit.
4. Click on "Calculate".

The interface will display the results of the indefinite and definite integrals of both functions, as well as the area between them. The graph of the functions will be plotted, showing the shaded area between `f(x)` and `g(x)`.

## Dependencies and Technologies Used
- **Tkinter**: Used to build the graphical user interface.
- **Matplotlib**: Used to plot the graphs of the functions and the area between them.
- **Numpy**: Used to create points and perform numerical calculations.
- **Re**: Used for handling regular expressions.

## Implementation Details
- The **indefinite integral** is calculated manually using polynomial expressions, being limited to a restricted set of function types.
- The **definite integral** is calculated through two approaches:
  1. **Manual**: Using the indefinite integral and applying the integration limits.
  2. **Riemann Sums**: Using left-endpoint Riemann sums for numerical approximation.
- The graph allows visualization of the function plotted in the interval between `-6` and `6`, with the areas of interest highlighted to facilitate analysis.

## Common Errors and Solutions
1. **Error entering an expression**: Make sure to use `x` as the variable and use `^` for power. Expressions should be entered in the format, for example, `3*x^2 + 2*x - 5`.
2. **Error in limits value**: Make sure that the integration limits `a` and `b` are different. If `a == b`, the result of the integral will be `0`.

## Authors
- João Pedro Gomes Machado
- Marcos Paulo Da Silva Laine
- Matheus Rossi
- Vitor Artur

This project was developed as part of a programming activity focused on mathematical calculations and graphical visualization, aiming to provide a didactic and intuitive experience in the study of integrals.

Feel free to contribute with improvements, suggest changes, or report problems encountered while using the project!

