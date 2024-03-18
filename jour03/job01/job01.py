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
    

task1 = Task("cours", "faire les cours", "15mars", False)

print(task1.get_title())
