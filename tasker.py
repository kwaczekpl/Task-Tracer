import string
import sys
import json
import argparse
import os

TASKS_FILE = "tasks.json"

def loadTasks():
    try:
        with open(TASKS_FILE,"r") as jsonFile:
            tasks=json.load(jsonFile)
    except FileNotFoundError:
        print("File not found")
        print("Add a task to create it")
        return {}
    except json.JSONDecodeError:
        print("Invalid type format")
        return {}
    return tasks

def saveTasks(tasks):
    with open(TASKS_FILE, "w") as jsonFile:
        json.dump(tasks,jsonFile,indent=4)

def listTask(_args):
    
    tasks = loadTasks()
    
    print(f"{'ID'}{'':<2} {'STATUS':<7} TASK")

    for number, key in tasks.items():

        print(f"{number}{'|':<3} {key['status']:<7} | {key['name']}")
  
def addTask(args):

    tasks = loadTasks()

    taskID = len(tasks) + 1

    statusString = "[✓]" if args.status else "[ ]"
    tasks[taskID] = {"name" : args.taskName,"status" : statusString}

    saveTasks(tasks)
    

def updateTask(args):
    
    tasks = loadTasks()

    tasks.insert(args.taskNum-1, {tasks[args.taskNum] : "Done" if args.status else "In progress"})
    
    saveTasks(tasks)

def removeTask(args):
    
    tasks = loadTasks()

    if args.all:
        tasks.clear()
    else:
        if not (args.taskNum < 1 or args.taskNum > len(tasks)):
            tasks.pop(str(args.taskNum))
        else:
            print(f"Pick number between 1 and {len(tasks)}")
    
    saveTasks(tasks)      


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
        help="used to create new tasks"
        )
    addParser.add_argument("taskName",type=str)
    addParser.add_argument("status",type=int, nargs='?',default=0,choices=[0,1])
    addParser.set_defaults(func=addTask)

    updateParser = subparsers.add_parser(
        "update",
        help="change task status"
        )
    updateParser.add_argument("taskNum",type=int,nargs='?')
    updateParser.add_argument("-s","--status",type=bool,choices=[0,1])
    updateParser.set_defaults(func=updateTask)

    removeParser = subparsers.add_parser(
        "remove",
        help="removes task by key",
        aliases=["rm"]
        ) 
    removeParser.add_argument("taskNum",type=int,nargs='?')
    removeParser.add_argument("-a", "--all",action="store_true",help="remove all tasks")
    removeParser.set_defaults(func=removeTask)
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()

