def pyr6():
    print("input list of nums")
    nums = list(map(int, input().split()))
    nums2 = []
    for i in range(len(nums)):
        print(str(nums[i]).zfill(3), end=" ")
    print()
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            nums2.append(nums[j]+nums[j+1])
            print(str(nums2[-1]).zfill(3), end=" ")
        print("")
        # print(str(nums2))
        nums = nums2
        nums2 = []

pyr6()