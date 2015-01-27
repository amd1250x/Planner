import time
import Tkinter

Tasks = []

class Task():
	def __init__(self, subject, name, month, day, done=False):
		self.id = len(Tasks)+1
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
		
def getTasks():
	f = open("data", "r")
	raw = f.read()
	lines = raw.split("\n")
	if lines[len(lines)-1] == "":	
		lines = lines[:len(Tasks)-1]
	for i in range(len(lines)):
		piece = lines[i].split(",")
		Tasks.append(Task(piece[1], \
				  piece[2], \
		                  piece[3].split("/")[0], \
			          piece[3].split("/")[1]))

def writeTasks():
	f = open("data", "w")
	s = ""
	for i in range(len(Tasks)):
		s += str(Tasks[i].id-1) + "," + \
		     Tasks[i].subject   + "," + \
		     Tasks[i].name      + "," + \
		     Tasks[i].month + "/" + Tasks[i].day + "\n"
	f.write(s)
	Tasks = []
	getTasks()
	
	


def showTasks():
	for i in range(len(Tasks)):
		if Tasks[i].done == False:
			print "ID: "       + str(Tasks[i].id) + " | " + \
			      "Subject: "  + Tasks[i].subject + " | " + \
			      "Name: "     + Tasks[i].name    + " | " + \
			      "Due date: " + Tasks[i].month   + "/" + Tasks[i].day

def addTask():
	sub     = raw_input("Subject: ")
	name    = raw_input("Name of Task: ")
	duedate = raw_input("Date due (mm/dd): ").split("/")
	
	Tasks.append(Task(sub, name, duedate[0], duedate[1]))
	writeTasks()	
	showTasks()
	

def remTask(iden):
	for i in range(len(Tasks)):
		if Tasks[i].id == iden:
			Tasks.remove(Tasks[i])
			

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
		elif i == "get":
			getTasks()
		elif i == "write":
			writeTasks()

main() 


