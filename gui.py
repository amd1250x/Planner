'''
gui.py - This is the GUI, it use Tkinter, and is a serious work in progress
'''

from Tkinter import *
from basicTask import *
from specialTask import *
	
def main():
	getTasks()
	TasksGUI = []
	comp = []
	main = Tk()
	main.title("Planner")
	main.geometry("640x480")
	
	def addGUI():

		textFieldx = 140
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
	
		def addGUIF():
			Tasks.append(Task(subject.get(), \
					  name.get(), \
					  month.get(), \
					  day.get(), \
					  imprt.get()))
			writeTasks()
			refreshGUI()
			add.destroy()

		Confirm = Button(add, text="Confirm", command=addGUIF)
		Confirm.place(x = 95, y = 100)	

	def showGUIF():
		m = getCurMonthDay()
		for i in range(len(Tasks)):
			if Tasks[i].done == False:
				TasksGUI.append(Label(main, text = \
					 str(Tasks[i].id) + "\t" + \
					 Tasks[i].subject + "\t" + \
					 Tasks[i].name + " "*(65-len(Tasks[i].name)) + "\t" + " "*10 + \
				    	 Tasks[i].month + "/" + \
					 Tasks[i].day + "   " + \
					 Tasks[i].imp))
				if getDayOfYear(Tasks[i].day, Tasks[i].month) < getDayOfYear(m[1], m[0]):
					TasksGUI[i]['fg'] = 'red'
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
			

		
	def refreshGUI():
		for i in range(len(TasksGUI)):
			TasksGUI[i].place_forget()
		del TasksGUI[:]
		showGUIF()

	def removeGUI():
		rem = Toplevel()
		rem.title("Remove Task")	
		rem.geometry("285x140")

		idl = Label(rem, text="ID")
		idl.place(x = 20, y = 20)

		ide = Entry(rem, width=2)
		ide.place(x = 60, y = 20)

		def remGUIF():
			TasksGUI[int(ide.get())].place_forget()	
			remTask(int(ide.get()))
			refreshGUI()
			rem.destroy()

		idb = Button(rem, text="Remove", command=remGUIF)
		idb.place(x = 40, y = 70)

	def forTomorrowGUI():
		ftList = []
		ft = Toplevel()
		ft.title("For Tomorrow")
		ft.geometry("360x240")
		
		for i in range(len(Tasks)):
			if getDaysUntilDue(Tasks[i].day, Tasks[i].month) < 7 and TasksGUI[i]['fg'] != 'red':
				ftList.append(Label(ft, text = Tasks[i].name + " "*(30-len(Tasks[i].name)) + "\t" + \
								Tasks[i].month + "/" + Tasks[i].day))
		for i in range(len(ftList)):
			ftList[i].place(x = 60, y = 50+(20*i))
		
		close = Button(ft, text="Close", command=ft.destroy)
		close.place(x = 140, y = 50+(20*len(ftList)))

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

	showGUIF()
	main.mainloop()	

main()

