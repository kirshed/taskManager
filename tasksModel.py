class TasksModel:
    def __init__(self):
        self.tasks = dict()
        self.new_id = 0

    # adding new task to dictionary
    def add_task(self, task):
        self.new_id += 1
        self.tasks[self.new_id] = task
        return self.new_id

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
            return 1
        else:
            return 0
