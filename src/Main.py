from clint.textui import prompt, validators, puts, indent, cols
import console



def printTasks():
    '''get data from db'''
    backlog = ['1.', 'This is task 1 it is cooliasidfisadfiasidfiasdfiasidfisadiiasdfjas djfisajdf isadfij asidfjisad fijsaidf isjdfiasdfi jaisdfj iasdjfi jasidfj iasdfj iasjdfi ajsdifj saidjf iasjdfijasdifjiasdjfi jaisdjfiasdfjf', 'EFL']
    inProgress = ['1', 'asdf is easy', 'SAM']
    done = ['1', 'wot', 'asdf', '2','asdf','asdf']
    tasks = [backlog,inProgress,done]
    
    (width, height) = console.getTerminalSize()
    print (width, height)
    

    for i in range(0,(max(len(taskType) / 3 for taskType in tasks ))):
        
        
        if len(backlog)/3 > i:
            for i in range(0,2):
                if backlog[i+1] > (width/3 - 5):
                    print'|',backlog[i], backlog[i+1][:(width/3 - 5)], '|'
                    backlog[i+1] = backlog[i+1][(width/3 - 5):]
                else:
                    print '|',backlog[i+1][(width/3 - 5):], ' ', backlog[i+2], '|'

        if (len(inProgress)/3 > i): 
            print backlog[i], backlog[i+1], ' ',backlog [i+2]    
        if len(done)/3 > i:
            print done[i], done[i+1], ' ',done[i+2]
in_data = 'login'


while in_data != 'quit':
    printTasks()
    if in_data == 'login':
        username = prompt.query('Enter username:')
        password = prompt.query('Enter password:')
        
        '''while in_data != valid:
            in_data = promy.query('Enter valid Log-in:')
           '''  
    
        in_data = 'boards' 


    if in_data == 'boards':
        #show boards
        in_data = prompt.query('Pick board:')

        if in_data == 'create':
            boardName = prompt.query('Enter board name:')
            '''creator = member.getName()
            do leader stuff?'''
            printTasks()
            


     
    


    '''with indent(4):
        puts('indented text')'''
    
    in_data = prompt.query('Enter Page')
