# https://leetcode.com/problems/longest-common-prefix/
# 14

def lengthOfLongestSubstring(s):
	"""
	:type s: str
	:rtype: int
	"""
	finalSubStr=""
	finalCnt=0

	while (len(s) != 0):
			#print(s)
			tmpSubstr=""
			tmpCnt=0
			# loop over the string
			for c in s:
					if c not in tmpSubstr:
							tmpSubstr += c
							tmpCnt += 1
					else:
							break
			#
			#print(tmpCnt," ", tmpSubstr)

			if tmpCnt > finalCnt:
					finalCnt = tmpCnt
					finalSubstr = tmpSubstr

			s = s[1:]

	return finalCnt

def main():
	tests = [
			"abcabcbb",
			"bbbbb",
			"pwwkew"
			]
			
	for test in tests:
			length = lengthOfLongestSubstring(test)
			print(test)
			print('result: ', length)
			print("")

if __name__ == '__main__':
	main()
