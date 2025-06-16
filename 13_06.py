# Even or Odd Checker:
# Take an integer as input and print whether it's even or odd.
def even_odd(v):
    if v%2 == 0:
        print("even")
    else:
        print("odd")

even_odd(32)
# Sum of Digits:
# Given a number, find the sum of its digits (e.g., 123 ➝ 6).
def sum_digits(v):
    sum = 0
    original = v
    while v>0:
       digit = v%10
       sum+=digit
       v=v//10
    return sum

print(sum_digits(123))

# Count Vowels in a String:
# Input a string and count how many vowels it contains.
def vowels_count(a):
    count =0
    for i in a:
        if i in "AEIOUaeiou":
            count+=1
    return count
print(vowels_count("education"))
    

# Check Palindrome:
# Check if a given string or number is a palindrome (same forward and backward).
def is_palindrome_string(s):
    s = s.lower()  
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome_string("madam"))

# Find Maximum in a List:
# Given a list of numbers, find and print the maximum number.
def max_list(a):
    m_list=a[0]
    for i in range(len(a)):
        if a[i]>m_list:
            m_list=a[i]
    return m_list

b = [1,22,34,53,33,21]
print(max_list(b))
