#Grade Calculator

import matplotlib.pyplot as plt
import os

directory = "data/submissions"
assignmentIDs = []
grades = []
found = False

print("1. Student grade\n2. Assignment statistics\n3. Assignment graph")
option = int(input("Enter your selection: "))
if option == 1:
    studentName = input("What is the student's name: ")
    with (open("data/students.txt", "r") as studentsList):
        for student in studentsList.readlines():
            if student.strip()[3:] == studentName:
                studentID = student[:3]
                found = True
                for file in os.listdir(directory):
                    with open("data/submissions/" + file, "r") as txt:
                        content = txt.read()
                        if content[:3] == studentID:
                            temp = content[4:].strip()
                            index = temp.index("|")
                            if index != -1:
                                assignmentIDs.append(temp[:index])
                                grades.append(int(temp[index + 1:]))
                for i in range(len(assignmentIDs)):
                    with open("data/assignments.txt", "r") as txt:
                        lines = txt.readlines()
                        for j in range(len(lines) + 1):
                            if lines[j].strip() == assignmentIDs[i]:
                                weight = int(lines[j + 1].strip()) / 100
                                grades[i] *= weight
                                break
                totalGrade = sum(grades) / 10
                print(f"{totalGrade:.0f}%")
    if not(found):
        print("Student not found")

elif option == 2:
    assignmentName = input("What is the assignment name: ")
    with open("data/assignments.txt", "r") as txt:
        lines = txt.readlines()
        for i in range(len(lines)):
            if lines[i].strip() == assignmentName:
                assignmentID = int(lines[i + 1].strip())
                found = True
                for file in os.listdir(directory):
                    with open("data/submissions/" + file, "r") as txt:
                        content = txt.read()
                        stuff = content.split("|")
                        if int(stuff[1]) == assignmentID:
                            grades.append(int(stuff[2]))
                print(grades)
                print(f"Min: {min(grades)}%")
                print(f"Avg: {int(sum(grades) / len(grades))}%")
                print(f"Max: {max(grades)}%")
    if not(found):
        print("Assignment not found")

elif option == 3:
    assignmentName = input("What is the assignment name: ")
    with open("data/assignments.txt", "r") as txt:
        lines = txt.readlines()
        for i in range(len(lines)):
            if lines[i].strip() == assignmentName:
                assignmentID = int(lines[i + 1].strip())
                found = True
                for file in os.listdir(directory):
                    with open("data/submissions/" + file, "r") as txt:
                        content = txt.read()
                        stuff = content.split("|")
                        if int(stuff[1]) == assignmentID:
                            grades.append(int(stuff[2]))
                plt.hist(grades, bins = range(50, 101, 5), color = "g", edgecolor = "w")
                plt.show()
    if not(found):
        print("Assignment not found")