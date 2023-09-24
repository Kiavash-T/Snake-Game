from Snake import Snake
from Food import Food
from tkinter import *


window = Tk()


window.title("Snake Game")
window.resizable(False, False)


window.update()
snake = Snake()
food = Food()
window.mainloop()