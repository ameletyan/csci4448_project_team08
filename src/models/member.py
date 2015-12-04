import ctypes
import database

class Member:
    def __init__(self, member_id, member_name, email, password, board_ids):
        self.id = member_id
        self.name = member_name
        self.email = email
        self.password = password
        self.boards = board_ids

    # leader: make board
    #   Will the members parameter be a list, string, or what?
    def makeBoard(self, name, leader, members):
        board_list = []
        # Get all boards from boards
        board_name= "SELECT board_name FROM boards"
        cursor.execute(board_name)
        for board in cursor:
            board_list.append(board)
        if name in boards:
            print 'Board name already exist, please try a different name' 
            return 0
        board_id = random.randint(0,1000000000)
        leader_id = leader.getID()

        existing_members = []
        member_name = 'SELECT member_name FROM members'
        cursor.execute(member_name)
        for name in cursor:
            existing_members.append(name)

        for name in members:
            if name not in existing_members:
                print 'This name is not in our database: %s' %name
                return 0

        task_ids = '' 

        existing_member_ids = []
        for name in members:
            member_ids = 'SELECT member_ids FROM members WHERE member_name=%s' %name
            cursor.execute(member_ids)
            existing_member_ids.append(member_ids)

        # Insert all the parameters into the boards
        query = "INSERT INTO boards (board_id, board_name, task_ids, leader_id, member_ids) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '')".format(random.randint(0,1000000000), board_id, name, task_ids, leader_id, existing_member_ids)

        cursor.execute(query3)
        conn.commit()

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
