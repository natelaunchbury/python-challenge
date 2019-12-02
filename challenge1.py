# Ceasarian shift cipher of shift 2

# add 'ab' to the end to not worry about mod for a 2-shift 
alphabet = "abcdefghijklmnopqrstuvwxyzab"

def shift(x):
  if x in alphabet:
      index = alphabet.find(x)
      return (alphabet[index+2])
  return x


def decode(x):
    mes = ''
    for c in x:
      mes += (shift(c))
    return mes

input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(decode(input))
print(decode("map"))     
