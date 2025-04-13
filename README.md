# To-Do List Application

A modern and user-friendly To-Do List application with both Command Line Interface (CLI) and Graphical User Interface (GUI) versions. This application helps you manage your tasks efficiently with features like categories, priorities, and due dates.

![To-Do List Application](screenshot.png)

## Features

### Core Features
- Add, edit, and delete tasks
- Mark tasks as completed/uncompleted
- Persistent storage using JSON
- Unique ID for each task

### Advanced Features
- Task Categories (Personal, Work, Shopping, Health, Other)
- Priority Levels (High, Medium, Low)
- Due Dates with calendar picker
- Modern table view of tasks
- Confirmation dialogs for important actions
- Success/error messages
- Toggle completion status

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/todo-list.git
cd todo-list
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### GUI Version
To run the GUI version of the application:
```bash
python todo_gui.py
```

### CLI Version
To run the command-line version:
```bash
python todo.py
```

## How to Use

### Adding a Task
1. Enter the task description
2. Select a category
3. Choose priority level
4. Set due date
5. Click "Add Task"

### Managing Tasks
- **Edit**: Select a task and click "Edit" to modify its details
- **Delete**: Select a task and click "Delete" to remove it
- **Mark Complete**: Select a task and click "Mark Complete" to toggle its completion status
- **Refresh**: Click "Refresh" to update the task list

## File Structure
- `todo.py` - Command Line Interface version
- `todo_gui.py` - Graphical User Interface version
- `tasks.json` - Data storage file
- `requirements.txt` - Project dependencies

## Dependencies
- Python 3.x
- tkinter (built-in)
- tkcalendar

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
[Your Name]

## Acknowledgments
- Thanks to all contributors who have helped this project grow
- Special thanks to the Python community for the amazing libraries 