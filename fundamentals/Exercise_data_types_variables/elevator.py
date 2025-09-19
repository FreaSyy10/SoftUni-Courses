from math import ceil
people_for_elevator=int(input())
max_space_elevator=int(input())

total_courses=ceil(people_for_elevator / max_space_elevator)

print(total_courses)

