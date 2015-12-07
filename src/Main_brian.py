#import task, board, member, leader
from models.leader import Leader
from models.Member import Member
from models.board import Board
from models.task import TaskState, BackLog, InProgress, Done, TaskContext
import models.database
from clint.textui import prompt, validators, puts, indent, cols
import console
from terminaltables import DoubleTable
import getpass

in_data = 'login'
while in_data != 'quit':
    if in_data == 'login':
        username = prompt.query('Enter username(0 to sign-up):')
        if username == '0': #create user
            username = prompt.query('Enter username:')
            email = prompt.query('Enter e-mail:')
            password = getpass.getpass('Enter password:')
            models.database.signUp(username, email, password)
        else:
            password = getpass.getpass('Password:')

        if models.database.checkLogin(username,password):
            #instantiat object after LOG IN!!!
            user = models.database.instantiateMember(username)

            in_data = 'boards' 
        else:
            in_data = 'login'
            

    if in_data == 'boards':
        listBoards =  models.database.getBoards(user.getID())
        printBoards = []
        temp = []
        #print listBoards
        for i in range (1,len(listBoards)+1):
            temp.append(listBoards[i-1])
            if i % 1 == 0:
                printBoards.append(temp)
                #print printBoards
                temp = []
        table = DoubleTable(printBoards, 'Boards')
        table.inner_row_border = True
        print(table.table)
        
        in_data = prompt.query('Pick board(0 to create):')

        if in_data == '0':
        	boardName = prompt.query('Enter board name:')
        	boardUsers = prompt.query('Enter users(separate by comma):')
        	#print boardUsers 
        	boardUsers = boardUsers.split(',')
        	#print boardUsers
        	currentBoard = user.makeBoard(boardName,user,boardUsers)
        else:
	    	try:
			(boardid,leaderid, memberid,taskids) = models.database.pickBoard(in_data)
	    		#currentBoard = Board(boardid,in_data,taskids,leaderid,memberid)
		except NameError:
			print "Enter valid board"
			in_data = 'exit'
		except TypeError:
			print "Enter valid board"
			in_data = 'exit'
       		else:
			currentBoard = Board(boardid,in_data,taskids,leaderid,memberid) 
        		models.database.printTasks(currentBoard.getID(),currentBoard.getName())
        #models.database.printTasks(currentBoard.getID(),currentBoard.getName())
        '''
        while in_data != 0:
            in_data = prompt.query('Enter task:')      
            members = prompt.query('Enter member for task:')
            task = currentBoard.makeTasks(in_data,members)
            models.database.printTasks(currentBoard.getID(),currentBoard.getName())

        '''    
        while in_data != 'exit':
         	in_data = prompt.query('Select task (0 to make task):')
         	if in_data == '0':
         		description = prompt.query('Enter the description for the task:')
         		members = prompt.query('Enter member for task:')
         		task = currentBoard.makeTasks(description,members)
         		models.database.printTasks(currentBoard.getID(),currentBoard.getName())
         	elif(in_data != 'exit'):
         		column = prompt.query("\n0 - Backlog\n1 - In Progress\n2 - Done\nMove to:")
         		currentBoard.moveTask(in_data, column)
        in_data = 'boards'
