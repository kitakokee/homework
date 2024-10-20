from random import randint, choice
from tkinter import Tk, Canvas

WIDTH = 300
HEIGHT = 200

class Ball:
    def __init__(self, x, y, r, color):
        self.R = r
        self.x = x
        self.y = y
        self.dx, self.dy = (10, 10)
        self.ball_id = canvas.create_oval(self.x - self.R,
                                           self.y - self.R,
                                           self.x + self.R,
                                           self.y + self.R, fill=color)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def random_color():
    return f'#{randint(0, 0xFFFFFF):06x}'  # Генерация случайного цвета в формате #rrggbb

def click_handler(event):
    r = randint(10, 50)  # Случайный радиус
    color = random_color()  # Генерация случайного цвета
    balls.append(Ball(event.x, event.y, r, color))  # Создание нового шарика с координатами нажатия


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = Canvas(root)
canvas.pack()
canvas.bind('<Button-1>', click_handler)
balls = []  

tick()
root.mainloop()