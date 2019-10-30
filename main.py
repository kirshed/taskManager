from task_view import TasksView
from tasks_vm import TasksVm
from tasks_model import TasksModel

def main():
    view = TasksView()
    model = TasksModel()
    vm = TasksVm(view, model)
    num = int(view.print_view())
    vm.execute(num)

if __name__ == "__main__":
    main()