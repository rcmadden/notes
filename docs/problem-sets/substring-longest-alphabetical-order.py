# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh

# Strategy 1

# input2 s = 'baabc'
# output = 'abc'
# longestString = ''

# For each letter in s                                     / a                   // b      /// a     //// b      5 c
# 	while the current letter is < the next letter          / true                // false  /// true  //// true   5 false
# 		keep track of the letters so far as currentString  / currenString = 'ab' // 'ab'   /// 'ab'  //// 'abc'
# 	if currentString length > longestString length         / true                          /// false //// true
# 		longestString = currentString                      / longestString = 'ab' // 'ab'  /// 'ab'  //// 'abc'
# print('Longest substring is: ' + longestString)

s = 'baabc'
nextLetter = 0
currentString = ''
longestString = ''
# For each letter in s 
for letter in s:
# 	while the current letter is < the next letter
    nextLetter += 1
    if (nextLetter <= len(s)-1) and (letter < s[nextLetter]):
    # 	keep track of the letters so far as currentString
        if nextLetter <= 3:
            currentString = currentString + letter + s[nextLetter]
        else: 
            currentString = currentString + s[nextLetter]
	# if currentString length > longestString length:
    if len(currentString) > len(longestString):
        longestString = currentString
        currentString = ''
print('Longest substring is: ' + longestString)


# Strategy 2 using Guess and check?
# s = 'ababc'

# letters = enumerate(s)  
# for letter in letters: