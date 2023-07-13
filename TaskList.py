from Task import Task


class TaskList:
    def __init__(self) -> None:
        self.listOfTask = {}

    def createTask(self, description):
        task = Task(description)

        self.listOfTask[task.id] = task

    def showList(self):
        print("\n===========================")
        for index, (id, task) in enumerate(self.listOfTask.items()):
            print(f"{index + 1}. {task.description}")
        print("===========================")
