Str1="hello ,how, r, u"
print(Str1[-0])
print("-1"*70)
print('el' in 'Hello')
print('Hello ' in 'Hello')
print(Str1.upper())
print(Str1.isalpha())
print(Str1.isalphanum())


print(Str1.split("':'"))#


partition function check
len,rstrip,partition,str,chr,ord,index etc
write a pgm to split at the following \,\\ ,blank space
diff between split and partition funs

"""Console input and output"""
a=input("enter  first no:")
b=input("enter  second no:")
c=a+b
print(c)
c=int()
c=int(a)+int(b)
print(c)
print(type(a))
Hw:
    How to convert a string to an integer: ASCII concept I think
a,b=input("enter a and b").split('')
print(a+b)
c=int(a)+int(b)
print(c)

a,b=input("enter  a and b with : seperator").split(":")
print(a+b)
name,department,semester,cgpa=input("enter nname dept semester cgpa").split()
print("name\t: department\t:semester\t:cgpa\t",name,department,semester,cgpa)
bio=input("enter nname dept semester cgpa").split()
print("name\t",bio[0]+"\tdept\t",bio[1])

bio=input("enter nname dept semester cgpa").split()
print("name\t",bio[0],end="\t")
print("dept\t",bio[1],end="\t")
print("sem\t",bio[2],end="\t")
print("cgpa\t",bio[3],end="\t")


"""Output statement"""
What are the various escape seque..emply in the print statement