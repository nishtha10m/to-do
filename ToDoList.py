class Task:
    def __init__(self, description):
        self.description = description
        self.is_done = False

    def get_description(self):
        return self.description

    def is_done(self):
        return self.is_done

    def mark_done(self):
        self.is_done = True

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task added successfully: {description}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Task List:")
            for i, task in enumerate(self.tasks):
                status = "Done" if task.is_done else "Pending"
                print(f"{i + 1}. {task.get_description()} [Status: {status}]")

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if not task.is_done:
                task.mark_done()
                print(f"Task marked as done: {task.get_description()}")
            else:
                print("Task is already marked as done.")
        else:
            print("Invalid task index.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task removed successfully: {removed_task.get_description()}")
        else:
            print("Invalid task index.")

def main():
    import sys
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)

            if choice == 1:
                description = input("Enter task description: ")
                todo_list.add_task(description)
            elif choice == 2:
                todo_list.list_tasks()
            elif choice == 3:
                done_index = int(input("Enter the task index to mark as done: ")) - 1
                todo_list.mark_task_done(done_index)
            elif choice == 4:
                remove_index = int(input("Enter the task index to remove: ")) - 1
                todo_list.remove_task(remove_index)
            elif choice == 5:
                print("Exiting the To-Do List Application. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
