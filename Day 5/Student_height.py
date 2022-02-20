student_height = input("Input a list of student height ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

sum = 0
count = 0

for i in student_height:
    sum += i
    count += 1

print(sum / count)