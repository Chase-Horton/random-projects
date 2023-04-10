#pasted program (original was a jupyter notebook)
def convertToBinary(s):
  binaryString = "1"
  for letter in s:
    if(letter == "!"):
      binaryString += "1"
    else:
      binaryString += "0"
  return binaryString


def binaryToDecimal(binary):
  return int(binary, 2)
def decimalToBinary(decimal):
  return bin(int(decimal)).replace("0b", "")



def programToDecimal(prog):
  binary = convertToBinary(prog)
  dec = binary(binary)
  return dec
def numberToProgram(number):
  binary = decimalToBinary(number)
  binary = binary[1:]
  prog = ""
  for n in binary:
    if n == "1":
      prog += "!"
    else:
      prog += "?"
  return prog


base = 1200000
def val(c):
    if c >= '0' and c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10
 
# Function to convert a number
# from given base 'b' to decimal
def toDeci(str,base):
    llen = len(str)
    power = 1 #Initialize power of base
    num = 0     #Initialize result
 
    # Decimal equivalent is str[len-1]*1 +
    # str[len-2]*base + str[len-3]*(base^2) + ...
    for i in range(llen - 1, -1, -1):
         
        # A digit in input number must
        # be less than number's base
        if val(str[i]) >= base:
            print('Invalid Number')
            return -1
        num += val(str[i]) * power
        power = power * base
    return num
def reVal(num):

  if (num >= 0 and num <= 9):
      return chr(num + ord('0'))
  else:
      return chr(num - 10 + ord('A'))
 
# Utility function to reverse a string
def strev(str):
 
    len = len(str)
    for i in range(int(len / 2)):
        temp = str[i]
        str[i] = str[len - i - 1]
        str[len - i - 1] = temp
 
# Function to convert a given decimal
# number to a base 'base' and
def fromDeci(res, base, inputNum):
 
    index = 0; # Initialize index of result
 
    # Convert input number is given base
    # by repeatedly dividing it by base
    # and taking remainder
    while (inputNum > 0):
        res+= reVal(inputNum % base)
        inputNum = int(inputNum // base)
 
    # Reverse the result
    res = res[::-1]
 
    return res
 
# Driver Code
import time
DEVEL = False
class discoids:
  def __init__(self, numOfMemDials, startMemIndex, startOpIndex, rotateMemAmt, rotateOpAmt, indexA, indexB):
    self.opDial = [self.increment, self.push, self.inputMem, self.startWhile, self.sumAB, self.outputTop, self.shift, self.decrement, self.endWhile, self.forget, self.pop, self.clr, self.inputStack]
    self.memory = 0
    self.stack = []
    self.opIndex = startOpIndex
    self.startOpIndex = startOpIndex

    self.rotateOpAmt = rotateOpAmt

    self.progIndex = 0
  def getMem(self):
    return self.memory
  def getOp(self):
    return self.opDial[self.opIndex]
  def rotateOp(self, i=1):
    self.opIndex += self.rotateOpAmt*i
    if(self.opIndex >= len(self.opDial)):
      self.opIndex = 0
    elif(self.opIndex < 0):
      self.opIndex = len(self.opDial) -1
    if(DEVEL): print('\033[94mrotating op dial: ' + self.opDial[self.opIndex].__name__ + '\033[92m')
  #operations
  def increment(self):
    if(DEVEL): print('\033[92mincrementing')
    self.memory += 1
  def decrement(self):
    if(DEVEL): print('decrementing')
    self.memory -= 1
  def push(self):
    if(DEVEL): print('pushing to stack')
    self.stack.insert(0, self.getMem())
  def pop(self):
    if(DEVEL): print('popping from stack')
    self.memory = self.stack.pop(0)
  def outputTop(self):
    if(DEVEL): print('outputting top')
    print(self.stack[0], end="")
    print('')
  def clr(self):
    if(DEVEL): print('clearing')
    self.stack = []
  def shift(self):
    self.stack = self.stack[:-1:1]
    if(DEVEL): print('shifting')
  def forget(self):
    if(DEVEL): print('forgetting top')
    self.stack = self.stack[1:]
  def compAB(self):
    pass
  def sumAB(self):
    if(DEVEL): print('adding a and b')
    self.stack.insert(0, self.stack[0] + self.stack[1])
  def startWhile(self):
    if(DEVEL): print('start while')
  def endWhile(self):
    if(DEVEL): print('end while')
    program = self.program[:self.progIndex]
    program = program[::-1]
    opIndex = self.opIndex
    if(self.memory > 0):
      cycles = 0
      for letter in program:
        cycles +=1
        if(letter == '<'):
          opIndex += self.rotateOpAmt
          if(opIndex < 0):
            opIndex = len(self.opDial) -1
          elif(opIndex >= len(self.opDial)):
            opIndex = 0
        elif(letter != '!'):
          opIndex -= self.rotateOpAmt
          if(opIndex < 0):
            opIndex = len(self.opDial) -1
          elif(opIndex >= len(self.opDial)):
            opIndex = 0
        elif(letter == '!'):
          if(self.opDial[opIndex] == self.startWhile):
            #print('LOOP FROM: ' + str(len(self.program) - cycles - 1))
            self.opIndex = opIndex
            self.progIndex = len(self.program) - cycles -1
            break
  def inputStack(self):
    x = input(":")
    self.stack.insert(0, int(x))
  def inputMem(self):
    x = input(":")
    self.memory = int(x)
  def swap(self):
    pass
  #test
  def reset(self):
    self.memory = 0
    self.stack = []
    self.opIndex = self.startOpIndex    
    self.progIndex = 0
    self.program = None
  def printData(self):
    print(f'\t\tMemory Dial: {self.memory},\n\t\tOperation Index: {self.opIndex},\n\t\tStack: {self.stack}.')
  def acceptInput(self, i=None):
    if(i == None):
      x = input('!/?: ')
    else:
      x=i
    if(x == '!'):
      self.opDial[self.opIndex]()
    elif(x == '<'):
      self.rotateOp(-1)
    else:
      self.rotateOp()
  def acceptString(self, x):
    #CHANGE BC ! OR ? CAN BE IN BASE 1M
    if("!" in x or "?" in x):
      self.program = x
    else:
      y = toDeci(x, 1200000)
      self.program = numberToProgram(y)
    while self.progIndex < len(self.program):
      self.acceptInput(self.program[self.progIndex])
      #self.printData()
      #input("")
      self.progIndex += 1

startMemIndex = 0  #@param {type: "number"}
startOpIndex = 0 # @param {type: "number"}
numOfMemoryDials = 3 #@param {type: "number"}
rotateMemAmt = 1  #@param {type: "number"}
rotateOpAmt = 1  #@param {type: "number"}
#@markdown A and B should not be equal for addition and comparison to work
indexOfA = 0 #@param {type:"number"}
indexOfB =  1#@param {type:"number"}
#@markdown ---

D = discoids(numOfMemoryDials, startMemIndex, startOpIndex, rotateMemAmt, rotateOpAmt, indexOfA, indexOfB)
D.printData()

DEVEL = True
D.reset()       #increment 1, rotate to x, input, pop, start while, sum ab

#񭖌
D.acceptString("񭖌")
D.printData()
#output stack, rotate to a, rotate to b, pop from stack !, rotate x, decrement

''''?!<!?!?!?!?!?!?!?!?!'
program = '!?!!?!?!?!?!?!?!?!'
binary = convertToBinary(program)

decimal = binaryToDecimal(binary)
#decimal = 693591
base = 1200000;
res = "";
x =  fromDeci(res, base, decimal)
print("Program:\t\t1" + program)
print("Binary conversion:\t" + str(binary))
print("Decimal conversion:\t" + str(decimal))
print("Program size:\t" + str(len(str(binary))/8) + " bytes") 
print("Conversion to base 1.2M:\t" + x);
if toDeci(x, base) == decimal:
  print("\033[92mCoversion Verified\033[97m")
else:
  print("\033[95mCoversion Failed, character likely missing from table\033[97m")
#print(numberToProgram(toDeci("Ř", 1000000)))'''




'''def convertToTernary(p):
  output = "1"
  for letter in p:
    if letter == "!":
      output  += "2"
    elif letter == "<":
      output += "1"
    else:
      output += "0"
  return output
def ternToDec(t):
  tern = list(t)
  tern.reverse()
  exponent = 0
  total = 0
  for l in tern:
    total += int(l) * 3 ** exponent
    exponent += 1
  return total
def decimalToTern(t):
  divisor = 1
  exponent = 1
  while t//divisor > 0:
    divisor = 3 ** exponent
    exponent += 1
  exponent -= 2
  number = ""
  for i in range(exponent, -1, -1):
      divisor = 3 ** (i)
      div = t // divisor
      t = t % divisor
      number += str(div)
  return number
tern = convertToTernary("!?!<!??!?!?!?!?!?!?!")
print(tern)
tot = ternToDec(tern)
print(tot)
print(tern)
decimalToTern(tot)'''