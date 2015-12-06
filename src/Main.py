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





'''def insert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

(width, height) = console.getTerminalSize()
i = 0
bl = '1. This is task 1 it is very very easy I think! and heres to hoping multi-line works!!!!!!'
j = 0
for char in bl:
    if i == width/3-4:
       bl = insert(bl,'\n',i) 
    i+=1

backLogWithSpacing = "Backlog" + " " * (width/3-4-len("Backlog"))
inProgressWithSpacing = "In Progress" + " " * (width/3-4-len("In Progress"))
doneWithSpacing = "Done" + " " * (width/3-4-len("Done"))
table_data = [
    [backLogWithSpacing, inProgressWithSpacing, doneWithSpacing],
    [bl, '1. This is in IN PROGRESS I HOPE', '1. This should be done yay!'],
    ['2. This is task 2 it will never be done', '2. There is no done', '']
]
table = DoubleTable(table_data, 'Board Name')

table.inner_row_border = True
print(table.table)'''

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
        print listBoards
        for i in range (1,len(listBoards)+1):
            temp.append(listBoards[i-1])
            if i % 1 == 0:
                printBoards.append(temp)
                print printBoards
                temp = []
        table = DoubleTable(printBoards, 'Boards')
        table.inner_row_border = True
        print(table.table)
        
        in_data = prompt.query('Pick board(0 to create):')

        if in_data == '0':
        	boardName = prompt.query('Enter board name:')
        	boardUsers = prompt.query('Enter users(separate by comma):')
        	print boardUsers 
        	boardUsers = boardUsers.split(',')
        	print boardUsers
        	currentBoard = user.makeBoard(boardName,user,boardUsers)
        else:
	    	(boardid,leaderid, memberid,taskids) = models.database.pickBoard(in_data)
	    	currentBoard = Board(boardid,in_data,taskids,leaderid,memberid)
        
        models.database.printTasks(currentBoard.getID(),currentBoard.getName())
       
        while in_data != 0:
            in_data = prompt.query('Enter task:')      
            members = prompt.query('Enter member for task:')
            task = currentBoard.makeTasks(in_data,members)
            models.database.printTasks(currentBoard.getID(),currentBoard.getName())




'''     
def printTasks():
    #get data from db
    backlog = ['1.', 'This is task 1 it is cooliasidfisadfiasidfiasdfiasidfisadiiasdfjas djfisajdf isadfij asidfjisad fijsaidf isjdfiasdfi jaisdfj iasdjfi jasidfj iasdfj iasjdfi ajsdifj saidjf iasjdfijasdifjiasdjfi jaisdjfiasdfjf', 'EFL']
    inProgress = ['1', 'asdf is easy', 'SAM']
    done = ['1', 'wot', 'asdf', '2','asdf','asdf']
    tasks = [backlog,inProgress,done]
    
    (width, height) = console.getTerminalSize()
    print (width, height)
    extraLineBacklog = False
    extraLineInProgress = False
    extraLineDone = False
    for i in range(0,(max(len(taskType) / 3 for taskType in tasks ))):
        if len(backlog)/3 > i:
            if backlog[i+1] > (width/3 - 5):
                print'|',backlog[3*i], backlog[3*i+1][:(width/3 - 5)], '|',
                backlog[3*i+1] = backlog[3*i+1][(width/3 - 5):]
                extraLineBackLog = True
            else:
                print '|',backlog[i+1][(width/3 - 5):], ' ', backlog[i+2], '|',

        if ((len(inProgress)+1)/3 > i): 
            print inProgress[3*i], inProgress[3*i+1], ' ',inProgress[3*i+2],'|',  
        if (len(done)+1)/3 > i:
            print done[3*i], done[3*i+1], ' ',done[3*i+2]
        #check if extra line(s) are needed
        if extraLineBacklog == True or extraLineDone == True or extraLineInProgress == True:
            print 'i lowered'
            i -= 1
'''

