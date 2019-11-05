import pandas as pd
import pymongo
from task import Task
from datetime import datetime


class TasksModel:
    def __init__(self):
        t = dict()
        column = {"task_name"}
        ids = {}
        self.df_tasks = pd.DataFrame(index=ids, columns=column)
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["tasksdatabase"]
        self.mycol = mydb["tasks1"]
        if self.mycol.find_one():
            # first = self.mycol.find_one({'_id': 1}, {})
            first = self.mycol.find_one()
            self.new_id = int(first['id'])
        else:
            self.new_id = 0
            init_id = {"id": str(self.new_id)}
            self.mycol.insert_one(init_id)

    # generate a new id
    def create_id(self):
        self.new_id += 1
        id_update = {"id": str(self.new_id)}
        # updating newist id in db
        self.mycol.replace_one({}, id_update)
        return self.new_id

    # adding new task to dictionary
    def add_task(self, task):
        new_task = {"id": str(task.id), "task": task.tsk, "time": task.t,
                    "edit": str(task.last_edit)}
        i = self.mycol.insert_one(new_task)
        return self.new_id

    # editing existing task in dict
    def edit_task(self, id, edited):
        if self.mycol.find_one({'id': str(id)}):
            try:
                tsk = self.get_task(id)
            except:
                return
            tme = tsk.t
            edt_t = tsk.edit_time(datetime.now())
            # updating task id in db
            self.mycol.replace_one({"id": str(id)},
                                   {"id": str(id), "task": edited, "time": tsk.t,
                                    "edit": tsk.last_edit}, upsert=False)
            return True
        else:
            return False

    # getting task form db
    def get_task(self, id):
        '''a = self.mycol.find({})
        for x in a:
            print(x)'''
        if self.mycol.find_one({'id': str(id)}):
            t = self.mycol.find_one({'id': str(id)}, {'task': 1, 'time': 1, 'edit': 1})
            tsk = Task(id, t['task'])
            tsk.set_time(t['time'])
            tsk.edit_time(t['edit'])
            return tsk
        else:
            return 0

    # removing task from dictionary
    def remove_task(self, id):
        if self.mycol.find_one({'id': str(id)}):
            self.mycol.delete_one({'id': str(id)})
            return True
        else:
            return False

    def delete_all_tasks(self):
        self.mycol.delete_many({})
        return
