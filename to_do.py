import argparse
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Added: {task}")

def list_tasks(show_all=False):
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        if show_all or not t["done"]:
            print(f"{i+1}. {t['task']} [{status}]")

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Marked task {index+1} as done.")
    else:
        print("Invalid task index.")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid task index.")

parser = argparse.ArgumentParser(description="Smart To-Do CLI App")
parser.add_argument("command", choices=["add", "list", "done", "delete"], help="Action")
parser.add_argument("arg", nargs="?", help="Task text or index", default=None)
parser.add_argument("--all", action="store_true", help="Show all tasks")

args = parser.parse_args()

if args.command == "add":
    add_task(args.arg)
elif args.command == "list":
    list_tasks(args.all)
elif args.command == "done":
    complete_task(int(args.arg) - 1)
elif args.command == "delete":
    delete_task(int(args.arg) - 1)
