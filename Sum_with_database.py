import matplotlib.pyplot as plt
import pandas as pd


class Expense:
    def _init_(self, user, name, amount, category, benefit):
        self.user = user
        self.name = name
        self.amount = amount
        self.category = category
        self.benefit = benefit
        self.insert_expenses()

    def _str_(self):
        return "Name: {}, Amount: {}, Category: {}, Benefit: {}".format(self.name, self.amount, self.category,
                                                                        self.benefit)

    def insert_expenses(self):
        db = open("expenses", mode="a")
        content = str(self.user) + ";" + str(self.name) + ";" + str(self.amount) + ";" + str(self.category) + ";" + str(self.benefit)
        db.write(content + "\n")
        db.close()




class Limit:
    def _init_(self, user, name, amount):
        self.name = name
        self.amount = amount
        self.user = user
        self.insert_limits()

    def _repr_(self):
        return repr((self.name, self.amount))

    def insert_limits(self):
        db = open("limits", mode="a")
        content = str(self.user + ";" + self.name + ";" + str(self.amount))
        db.write(content + "\n")



class User:
    def _init_(self, name, password):
        self.expenses = []
        self.limits = []
        self.name = name
        self.password = password
        self.insert_user()

    def _repr_(self):
        return repr((self.name, self.password, self.expenses, self.limits))

    def check_user(self):
        df = pd.read_csv("users", sep=";")
        for i in range(len(df["name"])):
            if df["name"][i] == self.name:
                return True
        return False


    def insert_user(self):
        if self.check_user is False:
            db = open("users", mode="a")
            content = str(self.name + ";" + str(self.password))
            db.write(content + "\n")
            db.close()

    def update_limits(self):  # user, name, amount
        self.limits = []
        df = pd.read_csv("limits", sep=";")
        limits = []
        for i in range(len(df["user"])):
            if df["user"][i] == self.name:
                limits.append(df["name"][i])
                limits.append(df["amount"][i])
                self.limits.append(limits)
                limits = []

    def update_expenses(self):
        self.expenses = []
        df = pd.read_csv("expenses", sep=";")
        expenses = []
        for i in range(len(df["name"])):
            if df["user"][i] == self.name:
                expenses.append(df["name"][i])
                expenses.append(df["amount"][i])
                expenses.append(df["category"][i])
                expenses.append(df["benefit"][i])
                self.expenses.append(expenses)
                expenses = []



def start():
    print("Welcome to the spending tracker!!!")
    print("1-login")
    print("2-register")
    user_input = eval(input("type the associated number to pick an option >>> "))
    if user_input == 1:
        return login()
    if user_input == 2:
        return register()
    else:

        return start()


def login():
    username = str(input("Enter your username here >>> "))
    password = str(input("Enter your password here >>> "))
    df = pd.read_csv("users", sep=";")
    for i in range(len(df["name"])):
        if df["name"][i] == username:
            if df["password"][i] == eval(password):
                user = User(username, password)
                return menu(user)
            else:
                print("incorrect password")
                return(start)
    print("you are not registered")
    return start()





def register():
    username = str(input("Enter your username here >>> "))
    password = str(input("Enter your password here >>> "))
    password_c = str(input("Confirm your password here >>> "))
    if password != password_c:
        print("Don't match")
        return register()

    db = open("users", mode="a")
    content = str(username + ";" + password)
    db.write(content + "\n")



    user = User(username, password)
    return menu(user)


def menu(user):
    print("\nWelcome to the homescreeen!")
    print("<----------------------->")
    print("1-Spending limits")
    print("2-Visualizations and insights")
    print("3-Manage spending")
    print("4-Log out")
    user_input = eval(input("Select one of the following options by typing the associated number >>> "))
    print("\n \n")
    if user_input == 1:
        return spending_limits(user)
    if user_input == 2:
        return insights(user)
    if user_input == 3:
        return manage_expenses(user)
    if user_input == 4:
        return log_out()


def log_out():
    return start()


def spending_limits(user):
    print("Welcome to the spending limit options")
    print("<----------------------->")
    print("1-Add")
    print("2-display")
    print("3-return to home")
    user_input = eval(input("Select one of the following options by typing the associated number >>> "))
    print("\n \n")
    if user_input == 1:
        return add_limit(user)
    if user_input == 2:
        return display_limit(user)
    if user_input == 3:
        return menu(user)


def add_limit(user):
    while True:
        name = input("Enter the name of the limit or enter 0 to return Home >>> ")
        if name == "0":
            return menu(user)
        amount = eval(input("enter the amount you want to add >>> "))
        Limit(user.name, name, amount)
        user.update_limits()
        print(user.limits)


def display_limit(user):
    user.update_limits()
    print(user.limits)
    return spending_limits(user)


def manage_expenses(user):
    print("Welcome to the expense managment")
    print("<----------------------->")
    print("1-Add")
    print("2-display")
    print("3-return to home")
    user_input = eval(input("Select one of the following options by typing the associated number >>> "))
    if user_input == 1:
        return add_expense(user)
    if user_input == 2:
        return display_expense(user)
    if user_input == 3:
        return menu(user)


def add_expense(user):
    while True:
        name = input("Enter the name of the expense or enter 0 to return Home >>> ")
        if name == "0":
            menu(user)
            break
        amount = eval(input("enter the amount of the expense >>> "))
        benefit = eval(input("rate from 1-10 how beneficial the expense was >>> "))
        df = pd.read_csv("limits", sep=";")
        categories = []
        for i in range(len(df["name"])):
            if df["user"][i] == user.name:
                categories.append(df["name"][i])
                print(df["name"][i])
        category = input("Enter one of the categories >>> ")
        for i in categories:
            if i == category:
                Expense(user.name, name, amount, category, benefit)
                user.update_expenses()
                print(user.expenses)
                return manage_expenses(user)
        print("You first have to create a limit to that category")
        return menu(user)


def display_expense(user):
    user.update_expenses()
    print(user.expenses)
    user_input = input("press any key and <enter> to return home")
    if user_input:
        return menu(user)


def insights(user):
    print("Welcome to the expense managment")
    print("<----------------------->")
    print("1-display percentage of budget reached")
    print("2-display composition")
    print("3-maximise benefit for given budget")
    print("0-home")
    user_input = eval(input("Select one of the following options by typing the associated number->"))
    if user_input == 1:
        return percentage(user)
    if user_input == 2:
        return composition(user)
    if user_input == 3:
        return algorithm2(user)
    if user_input == 0:
        return menu(user)


def algorithm2(user):
    user.update_expenses()
    user.update_limits()
    budget = eval(input("What is the budget or enter 0 to return home >>> "))
    costs = []
    benefits = []
    names = []
    for el in user.expenses:
        costs.append(el[1])
    for el in user.expenses:
        benefits.append(el[3])
    for el in user.expenses:
        names.append(el[0])

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
    che = input("Enter 0 to return to the menu >>> ")
    if str(che) == "0":
        return menu(user)


def composition(user):
    user.update_expenses()
    user.update_limits()
    total = 0
    for i in user.expenses:
        total += i[1]

    values = []
    categories = []
    for i in user.limits:
        category = i[0]
        expen = 0
        for j in user.expenses:
            if category == j[2]:
                expen += j[1]

        percent = expen * 100 / total
        categories.append(category)
        values.append(percent)

    plt.pie(values, labels=categories, autopct="%1.1f%%", counterclock=False, shadow=True)
    plt.title("Composition")
    plt.legend(categories, loc=4)
    plt.show()
    che = input("Enter 0 to return to the menu >>> ")
    if str(che) == "0":
        return menu(user)


def percentage(user):
    categories = []
    values = []
    user.update_limits()
    user.update_expenses()
    for i in user.limits:
        category = i[0]
        budget = i[1]
        num = 0
        for j in user.expenses:
            if category == j[2]:
                num += j[1]
        percent = (num / budget) * 100
        categories.append(category)
        values.append(percent)
    widths = [0.7] * len(categories)
    plt.bar(range(len(categories)), values, width=widths, align="center", tick_label=categories)
    plt.show()
    che = input("Enter 0 to return to the menu >>> ")
    if str(che) == "0":
        return menu(user)


start()