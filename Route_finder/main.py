"""v-6 Разбиение на клетки, круги, без промежуточных координат.
Препятствия-круги для этого алгоритма можно аппроксимировать многоугольниками с некоторым заданным числом вершин,
описанными вокруг кругов."""
from gui import GUI
from tkinter import Tk


def main():
    root = Tk()
    root.geometry("800x600")
    gui = GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
