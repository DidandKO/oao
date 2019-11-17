from tkinter import *
import math

x = int(input('Введите размерность графа'))
mid_x = 400
mid_y = 300
window = Tk()
window.title("Вот ваша матрица, сэр!")
window.geometry('800x600')
canv = Canvas(window, width=mid_x*2, height=mid_y*2, bg="lightblue", cursor="pencil")

def createMatrix(_x):
    matrix = []
    for j in range(_x):
        _matrix = []
        for i in range(_x):
            current_x = input('Введите ' + (i+1).__str__() + ' значение строки')
            _matrix.append(current_x)
        matrix.append(_matrix)
    print(matrix)
    return matrix


def find_V_Coordinates(_y):
    radius = 250
    delta = 360/_y
    delta_axes = []
    for i in range(_y):
        _ang = i*delta
        _ang = math.radians(_ang) #радианы и градусы
        print(_ang)
        sin = math.sin(_ang)
        print(sin)
        dy = radius*sin
        cos = math.cos(_ang)
        print(cos)
        dx = radius*cos
        _d = []
        _d.append(dx)
        _d.append(dy)
        delta_axes.append(_d)
    print(delta_axes)
    coordinates = []
    for point in delta_axes:
        point = [mid_x + point[0], mid_y + point[1]]
        coordinates.append(point)
    print(coordinates)
    return coordinates


def makeTransitions(_coordinates, _matrix):
    for i in range(_matrix.__len__()):
        for j in range(_matrix[i].__len__()):
            if _matrix[i][j] != '0':
                canv.create_line(_coordinates[i], _coordinates[j], width=int(_matrix[i][j])*1.5)
                text_coord = [(_coordinates[i][0]+_coordinates[j][0])/2, (_coordinates[i][1]+_coordinates[j][1])/2]
                canv.create_text(text_coord, text=_matrix[i][j], font="Verdana 25", fill='red')
    pass


def drawMatrix(_z):
    matrix = [['0', '1', '2', '3', '4'],
              ['1', '0', '5', '6', '7'],
              ['2', '5', '0', '8', '9'],
              ['3', '6', '8', '0', '10'],
              ['4', '7', '9', '10', '0']]
    v_size = 10
    points = find_V_Coordinates(_z)
    i = 0
    makeTransitions(points, matrix)
    for point in points:
        i += 1
        tl = [point[0]-v_size, point[1]-v_size]
        br = [point[0]+v_size, point[1]+v_size]
        canv.create_oval(tl, br, width=5, fill='brown')
        canv.create_text(tl, text='V' + str(i), fill='yellow', font="Verdana 15")
    canv.pack()
    window.mainloop()


drawMatrix(x)