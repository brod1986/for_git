#based on number given print an ascending, then descending star pattern

user_num = int(input("How any stars would you like in largest row?\n:"))

#I need to increase the range by 2 so the program can iterate enough times
rows = range(user_num * 2)

for i in rows:

    #variables used for printing, decrease needs +1 to account for 0 in range
    star_increase = i
    star_decrease = int(rows[-1]+1)

#logic to print the increasing pattern
    if star_increase <= user_num:
        print("*" * i)

#logic to print decreasing pattern
    else:
        print((star_decrease - i) * "*")
print("End of program")
