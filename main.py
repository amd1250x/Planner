import time
import Tkinter

Tasks = []

class Task():
	def __init__(self, subject, name, month, day, done=False):
		self.subject = subject		
		self.name = name
		self.month = month
		self.day = day
		self.done = done
	
	def setName(s):
		self.name = s

	def setDone(b):
		self.done = b
	
	def getCurMonthDay():
		curMonth = int(time.strftime("%m"))
		curDay   = int(time.strftime("%d"))

		return [curMonth, curDay]
		
		

def showTasks():
	for i in range(len(Tasks)):
		if Tasks[i].done == False:
			print "Subject: "  + Tasks[i].subject + " | " + \
			      "Name: "     + Tasks[i].name    + " | " + \
			      "Due date: " + Tasks[i].month   + "/" + Tasks[i].day

def addTask():
	sub     = raw_input("Subject: ")
	name    = raw_input("Name of Task: ")
	duedate = raw_input("Date due (mm/dd): ").split("/")
	
	Tasks.append(Task(sub, name, duedate[0], duedate[1]))
	showTasks()

def main():
	quit = False
	while quit != True:
		i = raw_input("Planner: ")
		if   i == "show":
			showTasks()
		elif i == "add":
			addTask()
		elif i == "quit":
			quit = True

main() 


