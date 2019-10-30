from task_view import TasksView
from tasks_model import TasksModel

class TasksVm:
    def __init__(self, vw, mdl):
        self.view = vw
        self.model = mdl
        # functions dictionary
        self.funcMap = dict()
        self.funcMap[1] = self.add_t
        self.funcMap[2] = self.edit_t
        self.funcMap[3] = self.get_t
        self.funcMap[4] = self.remove_t
        self.funcMap[5] = self.exit_program

    # calling specified function
    def execute(self, num):
        if num > 5 or num < 1:
            print("Not an option, please enter a number from the menu")
        else:
            # calling requested function
            self.funcMap.get(num)()
        # recalling execute
        newNum = int(self.view.print_view())
        self.execute(newNum)
    # adding task
    def add_t(self):
        print("Please enter the task you would like to add:")
        task = input()
        id = self.model.add_task(task)
        print("task", id, "added")

    # editing existing task if exists
    def edit_t(self):
        print("Please enter the task id you would like to edit:")
        id = int(input())
        # checking if id exists
        if self.model.get_task(id):
            print("please enter the edited task:")
            edited = input()
            self.model.edit_task(id, edited)
            print("task", id, "edited")
        else:
            print("task", id, "does not exist")

    # getting specified task
    def get_t(self):
        print("Please enter the task id you would like to get:")
        id = int(input())
        task = self.model.get_task(id)
        if task:
            print("the task you requested:", task)
        else:
            print("the task doesn't exist")

    # removing specified task
    def remove_t(self):
        print("Please enter the task id you would like to remove:")
        id = int(input())
        if self.model.remove_task(id):
            print("task", id, "was deleted")
        else:
            print("task", id, "does not exist")

    # exiting program
    def exit_program(self):
        exit()

