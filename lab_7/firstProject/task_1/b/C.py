def check_answer(correct_answer, student_answer):
    if correct_answer == student_answer:
        return "YES"
    else:
        return "NO"

# Input
correct_answer = int(input())
student_answer = int(input())

# Check if the student's answer is correct
result = check_answer(correct_answer, student_answer)
print(result)
