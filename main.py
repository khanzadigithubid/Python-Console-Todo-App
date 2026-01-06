import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from the JSON file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []
    
    def save_tasks(self):
        """Save tasks to the JSON file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)
    
    def add_task(self, description):
        """Add a new task"""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added with ID: {task['id']}")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks found.")
            return
        
        print("\n--- Your Tasks ---")
        for task in self.tasks:
            status = "✓" if task['completed'] else "○"
            print(f"{task['id']}. [{status}] {task['description']}")
        print("------------------\n")
    
    def mark_completed(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task with ID {task_id} not found.")
    
    def delete_task(self, task_id):
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                del self.tasks[i]
                self.save_tasks()
                print(f"Task {task_id} deleted.")
                return
        print(f"Task with ID {task_id} not found.")
    
    def run(self):
        """Main application loop"""
        print("Welcome to the Python Console Todo Application!")
        
        while True:
            print("\nOptions:")
            print("1. Add task")
            print("2. View tasks")
            print("3. Mark task as completed")
            print("4. Delete task")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                description = input("Enter task description: ").strip()
                if description:
                    self.add_task(description)
                else:
                    print("Task description cannot be empty.")
            
            elif choice == '2':
                self.view_tasks()
            
            elif choice == '3':
                try:
                    task_id = int(input("Enter task ID to mark as completed: "))
                    self.mark_completed(task_id)
                except ValueError:
                    print("Please enter a valid task ID (number).")
            
            elif choice == '4':
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    self.delete_task(task_id)
                except ValueError:
                    print("Please enter a valid task ID (number).")
            
            elif choice == '5':
                print("Thank you for using the Todo Application. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


def main():
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()