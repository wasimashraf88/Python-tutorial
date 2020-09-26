def createItem():
    print("Create a new ToDo item")

def listItems():
    print("List all ToDo items")

def markItemDone():
    print("Mark item as done")

def interface():
    print("Welcome to our todo application")

interface()
def interface():
    print("Welcome to our todo application")
    print("What would you like to do?")
    print("-> create: create a new todo item")
    print("-> list: list all todo items")
    print("-> done: mark a todo item as done")

    cmd = input("Command: ")

    if cmd == "create":
        createItem()
    elif cmd == "list":
        listItems()
    elif cmd == "done":
        markItemDone()
    else:
        print("I don't understand the command")
        


