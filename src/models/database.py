import mysql.connector
import random
import string
import unicodedata
import Member

conn = mysql.connector.connect(user='tempuser', password='password', database='project_brian_test')
cursor = conn.cursor()

def id_generator(size=6, char=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def checkLogin(username, password):
    cursor.execute("SELECT member_name,password FROM members")
    temp = False
    for (name,passe) in cursor:
        if name == username and passe == password:
            temp = True
    return temp
            
def instantiateMember(username):
    cursor.execute("SELECT member_id, member_name, email, password, board_ids FROM members")
    for (member_id, member_name, email, password, board_ids) in cursor:
        if username == member_name:
            newmember = Member.Member(member_id,member_name,email,password,board_ids)
            
    return newmember

def test():
    cursor.execute("INSERT INTO members (member_id, member_name, email, password, board_ids) VALUES ('{0}', 'artur', 'a@com.com', 'pasowrd', '')".format(random.randint(0,1000000000)))
    conn.commit()
# user: sign up
#	NEED TO FIGURE HOW LOGIN SYSTEM IS GONNA WORK
def signUp(name, email, password):
	members = []

	# Get all members from members
	query1 = "SELECT * FROM members"
	cursor.execute(query1)
	for member in cursor:
		members.append(member)

	# Insert all the parameters into the members
	query3 = "INSERT INTO members (member_id, member_name, email, password, board_ids) VALUES ('{0}', '{1}', '{2}', '{3}', '')".format(random.randint(0,1000000000), name, email, password)
	cursor.execute(query3)
        conn.commit()

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

def getAllUsers():
    query = "SELECT * FROM members"
    return cursor.execute(query)


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
