"""
https://www.hackerrank.com/challenges/grading/problem
"""
def next_multiple_of5(g):
    return g + (5-g%5)

def check_rounding_eligiblity(grade,next_mulitple_of5):
    return (next_mulitple_of5 - grade) < 3

def round_grades(grades):
    print("{}".format(grades))
    rounded_grades = []
    for g in grades:
        if g <38:
            rounded_grades.append(g)
        else:
            y = next_multiple_of5(g)
            if check_rounding_eligiblity(g,y):
                rounded_grades.append(y)
            else:
                rounded_grades.append(g)
    return rounded_grades



if __name__ =="__main__":
    grades = [73,67,38,33]
    print(round_grades(grades=grades))
