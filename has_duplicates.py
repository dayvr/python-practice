# Function that verifies if a list has duplicates values

def hasDuplicates(list):
  # write code here
  for i in range(len(list)):
    for j in range(i+1, len(list)):
      if list[i] == list[j]:
        return True
        break
  return False

