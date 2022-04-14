# city=open("question3.txt","r")
# a=city.read()
# print(a)
city=open("question3.txt","r")
for i in city:
    if "delhi" in i:
        city=open("delhi.txt","a")
        city.write(i)
    elif "shimla" in i:
        city=open("shimla.txt","a")
        city.write(i)
    else:
        city=open("other.txt","a")
        city.write(i)
    city.close()







