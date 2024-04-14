# students = ["noob", "pro", "harry"]

# # for student in students:
# #     print(student)

# # for i in range(len(students)):
# #     print(i + 1, students[i])

# houses = ["blr","blr","mlr"]

# students = {
#     "noob" : "blr",
#     "pro" : "blr",
#     "harry": "mlr",
# }


# # print(students["noob"])

# for student in students:
#     print(student, students[student], sep = ", ")

students =[
    {
        "name" : "Sandy",
        "house" : "blr",
        "game" : "FF",
    },
    {
        "name" : "yooo",
        "house" : "blr",
        "game" : "FF",
    },
    {
        "name" : "Sandy",
        "house" : "mlr",
        "game" : "pubg",
    },
     ]
    
for student in students:
    print(student["name"],student["house"],student["game"],sep = ", ")