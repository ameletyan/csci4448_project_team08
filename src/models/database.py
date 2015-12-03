import mysql.connector
import random
import string

conn = mysql.connector.connect(user='tempuser', password='password', database='project_brian_test')
cursor = conn.cursor()

def id_generator(size=6, char=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# user: sign up
#	NEED TO FIGURE HOW LOGIN SYSTEM IS GONNA WORK
def signUp(name, email, password):
	newID = 1
	members = []

	# Get all members from members
	query1 = "SELECT * FROM members"
	cursor.execute(query1)
	for member in cursor:
		members.append(member)

	if(len(members) > 0):
		# Get the highest member_id in members
		query2 = "SELECT MAX(member_id) FROM members"
		cursor.execute(query2)
		newID = int(cursor) + 1

	# Insert all the parameters into the members
	query3 = "INSERT INTO members (member_id, member_name, email, password, board_ids) VALUES (%d," % newID + " %s," % name + " %s," % email + " %s, '')" % password
	cursor.execute(query3)

# leader: make board
#	Will the members parameter be a list, string, or what?
def makeBoard(name, leader, members):
	newID = 1
	boards = []

	# Get all boards from boards
	query1 = "SELECT * FROM boards"
	cursor.execute(query1)
	for board in cursor:
		boards.append(board)

	if(len(boards) > 0):
		# Get the highest board_id in boards
		query2 = "SELECT MAX(board_id) FROM boards"
		cursor.execute(query2)
		newID = int(cursor) + 1

	# Get leader_id
	leaderID = leader.getID()

	# Put all member IDs into a string
	memberIDs = ""


	# Insert all the parameters into the boards
	query3 = "INSERT INTO boards (board_id, board_name, task_ids, leader_id, member_ids) VALUES (%d," % newID + " %s," % name + " %s," % email + " %d, '')" % leaderID
	cursor.execute(query3)

# leader: add members to board (?)
def addMembers(board, members):
    for n in members:
        rand_id = id_generator()
        query = "UPDATE boards SET member_ids = %s" % rand_id + " WHERE boards=%s" % board
        cursor.execute(query)

# user: see all tasks
#	this method will probably be called initially by default as opposed to seeOwnTasks()
def seeAllTasks(id):
	query = "SELECT * FROM tasks"
	cursor.execute(query)
	taskList = []

	for task in cursor:
		taskList.append(task)

	return taskList

# leader: make tasks/assign members
def makeTask(title, state, member):
	newID = 1
	state = 0
	tasks = []

	# Get all boards from boards
	query1 = "SELECT * FROM tasks"
	cursor.execute(query1)
	for task in cursor:
		tasks.append(board)

	if(len(tasks) > 0):
		# Get the highest task_id in tasks
		query2 = "SELECT MAX(task_id) FROM tasks"
		cursor.execute(query2)
		newID = int(cursor) + 1

	# Get memberID
	memberID = member.getID()

	# Insert all the parameters into the tasks
	query3 = "INSERT INTO boards (task_id, task_title, task_description, task_state, member_id) VALUES (%d," % newID + " %s," % title+ "'', %d," % state + " %d)" % memberID
	cursor.execute(query3)

# user: see user's tasks only
def seeOwnTasks(id):
	query = "SELECT * FROM tasks WHERE member_id = %d" % id
	cursor.execute(query)
	taskList = []

	for task in cursor:
		taskList.append(task)

	return taskList

# board: get users
def getUsers(board_name):
    query = "SELECT name FROM users JOIN boards ON boards.user_id = users.user_id WHERE board_name = %s" % board_name
    cursor.execute(query)
    nameList = []

    for name in cursor:
        nameList.append(name)

    return nameList

# board: get tasks
def getTasks(board_name):
	query = "SELECT tasks FROM boards WHERE board_name = %s" % board_name
	cursor.execute(query)
	taskList = []
	
	for task in cursor:
		taskList.append(task)

	return taskList

# board: get leader
def getLeader(board_name):
	query = "SELECT leader FROM boards WHERE board_name = %s" % board_name
	cursor.execute(query)
	leader = ""

	return leader

# MAIN
def main():
    board_name = 'temp board'
    getUsers(board_name)


    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
