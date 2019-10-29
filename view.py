class tasksView:
    task = ""
    def __init__(self):
        print("What would you like to do?")
        print("1. Add a new task")
        print("2. Edit an existing task")
        print("3. Delete an existing task")
        print("4. Exit")
        self.task = input()
