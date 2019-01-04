##
# https://leetcode.com/problems/longest-common-prefix/
# Author: Paul Chang
# LeetCode: 
##

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    if not strs:
        return ""

    prefix = strs[0]
    for elem in strs:
        prefix = get_prefix(prefix, elem)

    return prefix

def get_prefix(old_word,new_word):
    prefix_len = 0
    loop_len = min(len(new_word), len(old_word))
    for i in range(loop_len):
        if( old_word[i] == new_word[i] ):
           prefix_len += 1
        else:
            break
    return old_word[0:prefix_len]

tests = [
    ["flower", "flow", "flight"],
    ["flower", "flow", "floor"],
    ["dog","racecar","car"],
    [],
    ['dog', 'dog']
]

def main():
	for test in tests:
			prefix = longestCommonPrefix(test)
			print(test)
			print('result: ' + prefix)
			print("")

if __name__ == '__main__':
	main()