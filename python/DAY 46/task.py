# 1. Second largest number in a list
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None


# 2. Count uppercase and lowercase letters
def count_case(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return {"uppercase": upper, "lowercase": lower}


# 3. Remove duplicate elements from a list
def remove_duplicates(lst):
    return list(set(lst))


# 4. Check if two strings are anagrams
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


# 5. Find all prime numbers in a given range
def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes


# 6. Frequency of each character in a string
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# 7. Find the longest word in a sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)


# 8. Sort a list without using sort() (Bubble Sort)
def custom_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


# 9. Check Armstrong number
def is_armstrong(num):
    power = len(str(num))
    total = sum(int(digit) ** power for digit in str(num))
    return total == num


# 10. Merge two lists and remove duplicates
def merge_lists(lst1, lst2):
    return list(set(lst1 + lst2))


# Example usage
if __name__ == "__main__":
    print(second_largest([10, 20, 4, 45, 99]))
    print(count_case("Hello World"))
    print(remove_duplicates([1, 2, 2, 3, 4, 4]))
    print(is_anagram("listen", "silent"))
    print(find_primes(1, 20))
    print(char_frequency("hello"))
    print(longest_word("Python is very powerful language"))
    print(custom_sort([5, 2, 9, 1]))
    print(is_armstrong(153))
    print(merge_lists([1, 2, 3], [2, 3, 4]))