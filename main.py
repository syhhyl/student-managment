from student import StuManSys
import os

def clear_screen():
    os.system("cls")

def welcome():
    while True:
        clear_screen()
        print("------------------------")
        print("|欢迎来到学生信息管理系统|")
        print("------------------------")

        print("[1]start\n[0]quit")
        
        try:
            choice = int(input("请输入:"))
            if choice == 0:
                break
            elif choice == 1:
                #clear_screen()
                status = main()
                if status == 0:
                    break
        except:
            print("输入格式错误~~~")
    print("期待与您再次相见~~~")


def main():

    oper = ''
    sms = StuManSys()
    while True:
        num_of_stu = len(sms.students)
        print("[a]:添加学生\n[r]:移除学生\n[p]:显示学生信息\n[s]:查找学生\n[w]:写入数据\n[q]:退出")

        oper = input("请输入:")
        if oper == 'a' or oper == 'A':
            clear_screen()
            sms.add_student(input("name:"), input("num:"), input("age:"), input("sex:"))
        elif oper == 'r' or oper == 'R':
            if num_of_stu == 0:
                print("没有数据~~~")
                continue
            clear_screen()
            sms.remove_student(input("name:"), input("num:"))
        elif oper == 's' or oper == 'S':
            if num_of_stu == 0:
                print("没有数据~~~")
                continue
            clear_screen()
            sms.search_student(input("请输入学号:"))
            print()
        elif oper == 'p' or oper == 'P':
            if num_of_stu == 0:
                print("没有数据~~~")
                continue
            clear_screen()
            sms.display_students()
            print()
        elif oper == 'q' or oper == 'Q':
            return 0
        elif oper == 'w' or oper == 'W':
            with open("students.txt", "w") as file:
                for stu in sms.students:
                    file.write(stu.name+","+stu.num+","+stu.age+","+stu.sex+"\n")
            print("写入成功~~~")
        else:
            print("输入格式错误~~~")


if __name__ == "__main__":
    welcome()


