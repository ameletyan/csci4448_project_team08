from task import TaskState
from task import BackLog
from task import TaskContext

from database import Database

class Board:
    def __init__(self, members, leader, title, tasks):
        self.members = []
        self.leader = ''
        self.title = ''
        self.tasks = []

    def createTasks(self,taskContent,owners):
        newTask = TaskContext(taskContent,owners)
        self.tasks.append(newTask)

    def getTitle(self):
        return self.title

    def getMembers(self):
        return self.members

    def getTitle(self):
        return self.title

    def getTasks(self):
        return self.tasks
