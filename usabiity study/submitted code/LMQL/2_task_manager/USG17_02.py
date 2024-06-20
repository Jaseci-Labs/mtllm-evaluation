import lmql

taskObjects = []
taskDetails = []
class Task:
    
    @lmql.query
    def __init__(self, description, priority, time):
        self.description = description
        self.priority = priority
        self.time = time
        taskDetails.append(self.description,self.priority,self.time)
        taskObjects.append(taskDetails)
        taskDetails.clear
        
        
def taskAssigner(taskList):
    for tasks in taskList:
        task = tasks
    '''lmql
    "assign a description, priority rank(0-10), and an estimated time for completion based on the {{task}} task [@Task.__init__ TASK]"
    '''
