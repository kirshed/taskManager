class TasksView:
    task = ""

    # printing menu
    def print_view(self):
        print("What would you like to do?")
        print("1. Add a new task")
        print("2. Edit an existing task")
        print("3. Get an existing task")
        print("4. Delete an existing task")
        print("5. Delete all tasks")
        print("6. Exit")
        return input()
