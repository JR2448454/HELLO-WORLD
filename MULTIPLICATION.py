def TABLES():
    num = int(input("ENTER THE NUMBER OF WHICH YOU WANT IT'S TABLE :"))
    limit = int(input("TILL WHERE YOU WANT TO FIND IT'S TABLE :"))

    for i in range(1,limit + 1):
        val = num*i
        print(num,'X',i,'=',val)

TABLES()        