#At the start of the day you have a checklist The tasks which you were able to finish, should get added to completed_tasks The tasks 
#which you were not able to finish, should get added to incomplete_tasks This project is about organizing your daily tasks into
#two categories: completed tasks and incomplete tasks. Here’s how it works: 1. At the start of the day, you create a checklist of tasks you 
#want to accomplish. 2. At the end of the day, you review which tasks you could finish and which you couldn’t. – If a task is finished, you
#move it to the completed tasks list. – If a task is not finished, you move it to the incomplete tasks list. This way, by the end of each day, 
#you'll have a clear overview of what you completed and what still needs attention.

def main():
    tasklist=[]
    complete_task=[]
    incomplete_task=[]

    n=int(input("how many task you want to add for today ? : "))

    for i in range(n):
        task=input("enter task" + str(i+1) + ": ")
        tasklist.append(task)

    print("your tasks for today : ")
    for i in range(len(tasklist)):
        print(str(i+1) + ". "+ tasklist[i])

    print("\n Now let's review your tasks.")
    for task in tasklist:
        status=input("did you complete ' " + task + " ' ? (yes/no) : ")
        if status=="yes" or status=="Yes":
            complete_task.append(task)
        else:
            incomplete_task.append(task)

    print("\n***** summary of the Day *****")
    print("\ncompleted Tasks : ")
    if len(complete_task)>0:
        for t in complete_task:
            print(" - " + t)
    else:
        print("No tasks completed today.")

    print("\nIncompleted Tasks : ")
    if len(incomplete_task)>0:
        for t in incomplete_task:
            print(" - " + t)
    else:
        print("No tasks completed today.")

main()