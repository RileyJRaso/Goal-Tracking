import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import sys

#connecting to database
conn = sqlite3.connect('Goals.db')

# Function definitions are here
def Create(command):
    Server = conn.cursor()
    Server.execute(command)
    conn.commit()
    print("Table successfully created!")
    return;

def Insert(command):
    Server = conn.cursor()
    Server.execute(command)
    conn.commit()
    print("Data Inputed Successfully!")
    return;

def View(command):
    Server = conn.cursor()
    Server.execute(command)
    Result_List = Server.fetchall()
    return Result_List;

def ViewMonth():
    Date = input("Please enter the month you are looking for (Format = MM):\n")
    command = "SELECT * FROM Goals WHERE Date LIKE '%" + Date + "%'"
    Result_List = View(command)
    return Result_List;

def ViewYear():
    Date = input("Please enter the year you are looking for (Format = YYYY):\n")
    command = "SELECT * FROM Goals WHERE Date LIKE '" + Date + "%'"
    Result_List = View(command)
    return Result_List;


Action_List = ["Create", "Insert", "ViewGoal", "ViewDate", "ViewMonth", "ViewYear", "GraphMonth", "GraphYear"]
Action = sys.argv[1]

if Action not in Action_List:
    print("""\nERROR:The action requested is not possible with this application, the following are the currently avalible actions:\n
             \t Create     --- This command should be run when the application is first run in order to create the sql database used within this application
             \t Insert     --- This command is used to input data into the database, all information will be prompted from the user
             \t ViewGoal   --- This command is used to view all entries of a certain Goal, the goal desired will be prompted from the user
             \t ViewDate   --- This command is used to view all entries of a certain Date, the date desired will be prompted from the user
             \t ViewMonth  --- This command is used to view all entries of a certain month, the month desired will be prompted from the user
             \t ViewYear   --- This command is used to view all entries of a certain year, the year desired will be prompted from the user
             \t GraphMonth --- This command is used to Graph the data collected in a certain month, the month desired will be promted from the user
             \t GraphYear  --- This command is used to Graph the data collected in a certain year, the year desired will be promted from the user
             """)

if Action == "Create":
    print("Creating the Table...")
    command = (""" CREATE TABLE IF NOT EXISTS Goals (
                    Goal_Name   Text,
                    Time_Spent  integer,
                    Date        Text
                )""")
    Create(command)

if Action == "Insert":
    Goal_Name = input("Please enter the goal you worked towards:\n")
    Time_Spent = input("Please enter the time you spent towards it today:\n")
    Date = input("Please enter today's date (Format = YYYY,MM,DD):\n")
    command = "INSERT INTO Goals VALUES ('" + Goal_Name + "', " + Time_Spent + ", '" + Date + "')"
    Insert(command)

if Action == "ViewGoal":
    Goal_Name = input("Please enter the goal you are looking for:\n")
    command = "SELECT * FROM Goals WHERE Goal_Name LIKE '" + Goal_Name + "'"
    Result_List = View(command)
    if len(Result_List) == 0:
        print("there is no data for that Goal")
    else:
        for element in Result_List:
            print(element)

if Action == "ViewDate":
    Date = input("Please enter the day you are looking for (Format = YYYY,MM,DD):\n")
    command = "SELECT * FROM Goals WHERE Date LIKE '" + Date + "'"
    Result_List = View(command)
    if len(Result_List) == 0:
        print("there is no data for that Date")
    else:
        for element in Result_List:
            print(element)

if Action == "ViewMonth":
    Result_List = ViewMonth()
    if len(Result_List) == 0:
        print("there is no data for that Month")
    else:
        for element in Result_List:
            print(element)

if Action == "ViewYear":
    Result_List = ViewYear()
    if len(Result_List) == 0:
        print("there is no data for that Year")
    else:
        for element in Result_List:
            print(element)

if Action == "GraphMonth":
    Result_List = []
    Year_Result_List = ViewYear()
    Month_Result_List = ViewMonth()
    for element in Month_Result_List:
        if element in Year_Result_List and Month_Result_List:
            Result_List.append(element)
    List_of_Dates = []
    List_of_Minutes = []
    if len(Result_List) == 0:
        print("there is no data for that Month")
    else:
        for element in Result_List:
            List_of_Dates.append(element[2])
            List_of_Minutes.append(element[1])

    xpos = np.arange(len(List_of_Dates))
    plt.xticks(xpos, List_of_Dates)
    plt.bar(xpos, List_of_Minutes, width=0.6)
    plt.show()

if Action == "GraphYear":
    Result_List = ViewYear()
    List_of_Dates = []
    List_of_Minutes = []
    if len(Result_List) == 0:
        print("there is no data for that Year")
    else:
        for element in Result_List:
            Month = element[2][5:-3]
            if Month in List_of_Dates:
                for Date in List_of_Dates:
                    if Month == Date:
                        index = List_of_Dates.index(Date)
                        List_of_Minutes[index] = List_of_Minutes[index] + element[1]
            else:
                List_of_Dates.append(Month)
                List_of_Minutes.append(element[1])

    xpos = np.arange(len(List_of_Dates))
    plt.xticks(xpos, List_of_Dates)
    plt.bar(xpos, List_of_Minutes, width=0.6)
    plt.show()

#Still needs to be implemented
#if Action == "GraphLifetime":
#    Date

conn.close()
exit()
