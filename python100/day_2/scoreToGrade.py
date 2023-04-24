score = float(input('Enter the scores: '))

def score_to_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80 and score < 90:
        grade = 'B'
    elif score >= 70 and score < 80:
        grade = 'C'
    elif score >= 60 and score < 70:
        grade = 'D'
    else:
        grade = 'E'
    return grade

result = score_to_grade(score)
print(f'Your grade is {result}.')
