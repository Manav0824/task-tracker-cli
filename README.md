
# ✅ Task Tracker CLI

A simple command-line tool to manage your daily tasks using Python.  
Supports adding, listing, updating, marking done, and deleting tasks.  
Data is stored locally in a `tasks.json` file.

---

🔗 **View this project on GitHub**: Manav0824/task-tracker-cli (https://github.com/Manav0824/task-tracker-cli)

---

## 📦 Features

- ➕ Add new tasks
- 📋 List all tasks
- ✅ Mark tasks as done
- ✏️ Update task description
- ❌ Delete tasks

---

## 🚀 How to Run

### 🔧 Step 1: Navigate to the folder

```bash
cd task-tracker-cli
```

### 🐍 Step 2: Use Python to run commands

```bash
python main.py <command> [arguments]
```

---

## 🛠️ Available Commands

### ➕ Add a new task
```bash
python main.py add "Finish assignment"
```

### 📋 List all tasks
```bash
python main.py list
```

### ✅ Mark a task as done
```bash
python main.py done <task_id>
```
Example:
```bash
python main.py done 1
```

### ✏️ Update a task
```bash
python main.py update <task_id> "New description"
```
Example:
```bash
python main.py update 2 "Submit report"
```

### ❌ Delete a task
```bash
python main.py delete <task_id>
```
Example:
```bash
python main.py delete 3
```

---

## 📁 Data Storage

Tasks are stored in a file called `tasks.json`, using this format:
```json
[
  {
    "id": 1,
    "description": "Finish assignment",
    "status": "done"
  }
]
```

---

## 📚 Requirements

- Python 3.x  
(No external libraries required — just standard Python.)

---

## 👨‍💻 Author

Manav Khanna  


---

## 📜 License

This project is open-source and free to use.
## Project URL:
Project URL: https://github.com/Manav0824/task-tracker-cli


