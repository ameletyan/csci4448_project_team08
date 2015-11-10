class TaskState:
    def __init__(self,setTaskContent,setOwners):        
        self.taskContent = setTaskContent
        self.owners = setOwners
        
    def getTaskContent(self):
        return self.getTaskContent

    def getOwners(self):
        return self.owners
:w

class BackLog(TaskState):
    def __init__(self,taskState):
        self.taskContent = taskState.getTaskContent()
        self.owners = taskState.getOwners()


class InProgress(TaskState):
    def __init__(self,taskState):
        self.taskContent = taskState.getTaskContent()
        self.owners = taskState.getOwners()


class Done(TaskState):
    def __init__(self,taskState):
        self.taskContent = taskState.getTaskContent()
        self.owners = taskState.getOwners()

class TaskContext:
    def __init__(self,taskState):
        self.content = taskState

    def moveToInProgress(self):
        self.content = InProgress(taskState)
    
    def moveToBackLog(self):
        self.content = BackLog(taskState)

    def moveToDone(self):
        self.content = Done(taskState)

    def getOwners(self):
        return taskState.getOwners()

    def getTaskContent(self):
        return taskState.getTaskContent()
