import re

# - useful function zone
def get_date(file):
    i = 1
    lines = file.readlines()
    date_line = lines[-3].strip()
    date_list = date_line.split("/")
    for date in date_list:
        if i==1:
            i+=1
            c = int(date)
        elif i==2:
            i+=1
            b = int(date)
        elif i==3:
            a = int(date)   
    a+=1
    if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
        if a==32:
            a=1
            b+=1
            if b==13:
                b=1
                c+=1
                return a,b,c
            else:
                return a,b,c
        else:
            return a,b,c
    elif b==4 or b==6 or b==9 or b==11:
        if a==31:
            a=1
            b+=1
            return a,b,c
        else:
            return a,b,c
    elif b==2:
        if a==29:
            a=1
            b+=1
            return a,b,c
        else:
            return a,b,c

def get_coin(file):
    new_coin = int(input("今天你get了多少金币？"))
    lines = file.readlines()
    coin_line = lines[-2].strip()
    numbers = re.findall(r'\d+',coin_line)
    numbers = [int(num) for num in numbers]
    curr_coin = numbers[1]
    return new_coin,curr_coin
    
def write_date(file,a,b,c):
    file.write("\n")
    file.write(str(c))
    file.write("/")
    file.write(str(b))
    file.write("/")
    file.write(str(a))
    file.write("\n")

def write_coin(file,new_coin,curr_coin):
    file.write("Coins+= ")
    file.write(str(new_coin))
    file.write(" Coins= ")
    file.write(str(curr_coin))
    file.write("\n")
    
def end_line(file):
    file.write("-----------------------------")
  