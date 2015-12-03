from task import TaskState
from task import BackLog
from task import TaskContext
import database

class Board:
    def __init__(self, board_id, board_name, task_ids, leader_id, member_ids):
        self.id = board_id
        self.name = board_name
        self.tasks = task_ids
        self.leader = leader_id
        self.members = member_ids

    def createTasks(self,taskContent,owners):
        newTask = TaskContext(taskContent,owners)
        self.tasks.append(newTask)

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getTasks(self):
        return self.tasks

    def getLeader(self):
        return self.leader

    def getMembers(self):
        return self.members
