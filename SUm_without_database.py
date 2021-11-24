
import matplotlib.pyplot as plt
class Expense:
  def __init__(self, name, amount, category, benefit):
    self.name = name
    self.amount = amount
    self.category = category
    self.benefit = benefit
  def __str__(self):
    return "Name: {}, Amount: {}, Category: {}, Benefit: {}".format(self.name, self.amount, self.category, self.benefit)
class Limit:
  def __init__(self, name, amount):
    self.name = name
    self.amount = amount
  def __repr__(self):
    return repr((self.name, self.amount))

class User:
  def __init__(self, name, password):
    self.expenses = []
    self.limits = []
    self.name = name
    self.password = password

  def __repr__(self):
    return repr((self.name, self.password, self.expenses, self.limits))

class Users:
  def __init__(self):
    self.list = []
    self.name_passwords = {}

def dict_reading():
  my_dictionary = {}
  a_file = open("credentials.txt")
  for line in a_file:
    key, value = line.split()
    my_dictionary[key] = value
  return my_dictionary

def dict_writing(content):
  f = open("credentials.txt", "a")
  f.write(content + "\n")
  f.close()
def spending_tracker():
  users = Users()
  start(users)

def start(users):
  print("Welcome to the spending tracker!!!")
  print("1-login")
  print("2-register")
  user_input = eval(input("type the associated number to pick an option"))
  if user_input == 1:
    login(users)
  if user_input == 2:
    register(users)

def register(users):
  name = input("type in your name")
  password = input("type in your password")
  string = name +" " + password
  current_user = User(name, password)
  users.list.append(current_user)
  dict_writing(string)
  start(users)

def login(users):
  name = input("type in your name")
  password = input("type in your password")
  cred_list = dict_reading()

  if cred_list.get(name) == password:
    user = find(name, password, users)
    homescreen(user, users)
  else:
    print('login unsuccessful')
    login(users)


def find(name, password, users):
  for el in users.list:
    if el.name == name and el.password == password:
      return el


def homescreen(user, users):
  print("Welcome to the homescreeen")
  print("<----------------------->")
  print("1-spending limits")
  print("2-Visualizations and insights")
  print("3-Manage spending")
  print("4-log out")
  user_input = eval(input("Select one of the following options by typing the associated number->"))
  print("\n \n")
  if user_input == 1:
    spending_limits(user, users)
  if user_input == 2:
    insights(user, users)
  if user_input == 3:
    manage_expenses(user, users)
  if user_input == 4:
    log_out(user, users)

def log_out(user, users):
  for el in range(len(users.list)):
    if users.list[el].name == user.name and users.list[el].password == user.password:
      users.list
      [el] = user
  start(users)

def spending_limits(user, users):
  print("Welcome to the spending limit options")
  print("<----------------------->")
  print("1-Add")
  print("2-Delete")
  print("3-Edit incomplete")
  print("4-display")
  print("5-return to home")
  user_input = eval(input("Select one of the following options by typing the associated number->"))
  print("\n \n")
  if user_input == 1:
    add_limit(user, users)
  if user_input == 2:
    delete_limit(user, users)
  if user_input == 3:
    edit_limit(user, users)
  if user_input == 4:
    display_limit(user, users)
  if user_input == 5:
    homescreen(user, users)


def add_limit(user, users):
  while True:
    name = input("Enter the name of the limit or enter 0 to return Home")
    if name == "0":
      homescreen(user, users)
    amount = eval(input("enter the amount you want to add"))
    new_limit = Limit(name, amount)
    user.limits.append(new_limit)
    print(user.limits)



def display_limit(user, users):
  print(user.limits)
  user_input = input("press 0 to return home or any other key to continue")
  if user_input == "0":
    homescreen(user, users)

def delete_limit(user, users):
  display_limit(user, users)
  while True:
    user_input = input("input the name of the limit you want to delete or o to return home")
    if user_input == "0":
      homescreen(user, users)
      break
    for el in range(len(user.limits)):
      print(el)
      print(user.limits[el].name)
      if user_input == user.limits[el].name:
        user.limits.pop(el)


def manage_expenses(user, users):
  print("Welcome to the expense managment")
  print("<----------------------->")
  print("1-Add")
  print("2-display")
  print("3-reset")
  print("4-return to home")
  user_input = eval(input("Select one of the following options by typing the associated number->"))
  if user_input == 1:
    add_expense(user, users)
  if user_input == 2:
    display_expense(user, users)
  if user_input == 3:
    reset_expense(user, users)
  if user_input == 4:
    homescreen(user, users)


def add_expense(user, users):
  while True:
    name = input("Enter the name of the expense or enter 0 to return Home")
    if name == "0":
      homescreen(user, users)
      break
    amount = eval(input("enter the amount of the expense"))
    benefit = eval(input("rate from 1-10 how benefitial the expense was"))
    print("Enter one of the following categories")
    for el in user.limits:
      print(el.name)
    category = input("Enter one of the following categories")

    new_expense = Expense(name, amount, category, benefit)
    user.expenses.append(new_expense)
    print(user.expenses)

def reset_expense(user, users):
  user_input = input("Are you sure you want to reset your expenses? press 1 to continue or 0 to return to home!!")
  if user_input == "0":
    homescreen(user, users)
  if user_input == "1":
    user.expenses = []

def display_expense(user, users):
  for el in user.expenses:
    print(el)
    print("")
  user_input = input("press 0 to return home")
  if user_input == 0:
    homescreen(user, users)

def insights(user, users):
  print("Welcome to the expense managment")
  print("<----------------------->")
  print("1-display percentage of budget reached")
  print("2-display composition")
  print("3-maximise benefit for given budget")
  print("4- sort all expenses in ascending order")
  print("0-home")
  user_input = eval(input("Select one of the following options by typing the associated number->"))
  if user_input == 1:
    percentage(user, users)
  if user_input == 2:
    composition(user, users)
  if user_input == 3:
    algorithm2(user, users)
  if user_input == 0:
    homescreen(user, users)
  if user_input == 4:
    sort_algo(user, users)


def algorithm2(user, users):
  budget = eval(input("What is the budget or enter 0 to return home"))
  costs = []
  benefits = []
  names = []
  for el in user.expenses:
    costs.append(el.amount)
  for el in user.expenses:
    benefits.append(el.benefit)
  for el in user.expenses:
    names.append(el.name)
  def printknapSack(W, wt, val, n, name):
    K = [[0 for w in range(W + 1)]
         for i in range(n + 1)]
    for i in range(n + 1):
      for w in range(W + 1):
        if i == 0 or w == 0:
          K[i][w] = 0
        elif wt[i - 1] <= w:
          K[i][w] = max(val[i - 1]
                        + K[i - 1][w - wt[i - 1]],
                        K[i - 1][w])
        else:
          K[i][w] = K[i - 1][w]
    res = K[n][W]
    print("your max number of benefit points for that budget is", res)
    print("")
    print("the spending allocation for the benefit maximisation is composed of the following expenses:")
    w = W
    for i in range(n, 0, -1):
      if res <= 0:
        break
      if res == K[i - 1][w]:
        continue
      else:
        print(name[i - 1])
        res = res - val[i - 1]
        w = w - wt[i - 1]
  printknapSack(budget, costs, benefits, len(benefits), names)
  user_input = input("To go to the homescreen enter 0")
  if user_input == "0":
    homescreen(user, users)


def sort_algo(user, users):
  costs = []
  names = []
  for el in user.expenses:
    costs.append(el.amount)
  for el in user.expenses:
    names.append(el.name)

  def findthesmallest(list):
    Smallest = list[0]
    Index_smallest = 0
    for position in range(len(list)):
      if Smallest > list[position]:
        Smallest = list[position]
        Index_smallest = position
    return (Index_smallest)


  def selectionSort(costs, names):
    sorted_amounts = []
    sorted_names = []
    for position in range(len(costs)):
      sorted_amounts.append(costs[findthesmallest(costs)])
      sorted_names.append(names[findthesmallest(costs)])
      names.remove(names[findthesmallest(costs)])
      costs.remove(costs[findthesmallest(costs)])
    print(sorted_names)
  selectionSort(costs, names)
  user_input = input("To go to the homescreen enter 0")
  if user_input == "0":
    homescreen(user, users)


def percentage(user, users):
  categories = []
  values = []

  for i in user.limits:
    category = i.name
    budget = i.amount
    num = 0
    for j in user.expenses:
      if category == j.category:
        num += j.amount
    percent = (num / budget) * 100
    categories.append(category)
    values.append(percent)
  widths = [0.7] * len(categories)
  plt.bar(range(len(categories)), values, width=widths, align="center", tick_label=categories)
  plt.ylabel("percentage of limit reached")
  plt.xlabel("category")
  plt.title("Percentages reached of limit reached for each category")
  plt.show()
  user_input = input("To go to the homescreen enter 0")
  if user_input == "0":
    homescreen(user, users)

def composition(user, users):
  expens_list = []
  for el in user.expenses:
    expens_list.append(el.amount)
  total = sum(expens_list)
  names = []
  for li in user.limits:
    names.append(li.name)
  values = []
  for el in names:
    values.append(0)

  for ex in user.expenses:
    for index in range(len(names)):
      if ex.category == names[index]:
        values[index] = values[index] + ex.amount
  print(values)
  values = [(element * 100) / total for element in values]
  print(values)
  plt.pie(values, labels=names, autopct="%1.1f%%",
          counterclock=False, shadow=True)
  plt.title("Composition")
  plt.legend(names, loc=4)
  plt.show()
  user_input = input("To go to the homescreen enter 0")
  if user_input == "0":
    homescreen(user, users)

spending_tracker()
