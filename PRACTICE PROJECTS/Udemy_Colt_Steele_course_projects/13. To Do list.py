
# task = input("What would you like to do today? ")
#
# to_do.append(task)
#
# print(f'Added! Your task {task} has been added to your To Do List!')
#
# count = 0
# for tasks in to_do:
#     print(f'{count}. {tasks}')
#     count += 1

to_do = []
completed_tasks = []

while True:
    # this keeps going until we decide to quit
    task = input("What would you like to do today? (Type 'q' to quit): ")

    if task == "q":
        break
    elif task.isnumeric():
        # this is checking if the INPUT for TASK was a NUMBER or NOT
        num = int(task)-1
        # This converts the STRING from TASK to be an INT
        # I added the -1 here so that I wouldn't have to repeat myself later on
        if num >= len(to_do):
            print('That task does not exist!')
        else:
            done_to_do = to_do.pop(num)
            completed_tasks.append(done_to_do)

            # to_do.pop(num-1)
    #     THEN .pop will TAKE OUT NUM - 1 from the list
    #       I later took this out because it would be taking out TWO things instead of one

    else:
        to_do.append(task)
        print(f'Your task {task} has been added!')

    print(f'Current list:')
    count = 1
    for item in to_do:
        print(f'{count}. {item}')
        count += 1
if completed_tasks:
    count_up = 1
    print('Completed tasks today:')
    for task in completed_tasks:
        print(f'{count_up}.{task}')
        count_up += 1