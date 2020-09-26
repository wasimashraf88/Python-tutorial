import json
import random
import os

#createItem() to create a new todo item
#listItems() to list all items that we currently have in our todo system
#markItemDone() to mark a item as done
#interface()   to provde a commandline interface for the user to interact with our system

def createItem():

    print("Create a new ToDo item")

    title = input("Title: ")
    priority = input("Priorty: ")

    d = {}
    d["title"] = title
    d["priority"] = priority
    random_id = random.randint(1000,10000)
    d["id"] = random_id
    file_path = "todos/" + str(random_id) + ".todo"
    file_handler = open(file_path, "w")

    json.dump(d, file_handler)
    print("Saved todo item with id " + str(random_id))

def listItems():
    print("List all ToDo items")
    for todo_file_name in os.listdir("todos/"):
        todo_path = "todos/" + todo_file_name

        file_handler = open(todo_path, "r")
        item = json.load(file_handler)

        print("Id: " + str(item['id']))
        print("-> Title: " + str(item['title']))
        print("-> Priority: " + str(item['priority']))


def markItemDone():
    print("Mark as item done")

    todo_id = input("Id: ")
    
    todo_path = "todos/" + str(todo_id) + ".todo"
    os.remove(todo_path)
    print("Removed todo item with id " + str(todo_id))

    


name  = input("What is your name? ")
print("The name is " + name)

def interface():
    print("Welcome to our todo application")
    print("What would you like to do?")
    print("-> create: create a new todo item")
    print("-> list: list all todo items")
    print("-> done: mark a todo item as done")
interface()
cmd = input("Command: ")
if cmd == "create":
    createItem()
elif cmd == "list":
    listItems()
elif cmd == "done":
    markItemDone()
else:
    print("I don't understand the comamnd")