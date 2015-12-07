import mysql.connector
import random
import string
import unicodedata
import Member
from terminaltables import DoubleTable
import console
import task


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
def insert (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

def printTasks(board_id,board_name):
	query = "SELECT task_ids FROM boards WHERE board_id = {0}".format(board_id)
	cursor.execute(query)
	taskList = []
	for task in cursor:
		taskList.append(task)
	#print taskList

	tasks = []
	if str(taskList[0]) != "(u'',)":
		for task in str(taskList[0]).split(','):
			#print task
			if task != "'" and task != ')':
				#print task.strip('()').replace("u'","")
				query2 = "SELECT task_description,task_state FROM tasks WHERE task_id = {0}".format(task.strip('()').replace("u'",""))
				cursor.execute(query2)
				for i in cursor:
					#print i
					tasks.append(i)

	#print tasks

	bl = 0
	ip = 0
	done = 0
	blList = []
	ipList = []
	doneList = []
	i = 0
	(width, height) = console.getTerminalSize()
	for task in tasks:
		for char in task[0]:
			if i == width/3-4:
				task[0] = insert(task[0],'\n',i) 
	    	i+=1
		if task[1] == '0':
			bl += 1
			appender = '{0}'.format(i)+':'+task[0]
			#appender = '{0}'.format(i)+ ' '+task[0]
			update_query = "UPDATE tasks SET task_description= '{0}' WHERE task_description='{1}'".format(appender, task[0])
			cursor.execute(update_query)
			conn.commit()

			blList.append(appender)
		if task[1] == '1':
			update_query = "UPDATE tasks SET task_description= '{0}' WHERE task_description='{1}'".format(appender, task[0])
			cursor.execute(update_query)
			conn.commit()
			ip+= 1
			ipList.append(task[0])
		if task[1] == '2':
			done += 1
			update_query = "UPDATE tasks SET task_description= '{0}' WHERE task_description='{1}'".format(appender, task[0])
			cursor.execute(update_query)
			conn.commit()
			doneList.append(task[0])
	
	backLogWithSpacing = "Backlog" + " " * (width/3-4-len("Backlog"))
	inProgressWithSpacing = "In Progress" + " " * (width/3-4-len("In Progress"))
	doneWithSpacing = "Done" + " " * (width/3-4-len("Done"))
	allTasks = [[backLogWithSpacing,inProgressWithSpacing,doneWithSpacing]]
	#print bl
	#print ip
	#print done
	for i in range (0,max(bl,ip,done)):
		currentList = []
		if i < bl:
			currentList.append(blList[i])
		else:
			currentList.append('')
		if i < ip:
			currentList.append[ipList[i]]
		else:
			currentList.append('')
		if i < done:
			currentList.append(doneList[i])
		else:
			currentList.append('')
		allTasks.append(currentList)

	table = DoubleTable(allTasks, board_name)
	table.inner_row_border = True
	print(table.table)
def pickBoard(board_name):
	query = "SELECT board_id,leader_id,member_ids,task_ids FROM boards WHERE board_name = '{0}'".format(board_name)
	cursor.execute(query)
	for i in cursor:
		return i


def getBoards(member_id):
	finalList = []
	query = "SELECT board_name,member_ids FROM boards"
	cursor.execute(query)
	for i in cursor:
		a = str(i[1])
		a = a.strip('[]').replace(" ", "")
		a = a.split(',')

		for j in a:
			if str(member_id) == j:
				finalList.append(str(i[0]))
	
	query = "SELECT board_name,leader_id FROM boards"
	cursor.execute(query)
	for i in cursor:
		a = str(i[1])
		a = a.strip('[]').replace(" ", "")
		a = a.split(',')

		for j in a:

			if str(member_id) == j:
				finalList.append(str(i[0]))	

	#return listNames
	return finalList
if __name__ == '__main__':
    main()
