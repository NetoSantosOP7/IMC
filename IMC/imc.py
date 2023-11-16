import tkinter as tk

def calcular_imc():
    try:
        # Aqui obtem os valores dos campos de entrada e converte pra float
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        # aqui ja valida se os valores de peso e altura são positivos
        if peso <= 0 or altura <= 0:
            resultado.config(text="Digite valores válidos para peso e altura.")
        else:
            # Calcula o IMC
            imc = peso / (altura ** 2)

            # Determina o status com base no IMC calculado
            status = ""
            if imc < 18.5:
                status = "Você está abaixo do peso"
            elif 18.5 <= imc < 24.9:
                status = "Você está no peso ideal"
            elif 25 <= imc < 29.9:
                status = "Você está levemente acima do peso"
            elif 30 <= imc < 34.9:
                status = "Você está na obesidade grau 1"
            elif 35 <= imc < 39.9:
                status = "Você está na obesidade grau 2"
            else:
                status = "Você está na obesidade grau 3"

            # Exibe o resultado na interface gráfica
            resultado.config(text=f"IMC: {imc:.2f}\nStatus: {status}")
    except ValueError:
        # Trata exceção se valores não numéricos forem inseridos
        resultado.config(text="Digite valores numéricos válidos.")

def limpar_campos():
    # Limpa os campos de entrada e o resultado
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    resultado.config(text="")

# Cria a janela principal
janela = tk.Tk()
janela.title("Calcule seu IMC")

# Adiciona estilo à janela
janela.geometry("400x300")
janela.configure(bg="#001f3f")  # Define a cor de fundo

# Cria os rótulos, campos de entrada e botões
label_peso = tk.Label(janela, text="Digite seu peso (kg) separado por ponto:", bg="#001f3f", fg="white")
label_peso.pack()

entry_peso = tk.Entry(janela)
entry_peso.pack()

label_altura = tk.Label(janela, text="Digite sua altura (m) separada por ponto:", bg="#001f3f", fg="white")
label_altura.pack()

entry_altura = tk.Entry(janela)
entry_altura.pack()

calcular_button = tk.Button(janela, text="Calcular IMC", command=calcular_imc, bg="#4CAF50", fg="white")
calcular_button.pack()

limpar_button = tk.Button(janela, text="Limpar Campos", command=limpar_campos, bg="#f44336", fg="white")
limpar_button.pack()

resultado = tk.Label(janela, text="", bg="#001f3f", fg="white", font=("Arial", 12))
resultado.pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()
