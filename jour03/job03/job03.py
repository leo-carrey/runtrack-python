class Task:
    def __init__(self, title, description, due_date, completed):
        self.__title = title
        self.__description = description
        self.__due_date = due_date
        self.__completed = completed

    def get_title(self):
        return self.__title
    
    def get_description(self):
        return self.__description
    
    def get_due_date(self):
        return self.__due_date
    
    def get_completed(self):
        return self.__completed
    
    def set_title(self, new_title):
        self.__title = new_title
        return self.__title
    
    def set_description(self, new_description):
        self.__description = new_description
        return self.__description
    
    def set_due_date(self, new_due_date):
        self.__due_date = new_due_date
        return self.__due_date
    
    def set_completed(self, new_completed):
        self.__completed = new_completed
        return self.__completed
    

def repr_task(task: Task) -> None:
    print(task.get_title())
    print(task.get_description())
    print(task.get_due_date())
    print(task.get_completed())

class TaskManager():
    def __init__(self):
        self.tasks = []
            
    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

    def show(self):
        for task in self.tasks:
            repr_task(task)



def x():
    title = input("input the title :")
    description = input("input the description :")
    due_date = input("input the due date :")
    completed = input("input if it complete :")
    return Task(title, description, due_date, completed)

def your_choice():
    tm = TaskManager()
    user_input = input("choose one:/n1) add a new task /n2) delete a task/n3) show all task  ")
    if user_input == "1":
        x()
    elif user_input == "2":
        x()

