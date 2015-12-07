from task import TaskState
from task import BackLog
from task import TaskContext
import database
import random
import mysql.connector

#conn = mysql.connector.connect(user='tempuser',password='password',database='project_brian_test')
#cursor = conn.cursor()

class Board:
    def __init__(self, board_id, board_name, task_ids, leader_id, member_ids):
        self.iden = board_id
        self.name = board_name
        self.tasks = task_ids
        self.leader = leader_id
        self.members = member_ids

    def makeTasks(self, description, member):
        task_id = random.randint(0,1000000000)
        task_state = 0

        description_query = "SELECT task_description FROM tasks"
        database.cursor.execute(description_query)
        for i in database.cursor:
            if i == description:
                print 'This descrption is already in the database %s' %i
                return 0

        if len(description) > 256:
            print 'Description is too long'
            return 0

        existing_members = []
        member_name = 'SELECT member_name FROM members'
        database.cursor.execute(member_name)
        for i in database.cursor:
            existing_members.append(i[0]) 


        no_member = True
        for j in range(len(existing_members)):
            if(member == existing_members[j]):
                no_member = False

        if no_member:
            print "This member does not exist"
            return 0

        find_id = "SELECT member_id FROM members WHERE member_name = '{0}'".format(member)
        database.cursor.execute(find_id)
        for i in database.cursor:
            member_id = i

        
        query = "INSERT INTO tasks (task_id, task_description, task_state, member_id, board_id) VALUES ({0}, '{1}', {2}, {3}, {4})".format(task_id, description, task_state, member_id[0], self.iden)
        database.cursor.execute(query)
        database.conn.commit()

        # Update self.tasks
        self.tasks = self.tasks + str(task_id) + ','
        # Update database with new self.tasks
        update_board = "UPDATE boards SET task_ids = '{0}' WHERE board_id ={1}".format(self.tasks, self.iden)
        database.cursor.execute(update_board)
        database.conn.commit()
        return TaskContext(description, member, task_id)

    def moveTask(self, task_number, state): 
        print 'self.iden is ...'
        print type(self.iden)
        # TODO: finish this query
        query = "SELECT task_description FROM tasks JOIN boards ON task_id=k WHERE board_id={0}".format(self.iden)
        database.cursor.execute(query)
        description_list = []
        for i in cursor:
            description_list.append(i)
        
        task_number_list = []
        for i in description_list:
            task_number_list = description_list[i].split(':')[0]
        
        for i in task_number_list:
            if i == str(task_number):
                desc = description_list[i]
                task_id = "SELECT task_id FROM tasks WHERE task_description = '{0}'".format(desc)
                database.cursor.execute(task_id)
                for x in cursor:
                    iden = x
                member = "SELECT member FROM tasks WHERE task_description = '{0}'".format(desc)
                database.cursor.execute(member)
                for x in cursor:
                    mem = member
            
            task = TaskState(desc, mem, iden)

            if state == 0:
                task.moveToBacklog()
            elif state == 1:
                task.moveToInProgress()
            elif state == 2:
                task.moveToDone()
            else:
                print 'Invalid input: should be 0, 1, or 2'
                return 0
                

    def createTasks(self,taskContent,owners):
        newTask = TaskContext(taskContent,owners)
        self.tasks.append(newTask)

    def getID(self):
        return self.iden

    def getName(self):
        return self.name

    def getTasks(self):
        return self.tasks

    def getLeader(self):
        return self.leader

    def getMembers(self):
        return self.members
