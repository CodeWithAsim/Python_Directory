f=open("D:\\Python_Code\\file_handling\\myself.txt","r")
f2=open("D:\\Python_Code\\file_handling\\file2.txt","w")

#print(f.read())

for line in f:
    tokens = line.split(' ')
    #lst_into_str=str(tokens)
    words = len(tokens)
    #print(tokens)
    print("Word count is : ",str(words),line)
    wrt="Word count is : "+str(words)+" "+line
    f2.write(wrt)

f.close()
f2.close()
