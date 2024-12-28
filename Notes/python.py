# Strings: are immutable

s1 = "String1"
s2 = "String2"
s3 = """Multiline 
String3"""
print(s3)
print(s3[1]) #u
print(s3[-1]) #last index value = 3

# s3[0] = "C": Not a valid operation as String are immutable.
print(s3[:3]) # slicing from 0 to 2

del s1 # deleting String
print(len(s3))

s2 = s2.replace("String2", "String2 replaced")
print(s2)

s2.strip() # removes leading and trailing whitespaces
s4 = s2+s3 # concatenation

print("Hello "*3) # Hello Hello Hello