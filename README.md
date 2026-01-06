# Python Console Todo Application

A simple, console-based todo application built with Python using only standard library modules. This application allows users to manage their tasks efficiently through a command-line interface.

## Features

- ✅ Add new tasks with titles and descriptions
- ✅ View all tasks with their status
- ✅ Mark tasks as completed
- ✅ Delete tasks
- ✅ Save tasks to a local JSON file (tasks.json)
- ✅ Clean, user-friendly console menu
- ✅ Proper error handling
- ✅ Well-structured and readable code

## Requirements

- Python 3.6 or higher

## How to Run the App

1. Clone or download this repository to your local machine
2. Navigate to the project directory in your terminal
3. Run the application using Python:

```bash
python main.py
```

4. Follow the on-screen menu to interact with the application:
   - Press `1` to add a new task
   - Press `2` to view all tasks
   - Press `3` to mark a task as completed
   - Press `4` to delete a task
   - Press `5` to exit the application

## Project Structure

```
Python-Console-Todo-App/
│
├── main.py                 # Main application code
├── tasks.json             # File where tasks are stored (created automatically)
├── README.md              # This file
├── pyproject.toml         # Project metadata
└── .gitignore             # Git ignore file
```

## Data Storage

All tasks are stored in `tasks.json` in the following format:
```json
[
  {
    "id": 1,
    "title": "Sample Task",
    "description": "This is a sample task",
    "completed": false,
    "created_at": "2023-01-01T12:00:00"
  }
]
```

## Author

AI Khanzadi

## License

This project is open source and available under the MIT License.