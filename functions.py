FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
#when you define the function, it is called the parameter of the function
#there are some functions that get arguments
#when you call the function the argument value

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

#this will not allow the print statement to work when called
#in cli.py
#if we run name which is variable directly in the same py file.
# the output will be main. but if we run functions.py which
# contain the __name__ in the cli.py the output will be functions.
# to control the execution when the file is run directly
if __name__ == "__main__":
    print("Hello")
    print(get_todos())