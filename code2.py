# k=int(input());

# for i in range (k):
#     a = [int(x) for x in input().split()]
#     start_time=0
    


# paint_list=input().split();
# for i in range(len(paint_list)):
#     paint_list[i]=int(paint_list[i]);

# least = min(paint_list);

# paint_list = [x - least for x in paint_list]

# paint_list+=paint_list;

# li_new = [i for i, element in enumerate(paint_list) if element==0]

# diff=[li_new[i+1]-li_new[i] for i in range(len(li_new)-1)];

# res=least*t+max(diff)-1;
# print(res)

# paint_string="".join([str(item) for item in paint_list])
# print(paint_string)

t=int(input());
numList=input().split();
for i in range(len(numList)):
  numList[i]=int(numList[i]);
largest = max(numList);
smallest = min(numList);
dataLen=2;
res = 0;
res = largest - smallest;
lastDigit = numList[len(numList)-1]
while dataLen != len(numList):
    index=0;
    num = numList[0];
    while index!=len(numList):
        inc=0
        big=0
        small = numList[index];
        while inc!=dataLen:
            if numList[index]>big:
                big=numList[index]
            if numList[index]<small:
                small=numList[index]
            inc=+1;
        res = res + big - small;
        index+=1;
    dataLen+=1;
print(res);
    