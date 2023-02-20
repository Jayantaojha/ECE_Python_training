class Test:
    def main():
        a = str(input("Enter your first name --> "))
        b = str(input("Enter your last name --> "))
        c = a +" " +b
        print("Your name -> ", c)
    def main_2():
        a = str(input("Enter your school name: "))
        b = str(input("Enter your first name: "))
        c = str(input("Enter your last name: "))
        d = str(input("Enter your class: "))
        final_str = "My name is {1} {2}. I study in {0} school. I am in class {3}"
        print(final_str.format(a,b,c,d))


# Test.main()
# print("\n")
# Test.main_2()


object_sit = Test
object_sit.main()
print("\n")
object_sit.main_2()
