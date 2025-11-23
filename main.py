# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%A %b %d, %Y %I:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        new_todos = []
        for item in todos:
            new_item = item.strip("\n")
            new_todos.append(new_item)
        for index, item in enumerate(new_todos):
            item = item.title()
            fine = f"{index+1}. {item}"
            print(fine)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1
            todos = functions.get_todos()
            todo_to_remove = todos[number].strip("\n")
            todos.pop(number)
            message = f"Todo {todo_to_remove.upper()} was removed from the list as completed."
            print(message)
            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")


print("Bye for now!")

