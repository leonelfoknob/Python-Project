
s1 = int(input("enter first number"))
s2= int(input("enter second number"))
t = s1+s2
c=s1-s2
d=s1/s2
c1=s1*s2

Myfile = open('leo_file.txt','w+')
Myfile.write('my first file with python')
Myfile.write('\nMakinaFleo The best')
Myfile.write('\n'+'toplam :'+ str(t))
Myfile.write('\n'+'cikartma :'+ str(c))
Myfile.write('\n'+'bolme :'+ str(d))
Myfile.write('\n'+'carpma :'+ str(c1))
Myfile.close()