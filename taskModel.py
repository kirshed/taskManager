class TaskModel:
    def __init__(self):
        self.tasks = dict()
        self.size = 0

    # adding new task to dictionary
    def add_task(self, task):
        self.size += 1
        self.tasks[self.size] = task
        return self.size

    # editing existing task in dict
    def edit_task(self, id, edited):
        if self.tasks.get(id):
            self.tasks[id] = edited
            return 1
        else:
            return 0

    # getting task form dictionary
    def get_task(self, id):
        if self.tasks.get(id):
            return self.tasks.get(id)
        else:
            return 0

    # removing task from dictionary
    def remove_task(self, id):
        if self.tasks.get(id):
            del self.tasks[id]
        else:
            return 0
