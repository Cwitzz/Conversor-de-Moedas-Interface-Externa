from forex_python.converter import CurrencyRates
import tkinter as tk
from tkinter import ttk

c = CurrencyRates()

def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_entry.get().upper()
    to_currency = to_entry.get().upper()

    try:
        result = c.convert(from_currency, to_currency, amount)
        result_label.config(text=f"{from_currency} {amount} é igual a {to_currency} {result:.2f}")
    except:
        result_label.config(text=f"Moedas inválidas ou erro de conexão.")


# Interface
root = tk.Tk()
root.title("Conversor de Moedas")
root.geometry("450x425")

style = ttk.Style()
style.theme_use('clam')

style.configure("TButton",
    background="#2ecc71",
    foreground="white",
    font=("Roboto", 14, "bold"),
    padding=10,
    width=10,
    borderwidth=0)

style.map("TButton",
    background=[("active", "#27ae60")])
# Entrys
amount_label = ttk.Label(root, text="Valor:", font=("Roboto", 16))
amount_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

from_label = ttk.Label(root, text="De:", font=("Roboto", 16))
from_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

to_label = ttk.Label(root, text="Para:", font=("Roboto", 16))
to_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

result_label = ttk.Label(root, text="", font=("Roboto", 16))
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=20, sticky="w")

amount_entry = ttk.Entry(root, width=20, font=("Roboto", 16))
amount_entry.grid(row=0, column=1, padx=10, pady=10)

from_entry = ttk.Entry(root, width=20, font=("Roboto", 16))
from_entry.grid(row=1, column=1, padx=10, pady=10)

to_entry = ttk.Entry(root, width=20, font=("Roboto", 16))
to_entry.grid(row=2, column=1, padx=10, pady=10)

convert_button = ttk.Button(root, text="Converter", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Botões das moedas mais comuns
usd_button = ttk.Button(root, text="USD", command=lambda: from_entry.insert(0, "USD"))
usd_button.grid(row=5, column=0, padx=10, pady=10)

eur_button = ttk.Button(root, text="EUR", command=lambda: from_entry.insert(0, "EUR"))
eur_button.grid(row=5, column=1, padx=10, pady=10)

brl_button = ttk.Button(root, text="BRL", command=lambda: to_entry.insert(0, "BRL"))
brl_button.grid(row=6, column=0, padx=10, pady=10)

cad_button = ttk.Button(root, text="CAD", command=lambda: to_entry.insert(0, "CAD"))
cad_button.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()
