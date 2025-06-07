import tkinter as tk
from captacao import captar_dados
from salvar_dados import salvar_dados

def buscar_previsao():
    data_hora, temperatura, umidade = captar_dados()
    salvar_dados(data_hora, temperatura, umidade)

    texto_resultado.set(
        f"Data/Hora: {data_hora}\n"
        f"Temperatura: {temperatura} °C\n"
        f"Umidade: {umidade} %"
    )

# Criação da janela
janela = tk.Tk()
janela.title("Captador de Temperatura de São Paulo")
janela.geometry("400x200")

# Texto que vai ser atualizado
texto_resultado = tk.StringVar()
texto_resultado.set("Clique no botão para captar os dados.")

# Elementos da interface
label = tk.Label(janela, textvariable=texto_resultado, font=("Arial", 12), justify="left")
label.pack(pady=20)

botao = tk.Button(janela, text="Buscar previsão", command=buscar_previsao, font=("Arial", 12))
botao.pack()

# Rodar o app
janela.mainloop()
