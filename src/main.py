from Todo import Todo

def main() -> None:
    isRunning: bool = True

    while isRunning:
        choice: str = input("Enter your choice (add, read, delete, clear or exit): ").strip().lower()

        match choice:
            case "add" | "a":
                todo_item: str = input("Enter the todo item to add: ")
                Todo.addTodo(todo_item)
            
            case "read" | "r":
                allTodo: list[str] = Todo.readTodo()
                print(f"All todo items are: {allTodo}")
            
            case "delete" | "d":
                todo_remove: str = input("Enter the todo item to remove: ")
                Todo.deleteTodo(todo_remove)
                
            case "clear" | "c":
                Todo.clearTodo()
                print("Removed all todo items successfully.")
            
            case "exit" | "e":
                isRunning = False
                print("Exiting...")

            case _:
                print("Invalid choice")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")