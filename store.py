import pack

# - initial date
ini_year = 2024
ini_month = 1
ini_date = 13

# - Main function zone
f = open("test.txt","r")
date,month,year=pack.get_date(f)
f.seek(0)
new_coin,curr_coin=pack.get_coin(f)
curr_coin=curr_coin+new_coin
f.close()

g = open("test.txt","a")
pack.write_date(g,date,month,year)
pack.write_coin(g,new_coin,curr_coin)
pack.end_line(g)
g.close()