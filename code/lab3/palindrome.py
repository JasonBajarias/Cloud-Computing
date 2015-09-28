#this program check wether a string is a palindrome or not
def Check_Palindrome(string):
  check_string = string[::-1]
  if (string == check_string):
    return "String is a palindrome"
  else:
    return "String is not a palindrome"

def main():
  string = input("Enter String: ")
  answer = Check_Palindrome(string)
  print(answer)

if __name__ == '__main__':
  main()