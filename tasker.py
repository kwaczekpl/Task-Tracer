import string
import sys
import json
import argparse

TASKS_FILE = "tasks.json"

def listTask(_args):
    try:
        with open(TASKS_FILE,"r") as jsonFile:
            tasks=json.load(jsonFile)

    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    for number, task in enumerate(tasks,start = 1):
        print(number, task)

def addTask(args):#args.task
    try:
        with open(TASKS_FILE,"r") as jsonFile:
            tasks = json.load(jsonFile)

    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    tasks.append(args.task)

    with open(TASKS_FILE, "w") as jsonFile:
        json.dump(tasks,jsonFile,indent=4)
        
        
        

def removeTask(args):
    with open(TASKS_FILE,"w") as jsonFile:
        loadFile=json.load(jsonFile)
        loadFile[args] = ""

def main():
    parser = argparse.ArgumentParser(prog="tasker", description="tasker is a task tracker and manager which helps you with organising your tasks",epilog="temp nothing")
    subparsers = parser.add_subparsers(
        title="commands",
        dest="command",
        required=False
        )

    listParser = subparsers.add_parser(
        "list",
        help="prints all tasks from tasks.json",
        aliases = ["ls"]
        )
    listParser.set_defaults(func=listTask)

    addParser = subparsers.add_parser(
        "add",
        help="used to create new tasks",
        )
    addParser.add_argument("task",type=str)
    addParser.set_defaults(func=addTask)

    

    removeParser = subparsers.add_parser(
        "remove",
        help="removes task by key"
        ) 
     
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()

