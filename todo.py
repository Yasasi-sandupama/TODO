def show_menu():
    print("\n"+"="*30)
    print("MY TO DO LIST")
    print("="*30)
    print("1. View all tasks")
    print("2.add new task")
    print("3.make if the task is completed")
    print("4.delete a task")
    print("5.exit")
    print("="*30)

    def main():
        print("Welcome to the TO DO LIST APP!")
        tasks=[]
        while True:
            show_menu()
            choice = input("Enter your choice(1-5):")
            if choice == "1":
                view_tasks(tasks)    
            elif choice == "2":
                add_task(tasks)
            elif choice =="3":
                mark_done(tasks)
            elif choice =="4":
                delete_task(tasks)
            elif choice == "5":
                print("Bye Bye cutie pie! see you later!")
                break
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()


    