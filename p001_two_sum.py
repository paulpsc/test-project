##
# Two Sum
# Author: Paul Chang
# LeetCode: https://leetcode.com/problems/two-sum/
##

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}
    for i, e_i in enumerate(nums):
        #TODO check if target-e_i is in seen
        ref = target - e_i
        if( ref in seen ):
            return [i, seen[ref]]
        seen[e_i] = i

def main():
    tests = [
        ([1, 4, 5, 6], 9),
        ([4, 1, 5],    5)
    ]

    for test in tests:
        print(test)
        print("Result:   %s" % twoSum(test[0], test[1]))
        print("")

if __name__ == '__main__':
    main()