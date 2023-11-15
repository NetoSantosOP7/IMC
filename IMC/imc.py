import tkinter as tk

def calcular_imc():
    try:
        peso = float  (entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)

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

        resultado.config(text=f"IMC: {imc:.2f}\nStatus: {status}")
    except ValueError:
        resultado.config(text="Digite valores válidos.")


janela = tk.Tk()
janela.title("Calcule seu IMC")


label_peso = tk.Label(janela, text="Digite seu peso (kg) separado por ponto:")
label_peso.pack()

entry_peso = tk.Entry(janela)
entry_peso.pack()

label_altura = tk.Label(janela, text="Digite sua altura (m) separada por ponto:")
label_altura.pack()

entry_altura = tk.Entry(janela)
entry_altura.pack()

calcular_button = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
calcular_button.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()
