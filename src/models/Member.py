import ctypes
import database
import random
import mysql.connector
from board import Board

#conn = mysql.connector.connect(user='tempuser',password='password',database='project_brian_test')
#cursor = conn.cursor()

class Member:
    def __init__(self, member_id, member_name, email, password, board_ids):
        self.id = member_id
        self.name = member_name
        self.email = email
        self.password = password
        self.boards = board_ids

    # leader: make board
    #   Will the members parameter be a list, string, or what?
    def makeBoard(self, boardName, leader, members):
        board_list = []
        # Get all boards from boards
        board_name= "SELECT board_name FROM boards"
        database.cursor.execute(board_name)
        for board in database.cursor:
            board_list.append(board)
        if boardName in board_list:
            print 'Board name already exist, please try a different name' 
            return 0
        board_id = random.randint(0,1000000000)
        leader_id = leader.getID()
	#print members
        existing_members = []
        member_name = 'SELECT member_name FROM members'
        database.cursor.execute(member_name)
        for i in database.cursor:
            existing_members.append(i)
	#print existing_members
        expectedLength = len(members)
	gottenLength = 0
        for i in range (0,len(members)):
	    for name in existing_members:
		if members[i] == name[0]:
		    gottenLength += 1    	
		    break


	if gottenLength < expectedLength:
            print 'This name is not in our database: %s' %name
            return 0

        task_ids = '' 

        existing_member_ids = []
        for name in members:
            member_ids = "SELECT member_id FROM members WHERE member_name='%s'" %name
           # print member_ids
            database.cursor.execute(member_ids)
            for name in database.cursor:
               # print name
                existing_member_ids.append(name[0])
        #print 'existing member ids is.. '
        #print existing_member_ids 
	    # Insert all the parameters into the boards
        boardID = random.randint(0,1000000000)
        query3 = "INSERT INTO boards (board_id, board_name, task_ids, leader_id, member_ids) VALUES ({0}, '{1}', '{2}', {3}, '{4}')".format(boardID,  boardName, task_ids, leader_id, existing_member_ids)

        database.cursor.execute(query3)
        database.conn.commit()	
        return Board(boardID,boardName,task_ids,leader_id,existing_member_ids)

	def joinBoard(self, board):
		def Mbox(title, text, style):
			ctypes.windll.user32.MessageBoxA(0, text, title, style)
			Mbox('Your title', 'Your text', 1)
		return 0

    def getID(self):
        return self.id

    def getName(self):
        return self.name

	def getEmail(self):
		return self.email

	def getPassword(self):
		return self.password

	def getBoards(self):
		return self.boards
