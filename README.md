# Goal-Tracking

a python program for writing time spend on activites that will log the dates and the amount of time taken for the activity, once some activites are logged the program can be used to show the user their amount of time on each activity, the time on a certain activity, or the time on activites in a certain time frame. this program can be used to track someone's progress towards a goal, can be used to track how long different tasks take to see if the user is getting faster or doing the task more as the timeline gets longer.

the program performs different tasks based on command line arguements given, in the **steps to run program** section each command line arguement is given and what is done is explained.

# Installation

currently non of the libraries needed to run the program are installed by the program itself, in order to get all libraries needed run the following commands:

### matplotlib library

```bash
pip install matplotlib

```

### numpy library

```bash
pip install numpy

```

once all the libraries are linstalled through pip, in order to get the program run: git clone https://github.com/RileyJRaso/Goal-Tracking.git

and than go to the folder that is cloned in order to run the program

# Steps to run program

the program should be run with different arguements depending on the action the user wants to do. each of the dfferent actions are described below:

### Create

this action is preformed as follows: 
```bash
Python goalTracking.py Create

```

this action creates the database that is used to store the goals and entries for the user. this action should be done before any other action in the program, if this is not done you will get errors that the database does not exist.

### Insert

this action is preformed as follows: 
```bash
Python goalTracking.py Insert

```

once this is selected the program will prompt the user to enter what goal you want to enter time for. (IMPORTANT: capitals matter, "Dance" and "dance" are considered different goals and will be displayed as different goals which may mess with the graphs and display data)

once a goal is entered the user will be prompted to enter the time spent on that goal, this in my opinion should be in minutes however the user may select any time unit they want as long as it is consistent for all entries.

finally the user will be prompted to enter the date, the format is given by the program.

### ViewGoal

# Future plans
