import tkinter as tk

def inverse_modulaire(a, m):
    """
    Calcule l'inverse modulaire de a modulo m en utilisant l'algorithme d'Euclide étendu.
    Retourne x tel que (a * x) % m == 1.
    """
    # Calcul de l'algorithme d'Euclide étendu
    r, r_prec = m, a
    x, x_prec = 0, 1
    y, y_prec = 1, 0

    while r != 0:
        q = r_prec // r
        r_prec, r = r, r_prec - q * r
        x_prec, x = x, x_prec - q * x
        y_prec, y = y, y_prec - q * y

    # Si a et m ne sont pas premiers entre eux, il n'y a pas d'inverse modulaire
    if r_prec > 1:
        raise ValueError(f"{a} n'a pas d'inverse modulaire modulo {m}")

    # Retourne l'inverse modulaire
    return x_prec % m

def calculer_inverse_modulaire():
    a = int(a_entry.get())
    m = int(m_entry.get())
    try:
        x = inverse_modulaire(a, m)
        resultat_label.config(text=f"L'inverse modulaire de {a} modulo {m} est {x}")
    except ValueError as e:
        resultat_label.config(text=str(e))

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calcul de l'inverse modulaire")

# Création des widgets
a_label = tk.Label(fenetre, text="a :")
a_entry = tk.Entry(fenetre)
m_label = tk.Label(fenetre, text="m :")
m_entry = tk.Entry(fenetre)
calculer_button = tk.Button(fenetre, text="Calculer", command=calculer_inverse_modulaire)
resultat_label = tk.Label(fenetre, text="")

# Placement des widgets dans la fenêtre
a_label.grid(row=0, column=0, padx=5, pady=5)
a_entry.grid(row=0, column=1, padx=5, pady=5)
m_label.grid(row=1, column=0, padx=5, pady=5)
m_entry.grid(row=1, column=1, padx=5, pady=5)
calculer_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
resultat_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Boucle principale
fenetre.mainloop()
