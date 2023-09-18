import platform
import os

def addTodo():

    add = str(input("Enter the todo list items: "))

    todo = open("todo_items.txt", "a+")

    todo_content = todo.read()

    if todo_content.find(add) != -1:

        print("You already have this on your todo!")

    else:

        try:

            todo.write(add)

            print("Added successfully!")

        except IOError as error:

            print(f"Failed to add, the error is {error}")

        except Exception as Uerror:

            print(f"Unknown error has occured, the error is {Uerror}")

def readTodo():

    todo = open("todo_items.txt", "r")

    try:

        print(f"Your todo items are: {todo.read()}")

    except IOError as error:

        print(f"Cannot read items, the error is: {error}")

    except Exception as Uerror:

        print(f"Unknown error has occured, the error is {Uerror}")

def deleteTodo():

    deleteItem = str(input("Enter the todo item you want to delete: "))

    todo = open("todo_items.txt", "r+")

    if todo.read().find(deleteItem) != -1:

        if platform.system() == "Windows":

            os.system(f"""
                      
                        @echo off
                        setlocal enabledelayedexpansion

                        set "file_path=todo_items.txt"
                        set "string_to_remove={deleteItem}"

                        if not exist "%file_path% (
                            echo File "%file_path% not found.
                            exit /b 1
                        )

                        (
                            for /f "tokens=*" %%a in (%file_path%) do (
                                set "line=%%a"
                                set "line=!line:%string_to_remove%=!"
                                echo !line!
                            )
                        ) > "%file_path%.temp"

                        move /y "%file_path%.temp" "%file_path%"

                        echo Removed "%string_to_remove%" from "%file_path%" successfully!
                      
                    """)
        
        elif platform.system() == "Darwin" or platform.system() == "Linux" or platform.system() == "Linux" and "android" in platform.platform().lower():

            os.system(f"""

                        #!/bin/bash

                        file_path="todo_items.txt"
                        string_to_remove="{deleteItem}"


                        if [ ! -e "$file_path" ]; then
                            echo "File '$file_path' not found."
                            exit 1
                        fi

                        while IFS= read -r line; do
                            line="${{line//\$string_to_remove/}}"
                            echo "$line"
                        done < "$file_path" > "$file_path.temp"

                        mv "$file_path.temp" "$file_path"

                        echo "Removed '$string_to_remove' from '$file_path' successfully!"

                    """)

        '''try:

            todo.seek(0)

            todo.write(todo.read().replace(deleteItem, ''))

            print("Deleted successfully!")

        except IOError as error:

            print(f"Failed to delete, the error is: {error}")

        except Exception as Uerror:

            print(f"Unknown error has occured, the error is {Uerror}")'''

    else:

        print("Cannot find the item to delete")

def clearTodo():

    with open("todo_items.txt", "r+") as todo:

        try:

            todo.truncate(0)

            print("Cleared whole todo successfully!")

        except IOError as error:

            print(f"Cannot clear the todo, the error is {error}")

        except Exception as Uerror:

            print(f"Unknown error has occured, the error is {Uerror}")

def main():

    choice = str(input("Enter what you want to do (add/read/delete/clear): "))

    if choice.lower() == "add" or choice.lower() == "a":

        addTodo()

    elif choice.lower() == "read" or choice.lower() == "r":

        readTodo()

    elif choice.lower() == "delete" or choice.lower() == "d":

        deleteTodo()

    elif choice.lower() == "clear" or choice.lower() == "c":

        prompt = str(input("Are you sure you want to clear your todo? WARNING: THIS IS IRREVERSIBLE: "))

        if prompt.lower() == "yes" or prompt.lower() == "y":

            clearTodo()

        else:

            print("Aborted clearing todo")

    else:

        print("Invalid choice")

if __name__ == "__main__":

    main()
