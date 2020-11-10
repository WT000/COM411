import matplotlib.pyplot as plt

def smiley():
  x_border = [0, 0, 50, 50, 0]
  y_border = [0, 50, 50, 0, 0]
  plt.plot(x_border, y_border, "k-")
  plt.xlabel("x border")
  plt.ylabel("y border")
  
  left_x = [10, 10]
  left_y = [30, 40]
  plt.plot(left_x, left_y, "k-")
  
  right_x = [40, 40]
  right_y = [30, 40]
  plt.plot(right_x, right_y, "k-")

  mouth_x = [15, 15, 35, 35]
  mouth_y = [15, 10, 10, 15]
  plt.plot(mouth_x, mouth_y, "k-")
  plt.show()

def creeper():
  x_border = [0, 0, 80, 80, 0]
  y_border = [0, 80, 80, 0, 0]
  plt.plot(x_border, y_border, "g-")
  plt.xlabel("x border")
  plt.ylabel("y border")

  x_mouth = [20, 20, 30, 30, 50, 50, 60, 60, 50, 50, 30, 30, 20]
  y_mouth = [10, 40, 40, 50, 50, 40, 40, 10, 10, 20, 20, 10, 10]
  plt.plot(x_mouth, y_mouth, "k-")

  x_left_eye = [10, 10, 30, 30, 10]
  y_left_eye = [50, 70, 70, 50, 50]
  plt.plot(x_left_eye, y_left_eye, "k-")

  x_left_pupil = [20, 20, 30]
  y_left_pupil = [50, 60, 60]
  plt.plot(x_left_pupil, y_left_pupil, "k-")

  x_right_eye = [50, 50, 70, 70, 50]
  y_right_eye = [50, 70, 70, 50, 50]
  plt.plot(x_right_eye, y_right_eye, "k-")

  x_right_pupil = [60, 60, 50]
  y_right_pupil = [50, 60, 60]
  plt.plot(x_right_pupil, y_right_pupil, "k-")

  plt.show()

def run():
  choice = int(input("What do you wish to view? \n1. Smiley Face \n2. Creeper \n"))
  
  if (choice == 1):
    smiley()
  elif (choice == 2):
    creeper()
  else:
    print("Input not recognised.")

run()