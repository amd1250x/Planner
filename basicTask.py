'''
basicTask.py - This file is for functions that are essential to this program
and virtually any program attempting to accomplish what I am trying to do.
'''
import time

# First, we create a global task list
Tasks = [] 

# I created a Task class just for the sake of organization
class Task():
	# Done is automatically assumed false
	def __init__(self, subject, name, month, day, imp, done=False):
		# These properties were decided based of how I view my own tasks
		# ID for the sake of ease of manipulation		
		self.id = len(Tasks)
		self.subject = subject		
		self.name = name
		self.month = month
		self.day = day
		self.done = done
		self.imp = imp
	
	#Simple setter methods
	def setName(s):
		self.name = s

	def setDone():
		self.done = True

	
# We need to somehow, after storing the tasks, retrieve them. This function is for that purpose.
def getTasks():
	# Open whatever file has the stored data
	f = open("data", "r")
	raw = f.read()
	f.close()
	# Because of the formatting in the data file, we need to do a bit of manipulation
	lines = raw.split("\n")
	# The first element is empty, so we need to get rid of it
	lines = lines[:len(lines)-1]
	# This for loop is to split the lines into list elements.
	for i in range(len(lines)):
		piece = lines[i].split(",")
		Tasks.append(Task(piece[1], \
				  piece[2], \
		                  piece[3].split("/")[0], \
			          piece[3].split("/")[1], \
				  piece[4]))

# We need to write the data, otherwise how can we retrieve our data after exitting the program?
def writeTasks():
	f = open("data", "w")
	# s is an empty string, as it gets populated as more things are recognized as useful to write
	s = ""
	for i in range(len(Tasks)):
		s += str(Tasks[i].id)   + "," + \
		     Tasks[i].subject   + "," + \
		     Tasks[i].name      + "," + \
		     Tasks[i].month + "/" + Tasks[i].day + "," + \
		     Tasks[i].imp       + "\n"
	f.write(s)
	f.close()
	# This is just to 'refresh' the list of tasks
	del Tasks[:]	
	getTasks()
	
	
# Self-explanatory, it just prints the tasks in a nice-ish format
def showTasks():
	for i in range(len(Tasks)):
		# prints out only the not-done tasks.
		if Tasks[i].done == False:
			print "ID: "       + str(Tasks[i].id) + " | " + \
			      "Subject: "  + Tasks[i].subject + " | " + \
			      "Name: "     + Tasks[i].name    + " | " + \
			      "Due date: " + Tasks[i].month   + "/" + Tasks[i].day + " | " + \
			      "Importance:"+ Tasks[i].imp + "\n"

# Let's add some tasks!
def addTask():
	sub     = raw_input("Subject: ")
	name    = raw_input("Name of Task: ")
	duedate = raw_input("Date due (mm/dd): ").split("/")
	impor   = raw_input("Importance (1-5): ")
	
	Tasks.append(Task(sub, name, duedate[0], duedate[1], impor))
	writeTasks()
	showTasks()

# Let's remove some tasks! 
def remTask(iden):
	'''
	The temp list reads in all of the Tasks from the master task
	list and appends all tasks in which their ID does NOT match
	the parameter iden.
	'''
	temp = []
	for i in range(len(Tasks)):
		if Tasks[i].id != iden:
			temp.append(Tasks[i])
	# Tasks are cleared
	del Tasks[:]
	# Tasks are appended again, this time without the task you wanted removed
	for i in range(len(temp)):
		Tasks.append(temp[i])
	# Why don't we also save our tasks while we're at it
	writeTasks()
			
# Setter method that takes in the ID of the task you finished
def setComplete(i):
	Tasks[i-1].done = True
