# text = "Возвращает значение True или False, указывающее на то, содержит ли строка символы только верхнего регистра."
# text_split = text.split()
# text_sorted = sorted(text_split, key=len)
# result = " ".join(text_sorted)
# print(result)

x = int(input("enter first number:"))
y = int(input("enter second number:"))
print(x % 2 == 0 and y % 2 == 0)

student_score = int(input("enter your score: "))
if student_score < 25:
    print("F")
elif 25 <= student_score < 45:
    print("E")
elif 25 <= student_score < 50:
    print("D")
elif 50 <= student_score < 60:
    print("C")
elif 60 <= student_score < 80:
    print("B")
elif student_score >= 80:
    print("A")
else:
    print("error")
