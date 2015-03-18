from django.test import TestCase

# Create your tests here.

strs='32671'

for i in range(0,len(strs)):
    aa=''
    for k in range(i+1,len(strs)):
        aa+=strs[k]

    print strs[i],aa