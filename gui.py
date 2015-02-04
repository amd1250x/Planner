'''
gui.py - This is the GUI of Planner. It uses Tkinter because I have
the most experience in it out of all the Python GUIs. Although it 
isn't pretty, I could care less. 
'''

from Tkinter import *
from basicTask import *
from specialTask import *

# This entire function is run at the end.
def main():
	getTasks()
	TasksGUI = [] # These are the tasks displayed on the main screen
	main = Tk()
	main.title("Planner")
	main.geometry("640x480")
	
	def addGUI(): # Add a task, except in the GUI

		textFieldx = 140 # These are just variables so that I could just use them as factors
		textFieldy = 20
	
		labelx = 20
		labely = 20

		add = Toplevel()
		add.title("Add Task")
		add.geometry("285x150")
		
		subjectLabel = Label(add, text="Subject:")
		subjectLabel.place(x = labelx, y = labely)

		subject = Entry(add)
		subject.place(x = textFieldx, y = textFieldy, width = 120)
	
		nameLabel = Label(add, text="Task:")
		nameLabel.place(x = labelx, y = labely*2)

		name = Entry(add)
		name.place(x = textFieldx, y = textFieldy*2, width = 120)	
	
		dueLabel = Label(add, text="Due Date(mm/dd):")
		dueLabel.place(x = labelx, y = labely*3)

		month = Entry(add, width=2)
		month.place(x = textFieldx, y = textFieldy*3)
		slash = Label(add, text="/")
		slash.place(x = textFieldx+22, y = textFieldy*3)
		day = Entry(add, width=2)
		day.place(x = textFieldx+30, y = textFieldy*3)

		imprt = Entry(add, width=2)
		imprt.place(x = textFieldx, y = textFieldy*4)
		
		imprtLabel = Label(add, text="Importance(1-5):")
		imprtLabel.place(x = labelx, y = labely*4)
		# This is the function that is run when the "Add Task" button is pressed
		def addGUIF():
			Tasks.append(Task(subject.get(), \
					  name.get(), \
					  month.get(), \
					  day.get(), \
					  imprt.get()))
			writeTasks()
			# This re-writes everything on the main list of tasks
			refreshGUI()
			# Remove the window
			add.destroy()

		Confirm = Button(add, text="Confirm", command=addGUIF)
		Confirm.place(x = 95, y = 100)	
	
	# This is the function that actually writes the tasks to the main screen
	def showGUIF():
		# Made this variable to reduce the space it was taking up (and for optimization)
		m = getCurMonthDay()
		for i in range(len(Tasks)):
			# It does not print completed tasks
			if Tasks[i].done == False:
				TasksGUI.append(Label(main, text = \
					 str(Tasks[i].id) + "\t" + \
					 Tasks[i].subject + "\t" + \
					 Tasks[i].name + " "*(65-len(Tasks[i].name)) + "\t" + " "*10 + \
				    	 Tasks[i].month + "/" + \
					 Tasks[i].day + "   " + \
					 Tasks[i].imp))
				# The the day it was due has passed, it will be gray
				if getDayOfYear(Tasks[i].day, Tasks[i].month) < getDayOfYear(m[1], m[0]):
					TasksGUI[i]['fg'] = 'gray'
				TasksGUI[i].place(x = 20, y = 140+(25*i))

		'''for i in range(len(Tasks)):
			l[i][0] = Label(main, text = str(Tasks[i].id))
			l[i][1] = Label(main, text = Tasks[i].subject)
			l[i][2] = Label(main, text = Tasks[i].name)
			l[i][3] = Label(main, text = Tasks[i].month + "/" + Tasks[i].day)
			for j in range(4):
				if j == 1:
					l[i][j].place(x = 20+(20*j), y = 100+(20*i))
				elif j == 2:
					l[i][j].place(x = 20+(30*j), y = 100+(20*i))
				elif j == 3:
					l[i][j].place(x = 20+(150*j), y = 100+(20*i))
				else:
					l[i][j].place(x = 20+(20*j), y = 100+(20*i))'''
			

	# This function clears TasksGUI and re-writes the tasks to it
	def refreshGUI():
		for i in range(len(TasksGUI)):
			TasksGUI[i].place_forget()
		del TasksGUI[:]
		showGUIF()

	# This function removes a task
	def removeGUI():
		rem = Toplevel()
		rem.title("Remove Task")	
		rem.geometry("285x140")

		idl = Label(rem, text="ID")
		idl.place(x = 20, y = 20)

		ide = Entry(rem, width=2)
		ide.place(x = 60, y = 20)

		def remGUIF():
			# From the input, it removes it from main screen, then removes it from Tasks using remTask()
			TasksGUI[int(ide.get())].place_forget()	
			remTask(int(ide.get()))
			refreshGUI()
			rem.destroy()

		idb = Button(rem, text="Remove", command=remGUIF)
		idb.place(x = 40, y = 70)
	
	# Shows the tasks that are recommended for tomorrow (Due in 7 or less days)
	def forTomorrowGUI():
		ftList = []
		ft = Toplevel()
		ft.title("For Tomorrow")
		ft.geometry("360x240")
		
		for i in range(len(Tasks)):
			if getDaysUntilDue(Tasks[i].day, Tasks[i].month) < 7 and TasksGUI[i]['fg'] != 'grey':
				ftList.append(Label(ft, text = Tasks[i].name + " "*(30-len(Tasks[i].name)) + "\t" + \
								Tasks[i].month + "/" + Tasks[i].day))
		for i in range(len(ftList)):
			ftList[i].place(x = 60, y = 50+(20*i))
		
		close = Button(ft, text="Close", command=ft.destroy)
		close.place(x = 140, y = 50+(20*len(ftList)))
	
	# Creates a Google Calendar-like window in which the tasks for the week are written to
	def viewTheWeekGUI():
		weekGUI = [] # These are the labels for the days of the week
		framesGUI = [] # These are the boxes that make it look like a spreadsheet
		vList = [""]*7 # These are the tasks printed as labels

		v = Toplevel()
		v.title("Current Week")
		v.geometry("700x200")

		# (2/3/15) I made great improvements that make this element easier to understand and, possibly, more efficient

		
		# First, a loop iterates through Tasks and concatenates the tasks to their day (days are represented by gdud).
		for i in range(len(Tasks)):
			gdud = getDaysUntilDue(Tasks[i].day, Tasks[i].month)
			if gdud < 7 and TasksGUI[i]['fg'] != "grey":
				vList[gdud+datetime.datetime.today().weekday()] += Tasks[i].name + ","
		
		# A loop then goes through and removes the end comma, and uses .split on each element in vList.
		for i in range(len(vList)):
			vList[i] = vList[i][:len(vList[i])-1].split(',')

		# Another loop goes through and changes each element to a Label.
		for i in range(len(vList)):
			if vList[i] != ['']:
				for j in range(len(vList[i])):
					vList[i][j] = Label(v, text = vList[i][j])

		# These Labels are then placed on the screen v in coordinants from a 2-D loop.
		for i in range(len(vList)):
			if vList[i] != ['']:
				for j in range(len(vList[i])):
					vList[i][j].place(x = 5+(96*i), y = 35*(j+1))
		
		# The Frame and Weekdays are then initialized in their respective lists
		for i in range(len(vList)):
			framesGUI.append(Frame(v, width=96, height=30, bd=1, relief=SOLID))
			weekGUI.append(Label(v, text = days[i]))
		
		for i in range(len(weekGUI)):
			if i == datetime.datetime.today().weekday():
				weekGUI[i]['font'] = 'Verdana 9 bold'

		# The Frame and Weekdays are then placed on v.
		for i in range(len(vList)):
			framesGUI[i].place(x = 5+(96*i), y = 5)
			weekGUI[i].grid(row=0, column=i, padx = 19, pady = 10)

	# These next functions are sorting functions. They call the sorting algorithm in specialTask and then call refreshGUI
	def sortIDGUI():
		sortByID(Tasks)
		refreshGUI()

	def sortSubGUI():
		sortBySub(Tasks)
		refreshGUI()

	def sortNameGUI():
		sortByName(Tasks)
		refreshGUI()

	def sortDateGUI():
		sortByDate(Tasks)
		refreshGUI()

	def sortImpGUI():
		sortByImp(Tasks)
		refreshGUI()

	# These are all buttons which are tied to simpler functions
	addB = Button(main, text="Add Task", command=addGUI)
	addB.place(x = 20, y = 20)
	
	remB = Button(main, text="Remove Task", command=removeGUI)
	remB.place(x = 120, y = 20)

	refB = Button(main, text="Refresh", command=refreshGUI)
	refB.place(x = 20, y = 60)

	ftB  = Button(main, text="For Tomorrow", command=forTomorrowGUI)
	ftB.place(x = 120, y = 60)

	srtL = Label(main, text="Sort by: ")
	srtL.place(x = 20, y = 105)
	
	srtIDB = Button(main, text="ID", command=sortIDGUI)
	srtIDB.place(x = 80, y = 100)

	srtSB = Button(main, text="Subject", command=sortSubGUI)
	srtSB.place(x = 130, y = 100)
	
	srtNB = Button(main, text="Name", command=sortNameGUI)
	srtNB.place(x = 214, y = 100)

	srtDB = Button(main, text="Date", command=sortDateGUI)
	srtDB.place(x = 287, y = 100)
	
	srtIB = Button(main, text="Importance", command=sortImpGUI)
	srtIB.place(x = 353, y = 100)

	dateL = Label(main, text="Today's Date: " + str(getCurMonthDay()[0]) + "/" + str(getCurMonthDay()[1]))
	dateL.place(x = 250, y = 20)

	WkB = Button(main, text="Week", command=viewTheWeekGUI)
	WkB.place(x = 400, y = 20)

	showGUIF()
	main.mainloop()	

main()

