import turtle

import turtle

def btnclick(x, y):
    """Клик по кнопке"""
    px, py = btn.pos()
    # проверяем попадают ли координаты 
    # клика по холсту в координаты кнопки
    if px<x<px+btn_width and py<y<py+btn_height:
        # стираем кнопку
        btn.clear()
        # показываем круг
        circ.showturtle()
        circ.penup()
        
def draw_bth(width, height, pos=(00.00, 0.00), text=""):
    """Кнопка с надписью"""
    btn.penup()
    btn.setpos(pos)
    btn.pendown()
    # рисуем прямоугольник
    for i in range(4):
        if i in [1,3]:
            btn.fd(height)
        else:
            btn.fd(width)
        btn.left(90)
    # поднимаем перо 
    btn.penup()
    # перемещаем перо внутрь прямоугольника
    btn.sety(btn.ycor() + height/2 - 12)
    btn.setx(btn.xcor() + 5)
    # выводим надпись
    btn.write(text, font=("Arial", 12, "normal"))


# Настраиваем окно модуля
screen = turtle.Screen()
screen.setup(600, 600)

# создаем объект пера, который будет кругом
circ = turtle.Turtle()
# скрываем перо
circ.hideturtle()
# придаем объекту форму круга
circ.shape("circle")
circ.color("orange")

# объект пера, который будет кнопкой
btn = turtle.Turtle()
# скрываем перо
btn.hideturtle()
# размеры кнопки
btn_width = 100
btn_height = 100
# позиция кнопки на холсте
pos_1 = (-290, 190)
pos_2 = (-185, 190)
pos_3 = (-80, 190)
pos_1_1 = (-290, 85)
pos_2_1 = (-185, 85)
pos_3_1 = (-80, 85)
pos_1_2 = (-290, -20)
pos_2_2 = (-185, -20)
pos_3_3 = (-80, -20)
# рисуем кнопку
draw_bth(btn_width, btn_height, pos_1, 'Нажми меня.')
draw_bth(btn_width, btn_height, pos_2, 'Нажми меня.')
draw_bth(btn_width, btn_height, pos_3, 'Нажми меня.')
draw_bth(btn_width, btn_height, pos_1_1, 'Нажми меня.')
draw_bth(btn_width, btn_height, pos_2_1, 'Нажми меня.')
draw_bth(btn_width, btn_height, pos_3_1, 'Нажми меня.')
draw_bth(btn_width, btn_height, pos_1_2, 'Нажми меня.')
draw_bth(btn_width, btn_height, pos_2_2, 'Нажми меня.')
draw_bth(btn_width, btn_height, pos_3_3, 'Нажми меня.')
# прослушиваем события активного холста
screen.listen()
# клик мышки по кнопке
screen.onscreenclick(btnclick, 1)

# нажатия стрелок клавиатуры 
# (перемещение круга по холсту)
screen.onkeypress(lambda: circ.sety(circ.ycor() + 10), 'Up')
screen.onkeypress(lambda: circ.sety(circ.ycor() - 10), 'Down')
screen.onkeypress(lambda: circ.setx(circ.xcor() + 10), 'Right')
screen.onkeypress(lambda: circ.setx(circ.xcor() - 10), 'Left')
# Для закрытия холста нужно нажать любую 
# НЕ зарегистрированную выше клавишу
screen.onkeypress(lambda: turtle.bye())
turtle.mainloop()
