class taskModel:
    tasks = dict()
    size = 0
    def addTask(self, task):
        self.size+=1
        self.tasks[self.size] = task

    def getTask(self, id):
        return self.tasks.get(id)

    def removeTask(self, id):
        del self.tasks[id]
