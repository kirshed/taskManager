from view import TasksView
from tasksVm import TasksVm
from tasksModel import TasksModel

def main():
    view = TasksView()
    model = TasksModel()
    vm = TasksVm(view, model)
    num = int(view.print_view())
    vm.execute(num)

if __name__ == "__main__":
    main()