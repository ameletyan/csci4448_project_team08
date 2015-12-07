import mysql.connector

conn = mysql.connector.connect(user='tempuser',password='password',database='project_brian_test')
cursor = conn.cursor()

class TaskState:
    def __init__(self, description, member, task_id):        
        self.description = description
        self.member = member
        self.task_id = task_id
        
    def getDescription(self):
        return self.description

    def getMember(self):
        return self.member

    def getID(self):
        return self.task_id


class BackLog(TaskState):
    def __init__(self, taskState):
        self.description = taskState.getDescription()
        self.member = taskState.getMember()
        self.task_id = taskState.getID()


class InProgress(TaskState):
    def __init__(self, taskState):
        self.description = taskState.getDescription()
        self.member = taskState.getMember()
        self.task_id = taskState.getID()

class Done(TaskState):
    def __init__(self, taskState):
        self.description = taskState.getDescription()
        self.member = taskState.getMember()
        self.task_id = taskState.getID()


class TaskContext:
    def __init__(self, description, member, task_id):
        self.content = TaskState(description, member, task_id)
        self.content = BackLog(self.content)


    def moveToInProgress(self):
        self.content = InProgress(self.content)
        query = "UPDATE tasks SET task_state=1 WHERE task_id='{0}'".format(self.content.getID())
        cursor.execute(query)
        conn.commit()

    def moveToBackLog(self):
        self.content = BackLog(self.content)
        query = "UPDATE tasks SET task_state=0 WHERE task_id='{0}'".format(self.content.getID())
        cursor.execute(query)
        conn.commit()

    def moveToDone(self):
        self.content = Done(self.content)
        query = "UPDATE tasks SET task_state=2 WHERE task_id='{0}'".format(self.content.getID())
        cursor.execute(query)
        conn.commit()

    def getMember(self):
        return self.content.getMember()

    def getDescription(self):
        return self.content.getDescription()
