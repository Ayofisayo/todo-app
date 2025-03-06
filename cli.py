from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below:")
print("It is", now)

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, exit, edit, complete or show: ")
    user_action = user_action.strip()

    # Check if user action is 'add'
    if user_action.startswith('add'):
        todo= user_action[4:] #a break line for each item in the textfile

        todos = get_todos()

        todos.append(todo + '\n')
        # Write todos in the file
        write_todos( todos, "todos.txt")

    elif user_action.startswith('show'):

        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'): # to remove item from the list
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")
print ("Bye!")
