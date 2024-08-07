# Exercise 04. 16진수 출력하기

#  enumerate, reversed

def hex_output(str):
  str = str.lower()
  output = 0

  valid_str = "0123456789abcdefABCDEF"

  for i, n in enumerate(reversed(str)):
    if n not in valid_str:
      return 0
    
    output += int(n, 16) * (16 ** i)

  return output

print(hex_output('50'))
print(hex_output('5F'))
print(int('A', 16))

print(ord('A'))
print(chr(65))