import sys
import json
import argparse

TASKS_FILE = "tasks.json"

def listTask():
    with open(TASKS_FILE,"r") as jsonFile:
        loadFile=json.load(jsonFile)
        for x in loadFile:
            print(x,loadFile[x])

def removeTask(key):
    with open(TASKS_FILE,"w") as jsonFile:
        loadFile=json.load(jsonFile)
        loadFile[key] = ""

def main():
    parser = argparse.ArgumentParser(prog="tasker", description="tasker is a task tracker and manager which helps you with organising your tasks",epilog="temp nothing")
    #parser.add_argument("list",help="prints all tasks from tasks.json")
    subparsers = parser.add_subparsers(
        dest="command",
        required=True
        )
    
    list_parser = subparsers.add_parser(
        "list",
        help="prints all tasks from tasks.json",
        aliases = ["ls"]
        )

    remove_parser = subparsers.add_parser(
        "remove",
        help="removes task by key"
        ) 

    list_parser.set_defaults(func=listTask) 
    args = parser.parse_args()
    args.func()

    

    #if len(sys.argv) < 2:
    #    print("Usage: python program.py <name>")
    #    listTasks()
    #    sys.exit(1)
    
    #name = sys.argv[1]
    

    #print(f"Hello, {name}!")

    #print(f"Arguments: {sys.argv}")

if __name__ == "__main__":
    main()

