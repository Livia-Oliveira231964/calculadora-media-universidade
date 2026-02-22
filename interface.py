import tkinter as tk
from tkinter import messagebox
from calculo import calcular_nota_final   # importa a função do outro arquivo

def calcular():
    try:
        m1 = float(entry_m1.get())
        m2 = float(entry_m2.get())
        resultado = calcular_nota_final(m1, m2)
        messagebox.showinfo("Resultado", f"Nota final: {resultado:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos!")

janela = tk.Tk()
janela.title("Calculadora de Média Universitária")

label_m1 = tk.Label(janela, text="Nota do primeiro bimestre (M1):")
label_m1.pack()
entry_m1 = tk.Entry(janela)
entry_m1.pack()

label_m2 = tk.Label(janela, text="Nota do segundo bimestre (M2):")
label_m2.pack()
entry_m2 = tk.Entry(janela)
entry_m2.pack()

btn_calcular = tk.Button(janela, text="Calcular Média", command=calcular)
btn_calcular.pack()

janela.mainloop()