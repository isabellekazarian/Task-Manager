
from datetime import date, datetime, timedelta

# ---------- FUNCTION DECLARATIONS -----------------

# *****************************
# Function asks user to exit to main menu
# *****************************
def exitToMenu():
    toMenu = ""
    while(toMenu.lower() != "m") :
        print("")
        toMenu = input("Enter \"M\" to return to the main menu: ")
            
        # Loop if bad input
        if(toMenu.lower() != "m") :
            print("")
            print("  Error: invalid input.\n")

# **********************************************************


#**************************************
# Function generates file with task statistics
#**************************************

def generate_task_reports(taskList):
    taskReportFile = open('task_overview.txt', 'w')

    # Initialize variables
    tasks_complete = 0
    tasks_incomplete = 0
    tasks_overdue = 0
    
    today = datetime.today()  # Today's date

    for i in range(len(taskList)):

        # Complete Task
        if taskList[i][5] == "Yes":
            tasks_complete += 1

        # Incomplete tasks
        else:
            tasks_incomplete += 1

            # Check for overdue task
            current_due_date = datetime.strptime(taskList[i][4], "%d %b %Y")
            if(current_due_date < today):
                tasks_overdue += 1

    # Calculate percentages         
    tasks_complete_percentage   = round((tasks_complete   / len(taskList)) * 100)
    tasks_incomplete_percentage = round((tasks_incomplete / len(taskList)) * 100)
    tasks_overdue_percentage    = round((tasks_overdue    / len(taskList)) * 100)


    # -------------- Output ----------------------------
    # Print heading
    taskReportFile.write("Task Overview  -------------------------------------------\n")


    # --------- Print Task Stats ----------    
    taskReportFile.write(f"Total number of tasks:  {len(taskList)}")
    taskReportFile.write("\n\n")
    taskReportFile.write(f"Tasks Completed:        {tasks_complete}\tPercent of total:  {tasks_complete_percentage}%\n")
    taskReportFile.write(f"Tasks Incomplete:       {tasks_incomplete}\tPercent of total:  {tasks_incomplete_percentage}%\n")
    taskReportFile.write(f"Tasks Overdue:          {tasks_overdue}\tPercent of total:  {tasks_overdue_percentage}%\n")
    taskReportFile.write("\n")


    taskReportFile.close()
    
    print("Task reports sent to task_overview.txt")
    print("")





##############################################################


#**************************************
# Function generates file with user statistics
#**************************************

def generate_user_reports(userList, taskList):
    userReportFile = open('user_overview.txt', 'w')

    userTaskDict = {}   
    today = datetime.today()  # Today's date

    for i in range(len(taskList)):

        # Check task username / create dict entry
        task_user = taskList[i][0]

        if task_user not in userTaskDict :
            userTaskDict[task_user] = {'tasks_complete' : 0, 'tasks_incomplete' : 0, 'tasks_overdue' : 0, 'total_tasks' : 0}

        # Count task
        userTaskDict[task_user]['total_tasks'] += 1
        
        # Complete Task
        if taskList[i][5] == "Yes":
            userTaskDict[task_user]['tasks_complete'] += 1

        # Incomplete tasks
        else:
            userTaskDict[task_user]['tasks_incomplete'] += 1

            # Check for overdue task
            current_due_date = datetime.strptime(taskList[i][4], "%d %b %Y")
            if(current_due_date < today):
                userTaskDict[task_user]['tasks_overdue'] += 1


    # -------------- Output -----------------------
    userReportFile.write("User Overview  ------------------------------------------\n\n")
    userReportFile.write(f"Total number of registered users:  {len(userList)}\n")
    userReportFile.write(f"Total number of tasks:             {len(taskList)}\n")
    userReportFile.write("\n\n")


    for i in range(len(userList)):

        task_user = userList[i][0]

        # Print heading
        userReportFile.write(f"Task Overview: {task_user}  ")

        for i in range(40 - len(task_user)):
            userReportFile.write("-")

        userReportFile.write("\n\n")

        # Skip users with no tasks
        if task_user not in userTaskDict :
            userReportFile.write("User does not have any assigned tasks.\n\n")

        else :
    
            # --------- Print Task Stats ----------
            userReportFile.write(f"Total number of assigned tasks:  {userTaskDict[task_user]['total_tasks']}\n")
            userReportFile.write(f"Percent of total tasks:          {round((userTaskDict[task_user]['total_tasks'] / len(taskList)) * 100)}%\n\n")
            
            userReportFile.write(f"Assigned Tasks Completed %:      {round((userTaskDict[task_user]['tasks_complete']   / userTaskDict[task_user]['total_tasks']) * 100)}%\n")
            userReportFile.write(f"Assigned Tasks Incomplete %:     {round((userTaskDict[task_user]['tasks_incomplete'] / userTaskDict[task_user]['total_tasks']) * 100)}%\n")
            userReportFile.write(f"Assigned Tasks Overdue %:        {round((userTaskDict[task_user]['tasks_overdue']    / userTaskDict[task_user]['total_tasks']) * 100)}%\n")
            userReportFile.write("\n")

        userReportFile.write("\n")
    
    userReportFile.close()
    
    print("User reports sent to user_overview.txt")
    print("")



# *****************************
# Function registers a new user
# *****************************
def reg_user(userList, userFile):
    newUserMenuInput = ""
    newUser = ""
    newPass = ""
    passMatch = False

    print("")
    print("------------------------------------------------")
    print("USER REGISTRATION")
    print("")


    # --------- Add New Username ----------
    while newUser == "":
        newUser = input("Please enter a new username:  ")

        if newUser == "" :
            print("")
            print("  Error: Please enter a username.\n")

        # check if username exists
        for i in range (0, len(userList)) :
            if userList[i][0].lower() == newUser.lower() :
                print("")
                print("  Error: Username already exists. Please choose another username.\n")
                newUser = ""


    # --------- Add New Password ----------
    while(passMatch == False) :

        # New password input validation
        newPass  = input("Please enter a password:      ")

        if newPass == "" :
            print("")
            print("  Error: Please enter a password.\n")

       
        # Confirm password
        else:
            confPass = input("Please confirm password:      ")

            if(newPass == confPass) :
                passMatch = True
            else :
                print("")
                print("  Error: Passwords do not match. Please try again.\n")


    # --------- Confirm New User ----------
    while(newUserMenuInput != "y" and newUserMenuInput != "m") :

        # Preview credentials before saving
        print("")
        print("New user credentials:")
        print(f"  Username:  {newUser}")
        print(f"  Password:  {newPass}")
        print("")
        
        newUserMenuInput = input("Enter Y to confirm or M to return to the main menu:  ").lower()

        # Save New User
        if(newUserMenuInput == "y") :
            
            # Save to User file
            userFile.write("\n" + newUser + ", " + newPass)
            userFile.flush()

            # Update user list & password list  # Done to avoid reloading entire file
            userList.append([newUser, newPass])
          
            print("")
            print("New user saved successfully.")

        # Quit to main menu    
        elif(newUserMenuInput == "m") :
            print("")
            print("User not saved.")
            break
        
        # Loop if bad input
        else :
            print("")
            print("  Error: Enter \"Y\" to confirm or \"M\" to return to the main menu.")

    return None
# *************************************



# *****************************
# Function adds a new task
# *****************************
def add_task(userList, taskList, taskFile):
    
    print("------------------------------------------------")
    print("ADD A NEW TASK")
    print("")

    taskInputValid = False

    # --------- Get Task User ----------
    while taskInputValid == False :
        userIndex = 0
        taskUser  = input("  Username:    ")

        # Loop checks if username is valid
        while (userIndex < len(userList)) and (taskInputValid == False) :
            
            # Case: Username valid
            if taskUser.lower() == userList[userIndex][0].lower() :     # username not case-sensitive
                taskInputValid = True
                
            else :
                userIndex += 1
        
        # Case: Username invalid
        if taskInputValid == False :
            print("")
            print("  Error: Username not found. Please try again.\n")


    
    # --------- Get Task Title ----------
    taskInputValid = False
    
    while taskInputValid == False:
        task_title = input("  Task:        ")
        
        if (task_title == "") or (task_title == "\n"):
            print("")
            print( "  Error: Please enter a task name.\n")
            print(f"  Username:    {taskUser}")
            
        elif "," in task_title:
            print("")
            print( "  Error: Invalid character \",\" .\n")
            print(f"  Username:    {taskUser}")

        else:
            taskInputValid = True


    # --------- Get Task Description ----------
    taskInputValid = False
    
    while taskInputValid == False:
        task_description = input("  Description: ")
        
        if task_description == "" :
            print("")
            print( "  Error: Please enter a description.\n")
            print(f"  Username:    {taskUser}")
            print(f"  Task:        {task_title}")

        elif "," in task_description:
            print("")
            print( "  Error: Invalid character \",\" .\n")
            print(f"  Username:    {taskUser}")
            print(f"  Task:        {task_title}")
            
        else:
            taskInputValid = True

            
    # --------- Get Task Due Date ----------

    today = date.today()  # Today's date
    taskInputValid = False
   
    while taskInputValid == False:
        numDaysDue = input("  Task due in how many days?:  ")
     
        if numDaysDue.isdigit() and int(numDaysDue) > 0 :
            numDaysDue = int(numDaysDue)

            # Set / format due date
            dueDate = today + timedelta(days = numDaysDue)
            dueDate = dueDate.strftime("%d %b %Y")
            
            taskInputValid = True
            
        else :
            print("  Error: please enter a positive integer.")
            print("")
            print(f"  Username:    {taskUser}")
            print(f"  Task:        {task_title}")
            print(f"  Description: {task_description}")

    # Format today's date
    dateToday = today.strftime("%d %b %Y") #format 16 Sep 2019



    # --------- Save New Task ----------

    taskFile.write(f"\n{taskUser}, {task_title}, {task_description}, {dateToday}, {dueDate}, No")
    taskFile.flush()
    taskList.append([taskUser, task_title, task_description, dateToday, dueDate, "No"])

    print("\n  New task saved successfully.")

    exitToMenu()
    
    return None
# ********************************************


# *****************************
# Function displays all tasks
# *****************************
def view_all(taskList):
    
    print("")
    print("----------------------------------------------------------")
    print("CURRENT TASKS")
    print("")

    # Tasks data by index:
    #0 username , 1 title, 2 description, 3 date created, 4 due date, 5 complete y/n
    hasTasks = False

    for i in range(len(taskList)) :
        task_num = i+1
        hasTasks = True
        
        # Print heading
        if("yes" == taskList[i][5].lower()):
            print(f"Task #{task_num} (Complete) ---------------------------------")
        else :
            print(f"Task #{task_num}  -------------------------------------------")


        # --------- Print Task Details ----------    
        print(f"Assigned to:  {taskList[i][0]}")
        print("")
        print(f"Task:         {taskList[i][1]}")
        print(f"Description:  {taskList[i][2]}")
        print("")
        print(f"Assigned:     {taskList[i][3]}")
        print(f"Due Date:     {taskList[i][4]}")
        print(f"Complete?:    {taskList[i][5]}")
        print("")

    if not hasTasks :
        print("There are no current tasks.")
        print("")

    exitToMenu()


    return None
# **************************************************

# *****************************
# Function displays current user's tasks
# *****************************
def view_mine(taskList, taskFile, userList, username):
    
    print("")
    print("----------------------------------------------------------")
    print("MY TASKS")
    print("")

    hasTasks = False
    taskInput = ""

    # Tasks data by index:
    #0 username , 1 title, 2 description, 3 date created, 4 due date, 5 complete y/n

        
    for i in range(len(taskList)) :
        if(taskList[i][0].lower() == username.lower()) :
            task_num = i+1
            hasTasks = True

            print("")
            # Print heading
            if("yes" == taskList[i][5].lower()):
                print(f"Task #{task_num} (Complete)  --------------------------------")
            else :
                print(f"Task #{task_num}  -------------------------------------------")


            # --------- Print Task Details ----------    
            print(f"Assigned to:  {taskList[i][0]}")
            print("")
            print(f"Task:         {taskList[i][1]}")
            print(f"Description:  {taskList[i][2]}")
            print("")
            print(f"Assigned:     {taskList[i][3]}")
            print(f"Due Date:     {taskList[i][4]}")
            print(f"Complete?:    {taskList[i][5]}")
            print("")

    # If no tasks, return to main menu
    if not hasTasks :
        print("You do not currently have any tasks.")
        print("")
        exitToMenu()
        return

    # Check for valid menu input
    taskNum = ""
    while taskNum == "":
        taskNum = input("Enter a task number to edit or enter \"M\" to return to the main menu:  ")

        # Valid number entry
        if taskNum.isdigit():
            taskNum = int(taskNum)

            if taskNum < 1 or taskNum > len(taskList):
                print("")
                print(f"  Error: Task #{taskNum} does not exist.")
                print("")
                taskNum = ""

            elif taskList[taskNum-1][0].lower() != username.lower():
                print("")
                print(f"  Error: Task #{taskNum} is not assigned to {username}.")
                print("")
                taskNum = ""

        # Invalid entry          
        elif taskNum.lower() != "m":
            print("")
            print("  Error: Invalid input.")
            print("")
            taskNum = ""

        # If user chose to exit
        elif taskNum.lower() == "m":
           return


    taskIndex = taskNum - 1
    

    # Get & Validate Input
    
    taskInput = ""

    # Print task info
    print("")
    print("")
    print(f"Task #{taskNum} Details  ------------------------------------")
    print("")
    print(f"Assigned to:  {taskList[taskIndex][0]}")
    print(f"Task:         {taskList[taskIndex][1]}")
    print(f"Description:  {taskList[taskIndex][2]}")
    print("")
    print(f"Assigned:     {taskList[taskIndex][3]}")
    print(f"Due Date:     {taskList[taskIndex][4]}")
    print(f"Complete?:    {taskList[taskIndex][5]}")
    print("")
    print("")
    
    
    
    while taskInput != "s" :

        # Edit Task Menu
        print("Please select one of the following options:")
        print("")
        print("     c\t- Mark Complete")
        print("     i\t- Mark Incomplete")
        print("     e\t- Edit Task")
        print("     s\t- Save & Exit to Main Menu")
        print("")

        taskInput = ""
        taskInputValid = False
        

        # --------- Get & Validate Input ----------
        while taskInputValid == False :

            taskInput = input("Please choose:  ")
            taskInput = taskInput.lower()

            # Check for valid input
            if (   (taskInput == "e" ) or (taskInput == "i" ) \
                or (taskInput == "c") or (taskInput == "s") ) :
                taskInputValid = True    
              
            else :
                print("")
                print("Please enter a selection from the menu above.")


    
        # Menu: Mark Complete
        if taskInput == "c":
            if  taskList[taskIndex][5] == "No" :
                taskList[taskIndex][5] = "Yes"
                print("")
                print("Task marked complete.")
                print("")
            else:
                print("")
                print("Task already marked complete.")
                print("")


        # Menu: Mark Incomplete
        elif taskInput == "i":
            if  taskList[taskIndex][5] == "Yes" :
                taskList[taskIndex][5] = "No"
                print("")
                print("Task marked incomplete.")
                print("")

            else:
                print("")
                print("Task already marked incomplete.")
                print("")
                


        # Menu: Edit Task (incomplete)
        elif taskInput == "e" and taskList[taskIndex][5] == "No":


            # -------- Loop: User edits username for selected task --------
            editInput = ""
            while editInput == "":
                print("")
                editInput = input("Edit username? (Y/N):  ").lower()

                if editInput == "y":
                    userValid = False

                    # ----- Check for valid username entry ------
                    while userValid == False:
                        print("")
                        editUsername = input("Enter new username:  ")

                        for i in range(len(userList)):
                            if userList[i][0].lower() == editUsername.lower():
                                userValid = True

                        if editUsername == "" or editUsername == "\n":
                            print("")
                            print("  Error: please enter a username.")
                            

                        elif not userValid:
                            print("")
                            print("  Error: User does not exist. Please enter a valid username.")
                            

                    # ----- Change username ----
                    taskList[taskIndex][0] = editUsername
                    print("")
                    print(f"Task now assigned to:  {editUsername}")

                # Bad input
                elif editInput != "n":
                    print("  Error: Invalid input.\n")
                    editInput == ""


            # -------- Loop: User edits due date for selected task --------
            editInput = ""
            while editInput == "":
                print("")
                editInput = input("Edit due date? (Y/N):  ").lower()

                if editInput == "y":
                    dateValid = False
                    
                    # ----- Check for valid due date entry ------
                    while dateValid == False:
                        print("")
                        editDate = input("Task due in how many days?:  ")

                        if editDate.isdigit():
                            editDate = int(editDate)

                            # ------- Change due date ---------
                            if editDate > 0 :

                                today = date.today()

                                dueDate = today + timedelta(days = editDate)
                                dueDate = dueDate.strftime("%d %b %Y")
                                

                                taskList[taskIndex][4] = dueDate
                                dateValid = True
                                
                                print("")
                                print(f"Due date is now {dueDate}.")
                                print("")

                        # Bad input
                        else:
                            print("  Error: Please enter a positive integer.  ")
                            print("")

                # Bad input  
                elif editInput != "n":
                    print("  Error: Invalid input.\n")
                    editInput == ""


        # Menu: Edit Task (Already complete)
        elif taskInput == "e":
            print("")
            print("  Error: Cannot edit a completed task.")
            print("")
             
    
    
    # TODO : UPDATE TASK FILE
    taskFile = open('tasks.txt', 'r+')
    for i in range(len(taskList)) :
        lineInFile = ", ".join(taskList[i]) + '\n'
        taskFile.write(lineInFile)


    taskFile.flush()
    print("")
    print("Task updated successfully.")
   
    
    return None
# **********************************************************

# **********************
# Function logs user into task manager
# ***********************

def user_login(userList):

    userValid = False
    passValid = False

    # --------- Username ----------
    while userValid == False :
        userIndex = 0
        username  = input("  Username:  ")

        # Loop checks if username is valid
        while (userIndex < len(userList)) and (userValid == False) :
            
            # Case: Username valid
            if username.lower() == userList[userIndex][0].lower() :     # username not case-sensitive
                userValid = True
                
            else :
                userIndex += 1
        
        # Case: No input
        if username == "" :
            print("")
            print("  Error: Please enter a username.\n")

        # Case: Username invalid
        elif userValid == False :
            print("")
            print("  Error: Username not found. Please try again.\n")
            


    # --------- Password ----------

    # Password verification
    while passValid == False :
        password  = input("  Password:  ")

        # Check that password stored with given user matches password entered
        if (password == userList[userIndex][1]) :
                passValid = True
                print("")
                print("Login successful!")

        # Password invalid
        else :
            print("")
            print("  Error: username and password do not match. Password is case-sensitive. Please try again.\n")
            print(f"  Username:  {userList[userIndex][0]}")

    return userIndex
#***************************************************




# ----------- DATA ABSTRACTION ---------------------

# Declare variables
userList = []
taskList = []

taskInputValid = False

# Open files
userFile = open('user.txt' , 'r+')
taskFile = open('tasks.txt', 'a+')

# Create user list from user file
for line in userFile :
    line = line.replace("\n", "")
    line = line.split(", ")
    userList.append([line[0], line[1]]) #store username and password as a list within list

# Create task list from task file
taskFile.seek(0)
for line in taskFile :
    line = line.replace("\n", "")
    line = line.split(", ")
    taskList.append([line[0], line[1], line[2], line[3], line[4], line[5]])

    if line == "" or line == "\n" :
        continue  # skip empty lines



# ------------------ USER LOGIN --------------------

print("")
print("Welcome to the task manager. Please log in.")
print("")

userIndex = user_login(userList)
username  = userList[userIndex][0]



# -------------------------------- MAIN MENU ----------------------------------   
       
print("")
print("-----------------------------------------------------------------------")
print("")
print(f"Welcome back, {userList[userIndex][0]}!")

menuInput = ""


# --------- Print Menu ----------

while(menuInput != "e") :
    menuValid = False

    print("\n")
    print("Please select one of the following options:")
    print("")
    print("     r\t- Register User")
    print("     a\t- Add Task")
    print("     va\t- View All Tasks")
    print("     vm\t- View My Tasks")
    
    if(username.lower() == "admin"):       # Admin can view stats/generate reports
        print("     s\t- Statistics")
        print("     gr\t- Generate Reports")
    
    print("     su\t- Switch User")
    print("     e\t- Exit")
    print("")


    # --------- Get & Validate Input ----------
    while menuValid == False :

        menuInput = input("Please choose:  ")
        menuInput = menuInput.lower()

        # Check for valid input
        if (   (menuInput == "r" ) or (menuInput == "a" ) \
            or (menuInput == "va") or (menuInput == "vm") \
            or (menuInput == "su") or (menuInput == "e" )) :
            menuValid = True
            
        elif((menuInput == "s" ) and (username.lower() == "admin")) or \
             (menuInput == "gr") and (username.lower() == "admin"):  # Admin can generate reports
            menuValid = True
            
        else :
            print("")
            print("Please enter a selection from the menu above.")




    # ------------------ MENU SELECTION --------------------

    # ---- Register User -----
    if (menuInput == "r" and username.lower() == "admin") :
        reg_user(userList, userFile)


        
    # ---- Register User (Admin not logged in) -----
    elif menuInput == "r" :
         print("")
         print("  Error: administrator must be logged in to register a new user.")


    # ---- Add Task -----
    elif(menuInput == "a") :
        add_task(userList, taskList, taskFile)


    # ---- View All Tasks -----
    elif(menuInput == "va") :
        view_all(taskList)
                    

    # ---- View My Tasks -----
    elif(menuInput == "vm") :
        view_mine(taskList, taskFile, userList, username)



    # ---- View Stats (Admin Only) ---
    elif(menuInput == "s") :

        # Print Stats
        print("------------------------------------------------")
        print("STATISTICS")
        print("")
        print("")
        print(f"Total number of tasks:  {len(taskList)}")
        print(f"Total number of users:  {len(userList)}")


        exitToMenu()


    # ---- Generate Reports (Admin Only) ---
    elif(menuInput == "gr") :

        # Print Stats
        print("------------------------------------------------")
        print("GENERATE REPORTS")
        print("")

        generate_task_reports(taskList)
        generate_user_reports(userList, taskList)
        
        print("")

        taskOverviewFile = open('task_overview.txt', 'r')
        userOverviewFile = open('user_overview.txt', 'r')

        for line in taskOverviewFile:
            print(line, end = ' ')

        for line in userOverviewFile:
            print(line, end = ' ')


        taskOverviewFile.close()
        userOverviewFile.close()  
        


        exitToMenu()
        

    # ---- Switch User -----
    elif(menuInput == "su") :
        print("")
        userInput = input("Do you wish to log out? (Y/N):  ").lower()
        
        while userInput != "y" and userInput != "n" :
            print("")
            print("  Error: invalid input.\n")
            userInput = input("Do you wish to log out? (Y/N):  ").lower()
            
        if userInput == "y":
            print("")
            userIndex = user_login(userList)
            username  = userList[userIndex][0]

            print("")
            print("-----------------------------------------------------------------------")
            print("")
            print(f"Welcome back, {userList[userIndex][0]}!")
                   
        
        


# ------------------ MENU: EXIT --------------------
# Program will exit automatically if "e" is entered in main menu
# Main loop is conditional on "e"

userFile.close()
taskFile.close()

print("\nGoodbye!")




    
