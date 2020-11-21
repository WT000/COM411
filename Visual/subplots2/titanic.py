import csv
import matplotlib.pyplot as plt

def read_data():
  with open("Visual/subplots2/titanic.csv") as csvraw:
    csv_reader = csv.reader(csvraw)

    data = {
      "survived":[],
      "class":[],
      "sex":[],
      "age":[],
      "fare":[]
    }
    
    next(csv_reader)
    
    for line in csv_reader:
      if (line[1] == "" or line[2] == "" or line[4] == "" or line[5] == "" or line[9] == ""):
        pass
      else:
        data["survived"].append(int(line[1]))
        data["class"].append(int(line[2]))
        data["sex"].append(line[4])
        data["age"].append(round(float(line[5])))
        data["fare"].append(round(float(line[9]), 2))
    
    return data

def run():
  data = read_data()
  survived_list = data.get("survived")
  class_list = data.get("class")
  age_list = data.get("age")
  
  fig, axes = plt.subplots(1, 2)
  fig.suptitle("Titanic Data Analysis")

  ### THE DIFFERENT CLASSES ON TITANIC AND THEIR DEATHS ###
  print("\nLoading Class and Death comparison...")
  for class_loop in range(3):
    total_deaths = 0
    
    for count in range(len(survived_list)):
      if (survived_list[count] == 0 and class_list[count] == class_loop + 1):
        total_deaths += 1
    
    axes[0].bar(class_loop+1, class_list.count(class_loop+1), color="g")
    axes[0].bar(class_loop+1, total_deaths, color="r")

  axes[0].set_xlabel("Class")
  axes[0].set_ylabel("No. People")
  print("Done!")

  ### THE DIFFERENT AGES ON TITANIC AND THEIR DEATHS ###
  print("Loading Age and Death comparison...")
  age_set = set(age_list)
  
  for age in age_set:
    death_count = 0

    for count in range(len(age_list)):
      if (survived_list[count] == 0 and age_list[count] == age):
        death_count += 1

    axes[1].bar(age, age_list.count(age), color="g")
    axes[1].bar(age, death_count, color="r")

  axes[1].set_xlabel("Age")
  axes[1].set_ylabel("No. People")
  print("Done!")

  print("Visualising...")
  fig.tight_layout()
  plt.show()

run()
