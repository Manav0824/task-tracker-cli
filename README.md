# ✅ Task Tracker CLI

A simple command-line tool to manage your daily tasks using Python.  
Supports adding, listing, updating, marking done, and deleting tasks.  
Data is stored locally in a `tasks.json` file.  
**Project URL:** https://github.com/Manav0824/task-tracker-cli

---

## 📦 Features

- ➕ Add new tasks  
- 📋 List all tasks  
- ✅ Mark tasks as done  
- ✏️ Update task description  
- ❌ Delete tasks  

---

## 🚀 How to Run

```bash
cd task-tracker-cli
python main.py <command> [arguments]

# Examples:
python main.py add "Do something"
python main.py list
python main.py done 1
python main.py update 1 "New task"
python main.py delete 1
