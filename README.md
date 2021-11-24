
README - IMPORTANT INFORMATION

SUM
 
Our application will let you organize all your spending and set limits to each category. For example, you don’t want to spend more than 50€ on parties. Then, you can view how much have you spent, and you also can maximize your benefits points given a budget. There are two available versions: one which stores the data in other files, and the other one works with the data you just entered. The first one is designed for people that want to see the evolution of their spending during a period. And the second one is more efficient and is used more like a calculator.
 
INSTALLATION
 
It is necessary to install Python 3, and the following libraries:
●	Matplotlib: which creates the graphs.
●	Pandas: to analyze your data.
 
If you want to use the version that stores the data, you also need to install the following files: “users.txt”, “limits.txt”, and “expenses.txt”. Then, you are ready to open the file named “sum_store.py”. You may need to upload the “.txt” files to your interpreter or change the code including the path your computer needs to access them. For example instead of open(“users”, mode = “a”), use open(“/Users/angel/desktop/users, mode = “a”).
 
USAGE
 
People use Sum to see their expenses and try to minimize them. The user can add limits, expenses, and the application provides a good overview of them.
 
When the user initializes the app, it asks to log in or create an account. That way, different users can use the same app without interfering with each other. Then, the main menu is shown. You have 4 options: spending limits, visualizations and insights, manage spending and log out. You can access the option you want by typing its related number.

In order to let the program work, you first should access “spending limits”, and add some limits. Each limit has two values: category and amount. For example food, 500, if you don’t want to spend more than €500 on food. Then, if you want to see your limits, you can click on display limits.

Once you have inserted some limits, you can insert expenses by going to “manage spending”. Each expense has four inputs: name of the expense, amount, category, and benefit produced by that expense from 1 to 10.

After inserting limits and expenses, the main functions of the program are set to start working. When the user goes to “visualizations and insights”, the user can choose between three functions that will help him to organize his spendings, and prioritize them. The first option is to display the percentage of budget reached. This function calculates how much has the user spent on each category, and divides it by the limit, so it returns the percentage of the limit spent on each category. The second option “display composition”, creates a pie chart showing the weight of each category over the total money spent. Finally, the third function (“maximize benefit for given budget”) consist of an algorithm that maximizes the benefit points given a constraint budget that the user inserts.
 
EXTRA INFORMATION
 
We have used OOP, using the method “Class” in python. We have also used pandas to read and process the files with the data stored, and implemented different functions to accomplish our objectives.
 
CREDITS
 
Authors: Artur Renzenbrink, Ángel Conesa, Mario Guraieb, Abdallah Ghaddar, Ethan Lhoest and Blair Ferguson

![image](https://user-images.githubusercontent.com/87434940/143322270-ef03c84b-01a0-4ac1-a1c2-45b04f581faf.png)

