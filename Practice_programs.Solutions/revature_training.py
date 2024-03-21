for i in range(2000,3201):    #1
  if i%7==0 and i%5!=0:
    print(i,end=",")

num=int(input())          #2
dictionary={}
for i in range(1,num+1):
  dictionary[i]=i**2
print(dictionary)

val=input().split(",")    #3
print(list(val))
print(tuple(val))


class Strings:          #4
  def __init__(self):
    self.name=""
  def get_string(self):
    self.name=input()
  def print_string(self):
    print(self.name.upper())
test=Strings()
test.get_string()
test.print_string()


words=input().split(",")    #5
words.sort()
words


My_message=input().split(" ")     #6
My_message.sort()
print(My_message)
final_result=set(My_message)
for i in final_result:
  print(i,end=" ")


import re       #7
for i in range(1000,3001):
  if re.search(r'^[02468]+$', str(i)):
        print(str(i),end=" ")


check_case=input("Enter the sentence:")     #8
upper_case=[]
lower_case=[]
for letter in check_case:
  if letter.isupper():
    upper_case.append(letter)
  elif letter.islower():
    lower_case.append(letter)
print("UPPER CASE:",len(upper_case))
print("LOWER CASE:",len(lower_case))


import re         #9
psds = input("Enter passwords: ").split(",")
def valid_password(password):
    format = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,12}$"
    if re.match(format, password):
        return True
    else:
        return False
def print_valid_passwords(psds):
    valid_passwords = [password for password in psds if valid_password(password)]
    print(",".join(valid_passwords))
print_valid_passwords(psds)
