from basicTask import *
from specialTask import *

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
		elif i == "remove":
			remTask(input("ID: "))

main() 
