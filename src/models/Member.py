import ctypes
import database

class Member:
	def __init__(self, member_id, member_name, email, password, board_ids):
		self.ident = member_id
		self.name = member_name
		self.email = email
		self.password = password
		self.boards = board_ids

	def joinBoard(self, board):
		def Mbox(title, text, style):
			ctypes.windll.user32.MessageBoxA(0, text, title, style)
			Mbox('Your title', 'Your text', 1)
		return 0

        def getID(self):
            return self.ident

        def getName(self):
            return self.name

        def getEmail(self):
            return self.email

        def getPassword(self):
            return self.password

        def getBoards(self):
	    return self.boards
