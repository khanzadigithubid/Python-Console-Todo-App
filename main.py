import json
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task():
    """Add a new task."""
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty!")
        return
    
    description = input("Enter task description (optional): ").strip()
    
    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "completed": False,
        "created_at": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully with ID {task_id}!")

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return
    
    print("\n--- TASK LIST ---")
    for task in tasks:
        status = "✓ Completed" if task["completed"] else "○ Pending"
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description'] or 'N/A'}")
        print(f"Status: {status}")
        print("-" * 30)

def mark_task_completed():
    """Mark a task as completed."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return
    
    view_tasks()
    try:
        task_id = int(input("Enter task ID to mark as completed: "))
        task_found = False
        for task in tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print(f"Task '{task['title']}' is already completed!")
                else:
                    task["completed"] = True
                    save_tasks(tasks)
                    print(f"Task '{task['title']}' marked as completed!")
                task_found = True
                break
        
        if not task_found:
            print(f"Task with ID {task_id} not found!")
    except ValueError:
        print("Please enter a valid task ID (number)!")

def delete_task():
    """Delete a task."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return
    
    view_tasks()
    try:
        task_id = int(input("Enter task ID to delete: "))
        task_found = False
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                deleted_task = tasks.pop(i)
                save_tasks(tasks)
                print(f"Task '{deleted_task['title']}' deleted successfully!")
                task_found = True
                break
        
        if not task_found:
            print(f"Task with ID {task_id} not found!")
    except ValueError:
        print("Please enter a valid task ID (number)!")

def display_menu():
    """Display the main menu."""
    print("\n" + "="*40)
    print("         PYTHON TODO APPLICATION")
    print("="*40)
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")
    print("="*40)

def main():
    """Main function to run the todo application."""
    print("Welcome to the Python Console Todo Application!")
    
    while True:
        display_menu()
        try:
            choice = input("Choose an option (1-5): ").strip()
            
            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                mark_task_completed()
            elif choice == "4":
                delete_task()
            elif choice == "5":
                print("Thank you for using the Todo Application. Goodbye!")
                break
            else:
                print("Invalid option! Please choose a number between 1-5.")
        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()