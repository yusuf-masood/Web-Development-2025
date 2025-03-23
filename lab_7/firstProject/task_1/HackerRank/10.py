if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Sort the students list based on scores
    students.sort(key=lambda x: x[1])

    # Find the second lowest grade
    second_lowest_score = None
    for i in range(1, len(students)):
        if students[i][1] > students[0][1]:
            second_lowest_score = students[i][1]
            break

    # Print the names of students with the second lowest grade
    for student in students:
        if student[1] == second_lowest_score:
            print(student[0])
