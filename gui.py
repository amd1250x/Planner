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

	due = Entry(add)
	due.place(x = textFieldx, y = textFieldy*3, width = 120)

	Confirm = Button(add, text="Confirm", \
			 command=lambda: \
				Tasks.append(Task(subject.get, \
					       name.get, \
					       due.get.split("/")[0], \
					       due.get.split("/")[1])))
	Confirm.place(x = 95, y = 90)


def main():	
	main = Tk()
	main.title("Planner")


	b = Button(main, text="Add Task", command=addGUI)
	b.pack(padx = 10, pady = 10, side = LEFT)


	main.mainloop()	

	getTasks()



