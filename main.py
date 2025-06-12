import json
import os
import sys

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "description": description, "status": "pending"})
    save_tasks(tasks)
    print(f"✅ Task added: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"{task['id']}. [{task['status'].upper()}] {task['description']}")

def mark_done(task_id):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            found = True
            break
    if found:
        save_tasks(tasks)
        print(f"✅ Task {task_id} marked as done.")
    else:
        print("❗Task not found.")

def update_task(task_id, new_description):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            found = True
            break
    if found:
        save_tasks(tasks)
        print(f"✏️ Task {task_id} updated.")
    else:
        print("❗Task not found.")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(new_tasks) == len(tasks):
        print("❗Task not found.")
        return

    # Reassign IDs
    for i, task in enumerate(new_tasks, start=1):
        task["id"] = i

    save_tasks(new_tasks)
    print(f"🗑️ Task {task_id} deleted.")

# --- CLI Commands ---
if len(sys.argv) < 2:
    print("Usage:")
    print("  python main.py add \"Task description\"")
    print("  python main.py list")
    print("  python main.py done <task_id>")
    print("  python main.py update <task_id> \"new description\"")
    print("  python main.py delete <task_id>")
    sys.exit()

command = sys.argv[1]

if command == "add":
    description = " ".join(sys.argv[2:])
    if description:
        add_task(description)
    else:
        print("❗Please provide a task description.")

elif command == "list":
    list_tasks()

elif command == "done":
    if len(sys.argv) >= 3:
        try:
            task_id = int(sys.argv[2])
            mark_done(task_id)
        except ValueError:
            print("❗Task ID must be a number.")
    else:
        print("❗Usage: python main.py done <task_id>")

elif command == "update":
    if len(sys.argv) >= 4:
        try:
            task_id = int(sys.argv[2])
            new_desc = " ".join(sys.argv[3:])
            update_task(task_id, new_desc)
        except ValueError:
            print("❗Task ID must be a number.")
    else:
        print("❗Usage: python main.py update <task_id> <new_description>")

elif command == "delete":
    if len(sys.argv) >= 3:
        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        except ValueError:
            print("❗Task ID must be a number.")
    else:
        print("❗Usage: python main.py delete <task_id>")

else:
    print("❗Unknown command. Use add, list, done, update, or delete.")
