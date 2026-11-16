tasks = []
while True:
    print("\n--- МЕНЕДЖЕР ЗАДАЧ ---")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Выход")
    print("4. Редактировать задачу")
    choice = input("Выбери действие: ")
    
    if choice == "1":
        title = input("Введите задачу")
        new_task = {"title": title, "done": False}
        tasks.append(new_task)
        print(" Задача добавлена! ")
        
    elif choice == "2":
        if len(tasks) == 0:
            print(" Задачи нет.")
        else:
            for task in tasks:
                print("-", task["title"])
    
    elif choice == "4":
        if len(tasks) == 0:
            print(" Задач нет в списке.")
        else:
            index = 0
            for task in tasks:
                print(index, "-", task["title"])
                index = index + 1
            task_index = int(input("Введи номер задачи: "))
            new_title = input("Введи новый текст: ")
            tasks[task_index]["title"] = new_title
    
    
    elif choice == "3":
        print(" Выход. ")
        break 
    
        