import json
import os
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.tasks = json.load(file)
            except json.JSONDecodeError:
                self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        task_id = len(self.tasks) + 1
        new_task = {
            'id': task_id,
            'task': task,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'completed': False
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task added successfully! Task ID: {task_id}")

    def edit_task(self, task_id, new_task):
        for task in self.tasks:
            if task['id'] == task_id:
                task['task'] = new_task
                task['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_tasks()
                print(f"Task {task_id} updated successfully!")
                return
        print(f"Task with ID {task_id} not found!")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"Task {task_id} deleted successfully!")
                return
        print(f"Task with ID {task_id} not found!")

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"Task {task_id} marked as completed!")
                return
        print(f"Task with ID {task_id} not found!")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list!")
            return
        
        print("\nYour To-Do List:")
        print("-" * 50)
        for task in self.tasks:
            status = "✓" if task['completed'] else " "
            print(f"[{status}] ID: {task['id']} - {task['task']}")
            print(f"    Created at: {task['created_at']}")
            print("-" * 50)

def main():
    todo_list = TodoList()
    
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Display Tasks")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        
        elif choice == '2':
            try:
                task_id = int(input("Enter the task ID to edit: "))
                new_task = input("Enter the new task: ")
                todo_list.edit_task(task_id, new_task)
            except ValueError:
                print("Please enter a valid task ID!")
        
        elif choice == '3':
            try:
                task_id = int(input("Enter the task ID to delete: "))
                todo_list.delete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID!")
        
        elif choice == '4':
            try:
                task_id = int(input("Enter the task ID to mark as completed: "))
                todo_list.mark_completed(task_id)
            except ValueError:
                print("Please enter a valid task ID!")
        
        elif choice == '5':
            todo_list.display_tasks()
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 