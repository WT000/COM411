import matplotlib.pyplot as plt

def fib(n):
  fib_list = [0, 1]
  
  if (n <= 2):
    return fib_list
  
  else:
    for count in range(n):
      next_number = fib_list[count] + fib_list[count+1]
      fib_list.append(next_number)

  return fib_list

def main():
  to_graph = int(input("How many fib numbers do you wish to display?\n"))

  data = fib(to_graph)
  
  plt.plot(data)
  plt.show()

main()