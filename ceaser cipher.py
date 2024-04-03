def enc(text,key):
    c=''
    for i in text:
        if i.isupper():
            c=c+chr((ord(i)+k-65)%26+65)
        elif i.islower():
            c=c+chr((ord(i)+k-97)%26+97)
        else:
            c=c+i
    return c
ptext=input("enter a plaintext: ")
k=int(input("enter the key value: "))
ptext=enc(ptext,k)
print("the cipher text: ",ptext)
