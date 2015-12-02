import mysql.connector
import random
import string

conn = mysql.connector.connect(user='tempuser', password='password', database='project_brian_test')
cursor = conn.cursor()

def id_generator(size=6, char=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# user: sign up
#	NEED TO FIGURE HOW LOGIN SYSTEM IS GONNA WORK
def signUp(user_name):
	return 0

# user: login
#	NEED TO FIGURE HOW LOGIN SYSTEM IS GONNA WORK
def login(user_name):
	return 0

# leader: make board
#	NEED TO FIGURE OUT QUERY TO ADD TO SQL TABLE
def makeBoard(leader_name):
	return 0

# leader: add members to board (?)
def addMembers(board, members):
    for n in members:
        rand_id = id_generator()
        query = "UPDATE boards SET member_ids='%s'" % rand_id + " WHERE boards='%s'" % board
        cursor.execute(query)

# user: see all tasks
#	this method will probably be called initially by default as opposed to seeOwnTasks()
def seeAllTasks():
	query = "SELECT * FROM tasks" % user_name
	cursor.execute(query)
	taskList = []

	for task in cursor:
		taskList.append(task)
	#print(taskList)
	return taskList

# leader: make tasks/assign members
# 	"members" is a list of members to assign
#	"task" is the description of the task
#	NEED TO FIGURE OUT QUERY TO ADD TO SQL TABLE
def makeTask(task, members):
	return 0

# task: move to Backlog
#	part of the State DP, check slides/notes to implement
def toBacklog(task):
	return 0

# task: move to In Progress
#	part of the State DP, check slides/notes to implement
def toInProgress(task):
	return 0

# task: move to Done
#	part of the State DP, check slides/notes to implement
def toDone(task):
	return 0

# user: see user's tasks only
def seeOwnTasks(user_name):
	query = "SELECT * FROM tasks WHERE user_name = '%s'" % user_name
	cursor.execute(query)
	taskList = []

	for task in cursor:
		taskList.append(task)

	print(taskList)
	#return taskList

# board: get users
def getUsers(board_name):
    query = "SELECT name FROM users JOIN boards ON boards.user_id = users.user_id WHERE board_name = '%s'" % board_name
    cursor.execute(query)
    nameList = []

    for name in cursor:
        nameList.append(name)

    print(nameList)
    #return nameList

# board: get tasks
def getTasks(board_name):
	query = "SELECT tasks FROM boards WHERE board_name = '%s'" % board_name
	cursor.execute(query)
	taskList = []
	
	for task in cursor:
		taskList.append(task)

	print(taskList)
	#return taskList

# board: get leader
def getLeader(board_name):
	query = "SELECT leader FROM boards WHERE board_name = '%s'" % board_name
	cursor.execute(query)
	leader = ""

	print(leader)
	#return leader

# MAIN
def main():
    board_name = 'temp board'
    getUsers(board_name)


    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
