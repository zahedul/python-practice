student, subject = map(int, input().split())
scores = [map(float, input().split()) for _ in range(subject)]
[print(sum(marks)/subject) for marks in zip(*scores)]