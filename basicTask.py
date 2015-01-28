import time

Tasks = []

class Task():
	def __init__(self, subject, name, month, day, done=False):
		self.id = len(Tasks)
		self.subject = subject		
		self.name = name
		self.month = month
		self.day = day
		self.done = done
	
	def setName(s):
		self.name = s

	def setDone():
		self.done = True
	
	def getCurMonthDay():
		curMonth = int(time.strftime("%m"))
		curDay   = int(time.strftime("%d"))

		return [curMonth, curDay]
		
def getTasks():
	f = open("data", "r")
	raw = f.read()
	f.close()
	lines = raw.split("\n")
	lines = lines[:len(lines)-1]
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
		s += str(Tasks[i].id)   + "," + \
		     Tasks[i].subject   + "," + \
		     Tasks[i].name      + "," + \
		     Tasks[i].month + "/" + Tasks[i].day + "\n"
	f.write(s)
	f.close()
	del Tasks[:]	
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

def remTask(iden):
	temp = []
	for i in range(len(Tasks)):
		if Tasks[i].id != iden:
			temp.append(Tasks[i])
	del Tasks[:]
	for i in range(len(temp)):
		Tasks.append(temp[i])
	writeTasks()
			

def setComplete(i):
	Tasks[i-1].done = True
