s="vaishnavi patil"

# 0=v,1=a,2i,3s,4h,5n,6a,7v,8i,9,10p,11a,12t,13i,14l

s1=s[0:9]
print(s1)

s2=s[-5:]
print(s2) 

s3=s[ : :1]
print(s3)

s4=s[0:9:2]
print(s4)

# find total number of a in full name
count=0
for char in s:
    if char == "a":
        count=count+1

print(f"total number of char a in {s} =",count)      

i=0
for char in s:
  print(i,"--->",char)
  i=i+1

print(s[ :6])

print(s[10:])

print(s[ : ])

print(s[::-1])

print(s[-1: :-2])

print(s[6:1:-1])

print(s[1:2])

print(s[10:15:1])

print(s[-6::-1])

print(s[-1:-5])










