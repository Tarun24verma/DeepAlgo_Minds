nums = [-2,1,-3,4,-1,2,1,-5,4]
#expected output: [4,-1,2,1]
new=[]
for i in range(len(nums)):
    j=0
    t=0
    if nums[i]<0:
        if i!=0:
            if nums[i-1]<0:
                continue
        while nums[i]<0:
            # print("num",nums[i])
            t+=nums[i]
            # print('t=',t)
            i+=1
        new.append(t)
            
    else:
        if i!=0:
            if nums[i-1]>0:
                continue
        while nums[i]>0:
            # print("num",nums[i])
            t+=nums[i]
            # print('t=',t)
            i+=1
            if i>len(nums)-1:
                break
        new.append(t)
print(new)
