import ctypes
class Member:
	def __int__(self, email):
		self.boards = []
		self.email = email

	def joinBoard(self, board):
		def Mbox(title, text, style):
			ctypes.windll.user32.MessageBoxA(0, text, title, style)
			Mbox('Your title', 'Your text', 1)
		return 0

	def getEmail(self):
		return self.email

