def palindrome():
    statement = " "
    s = ''.join(ch.lower() for ch in statement if ch.isalnum())
    if(s == s[::-1]):
        return True
    else:
        return False

print(palindrome())