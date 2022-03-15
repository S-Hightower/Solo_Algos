# determine how often words appear in a given string or set of strings. Here's a version of this: return a list of duplicate words in a sentence.

# For example, given 'The dog is the best', returns ["the"].

# Likewise, given 'Happy thanksgiving, I am so full', you would return an empty array. This is because there are no duplicates in the string.

# Constraints
#     The total length of the string <= 100000
#     The string will consist of ASCII characters (may be some or all)
#     Expected time complexity : O(n) where n are the number of words in the string
#     Expected space complexity : O(n)


s = "Original String Original String"
# line 16 splits original string into words
split_s = s.lower().split(' ')

occurrences = {}

for word in split_s:
	if word not in occurrences:
		occurrences[word] = 1
	else:
		occurrences[word] += 1

dupes = []
for k in occurrences:
	if occurrences[k] == 2:
		dupes.append(k)

print(dupes)

# output: ['original', 'string']