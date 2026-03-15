# CLI Task Manager

A lightweight, interactive Command Line Interface (CLI) Task Manager built in Python. This project is designed for practice and to help beginners understand Python basics such as lists, dictionaries, file I/O, and control flow.

## 🚀 Features

- **Add Tasks**: Quickly add new tasks to your list.
- **View Tasks**: See all your current and completed tasks.
- **Remove Tasks**: Delete tasks you no longer need.
- **Progress Tracking**: Mark tasks as done to track your accomplishments.
- **Persistent Storage**: Automatically saves your tasks to `task.txt` and `done.txt` so you never lose your progress.
- **Easy Cleanup**: Built-in option to clear all tasks.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/CLI-TASKMANAGER.git
   cd CLI-TASKMANAGER
   ```

2. **Ensure you have Python installed**:
   This project requires Python 3.x. Check your version with:
   ```bash
   python --version
   ```

## 💻 Usage

Run the task manager using the following command:

```bash
python task_manager.py
```

### Main Menu Options:
1. **add**: Add a new task (type 'done' to return to menu).
2. **view**: List all tasks (current and completed).
3. **remove**: Remove a task by its index.
4. **task process**: Mark a specific task as completed.
5. **Save task**: Manually save the current state to file.
6. **Delete**: Clear all stored tasks.
0. **Exit**: Gracefully exit the application.

## 📂 Project Structure

- `task_manager.py`: The main script containing the application logic.
- `task.txt`: Storage file for active tasks.
- `done.txt`: Storage file for completed tasks.
- `README.md`: Project documentation.
- `CONTRIBUTING.md`: Guidelines for contributing to this project.

## 🤝 Contributing

Contributions are welcome! Whether you're fixing a typo, adding a feature, or improving documentation, please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get started.

## 📜 License

This project is open-source and available for practice and educational purposes.