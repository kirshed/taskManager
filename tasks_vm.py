from task_view import TasksView
from tasks_model import TasksModel
from task import Task


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
        self.funcMap[5] = self.delete_all
        self.funcMap[6] = self.exit_program

    # calling specified function
    def execute(self, num):
        if num > 6 or num < 1:
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
        task_str = input()
        id = self.model.create_id()
        # creating new task
        task = Task(id, task_str)
        # calling add_task from model
        self.model.add_task(task)
        print("task", id, "added at", task.t)

    # editing existing task if exists
    def edit_t(self):
        print("Please enter the task id you would like to edit:")
        id = int(input())
        print("please enter the edited task:")
        edited = input()
        if self.model.edit_task(id, edited):
            try:
                t = self.model.get_task(id)
            except:
                print("unable to perform task. try adding an addtional task first, then try again")
                return
            print("task", id, "edited at", t.last_edit)
        else:
            print("task", id, "does not exist")

    # getting specified task
    def get_t(self):
        print("Please enter the task id you would like to get:")
        id = int(input())
        try:
            task = self.model.get_task(id)
        except:
            print("unable to perform task. try adding an addtional task first, then try again")
            return
        if task:
            if task.last_edit == '0':
                print("the task you requested:", task.tsk, "was created at", task.t)
            else:
                print("the task you requested:", task.tsk, "was created at", task.t, "and was last edited at",
                      task.last_edit)
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

    def delete_all(self):
        self.model.delete_all_tasks()
        print("all tasks were deleted")
