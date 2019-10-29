from view import TasksView
from taskModel import TaskModel


class TasksVm:
    def __init__(self, vw, mdl):
        self.view = vw
        self.model = mdl
        self.funcMap = dict()
        self.funcMap[1] = self.add_t
        self.funcMap[2] = self.edit_t
        self.funcMap[3] = self.get_t
        self.funcMap[4] = self.remove_t
        self.funcMap[5] = self.exit_program

    # calling specified function
    def execute(self, num):
        if num > 5 or num < 1:
            print("not an option, please insert a number from the menu")
            # recalling execute
            self.execute(int(input()))
        self.funcMap.get(num)()

    # adding task
    def add_t(self):
        print("Please input the task you would like to add:")
        task = input()
        id = self.model.add_task(task)
        print("task", id, "added")

    # editing existing task if exists
    def edit_t(self):
        print("Please input the task id you would like to edit:")
        id = input()
        print("please input the edited task:")
        edited = input()
        if self.model.edit_task(id, edited):
            print("task", id, "edited")
        else:
            print("task", id, "does not exist")

    # getting specified task
    def get_t(self):
        print("Please input the class id you would like to get:")
        id = input()
        task = self.model.get_task(id)
        if task:
            print("the task you requested:", task)
        else:
            print("the task doesn't exist")

    # removing specified task
    def remove_t(self):
        print("Please input the task id you would like to remove:")
        id = input()
        if self.model.remove_task(id):
            print("task", id, "was deleted")
        else:
            print("task", id, "does not exist")

    # exiting program
    def exit_program(self):
        return


view = TasksView()
model = TaskModel()
vm = TasksVm(view, model)
num = int(view.print_view())
vm.execute(num)
