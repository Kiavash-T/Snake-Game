def next_turn(snake, food):
   x, y = snake.coordinates[0]
   if direction == "up":
      y -= SPACE_SIZE
   elif direction == "down":
      y += SPACE_SIZE
   elif direction == "left":
      x -= SPACE_SIZE
   elif direction == "right":
      x += SPACE_SIZE

   snake.coordinates.insert(0, [x, y])
   square = canvas.create_rectangle(x, y , x + SPACE_SIZE, y + SPACE_SIZE,fill =SNAKE_COLOR)
   snake.squares.insert(0, square)
   
def change_direction(new_dir):
   global direction

   if new_dir == "left":
      if direction != "right":
         
         direction = new_dir
   elif new_dir == "right":
      if direction != "left":
         direction = new_dir
   elif new_dir == "up":
      if direction != "down":
         direction = new_dir
   elif new_dir == "down":
      if direction != "up":
         direction = new_dir
