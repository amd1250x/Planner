'''
cli.py - This is the menu interface of the CLI for this program. It was
mostly used to test out my basic fuctions. It is usable, but I will not
be doing much with it.
'''

# Import all our functions
from basicTask import *
from specialTask import *


def main():
	# Simple while loop. Nothing fancy here. 
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
