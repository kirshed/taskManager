import pandas as pd
import pymongo


class TasksModel:
    def __init__(self):
        t = dict()
        column = {"task_name"}
        ids = {}
        self.df_tasks = pd.DataFrame(index=ids, columns=column)
        self.new_id = 0

    # adding new task to dictionary
    def add_task(self, task):
        self.new_id += 1
        self.df_tasks.loc[self.new_id] = task
        # print(self.df_tasks)
        return self.new_id

    # editing existing task in dict
    def edit_task(self, id, edited):
        if id in self.df_tasks.index:
            self.df_tasks.loc[id, 'task_name'] = edited
            return True
        else:
            return False

    # getting task form dictionary
    def get_task(self, id):
        if id in self.df_tasks.index:
            return self.df_tasks.loc[id]['task_name']
        else:
            return 0

    # removing task from dictionary
    def remove_task(self, id):
        if id in self.df_tasks.index:
            self.df_tasks.drop(id, inplace=True)
            return True
        else:
            return False
