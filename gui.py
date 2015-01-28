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
		add.destroy()

	Confirm = Button(add, text="Confirm", command=addGUIF)
	Confirm.place(x = 95, y = 90)



def main():
	getTasks()
	TasksGUI = []	
	main = Tk()
	main.title("Planner")
	main.geometry("640x480")
	
	def showGUIF(l):		
		l = []
		for i in range(len(Tasks)):
			l.append(Label(main, text = \
				 str(Tasks[i].id) + " | " + \
				 Tasks[i].subject + " | " + \
				 Tasks[i].name + " | " + \
			    	 Tasks[i].month + "/" + \
				 Tasks[i].day))
			l[i].place(x = 20, y = 100+(20*i))
		
	def checkTasks():
		for i in range(len(TasksGUI)):
			TasksGUI[i].place_forget()
		showGUIF(TasksGUI)

	addB = Button(main, text="Add Task", command=addGUI)
	addB.place(x = 20, y = 20)

	refB = Button(main, text="Refresh", command=checkTasks)
	refB.place(x = 20, y = 60)

	showGUIF(TasksGUI)
	main.mainloop()	

main()

