file1=open('Book1.txt')
file2=open('Book2.txt')
file3=open('Book3.txt')
l = file1.readlines()
l1= file2.readlines()
l2= file3.readlines()
string = l[0]
stringsplit = string.split()
file1 = []
   for i in stringsplit:
   file1.append(len(i))
   e = max(file1)
   for j in stringsplit:
     if len(j) == e:
 print("The longest word is", j, "and it is", len(j),"characters long")
