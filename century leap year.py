def ly(y): #ly=Leap year
     if y%4==0 or y%400==0:
          c="this year is a leap year. "
     else :
          c="this year isn't a leap year"
     return(c)

def cly(y): #cly= century before leap year
     for i in range(y-100,y):
          ly(i)
          if ly(i)=="this year is a leap year. ":
               print(i)

     



y=int(input("type a year :"))
print(ly(y))
print(cly(y))

 