import mysql.connector

conn = mysql.connector.connect(user='tempuser', password='password', database='project_brian_test')
cursor = conn.cursor()

# user: sign up
def signUp(user_name):
	return 0

# user: login
def login(user_name):
	return 0

# leader: make board
def makeBoard(leader_name):
	return 0

# leader: add members to board (?)

# user: see all tasks
def seeAllTasks(user_name):
	return 0

# leader: make tasks/assign members
# 	"members" is a list of members to assign
#	"task" is the description of the task
def makeTask(task, members):
	return 0

# task: move to Backlog
def toBacklog(task):
	return 0

# task: move to In Progress
def toInProgress(task):
	return 0

# task: move to Done
def toDone(task):
	return 0

# user: see my own tasks
def seeOwnTasks(user_name):
	return 0

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
	return 0

# board: get leader
def getLeader(board_name):
	return 0

# MAIN
def main():
    board_name = 'temp board'
    getUsers(board_name)


    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
