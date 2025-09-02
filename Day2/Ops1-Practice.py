n = input('Enter Number: ')
print(n)

for i in range(11):
    print(i,end='  ')
print()
st = "Python Developer" 
for i in st:
    print(i,end='')

print()

list = [1,2,3.5,'Hello',4+5j,True,[1,2,3]]
for i in list:
    print(i,end=' ')

print()

tuple = (1,2,3.5,'Hello',4+5j,True,False,"Tuang")
for i in tuple:
    print(i,end=',')

print()


dic = {1:'a',2:'b','c':45}
for	i in dic:
    print(i,end=' ')

#print the 10th table ?

for	i	in range(1,11): 
    r = 10 * i
    print(10 , '*', i, '=', r)

n=int(input("Enter the table number: "))
for	i	in range(1,11): 
    r = n * i
    print(n , '*', i, '=', r)


for i in range(5):
    for j in range(i+1): 
        print(j,end=' ')
    print()

for i in range(5):
    for j in range(i+1): 
        print(,end=' ')
    print()

#FUNCTION



ch = input("Enter a letter: ").lower()
if len(ch) == 1 and ch.isalpha():
    if ch in "aeiou":
        print(f"{ch} is a vowel.")
    else:
        print(f"{ch} is a consonant.")
else:
    print("Please enter a single alphabet letter.")

# My way

character = input("Enter a character: ")
    if character in 'aeiouAEIOU':
        print(f"{character} is a vowel.")
    else:
        print(f"{character} is a consonant.")
      
