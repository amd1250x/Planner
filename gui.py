'''
gui.py - This is the GUI, it use Tkinter, and is a serious work in progress
'''

from Tkinter import *
from basicTask import *
from specialTask import *



def addGUI():

	textFieldx = 140
	textFieldy = 20
	
	labelx = 20
	labely = 20

	add = Toplevel()
	add.title("Add Task")
	add.geometry("285x140")
		
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
	
	def addGUIF():
		Tasks.append(Task(subject.get(), \
			          name.get(), \
				  month.get(), \
				  day.get()))
		writeTasks()
		add.destroy()

	Confirm = Button(add, text="Confirm", command=addGUIF)
	Confirm.place(x = 95, y = 90)
	
def main():
	getTasks()
	TasksGUI = []	
	main = Tk()
	main.title("Planner")
	main.geometry("640x480")
	
	def showGUIF():		
		for i in range(len(Tasks)):
			TasksGUI.append(Label(main, text = \
				 str(Tasks[i].id) + " | " + \
				 Tasks[i].subject + " | " + \
				 Tasks[i].name + " | " + \
			    	 Tasks[i].month + "/" + \
				 Tasks[i].day))
			TasksGUI[i].place(x = 20, y = 100+(20*i))

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
			rem.destroy()

		idb = Button(rem, text="Remove", command=remGUIF)
		idb.place(x = 40, y = 70)

	addB = Button(main, text="Add Task", command=addGUI)
	addB.place(x = 20, y = 20)
	
	remB = Button(main, text="Remove Task", command=removeGUI)
	remB.place(x = 120, y = 20)

	refB = Button(main, text="Refresh", command=refreshGUI)
	refB.place(x = 20, y = 60)

	showGUIF()
	main.mainloop()	

main()

