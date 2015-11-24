import mysql.connector

conn = mysql.connector.connect(user='tempuser', password='password', database='project_brian_test')
cursor = conn.cursor()

def getUsers(board_name):
    query = "SELECT name FROM users JOIN boards ON boards.user_id = users.user_id WHERE board_name = '%s'" % board_name
    cursor.execute(query)
    nameList = []
    for name in cursor:
        nameList.append(name)

    print(nameList)
    #return nameList

def main():
    board_name = 'temp board'
    getUsers(board_name)


    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
