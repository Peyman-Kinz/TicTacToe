import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time

# Globale Variablen
current_player = "X"
board = [""] * 9
round_number = 1

# Funktion zur Überprüfung des Gewinners
def check_winner(player):
    # Überprüfen der Zeilen
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Überprüfen der Spalten
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Überprüfen der Diagonalen
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False

# Funktion, die aufgerufen wird, wenn ein Feld im Spiel geklickt wird
def on_click(button, index):
    global current_player, round_number

    if board[index] == "":
        board[index] = current_player
        button.config(text=current_player, state=tk.DISABLED, background='lightblue')
        
        if check_winner(current_player):
            messagebox.showinfo("Spiel beendet", f"Spieler {current_player} hat gewonnen!")
            board_clear()
            round_number += 1
        elif "" not in board:
            messagebox.showinfo("Spiel beendet", "Unentschieden!")
            board_clear()
            round_number += 1
        else:
            current_player = "O" if current_player == "X" else "X"
            
        round_label.config(text=f"Runde {round_number}")

# Funktion, um das Spielfeld zu löschen
def board_clear():
    global current_player, board, game_over
    current_player = "X"
    board = [""] * 9
    game_over = False
    for button in buttons:
        button.config(text="", state=tk.NORMAL, background='SystemButtonFace')

# GUI erstellen
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = []

for i in range(9):
    row = i // 3
    col = i % 3
    button = tk.Button(root, text="", font=("normal", 16), width=10, height=4, command=lambda i=i: on_click(buttons[i], i))
    button.grid(row=row, column=col)
    buttons.append(button)

round_label = tk.Label(root, text="Runde 1", font=("normal", 16))
round_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
