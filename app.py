import csv
import os


class TodoApp:
    def __init__(self):
        self._todos = []

    def get_todos(self):
        return self._todos

    def add_one_task(self, title):
        self._todos.append(title)

    def print_list(self):
        for i in range(len(self._todos)):
            print(str(i + 1) + ".  " + self._todos[i])

    def delete_task(self, number_to_delete):
        try:
            number = int(number_to_delete)
        except (ValueError, TypeError):
            print("Enter number of task to delete")
            return
        if 1 <= number <= len(self._todos):
            self._todos.pop(number - 1)
        else:
            print("That number does not exist")

    def save_todos(self):
        with open('todos.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for todo in self._todos:
                writer.writerow([todo])

    def load_todos(self):
        if not os.path.isfile('todos.csv'):
            print("There is no file")
            return
        self._todos = []
        with open('todos.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self._todos.append(row[0])


_app = TodoApp()


def get_todos():
    return _app.get_todos()


def add_one_task(title):
    _app.add_one_task(title)


def print_list():
    _app.print_list()


def delete_task(number_to_delete):
    _app.delete_task(number_to_delete)


def save_todos():
    _app.save_todos()


def load_todos():
    _app.load_todos()


# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    stop = False
    while not stop:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print()
            print_list()
        elif response == "2":
            if len(get_todos()) == 0:
                print("There are no tasks")
            else:
                print()
                print_list()
                print("What task number you want to delete?")
                number_to_delete = input()
                delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")
