intList=[y for y in range (0,11)]+([x*(-1) for x in range(11,16)])
print (intList,'\nCount of pos. numbers',len(intList[:10]),'\nSum of negative numbers',sum(intList[11:16]))