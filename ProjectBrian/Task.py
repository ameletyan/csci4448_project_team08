class TaskState:
    def __init__(self,setTaskContent,setOwners):        
        self.taskContent = setTaskContent
        self.owners = setOwners
        
    def getTaskContent(self):
        return self.getTaskContent

    def getOwners(self):
        return self.owners


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
    def __init__(self,taskContent,owners):
        self.content = TaskState(taskContent,owners)
        self.content = BackLog(self.content)


    def moveToInProgress(self):
        self.content = InProgress(self.content)
    
    def moveToBackLog(self):
        self.content = BackLog(self.content)

    def moveToDone(self):
        self.content = Done(self.content)

    def getOwners(self):
        return self.content.getOwners()

    def getTaskContent(self):
        return self.content.getTaskContent()
