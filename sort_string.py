# Sort any given string with Case sensitive result
# Using sort function, python sorts with Capital letter string first
# So convert string to lower case and add to starting of string
# for example: yellow car TRUNK
# yellowyello, carcar, trunkTRUNK
# then we use sort function to sort this
# are remove the initial lower case string.



def sort_words(input):
  words = input.split()
  words = [w.lower() + w for w in words]
  words.sort()
  words = [w[len(w)//2:] for w in words]
  return ' '.join(words)

wString = input("Enter your string: ")
result = sort_words(wString)
print (result)
