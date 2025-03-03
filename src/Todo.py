class Todo:
    """
    Creates todo and stores todo in a file called "todo_items.txt"
    """
    @staticmethod
    def addTodo(todo_item: str) -> None:
        """
        Checks if an item is already in todo if not then adds an item into the todo.

        :param todo_item: The todo item to add.
        :type todo_item: str
        """
        todo_content: list[str] = Todo.readTodo()

        with open("todo_items.txt", "a+") as todo:
            if todo_item in todo_content:
                print("You already have this on your todo!")
                return
            
            todo.write(todo_item)
            
        print(f"Added todo item '{todo_item}' successfully.")

    @staticmethod
    def readTodo() -> list[str]:
        """
        Reads the todo file.

        :return: Todo items as a list of strings.
        :rtype: list[str]
        """
        with open("todo_items.txt", "r") as todo:
            return todo.readlines()
    
    @staticmethod
    def deleteTodo(todo_remove: str) -> None:
        """
        Deletes/Removes a selected todo item.

        :param todo_remove: The todo item to remove.
        :type todo_remove: str
        """
        lines: list[str] = Todo.readTodo()
        with open("todo_items.txt", "w") as todo:
            for line in lines:
                if todo_remove.strip() == line.strip():
                    todo.write(line.replace(todo_remove, ""))
                    print(f"Deleted todo item '{todo_remove}' successfully.")
                    return
        print(f"The requested item '{todo_remove}' was not in the file.")

    @staticmethod
    def clearTodo() -> None:
        """
        Clears the whole todo list.
        """
        open("todo_items.txt", "w").close()