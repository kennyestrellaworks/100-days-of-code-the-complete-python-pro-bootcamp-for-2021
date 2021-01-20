def turn_right():
    turn_left()
    turn_left()
    turn_left()
    move()

while not at_goal():
  if wall_in_front():
    turn_left()
  elif right_is_clear():
    turn_right()
  else:
    move()  