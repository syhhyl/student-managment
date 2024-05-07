import os

class Student:
    def __init__(self, name, num, age, sex):
        self.name = name
        self.num = num
        self.age = age
        self.sex = sex

class StuManSys:
    def __init__(self):
        from file import file_open
        self.students = file_open()


    def add_student(self, name, num, age, sex):
        student = Student(name, num, age, sex)
        self.students.append(student)
        print(f"学生:{name} 添加成功~~~")

    def remove_student(self, name, num):
        for student in self.students:
            if student.num == num:
                self.students.remove(student)
                #print(f"姓名: {student.name}, 学号: {student.num}, 年龄: {student.age}, 性别: {student.sex} 移除成功~~~")
                print("移除成功~~~")
                return
        printf("未找到此学生~~~")

    def display_students(self):
        if not self.students:
            print("没有数据~~~")
            return
        print("学生信息如下~~~")
        print("姓名\t学号\t年龄\t性别\t")
        for student in self.students:
            print(f"{student.name}\t{student.num}\t{student.age}\t{student.sex}")

    def search_student(self, num):
        for student in self.students:
            if student.num == num:
                print(f"姓名: {student.name}, 学号: {student.num}, 年龄: {student.age}, 性别: {student.sex}")
                return
        print("未找到此学生~~~")


def file_open():
    stu_list = []
    if os.path.exists("students.txt"):
        print("检测到students文件，开始读取~~~")
        #读取每行
        with open("students.txt", "r") as file:
            for line in file:
                stu_info = line.strip().split(",")
                #print(stu_info)
                stu_list.append(Student(stu_info[0], stu_info[1], stu_info[2], stu_info[3]))
        print("读取完毕~~~")
    else:
        print("未检测到students文件，创建成功~~~")
    return stu_list