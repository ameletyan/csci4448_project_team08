from task import TaskState
from task import BackLog
from task import TaskContext

class Board:
    def __init__(self, members, leader, title, tasks):
        self.members = []
        self.leader = ''
        self.title = ''
        self.tasks = []

    def createTasks(self,taskContent,owners):
        newTask = TaskState(taskContent,owners)
        newTask = BackLog(newTask)
        newTask = TaskContext(newTask)
        self.tasks.append(newTask)

    def getTitle(self):
        return self.title

    def getMembers(self):
        return self.members

    def getTitle(self):
        return self.title

    def getTasks(self):
        return self.tasks
