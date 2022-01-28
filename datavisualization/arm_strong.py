# n=input('Enter the arm strong number')
n=153
nom=153
arm_st=str(n)
print(arm_st[1])
len_nth=len(arm_st)
sum=0
for i in range(len_nth):
    sum+=int(arm_st[i])**len_nth
    print(i)
    # digit=nom%10
    # print('dig',digit)
    # nom=nom//10
    # print('nom',nom)
if n==sum:
    print('this is armstrong number')
else:
    print('this is armstrong number')
print(sum)
# print('ano',150%10)
