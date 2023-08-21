def reverseVowels(s):
    s_list = list(s)
    left = 0
    right = len(s_list) - 1
    vowels = "aeiouAEIOU"
    
    while left < right:
        if s_list[left] in vowels and s_list[right] in vowels:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        elif s_list[left] in vowels:
            right -= 1
        elif s_list[right] in vowels:
            left += 1
        else:
            left += 1
            right -= 1
    
    return ''.join(s_list)


print(reverseVowels(s="race a car"))
