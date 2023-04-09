import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
def get_data():
    while True:
        try:
            n = int(input("Введите количество точек разбиения: "))
            if n > 0: break
            print("Необходимо ввести положительное число")
        except ValueError:
            print("Что-то пошло не так. Пожалуйста, введите целое число")
    while True:
        match input("Введите оснащение (левое, среднее или правое): "):
            case "левое":
                pos = 0
                pos_str = "Левое"
                break
            case "среднее":
                pos = 0.5
                pos_str = "Среднее"
                break
            case "правое":
                pos = 1
                pos_str = "Правое"
                break
            case _:
                print("Оснащение не найдено, пожалуйста, попробуйте еще раз")
    return n, pos, pos_str

def my_exp(x):
    return 2**x

def get_equipment(n, pos, func):
    return [func((2/n)*(i+pos)) for i in range(n)]

def integral_s(equipment):
    return sum([(2/len(equipment))*k for k in equipment])

def make_plot(equipment, summ, pos_str):
    a, fig = plt.subplots()
    n = len(equipment)
    for i in range(n):
        fig.add_patch(Rectangle(((2/n)*i, 0), 2/n, equipment[i], color = [(1-i/n), 1, 0, 0.5]))
    ar = [i/10 for i in range(21)]
    fig.plot(ar, [2**i for i in ar], color = [0, 0.5, 0, 1])
    fig.text(0.5, 3.5, 'S = ' + str(summ),  color = [0, 0.5, 0, 1])
    fig.text(0.5, 3, pos_str[0].upper() + pos_str[1:] + ' разбиение',  color = [0, 0.5, 0, 1])
    fig.text(0.5, 2.5, "Кол-во точек: " + str(len(equipment)),  color = [0, 0.5, 0, 1])
    plt.show()
    return

def make_laboratornaya():
    n, pos, pos_str = get_data()
    equipment = get_equipment(n, pos, my_exp)
    my_summ = integral_s(equipment)
    make_plot(equipment, my_summ, pos_str)
    return "success!"
for i in range(4):
    make_laboratornaya()