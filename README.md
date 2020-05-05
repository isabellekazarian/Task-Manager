# Task Manager

## About
This program acts as a task manager for multiple users. The adminstrator can create new users, assign tasks, and view statistics for all tasks. All users can view tasks and mark them as completed. Login is required to perform any action. Data is stored and updated in local text files.

## Prerequisites

Requires Python 3


## Getting Started

To run, save **task_manager.py** and **user.txt** to computer. Optionally save **tasks.txt** to computer.
Be sure that **user.txt** and **tasks.txt** are in the same directory as **task_manager.py**.

Please note that **user.txt** is in the format: ```username, password```
and must contain the username ```admin``` with a corresponding password for the program to be fully functional.
This is the only requirement for **user.txt**

**tasks.txt** is optional and will be created by the program if not provided. The file provided is an example.

Open **task_manager.py** using the Python 3 IDLE. Then run the program using the IDLE.

## Using the program
All user input will be entered into the Python Shell window. 
The program will first ask for a username and password. From here, a menu will be displayed containing the different functionalities of the program.
*Please note that the "admin" user must be logged in to register a new user, view statistics, and generate reports.*

All tasks and users created from the **task_manager.py** program will be saved to their respective .txt files in the local directory.
The program will load the saved information from these files when it is next run.

## Input & Output files

### tasks.txt and user.txt
These files are read and written to by **task_manager.py**.
If these files are modified outside the **task_manager.py** program, the program may not run properly.
To make changes to the users or tasks, it is best to use the **task_manager.py** program.
However, it is safe to remove a user or task by removing an entire line as follows:

``` Before: 
letty, Sample Task, This task is a sample for an example., 14 Apr 2020, 08 May 2020, No
amy, Organize Files, Organize the files in the administrative folder., 14 Apr 2020, 17 Apr 2020, No
admin, Employee Meeting, Hold meeting in regards to new personnel changes., 14 Apr 2020, 21 Apr 2020, No
letty, Call AmeriServe, Reach out to corporation to get updated billing info., 14 Apr 2020, 24 Apr 2020, No
```

``` After -- removed task for user "amy" :
letty, Sample Task, This task is a sample for an example., 14 Apr 2020, 08 May 2020, No
admin, Employee Meeting, Hold meeting in regards to new personnel changes., 14 Apr 2020, 21 Apr 2020, No
letty, Call AmeriServe, Reach out to corporation to get updated billing info., 14 Apr 2020, 24 Apr 2020, No
```


### task_overview.txt and user_overview.txt
These files are written by the program (write-only).
If these files are modified outside the **task_manager.py** program, the program will overwrite any changes the next time reports are generated.


