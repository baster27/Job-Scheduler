from datetime import datetime
from BST import BST, Node

def getJobInputDetails():
    startTime = input("Enter the time in hh:mm format, example 14:30 or 2:30 -> ")
    while True:
        try:
            datetime.strptime(startTime, '%H:%M')
        except ValueError:
            print("Incorrect time format, should be hh:mm")
            startTime = input("Enter the time in hh:mm format, example 14:30 or 2:30 -> ")
        else:
            break
    durationOfJob = input("Enter the duration of the job in minutes, example 60 -> ")
    while True:
        try:
            int(durationOfJob)
        except ValueError:
            print("Please enter a number for number of  minutes")
            durationOfJob = input("Enter the duration of the job in minutes, example 60 -> ")
        else:
            break
    jobName = input("Enter the name of the job (case sensitive) -> ")
    return startTime, durationOfJob, jobName
myTree = BST()

with open('data.txt') as f:
    for line in f:
        myTree.insert(line)

while True:
    print("Please choose an option from the list below:")
    print("Press 1 to view today's scheduled jobs")
    print("Press 2 to add a job to today's sccedule")
    print("Press 3 to remove a job from the schedule")
    print("Press 4 to quit")
    selection = input("Enter your choice ->")
    try:
        entry = int(selection)
    except ValueError:
        print("Please enter a number between 1 and 4")
        continue
    if int(selection) == 1:
        myTree.inOrder()
    elif int(selection) == 2:
        print("You have chosen to add a job to the schedule")
        startTime, durationOfJob, jobName = getJobInputDetails()
        line = startTime + "," + durationOfJob + "," + jobName
        num = myTree.length()
        myTree.insert(line)
        if num == myTree.length() - 1:
            with open("data.txt", "a+") as toWrite:
                toWrite.write(line + '\n')
        input("Press any key to continue... ")
    elif int(selection) == 3:
        print("You have chosen to remove a job from the schedule")
        startTime, durationOfJob, jobName = getJobInputDetails()
        keyToFind = datetime.strptime(startTime, '%H:%M').time()
        result = myTree.findVal(keyToFind)
        if result:
            if result.nameOfJob == jobName and result.duration == durationOfJob:
                print("Removing job:")
                print(result)
                myTree.deleteVal(keyToFind)
                print("Job successfully removed")
                with open('data.txt','r') as f:
                    lines = f.readlines()
                with open('data.txt','w') as f:
                    for line in lines:
                        if line.strip("\n") != startTime + ',' + durationOfJob + ',' + jobName:
                            f.write(line)
                input("Press any key to continue... ")
            else:
                print("The name and or duration of job did not match, delete failed")
                input("Press any key to continue... ")
        else:
            print("Job not found")
            input("Press any key to continue... ")
    elif int(selection) == 4:
        print("Exiting program...")
        break
    else:
        print("Please enter a number between 1 and 4")
