from django.test import TestCase

# Create your tests here.

# strs='32671'
#
# for i in range(0,len(strs)):
# aa=''
#     for k in range(i+1,len(strs)):
#         aa+=strs[k]
#
#     print strs[i],aa


strs = 'abdaeabef'
lists = []
for i in range(0, len(strs)):
    if not strs[i] in lists:
        lists.append(strs[i])
print lists