teksts = input("Ievadiet tekstu: ")
def reverseWords(teksts):
  sar1 = teksts.split()
  if len(sar1)>1:
    sar1.reverse()
    teksts=" "
    for elements in sar1:
     teksts+=elements
    print(teksts)
  else:
    teksts = "Parāk īss teikums!"
    print(teksts)
  return teksts 
reverseWords(teksts)