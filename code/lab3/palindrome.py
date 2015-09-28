#Jason Bajarias
#C13379416
#28/09/2015
#this program check wether a string is a palindrome or not

#function that checks if the string is a palindrome
def Check_Palindrome(string):
  #the string is sliced which reverses the string
  check_string = string[::-1]
  #checks if the two strings are the same
  if (string == check_string):
    return "String is a palindrome"
  else:
    return "String is not a palindrome"

#function main()
def main():
  #string is store in string
  string = input("Enter String: ")
  #calling function Check_Palindrome
  answer = Check_Palindrome(string)
  #prints the return from Check_Palindrome
  print(answer)

#makes the program start at function main()
if __name__ == '__main__':
  main()