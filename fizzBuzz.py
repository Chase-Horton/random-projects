#prints fizzBuzz with obfuscation

end = "".join([dir(str)[-1][0] 
for x in range(2)])

word = "".join([(0.5.__class__.__name__[0]),
 (9).__class__.__name__[0], end])

word += "".join([True.__class__.__name__[0].upper() + 
().__class__.__name__[1], end])

print(word)

# Explanation
# dir returns all methods for class 
# z is taken from str method zfill
# __class__.__name__ returns the name of the 
# class of the object it is attached to
# classes used are float, int, bool, and tuple