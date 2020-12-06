# python program for all cases which can check a string contains only a certain set of characters(in this case a-z A-Z 0-9)
import  re
str = "The Quick Brown Fox Jumps Over a Lazy Dog"
print(re.search(r"[a-zA-Z0-9\s_]+", str))


# python program that matches a word containing 'ab'
str1 = "able cable cab bus boom"
print(*list(filter(lambda i: re.search(r"(ab)", i), str1.split(" "))))

# python program to check for a number at the end of a word/sentence
str2 = "shreya10 shetty56 maxi30"
print(*re.findall(r"[0-9]+",str2))

# python program to search the numbers (0-9) of length between 1 to 3 in a given string
str3 = "123 456 789 be positive "
print(*re.findall(r"\d{1,3}",str3))

# pyhton program to match a string that contains only uppercase letters
str4 = "LIFE IS PRECIOUS"
print(*re.findall(r"[A-Z]+",str4))