# Input with forced capilization for dictionary purposes
romanNumber = input().upper()

# Processing
#dictionary building
romanToInt = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}
#immediately creating a list and populating it with integer values (for each numeral in input string)
integerValue = [romanToInt[x] for x in romanNumber]
#setting some base values
result = 0
##this if statement is my catch case for numerals ending in multiple 1s or a single 1.
if integerValue[-1] == 1:
    result += 1
num=0
#while loop
##while the number is in range between 0 and the end of the list is will perform these functions inside it
while num in range(0, len(integerValue)-1):
    ##if the int values beside each other are equal, add it to the total, move on
    if integerValue[num] == integerValue[num+1]:
        result += integerValue[num]
        num += 1
    ##if the int value on the right is greater, subtract the one in front. c
    elif integerValue[num] < integerValue[num+1]:
        result -= integerValue[num]
        result += integerValue[num+1]
        num += 2
    else:
        result += integerValue[num]
        num += 1
###could not get last digit 1s to add onto total. was a trend, at least with visible test 0 and 2
#print statements for string and variable names
print('Roman Number:', romanNumber)
print('Hindu-Arabic:', result)