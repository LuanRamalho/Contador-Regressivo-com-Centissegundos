import tkinter as tk
from tkinter import messagebox
import time

def iniciar_contagem():
    try:
        tempo_total = float(entrada_tempo.get())
        if tempo_total <= 0:
            raise ValueError("O tempo deve ser maior que zero.")
        executar_contagem(tempo_total)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor válido em segundos.")

def executar_contagem(tempo):
    while tempo >= 0:
        minutos, segundos = divmod(int(tempo), 60)
        centesimos = int((tempo - int(tempo)) * 100)
        texto_tempo.set(f"{minutos:02}:{segundos:02}:{centesimos:02}")
        root.update()
        time.sleep(0.01)
        tempo -= 0.01

    texto_tempo.set("00:00:00")
    messagebox.showinfo("Concluído", "A contagem regressiva terminou!")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Contagem Regressiva")
root.geometry("400x300")
root.configure(bg="#282c34")

# Título
titulo = tk.Label(
    root, text="Contagem Regressiva", font=("Helvetica", 18, "bold"), bg="#61afef", fg="white"
)
titulo.pack(pady=10)

# Entrada de tempo
frame_entrada = tk.Frame(root, bg="#282c34")
frame_entrada.pack(pady=20)
tk.Label(
    frame_entrada, text="Digite o tempo em segundos:", font=("Helvetica", 12), bg="#282c34", fg="#abb2bf"
).pack(side="left", padx=5)

entrada_tempo = tk.Entry(frame_entrada, font=("Helvetica", 12), width=10, justify="center")
entrada_tempo.pack(side="left")

# Botão de iniciar
botao_iniciar = tk.Button(
    root,
    text="Iniciar",
    font=("Helvetica", 12, "bold"),
    bg="#98c379",
    fg="white",
    command=iniciar_contagem,
)
botao_iniciar.pack(pady=10)

# Relógio
texto_tempo = tk.StringVar()
texto_tempo.set("00:00:00")
relogio = tk.Label(
    root, textvariable=texto_tempo, font=("Helvetica", 30, "bold"), bg="#282c34", fg="#e06c75"
)
relogio.pack(pady=20)

# Iniciar a interface
root.mainloop()
