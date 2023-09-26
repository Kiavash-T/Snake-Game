from Snake import Snake
from Food import Food
from tkinter import *


window = Tk()


window.title("Snake Game")
window.resizable(False, False)

# The Background & Introductions
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH) 
canvas.pack()
canvas.create_text(GAME_WIDTH / 2 , GAME_HEIGHT / 2, font= ("@Kozuka Gothic Pro EL", 40), text="Snake Game", fill="black")

# Create a lable
label = Label(window, text="Enter The color of the Snake And the Speed(1 to 10):         ")
label.pack()

# Create an Entry field
entry = Entry(window)
entry.pack()

# Create a Button
button_pressed = StringVar()
button = Button(window, text="Submit", fg="green", command=lambda: button_pressed.set("button pressed"))
button.pack()

# Put the Window at the center
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width // 2) - (window_width // 2))
y = int((screen_height // 2) - (window_height // 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

button.wait_variable(button_pressed)

label.destroy()

window.update()
snake = Snake()
food = Food()
window.mainloop()
