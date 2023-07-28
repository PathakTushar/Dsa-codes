import math
t=int(input())
for i in range(t):
    n=int(input())
    if n%2==0:
        print(n//2,'',1)
    else:
        print(-1)


# import math
# t=int(input())
# for i in range(t):
#     h=input().split();
#     h=[int(i) for i in h]
#     n=h[0]
#     s=h[1]
#     r=h[2]
#     extra = s-r
#     repeat = math.floor(r/(n-1))
#     left=r%(n-1)
#     mylist = [repeat]*(n-1)
#     mylist.append(extra)
#     for i in range(left):
#         mylist[i]+=1
#     print(*mylist)
    


# piValue="314159265358979323846264338327"
# t=int(input())
# for i in range(t):
#     n=input()
#     res=0
#     while res < len(n):
#         if n[res]!=piValue[res]:
#             break
#         else:
#             res+=1
#     print(res)



# t=int(input())
# for i in range(t):
#     n=int(input())
#     h=input().split();
#     h=[int(i) for i in h]
#     noOfOne = h.count(1);
#     temp = math.ceil(noOfOne/2);
#     print(n-noOfOne+temp);


# def Log2(x):
# 	return (math.log10(x) /
# 			math.log10(2));

# def isPowerOfTwo(n):
# 	return (math.ceil(Log2(n)) == math.floor(Log2(n)));

# t= int(input())
# for i in range(t):
#     n=int(input());
#     if isPowerOfTwo(n):
#         print("NO");
#     else:
#         print("YES");

