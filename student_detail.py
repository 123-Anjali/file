obj=open("student.text","w")
for i in range(5):
    name=input("enter your name:")
    obj.write(name)
    obj.write("\n")
obj.close()