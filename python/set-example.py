"""input = ['not', 'hashable']
hash(input)"""

firstSet = {'NV', 'AK', 'CO', 'TN', 'NV', 'NY'}      
secondSet = set('zzyzx') 

print(f"First set: {firstSet}")
print(f"Second set: {secondSet}")

emptyDict = {}
emptySet = set()

print(type(emptyDict)) # <class 'dict'>
print(type(emptySet))  # <class 'set'>