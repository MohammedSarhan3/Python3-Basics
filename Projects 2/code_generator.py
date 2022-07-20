# replaces each letter with another letter, and outputs the “encoded” message
txt = input("Enter your Sentence in upper case: ")

def encoded(txt):
   OLD ="A""B""C""D""E""F""G""H""I""J""K""L""M""N""O""P""Q""R""S""T""U""V""W""X""Y""Z"
   
   for specialChar in OLD:
       txt = txt.replace( specialChar, "*") 
   print(txt)
   return

#encoded(txt)

nw=encoded(txt)
print(nw)
