from member import Member

class Leader (Member):

    def addMembers(self, board, members):
        for n in members:
            self.members.append(n)
            database().addMembers(board, members)

	def assignTasks(self, task):
		return 0

	def makeBoard(self):
		return 0
