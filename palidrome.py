def palindrome(word):
    return word==word[::-1]
result_palidrome = palindrome("radar")
print(result_palidrome)