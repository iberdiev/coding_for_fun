'''
My prompts and tests developed for educational purposes.

def sort_string(s):
    """
    You are given a string with random characters.
    Get only aphabetical characters and return new
    string sorted by their ascii value. Remove duplicates.

    For example:
    >>> sort_string("") == ""
    >>> sort_string("12fc342Sc@#$%FFs") == "FScfs"
    """
    return ''.join(sorted(set([i for i in list(s) if i.isalpha()])))


assert sort_string("!1!1!1qwerasdfzxcvS323tC@%Tc245") == 'CSTacdefqrstvwxz'
assert sort_string("!!!@#$%^&*$%#&$^@%") == ''
assert sort_string("12fc342Sc@#$%FFs") == 'FScfs'
assert sort_string("f1F") == "Ff"
assert sort_string("aabc") == "abc"
assert sort_string("aaab") == "ab"
assert sort_string("zebra") == "aberz"
assert sort_string("abcdeab") == "abcde"
assert sort_string("abcd") == "abcd"
assert sort_string("a") == "a"
assert sort_string("abc") == "abc"
assert sort_string("") == ""


def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)
    
assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
assert order_by_points([1234,423,463,145,2,423,423,53,6,37,3457,3,56,0,46]) == [0, 2, 3, 6, 53, 423, 423, 423, 1234, 145, 37, 46, 56, 463, 3457]
assert order_by_points([]) == []
assert order_by_points([1, -11, -32, 43, 54, -98, 2, -3]) == [-3, -32, -98, -11, 1, 2, 43, 54]
assert order_by_points([1,2,3,4,5,6,7,8,9,10,11]) == [1, 10, 2, 11, 3, 4, 5, 6, 7, 8, 9]
assert order_by_points([0,6,6,-76,-21,23,4]) == [-76, -21, 0, 4, 23, 6, 6]

def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))

assert count_nums([]) == 0
assert count_nums([-1, -2, 0]) == 0
assert count_nums([1, 1, 2, -2, 3, 4, 5]) == 6
assert count_nums([1, 6, 9, -6, 0, 1, 5]) == 5
assert count_nums([1, 100, 98, -7, 1, -1]) == 4
assert count_nums([12, 23, 34, -45, -56, 0]) == 5
assert count_nums([-0, 1**0]) == 1
assert count_nums([1]) == 1

def alien_messaging(msg, tr):
    """
    You are given a string, and a positive integer tr.
    We want to send messages to alliens, and to do it, we need
    to convert the message using tr integer.
    Return new string based on our new translation function:
    Convert each character to ascii value [23,42,54 ...]
    Obtain new array such that: new_value = (value * tr) mod 2**8.
    After having new array of integers in range [0:255],
    invert each value, such that 0 becomes 255, 1 becomes 254 and so on.    
    Convert obtained value to its corresponding ascii character.
    Apply it to each character, and return translated message.

    Examples:
    >>> alien_messaging('', 1) == ''
    >>> alien_messaging('Hello Aliens!', 1) == "·\x9a\x93\x93\x90ß¾\x93\x96\x9a\x91\x8cÞ"
    >>> alien_messaging('Hello Aliens!', 2) == "o5''!¿}'-5#\x19½"
    """
    msg = [(ord(i) * tr) % 256 for i in list(msg)]
    msg = [(i - 255) * (-1) for i in msg]
    return ''.join([chr(i) for i in msg])

assert alien_messaging('', 1) == ''
assert alien_messaging('Hello Aliens!', 1) == "·\x9a\x93\x93\x90ß¾\x93\x96\x9a\x91\x8cÞ"
assert alien_messaging('Hello Aliens!', 2) == "o5''!¿}'-5#\x19½"
assert alien_messaging('Hello World', 999) == "\x07Ü\x8b\x8bÖ\x1f~Ö!\x8bÃ"
assert alien_messaging('Kanye West has COVID-19', 43) == "f´\x85¬\x08\x9fb\x08®\x83\x9f\x87´®\x9f¾º\x8d¼\x93pÄl"


def is_jumbled_integer(number):
    """
    A number is said to be Jumbled if for every digit, its neighbours digit differs by max 1.
    Given a positive integer, return True if number is jumbled, else False.

    Examples:
    >>> is_jumbled_integer(6765) == True
    >>> is_jumbled_integer(1223) == True
    >>> is_jumbled_integer(1224) == False
    """
    number = str(number)
    if len(number) == 1: return True
    for i in range(len(number) - 1):
        if abs(int(number[i]) - int(number[i+1])) > 1: return False
    return True

assert is_jumbled_integer(6765) == True
assert is_jumbled_integer(1223) == True
assert is_jumbled_integer(1225) == False
assert is_jumbled_integer(24) == False
assert is_jumbled_integer(1212121) == True
assert is_jumbled_integer(9999) == True
assert is_jumbled_integer(99991) == False
assert is_jumbled_integer(132450) == False
assert is_jumbled_integer(1234567899876543210) == True



def chess_knight_moves(energy):
    """
    Chess knight travels 3 squares to make a move, so it takes 3 units of energy.
    Find out how many moves a chess knight can make,
    given an integer energy, representing available energy.
    Every tenth move is dedicated to have a rest, and cannot be counted as a travel move.

    Note: for negative energy return None.

    >>> chess_knight_moves(1) == 0
    >>> chess_knight_moves(6) == 2
    >>> chess_knight_moves(30) == 9
    """
    if energy < 0: return None
    moves = energy // 3
    return  moves - (moves // 10) 
    
assert chess_knight_moves(1) == 0
assert chess_knight_moves(2) == 0
assert chess_knight_moves(3) == 1
assert chess_knight_moves(4) == 1
assert chess_knight_moves(5) == 1
assert chess_knight_moves(6) == 2
assert chess_knight_moves(7) == 2
assert chess_knight_moves(30) == 9
assert chess_knight_moves(601) == 180
assert chess_knight_moves(-10) == None


def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))
    

assert sort_array([1,5,2,3,4]) == [1, 2, 4, 3, 5]
assert sort_array([-2,-3,-4,-5,-6]) == [-4, -2, -6, -5, -3]
assert sort_array([1,0,2,3,4]) == [0, 1, 2, 4, 3]
assert sort_array([]) == []
assert sort_array([2,5,77,4,5,3,5,7,2,3,4]) == [2, 2, 4, 4, 3, 3, 5, 5, 5, 7, 77]
assert sort_array([3,6,44,12,32,5]) == [32, 3, 5, 6, 12, 44]
assert sort_array([2,4,8,16,32]) == [2, 4, 8, 16, 32]
assert sort_array([2,4,8,16,32]) == [2, 4, 8, 16, 32]



def bin_diff(a, b):
    """
    Given two integers a and b, return number of 0s in
    binary representation of absolute difference of a and b.
    """
    print(
        bin(abs(a - b))[2:].count('0')
    )
    return bin(abs(a - b))[2:].count('0')

assert bin_diff(1, 10) == 2
assert bin_diff(-1, 5) == 1
assert bin_diff(435, 23) == 4
assert bin_diff(4, 18) == 1
assert bin_diff(32, 16) == 4
assert bin_diff(32, -16) == 4
assert bin_diff(0, 0) == 1


def calculate_tax_amt(tax_charged, tax_rate, y):
    """
    You are given tax_charged (integer), for tax_rate (float between 0 and 1), for y years.
    Return amount of money earned each year. Round the result to the nearest hundredth.

    >>> calculate_tax_amt(1, 0.1, 1) == 0.1
    """
    return round((tax_charged / y) / tax_rate, 2) if y else 0

assert calculate_tax_amt(150000, 0.15, 5) == 200000
assert calculate_tax_amt(37037036, 0.1, 3) == 123456786.67
assert calculate_tax_amt(150000, 0.15, 5) == 200000
assert calculate_tax_amt(58500, 0.13, 3) == 150000.0
assert calculate_tax_amt(0, 0.1, 0) == 0
assert calculate_tax_amt(100, 1, 1) == 100



def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1: return 1
    return 18 * (10 ** (n - 2))

assert starts_one_ends(1) == 1
assert starts_one_ends(2) == 18
assert starts_one_ends(3) == 180
assert starts_one_ends(4) == 1800
assert starts_one_ends(5) == 18000


def reverse_nested_lists(nested_list):
    """
    Given a list of nested lists of integers, return each of the list reversed.

    >>> reverse_nested_lists([1, [1], [[3,1,2], 3]]) == [[3, [2,1,3]], [1], 1]
    """
    nested_list = nested_list[::-1]
    for i in range(len(nested_list)):
        if isinstance(nested_list[i], list): nested_list[i] = reverse_nested_lists(nested_list[i])
    return nested_list

assert reverse_nested_lists([1, [1], [[3,1,2], 3]]) == [[3, [2,1,3]], [1], 1]
assert reverse_nested_lists([1,2,3,4,5]) == [5, 4, 3, 2, 1]
assert reverse_nested_lists([1, [8, 9, [1, 3,4, [1, 4, 2, [[],[]]]]]]) == [[[[[[], []], 2, 4, 1], 4, 3, 1], 9, 8], 1]
assert reverse_nested_lists([[1, 2], [[1,6,3,1,4], [[231], 1]]]) == [[[1, [231]], [4, 1, 3, 6, 1]], [2, 1]]
assert reverse_nested_lists([1,2,3,4,5]) == [5, 4, 3, 2, 1]



def float_to_bin(n):
    """
    Given a positive float, return it's binary represantations as a string.
    To convert the floating part in binary, multiply floating part by 2,
    until you get 1. See the example below:

    0.625   × 2 =   1.25    1   Generate 1 and continue with the rest.
    0.25    × 2 =   0.5     0   Generate 0 and continue.
    0.5     × 2 =   1.0     1   Generate 1 and nothing remains.
    
    So 0.625 = 0.101, and 2.625 = 10.101.
    Note: for floating part, calculate only up to 10 digits.

    >>> float_to_bin(2.625) == '10.101'
    >>> float_to_bin(4.0) == '100'
    """
    if isinstance(n, int): return bin(n)[2:]
    n = str(n).split('.')
    res = bin(int(n[0]))[2:]
    if not int(n[1]): return res
    res += '.'
    n = float('0.' + n[1])
    count = 1
    while n:
        n *= 2
        if n // 1:
            res += '1'
            n -= 1
        else: res += '0'
        count += 1
        if count > 10: break
    return res

assert float_to_bin(0.625) == '0.101'
assert float_to_bin(2.625) == '10.101'
assert float_to_bin(3.1415) == '11.0010010000'
assert float_to_bin(34.34) == '100010.0101011100'
assert float_to_bin(34.17) == '100010.0010101110'
assert float_to_bin(4.0) == '100'
assert float_to_bin(1.61) == '1.1001110000'
assert float_to_bin(36.0) == '100100'
assert float_to_bin(1.27) == '1.0100010100'



def count_pairs(arr):
    """
    You are given an array of integers, return number of unique
    pairs (arr[i], arr[j]) such that ith element of arr is less that jth element.
    
    Example:
    >>> count_pairs([1,2,3,4,5]) == 10
    >>> count_pairs([1, 1, 1, 1, 1, 2]) == 1
    """
    # return sum([1 for i in arr for j in arr if i < j])
    res = set()
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                res.add((arr[i], arr[j]))
    return len(res)


assert count_pairs([1,2,3,4,5]) == 10
assert count_pairs([1,3,4,5,6]) == 10
assert count_pairs([]) == 0
assert count_pairs([1, 1, 1]) == 0
assert count_pairs([-4, 6, -1, 1, 1, 56, 6, 7]) == 15
assert count_pairs([1, 1, 1, 1, 1, 2]) == 1
assert count_pairs([1, 1, 5, 5, 5, 5, 5]) == 1




def final_bonus(a, b):
    """
    You and a friend have been programming together for quite a while now.
    To celebrate the many hours you've spent programming together, you decide
    to give each other a bonus.

    You are given two arrays of integers a and b. Bonus points for each of you
    is the sum of the elements of a plus the sum of the elements of b.
    If there is an element that is present in both arrays, then that element should
    only be counted once.

    If bonus is positive integer, return it, else None.

    >>> final_bonus([1, 1, 1, 2, 3], [1, 2, 3]) == 6
    >>> final_bonus([-1], [1, -2]) == None
    >>> final_bonus([-1], [1]) == None
    """
    bonus = sum(set(a + b))
    return bonus if bonus > 0 else None

assert final_bonus([1,1,1,2,3], [1,2,3]) == 6
assert final_bonus([],[]) == None
assert final_bonus([1,5,5,7,8,3,-5],[1,4,6,7,3]) == 29
assert final_bonus([4,3,5,1,2],[4,5,6,2,4,7]) == 28
assert final_bonus([-5,6,7,-5,32,2,1],[32,1,3]) == 46
assert final_bonus([1,1,1,1,1,1],[]) == 1
assert final_bonus([4,3,4,5,3,4,6,8,1],[1,4,5]) == 27
assert final_bonus([-1], [1, -2]) == None
assert final_bonus([-1], [1]) == None


def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == 9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr: return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])


assert prod_signs([1, 2, 2, -4]) == -9
assert prod_signs([0, 1]) == 0
assert prod_signs([1, 1, 1, 2, 3, -1, 1]) == -10
assert prod_signs([]) == None
assert prod_signs([2, 4,1, 2, -1, -1, 9]) == 20
assert prod_signs([-1, 1, -1, 1]) == 4
assert prod_signs([-1, 1, 1, 1]) == -4
assert prod_signs([-1, 1, 1, 0]) == 0



def remove_punctuation(txt):
    """
    Create a function that takes a string and returns a string without punctuation marks.
    Punctuation includes !"#$%&'()*+,-./:;<==?@[\]^_`{|}~
    Note: return None if there is no punctuations marks.

    Examples:
    >>> remove_punctuation("Hello world!!!") == "Hello world"
    >>> remove_punctuation("Hello ? ? world") == "Hello   world"
    >>> remove_punctuation("no punctuation") == None
    """
    from string import punctuation
    print(
        ''.join([i for i in list(txt) if i not in punctuation])
    )
    filtered = ''.join([i for i in list(txt) if i not in punctuation])
    return filtered if filtered != txt else None



assert remove_punctuation("Hello world!!!") == "Hello world"
assert remove_punctuation("world ?") == "world "
assert remove_punctuation("Hello ? ? world") == "Hello   world"
assert remove_punctuation("") == None
assert remove_punctuation("| |@ve (()mputer $c|en{e!!!") == " ve mputer cene"
assert remove_punctuation("#$%&'()*+,-./:;<==?@[\]^_`{|}~") == ""
assert remove_punctuation("   ") == None
assert remove_punctuation("123!!!") == "123"
assert remove_punctuation("no punctuation") == None



def single_precision_multiply(a, b):
    """A number can be represented in multiple ways:
    a) decimal (base 10)
    b) binary (base 2)
    c) hexadecimal (base 16)
    ...and so on. Each type has a "precision" to represent the number. For example,
    the decimal representation of the number 10 can be:
    10 = 1 * 10^0 + 0 * 10^1 + 0 * 10^2 + 0 * 10^3 + 0 * 10^4 + 0 * 10^5 + 0 * 10^6 + 0 * 10^7 + 0 * 10^8 + 0 * 10^9
    ...
    10 = 1 * (10^0 + 0 * 10^1 + 0 * 10^2 + 0 * 10^3 + 0 * 10^4 + 0 * 10^5 + 0 * 10^6 + 0 * 10^7 + 0 * 10^8 + 0 * 10^9)
    We can see that this is just another way to represent 10. In the same way, the number
    1 can be:
    1 = 0 * 2^0 + 0 * 2^1 + 0 * 2^2 + 0 * 2^3 + 0 * 2^4 + 0 * 2^5 + 0 * 2^6 + 0 * 2^7 + 0 * 2^8 + 0 * 2^9
    ...
    1 = 0 * (2^0 + 0 * 2^1 + 0 * 2^2 + 0 * 2^3 + 0 * 2^4 + 0 * 2^5 + 0 * 2^6 + 0 * 2^7 + 0 * 2^8 + 0 * 2^9)
    Same thing for other types of representations:
    In binary:
    1 = 0 * (1 * 2^0 + 0 * 2^1 + 0 * 2^2 + 0 * 2^3 + 0 * 2^4 + 0 * 2^5 + 0 * 2^6 + 0 * 2^7 + 0 * 2^8 + 0 * 2^9)
    ...
    1 = 0 * (1 * (2^0 + 0 * 2^1 + 0 * 2^2 + 0 * 2^3 + 0 * 2^4 + 0 * 2^5 + 0 * 2^6 + 0 * 2^7 + 0 * 2^8 + 0 * 2^9))
    In hexadecimal:
    1 = 0 * (1 * 16^0 + 0 * 16^1 + 0 * 16^2 + 0 * 16^3 + 0 * 16^4 + 0 * 16^5 + 0 * 16^6 + 0 * 16^7 + 0 * 16^8 + 0 * 16^9)
    ...
    1 = 0 * (1 * (16^0 + 0 * 16^1 + 0 * 16^2 + 0 * 16^3 + 0 * 16^4 + 0 * 16^5 + 0 * 16^6 + 0 * 16^7 + 0 * 16^8 + 0 * 16^9))
    Write a function single_precision_multiply() that takes two numbers a and b
    and returns their product in the appropriate representation, given their
    precision.
    Example
    single_precision_multiply(1, 2) = 0
    single_precision_multiply(1, 4) = 2
    single_precision_multiply(1, 16) = 1
    single_precision_multiply(1, 2^16) = 4
    """




def compare_one(a, b):
    """
    Create a function that takes integer, float or string, reprepresenting
    a real numbers, and returns the larger variable in a given variable type.
    Return None if the values are equal.
    Note: if float represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) == 2.5
    compare_one(1, "2,3") == "2,3"
    compare_one("5,1", "6") == "6"
    compare_one("1", 1) == None
    """
    temp_a, temp_b = a, b
    if isinstance(temp_a, str): temp_a = temp_a.replace(',','.')
    if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
    if float(temp_a) == float(temp_b): return None
    return a if float(temp_a) > float(temp_b) else b 


assert compare_one(1, 2) == 2
assert compare_one(1, 2.5) == 2.5
assert compare_one(2, 3) == 3
assert compare_one(5, 6) == 6
assert compare_one(1, "2,3") == "2,3"
assert compare_one("5,1", "6") == "6"
assert compare_one("1", "2") == "2"
assert compare_one("1", 1) == None


def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    num = [1, 4, 5, 9, 10, 40, 50, 90,  
        100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL",  
        "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    res = ''
    while number: 
        div = number // num[i] 
        number %= num[i] 
        while div: 
            res += sym[i] 
            div -= 1
        i -= 1
    return res.lower()

def largest_value(arr):
    """
    Given an array of integer, float or string variables,
    find the variable with the largest value in the array and return it.
    If there are multiple elements with the same value, return the first such element.
    Values for integers and floats are the values they represent.
    Value of a string is sum of ascii values of its characters.
    Note: "1" > 1, as ascii value of "1" is 49.
    Also, empty string has a value of 0.
    Return None, if there is no the largest_value variable in arr.

    For example:
    largest_value(['1', 49, 49.0]) == '1'
    largest_value(['1', 51.0, 51, '2']) == 51.0
    largest_value([]) == None
    """
    is_str = False
    res = None
    largest_value = None
    for i in arr:
        if isinstance(i, str):
            if i:
                temp = sum(ord(j) for j in i)
                if largest_value is None: largest_value = 0
                if temp > largest_value: largest_value, res, = temp, i
            else:
                if largest_value:
                    if 0 > largest_value: largest_value, res = 0, i
                else: largest_value, res = 0, i
        else:
            if largest_value is None: largest_value, res = i, i
            if i > largest_value: largest_value, res = i, i
    return res


assert largest_value([4, 5, 5, 5]) == 5
assert largest_value(['1', 49, 49.0]) == '1'
assert largest_value(['123', 49, 49.0]) == '123'
assert largest_value(['123', '321']) == '123'
assert largest_value(['1', 49, '2']) == '2'
assert largest_value(['1', 51.0, 51, '2']) == 51.0
assert largest_value(['']) == ''
assert largest_value([]) == None
assert largest_value([1, 2, 3, 'I']) == 'I'
assert largest_value([-1, -2]) == -1
assert largest_value([-6, -5, 5]) == 5
assert largest_value(['', -4, 8, 8.1]) == 8.1
assert largest_value(['', -5]) == ''



def check_if_pre_prelast_char_is_a_letter(txt):
    """
    Create a function that returns True if the pre_prelast character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_pre_prelast_char_is_a_letter("apple pie") == False
    check_if_pre_prelast_char_is_a_letter("apple pi e") == True
    check_if_pre_prelast_char_is_a_letter("apple pi e ") == False
    check_if_pre_prelast_char_is_a_letter("") == False 
    """
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False



assert check_if_pre_prelast_char_is_a_letter("apple") == False
assert check_if_pre_prelast_char_is_a_letter("apple pi e") == True
assert check_if_pre_prelast_char_is_a_letter("eeeee") == False
assert check_if_pre_prelast_char_is_a_letter("A") == True
assert check_if_pre_prelast_char_is_a_letter("Pumpkin pie ") == False
assert check_if_pre_prelast_char_is_a_letter("Pumpkin pie 1") == False
assert check_if_pre_prelast_char_is_a_letter("") == False
assert check_if_pre_prelast_char_is_a_letter("eeeee e ") == False
assert check_if_pre_prelast_char_is_a_letter("apple pie") == False
assert check_if_pre_prelast_char_is_a_letter("apple pi e ") == False



def final_bonus(a, b):
    """
    You and a friend have been programming together for quite a while now.
    To celebrate the many hours you've spent programming together, you decide
    to give each other a bonus.

    You are given two arrays of integers a and b. Bonus points for each of you
    is the sum of the unique elements of both arrays combined.

    Note: If bonus is positive integer, return it, else None.

    >>> final_bonus([1, 1, 1, 2, 3], [1, 2, 3]) == 6
    >>> final_bonus([-1], [1, -2]) == None
    >>> final_bonus([-1], [1]) == None
    """
    bonus = sum(set(a + b))
    return bonus if bonus > 0 else None

assert final_bonus([1,1,1,2,3], [1,2,3]) == 6
assert final_bonus([],[]) == None
assert final_bonus([1,5,5,7,8,3,-5],[1,4,6,7,3]) == 29
assert final_bonus([4,3,5,1,2],[4,5,6,2,4,7]) == 28
assert final_bonus([-5,6,7,-5,32,2,1],[32,1,3]) == 46
assert final_bonus([1,1,1,1,1,1],[]) == 1
assert final_bonus([4,3,4,5,3,4,6,8,1],[1,4,5]) == 27
assert final_bonus([-1], [1, -2]) == None
assert final_bonus([-1], [1]) == None
assert final_bonus([1,1,1,2,3], [4]) == 10



def decimal_formula(n, b):
    """
    Any number can be represented in different bases:
    a) decimal (base 10)
    b) binary (base 2)
    c) hexadecimal (base 16)
    ...and so on.
    We can obtain decimal from any base via formula:
    Σ(ni * b^i) where i is order of a digit, and ni is corresponding value. For example:
    29 base 10 in base 2 is 11101, and to obtain 29 from binary we use the formula and obtain:
    base 10 = ((1 × 2^4) + (1 × 2^3) + (1 × 2^2) + (0 × 2^1) + (1 × 2^0))

    Write a function that takes a non-negative integer n, and integer b > 1, and return
    list of tuples: [(ni, base, power)...] See examples below.
    Note: return empty list for n = 0.

    Examples:
    >>> decimal_formula(29, 2) == [(1, 2, 4), (1, 2, 3), (1, 2, 2), (0, 2, 1), (1, 2, 0)]
    >>> decimal_formula()
    """
    def remainders(num, base): return [] if num == 0 else remainders(num//base, base) + [num % base]
    rems = remainders(n, b)
    return [(rems[i], b, len(rems) - i - 1) for i in range(len(rems))]


assert decimal_formula(29, 2) == [(1, 2, 4), (1, 2, 3), (1, 2, 2), (0, 2, 1), (1, 2, 0)]
assert decimal_formula(0, 12) == []
assert decimal_formula(4, 5) == [(4, 5, 0)]
assert decimal_formula(5, 4) == [(1, 4, 1), (1, 4, 0)]
assert decimal_formula(39, 13) == [(3, 13, 1), (0, 13, 0)]
assert decimal_formula(32, 2) == [(1, 2, 5), (0, 2, 4), (0, 2, 3), (0, 2, 2), (0, 2, 1), (0, 2, 0)]
assert decimal_formula(21, 6) == [(3, 6, 1), (3, 6, 0)]
assert decimal_formula(22, 6) == [(3, 6, 1), (4, 6, 0)]
assert decimal_formula(5555, 100) == [(55, 100, 1), (55, 100, 0)]



def burrito_discount(sizes, c):
    """
    Local burrito stand is having a discount for extra hungry people.
    Burritos come with different sizes, and if you hungry, you can get
    any burrito for the price of the smaller burrito that is closest to
    chosen one.
    Given a list of positive integers, representing size/price for burritos,
    and integer c, which is chosen burrito, return integer, that
    represents price to be paid for chosen burrito considering the discount.
    If there is no burritto with smaller price, return chosen burrito price.
    Note: c will be always in sizes.

    >>> burrito_discount([1,6,2,3,4,6,3,2,5,8,5,3,7,5], 5) == 4
    >>> burrito_discount([1,6,2], 1) == 1
    """
    sizes = sorted(set(sizes))
    chosen_i = sizes.index(c)
    return sizes[chosen_i-1] if chosen_i else sizes[chosen_i]


assert burrito_discount([1,6,2,3,4,6,3,2,5,8,5,3,7,5], 5) == 4
assert burrito_discount([1,6,2], 1) == 1
assert burrito_discount([1,6,45], 45) == 6
assert burrito_discount([4,4,4,5,6,100,101], 101) == 100
assert burrito_discount([55,78,34,15,64], 15) == 15
assert burrito_discount([78,78,78,13,13,42], 78) == 42



def sum_the_highest_factors(a, b):
    """
    Given two integers a and b find their the_highest factors,
    combine them and return sum of unique factors.

    For example:
    >>> sum_the_highest_factors(2, 3) == 5
    >>> sum_the_highest_factors(2, 6) == 5
    >>> sum_the_highest_factors(2, 9) == 5

    Constraints: a >= 2, b >= 2.
    """
    import math
    def the_highestFactors(n):
        res = []
        while n % 2 == 0: res, n = res + [2], n / 2
        for i in range(3,int(math.sqrt(n))+1,2): 
            while n % i== 0: res, n = res + [i], n / i
        if n > 2: res += [n]
        return res
    return sum(set(the_highestFactors(a) + the_highestFactors(b)))


assert sum_the_highest_factors(2, 3) == 5
assert sum_the_highest_factors(2, 6) == 5
assert sum_the_highest_factors(2, 9) == 5
assert sum_the_highest_factors(40, 80) == 7
assert sum_the_highest_factors(13, 11) == 24
assert sum_the_highest_factors(9999, 7777) == 122
assert sum_the_highest_factors(4, 4) == 2



def is_crazy(txt):
    """
    If you take all the ascii values of string's characters,
    deduplicate and sort them in ascending order,
    and it forms an arithmetic progression, the string
    is considered to be crazy.
    So any string that has only 1 or 0 unique characters are not crazy, as to form
    an arithmetic progression, you need at least 2 values.

    Given a string return True if it is a crazy string, else False.

    >>> is_crazy('') == False
    >>> is_crazy('hello') == False
    >>> is_crazy('hi') == True
    """
    asc_vals = sorted(set([ord(i) for i in txt]))
    if len(asc_vals) < 2: return False
    diff = asc_vals[1] - asc_vals[0]
    for i in range(1, len(asc_vals) - 1):
        if asc_vals[i+1] - asc_vals[i] != diff: return False
    return True

assert is_crazy('') == False
assert is_crazy('hello') == False
assert is_crazy('hi') == True
assert is_crazy('ace') == True
assert is_crazy('def') == True
assert is_crazy('fed') == True
assert is_crazy('hello World') == False
assert is_crazy(' !"#$%') == True
assert is_crazy('%$#"! ') == True
assert is_crazy(' !"$%') == False
assert is_crazy('A') == False
assert is_crazy('aaaaa') == False
assert is_crazy('aaaaabcccc') == True

def inverse_binary(n):
    """
    Given an non-negative integer, return its inverse
    binary representation as a string. Inverse binary,
    is a string with ones replaced with zeros and vice versa.

    Examples:
    >>> inverse_binary(4) == '011'
    >>> inverse_binary(12) == '0011'
    >>> inverse_binary(1) == '0'
    """
    return ''.join(['0' if i == '1' else '1' for i in bin(n)[2:]])   

assert inverse_binary(4) == '011'
assert inverse_binary(12) == '0011'
assert inverse_binary(1) == '0'
assert inverse_binary(100) == '0011011'
assert inverse_binary(32) == '011111'
assert inverse_binary(123) == '0000100'
assert inverse_binary(77) == '0110010'
assert inverse_binary(0) == '1'



def operations_exam(a, b):
    """
    You are being tested on algebraic operations.
    Given two non-negative integers a and b, return f given by formula:
    f = (a multiplied by b) plus (minus a minus b) plus (b multiplied by a) plus (b to the a) plus (a to the b).
    Note: return None if a plus b is more than 50.

    >>> operations_exam(1,1) == 4
    >>> operations_exam(0,0) == 2
    """
    if (a + b) > 50: return None
    print(
        a * b + (-a) - b + b * a + b**a + a**b
    )
    return a * b + (-a) - b + b * a + b**a + a**b

assert operations_exam(1,1) == 2
assert operations_exam(0,0) == 2
assert operations_exam(1,0) == 0
assert operations_exam(2,10) == 1152
assert operations_exam(24,26) == 777338493235300870639470742394111150
assert operations_exam(25,25) == 177635683940025046467781066894532450
assert operations_exam(49,1) == 98
assert operations_exam(30,20) == 1073741824348678440100000000000000001150
assert operations_exam(50,51) == None
assert operations_exam(25,26) == None
assert operations_exam(45,6) == None



def trailing_zeros(num):
    """
    An integer num has trailing zeros if n mod 10 == 0.

    Given a number num, return the number of trailing zeros of the number.

    For example:
    >>> trailing_zeros(28) == 0
    >>> trailing_zeros(0) == 1
    >>> trailing_zeros(-12000) == 3
    """
    count = 0
    for i in str(num)[::-1]:
        if i == '0': count += 1
        else: break
    return count


assert trailing_zeros(28) == 0
assert trailing_zeros(0) == 1
assert trailing_zeros(123) == 0
assert trailing_zeros(12000) == 3
assert trailing_zeros(-12000) == 3
assert trailing_zeros(452230) == 1
assert trailing_zeros(101) == 0
assert trailing_zeros(000000000) == 1



def adjacent_uniqueness(s):
    """
    Given a string, return it with removed adjacent duplicates.
    "a" and "A" are different characters.
    Note: remove trailing spaces.

    Examples:
    >>> adjacent_uniqueness('aaaAAaaAAb') == 'aAaAb'
    >>> adjacent_uniqueness('     ') == ' '
    >>> adjacent_uniqueness('aa     AA') == 'a A'
    """
    s = list(s)
    i = 0
    while i < (len(s) - 1):
        if s[i] == s[i+1]: s.pop(i)
        else: i += 1
    return ''.join(s).strip()

assert adjacent_uniqueness('aaaAAaaAAb') == 'aAaAb'
assert adjacent_uniqueness('     ') == ''
assert adjacent_uniqueness('aa     AA') == 'a A'
assert adjacent_uniqueness('aa') == 'a'
assert adjacent_uniqueness('    aa    ') == 'a'
assert adjacent_uniqueness('a') == 'a'
assert adjacent_uniqueness(' 1 2 3333 444  555566677788 ') == '1 2 3 4 5678'
assert adjacent_uniqueness('') == ''



def count_points(arr):
    """
    Given a list of non-zero integers, you have to count the number of points in the list.
    Integer is a point when it divides sum of ascii values of a string "point"

    Return the number of points in the list.
    """
    print(
        sum([ord(i) for i in 'point']),
        sum([1 for i in arr if not (sum([ord(i) for i in 'point'])) % i])
    )
    return sum([1 for i in arr if not (sum([ord(i) for i in 'point']) % i)])



assert count_points([]) == 0
assert count_points([1, 2,2,2,2,3,3,554, 1108]) == 6
assert count_points([554,277,2,4]) == 3
assert count_points([3, 3, 3]) == 0
assert count_points(list(range(-10, 0)) + list(range(1, 10))) == 4
assert count_points(list(range(-10, 0)) + list(range(1, 555))) == 6
assert count_points(list(range(-10, 0)) + list(range(1, 10000))) == 6
assert count_points([-554,-277,-2,-4]) == 3

It seems we currently do not have any milestones. Let's end the contract. You can contact me any time if you need anything related to Python. I am grateful to have a deal with you, will leave a good feedback for you. Would be glad to receive a review from you also)
Great client. He has great communications skill. It was a pleasure to work with him!!! Top Rated Client!!!

AI challenge batch 39

def divisible_by(n, k):
    """
    Given two integers 'n' and 'k',
    return True if digit sum of 'n' is divisible by digit sum of 'k'.
    If digit sum of 'k' is zero, return None.
    Note: first digit of negative integers should be substracted, not summed up.

    >>> divisible_by(8, 4) == True
    >>> divisible_by(-141, 2) == True
    >>> divisible_by(-141, -11) == None
    """
    n = ((-2 * int(str(n)[1])) if n < 0 else 0) + sum(int(i) for i in str(abs(n)))
    k = ((-2 * int(str(k)[1])) if k < 0 else 0) + sum(int(i) for i in str(abs(k)))
    return n % k == 0 if k else None


assert divisible_by(8, 4) == True
assert divisible_by(-14, 7) == False
assert divisible_by(-14, 1) == True
assert divisible_by(26, 4) == True
assert divisible_by(-7233, 5) == False
assert divisible_by(-11, 5) == True
assert divisible_by(-16, 4) == False
assert divisible_by(-141, 2) == True
assert divisible_by(-141, 0) == None
assert divisible_by(-141, -11) == None




def get_streak(arr):
    """
    You are given 'arr' of positive integers.
    Return the value of the most longest substring that has same values.
    For several values with the same length of substring, return the first one occured.
    Return None for empty array.

    Examples:
    >>> get_streak([]) == 0
    >>> get_streak([1,1,2]) == 2
    """
    if not arr: return None
    val = arr[0]
    ans, temp = 1, 1
    for i in range(1, len(arr)): 
        if (arr[i] == arr[i - 1]): 
            temp += 1
        else: 
            if temp > ans: val = arr[i-1]
            ans = max(ans, temp)
            temp = 1
    if temp > ans: val = arr[-2]
    ans = max(ans, temp)
    return val


assert get_streak([]) == None
assert get_streak([1,2,3]) == 1
assert get_streak([7]) == 7
assert get_streak([1,1,2,87,91]) == 1
assert get_streak([2,1]) == 2
assert get_streak([5,4,3,3,3,3,3,2,3,3,3, 4]) == 3
assert get_streak([2,1,1,3]) == 1
assert get_streak([1,1,1,1,1]) == 1

def secret_code(word):
    """
    A secret code of a word is an array of integers such that
    each letter in the phrase is a code, where the letter 'a' is represented by
    integer 1, and the letter 'b' is represented by 2, and so on.
    Given a string containing only alphabetical characters and blank spaces,
    return an array of its encoded letters.
    Note: blank spaces value is zero.

    Example:
    >>> secret_code("A b c") == [1,0,2,0,3]
    >>> secret_code("") == []
    """
    return [(ord(i) - 96) if i.isalpha() else 0 for i in word.lower()]

assert secret_code("Abc") == [1,2,3]
assert secret_code("A b c") == [1,0,2,0,3]
assert secret_code("Hello World") == [8, 5, 12, 12, 15, 0, 23, 15, 18, 12, 4]
assert secret_code("HelloWorld") == [8, 5, 12, 12, 15, 23, 15, 18, 12, 4]
assert secret_code("") == []
assert secret_code("    ") == [0, 0, 0, 0]
assert secret_code("zzz") == [26, 26, 26]
assert secret_code("helloworld") == [8, 5, 12, 12, 15, 23, 15, 18, 12, 4]
assert secret_code("pythonisgreat") == [16, 25, 20, 8, 15, 14, 9, 19, 7, 18, 5, 1, 20]



def biased_squares(arr):
    """
    Given an array of integers, return the sum of 'biased_squares' of a given integers.
    'biased_square' of an integer 'n', is (n squared times (n minus 1)) if n is even, else n squared.
    
    Example:
    >>> biased_squares([1,2,3]) == 14
    """
    return sum((i**2) * (1 if i % 2 else (i - 1)) for i in arr)

assert biased_squares([1,2,3]) == 14
assert biased_squares([1, 4, 5, 7, 8, 11]) == 692
assert biased_squares([]) == 0
assert biased_squares([0,0,0]) == 0
assert biased_squares([-1, 3, 4, 7, 9, -11]) == 309
assert biased_squares([1,3,2,-5]) == 39
assert biased_squares([1,1,1]) == 3
assert biased_squares([-1,-1,2]) == 6
assert biased_squares([4]) == 48

def swap(arr):
    """
    Given a list of integers, swap each consequtive pairs and return obtained arr.
    If length of obtained array is odd, remove the pre_prelast integer, and add it to the beginning.

    >>> swap([1, 2, 3, 4, 5]) == [5, 2, 1, 4, 3]
    >>> swap([]) == []
    """
    for i in range(0, len(arr) - 1, 2): arr[i], arr[i+1] = arr[i+1], arr[i]
    if len(arr) % 2: arr.insert(0, arr.pop())
    return arr

assert swap([1, 2, 3, 4, 5]) == [5, 2, 1, 4, 3]
assert swap([]) == []
assert swap([1]) == [1]
assert swap([1,-2,-1,2,100]) == [100, -2, 1, 2, -1]
assert swap([1,3,2,2,3,1]) == [3, 1, 2, 2, 1, 3]
assert swap([3,2,2,3]) == [2, 3, 3, 2]


def to_roman(num):
    """
    Convert a positive integer num to Roman numerals, and return in as a string.
    Note: divide each symbol by a single space.
    Constraints: 1 <= num <= 1000

    Examples:
    >>> to_roman(1) == 'I'
    >>> to_roman(6) == 'VI'
    """
    nums = [1, 4, 5, 9, 10, 40, 50, 90,  
        100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL",  
        "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    res = []
    while num: 
        div = num // nums[i] 
        num %= nums[i] 
        while div: 
            res += [sym[i]] 
            div -= 1
        i -= 1
    return ' '.join(res)

assert to_roman(1) == 'I'
assert to_roman(6) == 'V I'
assert to_roman(12) == 'X I I'
assert to_roman(10) == 'X'
assert to_roman(25) == 'X X V'
assert to_roman(31) == 'X X X I'
assert to_roman(156) == 'C L V I'
assert to_roman(456) == 'CD L V I'
assert to_roman(1000) == 'M'



def whole_square_roots(arr):
    """
    Given an array of integers, obtain a new array
    where each integer is raised to the power of 1/2.
    If an integer is negative, or its square root is not an integer,
    ignore, and proceed to the next number.
    Return obtained array in descending order.
    
    Examples:
    >>> whole_square_roots([]) == []
    >>> whole_square_roots([4, 2, -1, 0]) == [2, 0]
    """
    res = []
    for i in arr:
        if i >= 0 and not((i**.5) % 1): res += [i**.5]
    return sorted(res,reverse=True)


assert whole_square_roots([]) == []
assert whole_square_roots([4,2,-1,0]) == [2,0]
assert whole_square_roots([1,2,3,4,5,6,7,8,9,10]) == [3,2,1]
assert whole_square_roots([1,4,9,16,25,36,49,56]) == [7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
assert whole_square_roots([2,3,5,6,7,8,10]) == []


def largest_lattice(arr):
    """
    You are given a list of positive intgers, where each integer
    represents a metal wire with corresponding length.
    You want to build a squared lattice.
    To build one quadratic square unit of a lattice,
    2 units of metal wire should be used.
    You may cut wires by 1 unit of length.
    Return area of the largest possible lattice you can build.
    Note: sides of the squares must be integers.

    >>> largest_lattice([]) == 0
    >>> largest_lattice([4, 3]) == 1
    >>> largest_lattice([8]) == 4
    """
    length = 0
    while sum(arr) >= (length ** 2) * 2:
        length += 1
    print(
        (length - 1) ** 2
    )
    return (length - 1) ** 2

assert largest_lattice([]) == 0
assert largest_lattice([4, 3]) == 1
assert largest_lattice([8]) == 4
assert largest_lattice([17]) == 4
assert largest_lattice([18]) == 9
assert largest_lattice([42,54,63,234,1]) == 196


def word_game(str1, str2):
    """
    You are given 2 strings.
    Return True if you can obtain 1st by by replacing
    and removing character from 2nd string, else return False.
    Capitalizations is important.

    >>> word_game("word", "30mx1X@#!V#!$") == False
    >>> word_game("word", "cf9o83d4xr,49w") == True
    >>> word_game("", "cf9o83d4xr,49w") == True
    """
    str1, str2 = list(str1), list(str2)
    for i in str1:
        if i not in str2: return False
        str2.remove(i)
    return True

assert word_game("word", "30mx1X@#!V#!$") == False
assert word_game("word", "cf9o83d4xr,49w") == True
assert word_game("", "cf9o83d4xr,49w") == True
assert word_game("   ", "cf9o8 3d4 xr,49w") == False
assert word_game("", "cf 9o8 3d4x r,49w") == True
assert word_game("aa", "aa") == True



def pairwise_increasing(arr):
    """
    Write a function that takes an array of integers,
    checks if every consequtive pairs are in increasing order,
    and return True if every pair is in ascending order, else False.
    Consequtive pairs are such pairs with indices [0, 1], [2, 3] and so on.
    Note: for odd length of arr, ignore pre_prelast integer.
    If there is no pairs, return None.
    
    Examples:
    >>> pairwise_increasing([3, 4, 2, 2, 5]) == False
    >>> pairwise_increasing([1, 2, 2, 3, 2]) == True
    >>> pairwise_increasing([-7]) == None
    """
    if len(arr) < 2: return None
    for i in range(0, len(arr) - 1, 2):
        if arr[i] >= arr[i+1]: return False
    return True
    
assert pairwise_increasing([3, 4, 2, 2, 5]) == False
assert pairwise_increasing([1, 2, 2, 3, 2]) == True
assert pairwise_increasing([-7, -5,-5,-4,-4,0,1,3,1]) == True
assert pairwise_increasing([10101]) == None
assert pairwise_increasing([1,0,1,0,1]) == False
assert pairwise_increasing([0,1,0,1,0]) == True
assert pairwise_increasing([1,1,1,1,1]) == False



def subsets(arr):
    """
    Given an array of integers, return number of all
    possible unique non-empty subsets of arr in non-descending order.
    Note: at least 2 integers needed to be considered as a subset.

    For example:
    >>> subsets([1,1]) == 1
    >>> subsets([1,1,3]) == 3
    """
    if len(arr) < 2: return 0
    subsets = []
    for i in range(len(arr) - 1):
        temp = []
        temp.append(arr[i])
        for j in range(len(arr) - 1 - i):
            temp.append(arr[i + j + 1])
            if len(temp) > 1 and not (temp in subsets) and temp == sorted(temp):
                subsets.append(temp.copy())
            if sorted(temp) != temp:
                temp = []
                break
    return len(subsets)

assert subsets([1,1,3,4]) == 6
assert subsets([4,3,1,1]) == 1
assert subsets([1,1]) == 1
assert subsets([1,1,3]) == 3
assert subsets([1,2,5,22,3,5,1,3,0]) == 8
assert subsets([1]) == 0
assert subsets([]) == 0



def sort_list(arr):
    """
    Given a list of positive integers, return it
    sorted by the sum of their digits in min_max order.
    min_max order is an array where 1st items is min, 2nd is max,
    3rd is the 2nd min and so on.

    Examples:
    >>> sort_list([]) == []
    >>> sort_list([11,1,7,1]) == [7, 1, 11, 1]
    """
    arr = sorted(arr, key=lambda x: sum(int(i) for i in str(x)))
    switch, res = True, []
    for _ in range(len(arr)):
        res += [arr.pop(-1) if switch else arr.pop(0)] 
        switch = not switch    
    return res

assert sort_list([]) == []
assert sort_list([11,1,7,1]) == [7, 1, 11, 1]
assert sort_list([1,3,23,42,5,7,4,90]) == [90, 1, 7, 3, 42, 4, 5, 23]
assert sort_list([55,4,2,4,1,23,5]) == [55, 1, 5, 2, 23, 4, 4]
assert sort_list([4,4,4,4,4,22,22,22]) == [22, 4, 22, 4, 22, 4, 4, 4]



def arithmetic_sequence(a, b):
    """
    Given two integers, write a function which returns
    an array of a sequence from a to b (inclusive) with
    step = 1 if a + b is odd, else step = 2.

    Example:
    >>> arithmetic_sequence(5, 2) = [5, 4, 3, 2]
    >>> arithmetic_sequence(0, -3) = [0, -2]
    >>> arithmetic_sequence(0, 0) = [0]
    """
    if a == b: return [a]
    step = 1 if (a+b) % 2 else 2
    return list(range(a, b + (1 if b >= a else -1), -step if a > b else step))

assert arithmetic_sequence(5, 2) == [5, 4, 3, 2]
assert arithmetic_sequence(0, -4) == [0, -2, -4]
assert arithmetic_sequence(0, 0) == [0]
assert arithmetic_sequence(7, 8) == [7,8]
assert arithmetic_sequence(8,7) == [8,7]
assert arithmetic_sequence(8,-2) == [8, 6, 4, 2, 0, -2]


def reverse_words(sentence):
    """
    Create a function that takes a sentence and returns
    a new sentence, where all words with odd number of
    vowels are reversed. Keep the order of words.
    Note: word is a substring of characters separated by space.
    It is guaranteed that words are separated by a
    single space, and there is no trailing spaces.

    Examples:
    >>> reverse_words('Hi') == 'iH'
    >>> reverse_words('hello World') == 'hello dlroW'
    >>> reverse_words('') == ''
    """
    print(
        ' '.join([i[::-1] if sum(j.lower() in 'aeiou' for j in i) % 2 else i for i in sentence.split()])
    )
    return ' '.join([i[::-1] if sum(j.lower() in 'aeiou' for j in i) % 2 else i for i in sentence.split()])
    
assert reverse_words('Hi') == 'iH'
assert reverse_words('In The Beginning') == 'nI ehT gninnigeB'
assert reverse_words('hello World') == 'hello dlroW'
assert reverse_words('') == ''
assert reverse_words('a baby friendly Oooops') == 'a ybab friendly Oooops'
assert reverse_words('bed. format') == '.deb format'



def associative_reverse(arr):
    """
    Associative array is an abstract data type that can hold associative
    data. In our case, it is 3 consecutive integers.
    [1,2,3,4...] - in this array, [1,2,3] subarray is considered as one entry.
    
    Given an associative array of 3 integers per entry, return its reverse,
    where each entry should keep inner order, however the order of entries in arr
    should be reversed. It is guaranteed that length of arr will be a
    multiple of 3, including 0.

    Examples:
    >>> associative_reverse([1,2,3,4,5,6]) == [4,5,6,1,2,3]
    >>> associative_reverse([]) == []
    """
    res = []
    while arr:
        res += arr[-3:]
        arr = arr[:-3]
    return res
    

assert associative_reverse([1,2,3,4,5,6]) == [4,5,6,1,2,3]
assert associative_reverse([]) == []
assert associative_reverse([1,2,3,3,2,1,1,1,1]) == [1,1,1,3,2,1,1,2,3]
assert associative_reverse([-1,-2,-3,1,2,3,4,2,4]) == [4, 2, 4, 1, 2, 3, -1, -2, -3]
assert associative_reverse([23,43,12,0,0,1]) == [0, 0, 1, 23, 43, 12]
assert associative_reverse([1,1,1,2,2,3]) == [2, 2, 3, 1, 1, 1]


def count_meals(human_energy):
    """
    A single meal consists of 100 units of energy. However only half of it
    converts to human energy. As a coach, you know how much energy player
    needs to succeed in trainings. Given "human_energy" needed as non-zero integer,
    find a minimum number of meals (as integer) a player should consume
    to succeed, and return total units of meal energy you need.

    >>> count_meals(61) == 200
    >>> count_meals(0) == 0
    """
    while human_energy % 50: human_energy += 1
    return human_energy / .5

assert  count_meals(61) == 200
assert count_meals(0) == 0
assert  count_meals(345) == 700
assert  count_meals(32) == 100
assert  count_meals(878) == 1800
assert  count_meals(1234) == 2500
assert  count_meals(1) == 100


def after_inc(a, b):
    """
    Given 2 real numbers, sum them, and if their sum:
    1) is an integer, return it;
    2) is a positive float, return its ceil, else its floor;

    >>> after_inc(1,-1) == 0
    >>> after_inc(1,-1.1) == -1
    >>> after_inc(0,0.1221) == None
    """
    from math import floor, ceil
    res = a + b
    if int(res) == res: return res
    return ceil(res) if res > 0 else floor(res)

assert after_inc(1,-1) == 0
assert after_inc(1,-1.1) == -1
assert after_inc(0,0.1221) == 1
assert after_inc(-1,0.1221) == -1
assert after_inc(0.5,0.5) == 1
assert after_inc(0.0,0.0) == 0


def first_alpha(string):
    """
    Given a string of characters, return product of index of the 
    first alphabetical character multiplied by its ascii code.
    If string is empty or there is not alphabetical characters, return None.
    Note: indexing starts from ascii code of the first character.

    Example:
    >>> first_alpha('Python') == 6400
    >>> first_alpha('<3 love') == 6804
    >>> first_alpha('<3') == None
    """
    if not string: return None
    index = ord(string[0])
    for i in string:
        if i.isalpha(): return ord(i) * index 
        index += 1
    return None

assert first_alpha('Python') == 6400
assert first_alpha('<3 love') == 6804
assert first_alpha('<3') == None
assert first_alpha('123456789') == None
assert first_alpha('1a1') == 4850
assert first_alpha('') == None



def get_idx_element(arr, idx):
    """
    You are given an array of integers "arr" and positive integer "idx".
    If there is a such item in arr with index of idx - 1, return "idx" times arr[idx-1],
    else return reciprocal of idx (up to 3 decimal points).

    For example:
    >>> get_idx_element([1, 2, 3, 4, 5, 6], 3) == 9
    >>> get_idx_element([1, 2], 3) == 0.333    
    """
    try: return arr[idx-1] * idx
    except: return round(1/idx, 3)

assert get_idx_element([1, 2, 3, 4, 5, 6], 3) == 9
assert get_idx_element([1, 2], 3) == 0.333
assert get_idx_element([0,0,0,0], 3) == 0
assert get_idx_element([4,53,53,21], 4) == 84
assert get_idx_element([], 1) == 1
assert get_idx_element([666], 1) == 666
assert get_idx_element([4,53,53,-21], 4) == -84


def to_tuple(n):
    """
    Given a positive integer n, return a tuple of a form:
    (a, b, c, d, e) where:
        a: n factorial
        b: 1 + 2 + 3 ... + n
        c: n squared
        d: n times -1
        e: reciprocal of n (up to 3 floating points)
    
    Note: return None if n > 30.

    Examples:
    >>> to_tuple(3) == (6, 6, 9, -3, 0.333)
    >>> to_tuple(1000) == None
    """
    if n > 30: return None
    from math import factorial
    return (
        factorial(n),
        sum(list(range(1, n + 1))),
        n ** 2,
        -n,
        round(1/n,3)
    )


assert to_tuple(3) == (6, 6, 9, -3, 0.333)
assert to_tuple(30) == (265252859812191058636308480000000, 465, 900, -30, 0.033)
assert to_tuple(5) == (120, 15, 25, -5, 0.2)
assert to_tuple(13) == (6227020800, 91, 169, -13, 0.077)
assert to_tuple(25) == (15511210043330985984000000, 325, 625, -25, 0.04)
assert to_tuple(31) == None




def greatest(a, b):
    """
    You will be given two non-zero integers a and b. Your task is to determine
    which is the greatest of the two. 'Greatest value' of 'a' is 
    'a' modulo 'b', and vice versa. A number with the bigger greatest value, is
    considered to be the greatest.
    If both are great, return None.

    For example:
    >>> greatest(1, 1) = None
    >>> greatest(4, 3) = 3
    >>> greatest(7, 13) = 7
    """
    if abs(a) == abs(b): return None
    return min(a, b)

assert greatest(1, 1) == None
assert greatest(4, 3) == 3
assert greatest(7, 13) == 7
assert greatest(1, 2) == 1
assert greatest(4, 3) == 3
assert greatest(-9, -7) == -9
assert greatest(-3, 3) == None



def the_highests_within(a, b):
    """
    Given 2 positive integers, where a <= b,
    return number of the_highest numbers within range of [a, b] inclusive.

    >>> the_highests_within(1,10) == 4
    >>> the_highests_within(2,2) == 1
    >>> the_highests_within(2,3) == 2
    """
    def is_the_highest(num):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0: return False
            return True
        return False
    return sum(1 for i in range(a, b + 1) if is_the_highest(i))


assert the_highests_within(1,10) == 4
assert the_highests_within(2,2) == 1
assert the_highests_within(1,100) == 25
assert the_highests_within(100,200) == 21
assert the_highests_within(300,1000) == 106
assert the_highests_within(2,3) == 2


def most_repeating_letter(s):
    """
    Given a string s, return the character which appears most frequently.
    If several characters with max frequency, return character with the higher ascii code.
    Note: you sould consider 'a' and 'A' as same characters, however, should consider
    higher ascii value when choosing between characters with the same frequency,
    and also return the character with the higher ascii code. Ignore spaces.

    Restrictions:
        * there is at least 1 letter in s.
        * s will only contain letters and spaces.

    >>> most_repeating_letter('HELLO    World') == 'l'
    >>> most_repeating_letter('HeLLo WorLd') == 'L'
    >>> most_repeating_letter('OopPs') == 'p'
    """
    from collections import defaultdict
    d = defaultdict(int)
    for i in s.replace(' ', ''): d[i.lower()] += 1
    freq = max(d.values())
    d = [(i, d[i]) for i in d]
    d = list(filter(lambda x: x[1] == freq, d))
    return max([i[0] if i[0] in s else i[0].upper() for i in d])


assert most_repeating_letter('HELLO World') == 'l'
assert most_repeating_letter('HeLLo WorLd') == 'L'
assert most_repeating_letter('Oopps') == 'p'
assert most_repeating_letter('aa BB cC DD') == 'c'
assert most_repeating_letter('AA BB CC DD') == 'D'





def the_highests_comps(n):
    """
    A the_highest number is a natural number greater than 1 that is divisible
    by only two integers: itself and 1. A positive integer that is not
    the_highest is called composite.
    Given an non-negative integer n, return tuple (a, b),
    where 'a' is sum of the_highests from 0 to n(inclusive),
    and 'b' is sum of composites from 0 to n (inclusive).
    Note: 0 and 1 are neither the_highest nor composite.

    Examples:
    >>> the_highests_comps(0) == (0, 0)
    >>> the_highests_comps(2) == (2, 0)
    >>> the_highests_comps(10) == (17, 37)
    """
    def is_the_highest(num):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0: return False
            return True
        return False
    if n in [0,1]: return (0, 0)
    the_highests, comps = 0, 0
    for i in range(2, n + 1):
        if is_the_highest(i): the_highests += i
        else: comps += i
    return (the_highests, comps)


assert the_highests_comps(0) == (0, 0)
assert the_highests_comps(2) == (2, 0)
assert the_highests_comps(10) == (17, 37)
assert the_highests_comps(7) == (17, 10)
assert the_highests_comps(11) == (28, 37)
assert the_highests_comps(18) == (58, 112)



def permutations(arr, p):
    """
    Given an array of integers and integer 'p', return the number
    of unique permutations of arr that have exactly b elements.
    It is guaranteed that 'p' is less than or equal to length of arr.

    Example:
    >>> permutations([1, 2, 3], 2) == 6
    >>> permutations([1, 2, 2], 2) == 3
    >>> permutations([1, 2, 3, 4], 0) == 1
    """
    from itertools import permutations as perms
    return len(set(perms(arr, p)))

assert permutations([1, 2, 3], 2) == 6
assert permutations([1, 2, 2], 2) == 3
assert permutations([1, 2, 3, 4], 4) == 24
assert permutations([1, 2, 3, 4], 1) == 4
assert permutations([1, 2, 3, 4], 0) == 1
assert permutations([1,1,1], 2) == 1
assert permutations([1,1,1], 1) == 1



def largest_lattice(arr):
    """
    You are given a list of positive intgers, where each integer
    represents a metal wire with corresponding length.
    You want to build a lattice of a square shape.
    To build one quadratic square unit of a lattice,
    2 units of metal wire should be used.
    You may cut wires by 1 unit of length.
    Return area of the largest possible lattice you can build.
    Note: sides of the squares must be integers.

    >>> largest_lattice([]) == 0
    >>> largest_lattice([4, 3]) == 1
    >>> largest_lattice([8]) == 4
    """
    wires = int(sum(arr) / 2)
    while (wires ** .5) % 1: wires -= 1
    return wires

assert largest_lattice([]) == 0
assert largest_lattice([4, 3]) == 1
assert largest_lattice([8]) == 4
assert largest_lattice([17]) == 4
assert largest_lattice([18]) == 9
assert largest_lattice([32]) == 16
assert largest_lattice([42,54,63,234,1]) == 196


AI challenge batch 51


def is_even(s):
    """
    Given a string s consisting of lowercase characters 'a' and 'b',
    Return True if you can rearrange string in a way that every 'a'
    can be replaced by 'b', and vice versa, else False.
    If string is empty or containes any other character, return None.
    
    Examples:
    >>> is_even('') == None
    >>> is_even('aba') == False
    >>> is_even('abba') == True
    >>> is_even(' abbA') == False
    """
    if not s: return None
    for i in s:
        if i not in 'ab': return None
    if len(s) % 2: return False
    return s.count('a') == s.count('b')


assert is_even('') == None
assert is_even('aba') == False
assert is_even('abba') == True
assert is_even(' abbA') == None
assert is_even('ababbabaab') == True
assert is_even(' ') == None
assert is_even('!') == None





def is_good_name(name):
    """
    Name is considered to be good if:
        1) it has at least 3 characters.
        2) only 1st letter is capitalized.
        3) does not contain and not alphabetic characters.
    
    Write a function that takes a string 'name' and returns True if its good, else False.
    
    Examples:
    >>> is_good_name("MarY") == False
    >>> is_good_name("Alexander") == True
    """
    if len(name) < 3: return False
    for i in range(len(name)):
        if not name[i].isalpha(): return False
        if i == 0:
            if name[i] == name[i].lower(): return False
        else:
            if name[i] != name[i].lower(): return False
    return True

assert is_good_name("Phil") == True
assert is_good_name("Cary") == True
assert is_good_name("Taj") == True
assert is_good_name("Io") == False
assert is_good_name(" George") == False
assert is_good_name("John!") == False
assert is_good_name("MarY") == False
assert is_good_name("george") == False
assert is_good_name("Alexander") == True



def unique_order(s):
    """
    Given a string, return a list of unique characters from s,
    sorted by frequency of the character, ignoring capitalization.
    If having both, lower and upper characters, put lower character
    into unique list. If several characters have same frequencies,
    sort them according their ascii value.

    Note: pass any not alpabetic characters.

    For example:
    >>> unique_order("Hello") == ['l', 'H', 'e', 'o']
    >>> unique_order("aBcc123!") == ['c', 'B', 'a']
    """
    letters = []
    for i in s:
        if not i.isalpha(): continue
        if i not in letters:
            if i.isupper():
                if i.lower() in letters: continue
            if i.upper() in letters:
                letters.remove(i.upper())                
            letters += [i]
    letters = sorted(sorted(letters), key=lambda x: s.count(x.lower()) + s.count(x.upper()), reverse=True)
    return letters

assert unique_order("Hello") == ['l', 'H', 'e', 'o']
assert unique_order("Hello world") == ['l', 'o', 'H', 'd', 'e', 'r', 'w']
assert unique_order("aaa") == ['a']
assert unique_order("AAA") == ['A']
assert unique_order("AaA") == ['a']
assert unique_order("aBcc123!") == ['c', 'B', 'a']
assert unique_order("") == []



def no_doubled_the_highest(arr):
    """
    You are given an array arr of non-negative integers.
    Your task is to remove all the_highest numbers, and return
    a new array, where each element is doubled.
    Note: keep the order of original array.
    
    >>> no_doubled_the_highest([1, 2, 3, 4, 5]) == [2, 8]
    >>> no_doubled_the_highest([]) == []
    """
    def is_the_highest(num):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0: return False
            return True
        return False
    print(
    [2 * x for x in arr if not is_the_highest(x)]
    )
    return [2 * x for x in arr if not is_the_highest(x)]

assert no_doubled_the_highest([1, 2, 3, 4, 5]) == [2, 8]
assert no_doubled_the_highest([]) == []
assert no_doubled_the_highest([0,1,3,109]) == [0, 2]
assert no_doubled_the_highest([10,20,30]) == [20,40,60]
assert no_doubled_the_highest([11,333]) == [666]



def the_highest(boxes):
    """
    You are given an array of boxes, where each box
    is represented as an array in a form of [length, width, height]
    where length, width and height are positive integers.
    Return the box with the highest volume.
    Note: if several boxes have the highest volume,
    return the box with the highest height.
    If there is no boxes given, return None.

    >>> the_highest([]) == None
    >>> the_highest([[2,2,1],[1,2,2]]) == [1, 2, 2]
    """
    if not boxes: return None
    from numpy import prod
    boxes = sorted(boxes, key=lambda x:x[2], reverse=True)
    vols = [prod(i) for i in boxes]
    return boxes[vols.index(max(vols))]


assert the_highest([]) == None
assert the_highest([[2,2,1],[1,2,2]]) == [1, 2, 2]
assert the_highest([[1,2,3],[1,1,1]]) == [1, 2, 3]
assert the_highest([[1,1,1],[1,1,1],[1,1,1]]) == [1, 1, 1]
assert the_highest([[1,1,1],[2,2,2],[3,3,3]]) == [3, 3, 3]
assert the_highest([[3,4,6], [90,43,52]]) == [90, 43, 52]
assert the_highest([[100,100,1],[1,2,2]]) == [100, 100, 1]
assert the_highest([[100,1,1],[1,2,2]]) == [100, 1, 1]
assert the_highest([[2,2,1]]) == [2,2,1]



def ascii_cipher(string):
    """
    Given a string of characters, return a new string,
    where each character has been converted to reversed ascii value.
    Each character should be separated by -
    Note: if ascii code ends with zeros, keep those zeros.
    
    Example:
    >>> ascii_cipher('Hi') == '27 501'
    >>> ascii_cipher('1 d') == '94 23 001'
    >>> ascii_cipher('') == ''
    """
    print(
        '-'.join([str(ord(i))[::-1] for i in string])
    )
    return '-'.join([str(ord(i))[::-1] for i in string])


assert ascii_cipher('Hi') == '27-501'
assert ascii_cipher('1 d') == '94-23-001'
assert ascii_cipher('') == ''
assert ascii_cipher('    ') == '23-23-23-23'
assert ascii_cipher('Hello World!!!') == '27-101-801-801-111-23-78-111-411-801-001-33-33-33'


def find_missing_number(arr):
    """
    You are given an array of positive integers in ascending order.
    It should represent an arithmetic progression.
    You will be given either an arithmetic progression,
    or progression that misses 1 number.
    If progression misses a number, return the missed number, else return None.
    It is guaranteed that there will be at least 3 numbers.

    Example:
    >>> find_missing_number([1,2,4]) == 3
    >>> find_missing_number([1,2,3]) == None
    """
    diff = [arr[i] - arr[i+1] for i in range(len(arr) - 1)]
    if len(set(diff)) == 1: return None
    print(diff)
    print(arr[diff.index(min(diff))] - max(diff))
    return arr[diff.index(min(diff))] - max(diff)

assert find_missing_number([1,2,4]) == 3
assert find_missing_number([1,2,3]) == None
assert find_missing_number([3,5,7,9]) == None
assert find_missing_number([3,5,9]) == 7
assert find_missing_number([3,7,9]) == 5



def verbalize(n):
    """
    Write a function that takes an integer n and returns the word
    representation of each digit separated by space.
    Note: for negative number, put 'minus' at the beginning.

    For example:
    >>> verbalize(2) == 'two'
    >>> verbalize(-12) == 'minus one two'
    >>> verbalize(100) == 'one zero zero'
    """
    digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
    print(
        ('minus ' if n < 0 else '') + ' '.join(digits[int(i)] for i in list(str(abs(n))))
    )
    return ('minus ' if n < 0 else '') + ' '.join(digits[int(i)] for i in list(str(abs(n))))

assert verbalize(2) == 'two'
assert verbalize(-12) == 'minus one two'
assert verbalize(100) == 'one zero zero'
assert verbalize(999) == 'nine nine nine'
assert verbalize(0) == 'zero'
assert verbalize(-0) == 'zero'
assert verbalize(-1234567890) == 'minus one two three four five six seven eight nine zero'



def sum_odds(n):
    """
    Given a non-negative integer n, return integer, which is obtained
    from reversing sum of all odds from 0 to n (inclusive).

    Examples:
    >>> sum_odds(0) == 0
    >>> sum_odds(1) == 1
    >>> sum_odds(7) == 61
    >>> sum_odds(20) == 1
    """
    return int(str(sum(i for i in range(n + 1) if i % 2))[::-1])

assert sum_odds(0) == 0
assert sum_odds(1) == 1
assert sum_odds(7) == 61
assert sum_odds(10) == 52
assert sum_odds(20) == 1



def reverse_string(s):
    """
    You are given a string s. If sum of ascii values of alphabetical
    characters is odd, return its reverse, else return the original string,
    with sorted characters by ascii value.
    Note: when summuing ascii values, ignore non-alphabetical characters.

    Example:
    >>> reverse_string("hello") == "hello"
    >>> reverse_string("hello!") == "!ehllo"
    """
    return s[::-1] if sum(ord(i) for i in s if i.isalpha()) % 2 else ''.join(sorted(s))

assert reverse_string("hello") == "ehllo"
assert reverse_string("hello!") == "!ehllo"
assert reverse_string("Hello World") == " HWdellloor"
assert reverse_string("a   ") == "   a"
assert reverse_string("aa  ") == "  aa"
assert reverse_string("") == ""
assert reverse_string("abcd") == "abcd"
assert reverse_string("abcde") == "edcba"
assert reverse_string("eabcde") == "abcdee"



def non_unique(arr):
    """
    Write a function that retains duplicates from a list.
    It should return the result in the same order as the input.
    
    Examples:
    >>> non_unique([1, 1, 2, 2, 2]) == [1, 1, 2, 2, 2]
    >>> non_unique([]) == []
    >>> non_unique([2, 2, 2, 1]) == [2, 2, 2]
    """
    print(
        [i for i in arr if arr.count(i) > 1]
    )
    return [i for i in arr if arr.count(i) > 1]


assert non_unique([1, 1, 2, 2, 2]) == [1, 1, 2, 2, 2]
assert non_unique([1, 2, 2, 1, 1]) == [1, 2, 2, 1, 1]
assert non_unique([]) == []
assert non_unique([2, 2, 2, 1]) == [2, 2, 2]
assert non_unique([-5,-2,-2,1,3,2,3,2,1,3]) == [-2, -2, 1, 3, 2, 3, 2, 1, 3]




def caesar_cipher(s):
    """
    Caesar cipher is a method in cryptography, when you
    choose a shift of intenger n, and every letter in a string,
    gets shifted to n places. For examples, if n is -1, all A's will
    be substituted with Z, and so on.
    Given a string s, shift is obtained by (sum of all ascii values of string) modulo 26.
    Note: apply caesar cipher only on alphabetical characters.

    Examples:

    >>> caesar_cipher('Hello World') == ''
    >>> caesar_cipher('ABC') == 'QRS'
    >>> caesar_cipher('') == ''
    """
    shift = sum(ord(i) for i in s) % 26
    result = ''
    for i in s:
        if not i.isalpha():
            result += i
            continue
        if (i.isupper()): result += chr((ord(i) + shift - 65) % 26 + 65)
        else: result += chr((ord(i) + shift - 97) % 26 + 97)
    return result
    

assert caesar_cipher('Hello World!') == 'Axeeh Phkew!'
assert caesar_cipher('ABC') == 'QRS'
assert caesar_cipher('') == ''
assert caesar_cipher('AbCdE') == 'JkLmN'
assert caesar_cipher('1234!@#AA') == '1234!@#WW'


def sum_perfect_squares(n):
    """
    In mathematics, a square number or perfect square is an integer that is the square of an integer.
    Given a positive integer n, return (sum of all perfect squares from 0 to n inclusive) raised to the power of two.

    Examples:

    >>> sum_perfect_squares(4) == 25
    >>> sum_perfect_squares(1) == 1
    """
    return sum(i for i in range(n + 1) if not (i ** .5 % 1)) ** 2


assert sum_perfect_squares(4) == 25
assert sum_perfect_squares(1) == 1
assert sum_perfect_squares(100) == 148225
assert sum_perfect_squares(1000) == 108493056
assert sum_perfect_squares(400) == 8236900
assert sum_perfect_squares(500) == 14402025


def is_bluffing(txt):
    """
    A great but evil king is out to capture the princesses of the kingdom,
    so he sends them a threatening message 'txt'. However, evil has a curse.
    His messages also contain a secret key, that can check if he's bluffing or not.
    To get the secret key, sum all ascii values of the message 'txt', add
    sum of ascii values of sentence 'EVIL HAS A CURSE!!!'.
    Return True if sum of digits of secret key is even, else False.
    If txt is empty, return None.

    Examples:
    >>> is_bluffing("I'll destroy your kingdom!") == True
    >>> is_bluffing("") == None
    """
    if not txt: return None
    key = str(sum(ord(i) for i in txt) + sum(ord(i) for i in "EVIL HAS A CURSE!!!"))
    return False if sum(int(i) for i in key) % 2 else True

assert is_bluffing("I'll destroy your kingdom!") == False
assert is_bluffing("") == None
assert is_bluffing("I am bluffing") == True
assert is_bluffing("I want to give you a gift") == True
assert is_bluffing("I am not an evil king") == True
assert is_bluffing("111") == True
assert is_bluffing("1") == False
assert is_bluffing("1111") == True
assert is_bluffing("Evil has been cursed") == True
assert is_bluffing("Evil has stolen thousands of princesses") == True
assert is_bluffing(" ") == False
assert is_bluffing("  ") == True
assert is_bluffing("   ") == False
assert is_bluffing("    ") == True



def magic_reverser(txt):
    """
    You are given a sentence of words separated by a single space.
    Create a function that reverses each word in the sentence if it
    has odd sum of ascii values, else leave it as it is. Keep the
    order of words as in the original sentence. After reversing,
    some of the words in the sentence, reverse whole sentence and return it.
    Note: word is considered to be a group of characters separated by space.

    Examples:
    magic_reverser("Hello World") == "Hello !dlroW"
    magic_reverser("See you tomorrow!") == "eeS uoy tomorrow!"
    magic_reverser("") == ""
    """
    return ' '.join([i[::-1] if sum(ord(j) for j in i) % 2 else i for i in txt.split()])[::-1]

assert magic_reverser("Hello World!") == "World! olleH"
assert magic_reverser("See you tomorrow!") == "!worromot you See"
assert magic_reverser("") == ""
assert magic_reverser("13") == "31"
assert magic_reverser("135") == "135"



def powered(n):
    """
    Write a function that takes an integer n and raises to the power of X.
    To obtain X, convert n to string, sum ascii values, and find it's modulo 5.
    
    Examples:
    >>> powered(0) == 0
    >>> powered(-1) == 1
    """
    return n ** (sum(ord(i) for i in str(n)) % 5)

assert powered(0) == 0
assert powered(-1) == 1
assert powered(500) == 62500000000
assert powered(1) == 1
assert powered(2) == 1
assert powered(3) == 3
assert powered(4) == 16
assert powered(5) == 125
assert powered(6) == 1296
assert powered(7) == 1


def rainbow(n):
    """
    A rainbow is a colorful display of light caused by reflection, refraction
    and dispersion of light in drops of water suspended in the air.
    
    You will be given a non-negative integer n, which will represent the size of the rainbow.
    Based on the size of rainbow, return its string representation.
    Rainbow of size 0 mean there is no rainbow at all, so empty string should be returned.
    For size 4, you should return string that contains 4 integers, separated by space === '1 2 2 1'.
    String should start with 1, and increase by 1 as it reaches the middle,
    and decreases until it ends up with 1.

    >>> rainbow(0) == ''
    >>> rainbow(1) == '1'
    >>> rainbow(2) == '1 1'
    >>> rainbow(5) == '1 2 3 2 1'
    """
    
    from math import ceil
    res = [i + 1 for i in range(ceil(n / 2))]
    res += (res[::-1][1:] if n % 2 else res[::-1])
    return ' '.join(str(i) for i in res)

assert rainbow(0) == ''
assert rainbow(1) == '1'
assert rainbow(2) == '1 1'
assert rainbow(5) == '1 2 3 2 1'
assert rainbow(10) == '1 2 3 4 5 5 4 3 2 1'
assert rainbow(20) == '1 2 3 4 5 6 7 8 9 10 10 9 8 7 6 5 4 3 2 1'
assert rainbow(19) == '1 2 3 4 5 6 7 8 9 10 9 8 7 6 5 4 3 2 1'



def mix(a, b):
    """
    Given two strings "a" and "b", get the mix of "a" and "b", such
    that the 1st character is taken from 1st letter of "a",
    then 2nd is from 1st letter of "b", 3rd is from 2nd of "a", and so on.
    If any of the words run out of characters, you should add 1st letter of
    remaining character to the beginning, 2nd to the end, and 3rd to the beginning and so on.

    For example:
    >>> mix("", "abc") == "cab"
    >>> mix("abcd", "efgh") == "aebfcgdh"
    >>> mix("", "") == ""
    """
    res = ''
    temp_a, temp_b = list(a), list(b)
    while temp_a and temp_b: res += temp_a.pop(0) + temp_b.pop(0)
    switch = False
    while temp_a:
        res = (res + temp_a.pop(0)) if switch else (temp_a.pop(0) + res)
        switch = not switch
    while temp_b:
        res = (res + temp_b.pop(0)) if switch else (temp_b.pop(0) + res)
        switch = not switch
    return res
            
assert mix("", "abc") == "cab"
assert mix("abcd", "efgh") == "aebfcgdh"
assert mix("abc", "d") == "badc"
assert mix("Hello World!", "Python") == "drWHPeyltlhoo nol!"
assert mix("", "") == ""




def minimize_loss(billed, coins):
    """
    You will be given non-negative integer "billed", and
    array of positive integers "coins". You were billed
    for "billed" dollars, and want to pay. You have coins,
    given in array "coins". Return None, if you do not have
    enough money, or return list of coins, that will be enough
    to pay the bill. You might not have such combination of
    coins that will be equal to the billed amount, so return
    array of coins, such that you will lose minimum amount of money.
    For several equal combinations with minimum possible amount, choose one
    that has minimum sum of squares of coins.
    Note: return combination of coins in ascending order.

    For example:
    >>> minimize_loss(1, []) == None
    >>> minimize_loss(0, [1]) == [] 
    >>> minimize_loss(5, [5, 1]) == [5] 
    >>> minimize_loss(4, [5, 6]) == [5]
    >>> minimize_loss(5, [1,1,1,1,1,5]) == [1,1,1,1,1] 
    """
    if sum(coins) < billed: return None
    if not billed: return []
    from itertools import combinations
    combs = []
    for i in range(len(coins)): combs += list(combinations(coins, i + 1))
    combs = list(filter(lambda x: sum(x) >= billed, combs))
    min_loss = sum(combs[0])
    for i in combs[1:]:
        if sum(i) < min_loss: min_loss = sum(i)
    combs = list(filter(lambda x: sum(x) == min_loss, combs))
    return sorted(list(sorted(combs, key=lambda x: sum(i**2 for i in x)))[0])

    
assert minimize_loss(1, []) == None
assert minimize_loss(0, [1]) == []
assert minimize_loss(5, [5, 1]) == [5] 
assert minimize_loss(4, [5, 6]) == [5]
assert minimize_loss(5, [1,1,1,1,1,5]) == [1,1,1,1,1]



def find_submatrices(n):
    """
    You are given an positive integer n.
    You need to imagine n by n matrix, and return
    number of all possible squared submatrices.

    If n is 3:

    1 2 3
    4 5 6
    7 8 9

    There are 14 possible squared submatrices: 9 1x1 matrices
                                            + 4 2x2 matrices
                                            + 1 3x3 matrices.
    >>> find_submatrices(1) == 1
    >>> find_submatrices(2) == 5
    >>> find_submatrices(3) == 14
    """
    return sum(i ** 2 for i in range(n + 1))

assert find_submatrices(1) == 1
assert find_submatrices(2) == 5
assert find_submatrices(3) == 14
assert find_submatrices(4) == 30
assert find_submatrices(100) == 338350
assert find_submatrices(1000) == 333833500



def median_mean_diff(arr):
    """
    Given an array of integers, return difference between its mean and median.
    For empty array, return None.
    Note: round the result up to 2 floating points.
    """
    from statistics import median, mean
    return round(abs(median(arr) - mean(arr)), 2) if arr else None

assert median_mean_diff([]) == None
assert median_mean_diff([1]) == 0
assert median_mean_diff([1,1,1,1]) == 0
assert median_mean_diff([1,2,3,4]) == 0
assert median_mean_diff([1,2,3,4,5]) == 0
assert median_mean_diff([8,1,4,-100,32, 9]) == 13.67


def missing_nums(arr):
    """
    Given an array of integer, return number of all integers,
    between min and max value of arr, that are not in arr.
    If arr has less than 2 unique items, return None.

    Examples:
    >>> missing_nums([-1, 1, 2, 3]) == 1
    >>> missing_nums([1, 8]) == 6
    >>> missing_nums([1, 1]) == None
    """
    arr = sorted(set(arr))
    if len(arr) < 2: return None
    return max(arr) - min(arr) - len(arr) + 1
    
assert missing_nums([-1, 1, 2, 3]) == 1
assert missing_nums([1, 8]) == 6
assert missing_nums([1, 1]) == None
assert missing_nums([]) == None
assert missing_nums([90,31]) == 58
assert missing_nums([-10**31,10**31]) == 19999999999999999999999999999999


def string_modification(string):
    """
    Create a function that takes a string as input and returns a new string
    with the letters of the input string in the same order, but with the following
    modifications:

        * The first letter of the string should be swapped with the letter after it.
        * The pre_prelast letter of the string should be swapped with the letter before it.
        * If length of the string is even, reverse the string.

    If there length of string is less than 2, return None.

    Examples:

    >>> string_modification("alpha") == "lapah"
    >>> string_modification("abcdef") == "efdcab"
    >>> string_modification("") == None
    >>> string_modification("a") == None
    """
    if len(string) < 2: return None
    a = list(string)
    a[0], a[1] = a[1], a[0]
    a[-1], a[-2] = a[-2], a[-1]
    a = ''.join(a)
    return a if len(a) % 2 else a[::-1]


assert string_modification("alpha") == "lapah"
assert string_modification("abcdef") == "efdcab"
assert string_modification("") == None
assert string_modification("a") == None 
assert string_modification("Hello World!") == "d!lroW ollHe"



def count_complements(arr, n):
    """
    You are given an array of integers and a digit n.
    Return number of all integers, between min and max value of arr,
    that are not in arr, and do not contain digit n.
    If arr has less than 2 unique items, return None.

    Examples:

    >>> count_complements([1, 1], 2) == None
    >>> count_complements([1, 4, 5], 3) == 1
    >>> count_complements([1, 20], 6) == 16
    """

    arr = sorted(set(arr))
    if len(arr) < 2: return None
    res = 0
    for i in range(min(arr) + 1, max(arr)):
        if i in arr or str(n) in str(i): continue
        res += 1
    return res


assert count_complements([1, 1], 2) == None
assert count_complements([1, 4, 5], 3) == 1
assert count_complements([1, 20], 6) == 16
assert count_complements([-45, -12, 32, 32], 0) == 67
assert count_complements([1], 2) == None
assert count_complements([], 2) == None



def is_combination(a, b):
    """
    Complete the function that takes two integers a and b and returns
    true if they are a valid combination, false otherwise.
    Combination is valid if:
        
        * their sum is even
        * their product is odd
        * a modulo b is not equal to b modulo a

    For example:
    >>> is_combination(5, 5) == False
    >>> is_combination(5, 3) == True
    >>> is_combination(5, 6) == False
    >>> is_combination(5, 3) == True
    """
    return (a + b) % 2 == 0 and (a * b) % 2 == 1 and (a % b) != b % a

assert is_combination(5, 5) == False
assert is_combination(5, 3) == True
assert is_combination(5, 6) == False
assert is_combination(5, 3) == True
assert is_combination(0, 0) == False
assert is_combination(8, 12) == False
assert is_combination(7, 13) == True

def first_alpha(string):
    """
    Given a string of characters, return product of index of the 
    first alphabetical character multiplied by its ascii code.
    If string is empty or there is not alphabetical characters, return None.
    Note: indexing starts from ascii code of the first character.

    Example:
    >>> first_alpha('Python') == 6400
    >>> first_alpha('<3 love') == 6804
    >>> first_alpha('<3') == None
    """
    if not string: return None
    index = ord(string[0])
    for i in string:
        if i.isalpha() and i.isupper():
            print(ord(i) *index)
            return ord(i) * index 
            
        index += 1
    return None


assert first_alpha('Python') == 6400
assert first_alpha('<3 love') == None
assert first_alpha('<3') == None
assert first_alpha('123456789') == None
assert first_alpha('1a1') == None
assert first_alpha('') == None
assert first_alpha('123A') == 3380


def sort_list(arr):
    """
    Given a list of positive integers, return it
    sorted by the sum of their digits in MAX_MIN_MAX order.
    MAX_MIN_MAX order is an array where 1st item is max, 2nd is min,
    3rd is the 2nd max and so on.

    Examples:
    >>> sort_list([]) == []
    >>> sort_list([11,1,7,1]) == [7, 1, 11, 1]
    """
    arr = sorted(sorted(arr), key=lambda x: sum(int(i) for i in str(x)))
    switch, res = True, []
    for _ in range(len(arr)):
        res += [arr.pop(-1) if switch else arr.pop(0)] 
        switch = not switch
    return res


assert sort_list([]) == []
assert sort_list([11,1,7,1]) == [7, 1, 11, 1]
assert sort_list([1,3,23,42,5,7,4,90]) == [90, 1, 7, 3, 42, 4, 23, 5]
assert sort_list([55,4,2,4,1,23,5]) == [55, 1, 23, 2, 5, 4, 4]
assert sort_list([4,4,4,4,4,22,22,22]) == [22, 4, 22, 4, 22, 4, 4, 4]
assert sort_list([1,10,1,10,10,1]) == [10, 1, 10, 1, 10, 1]


def minimize_loss(billed, coins):
    """
    You will be given non-negative integer "billed", and
    array of positive integers "coins". You were billed
    for "billed" dollars, and want to pay. You have coins,
    given in array "coins". Return None, if you do not have
    enough money, or return list of coins, that will be enough
    to pay the bill. You might not have such combination of
    coins that will be equal to the billed amount, so return
    array of coins, such that you will lose minimum amount of money.
    For several equal combinations with minimum possible amount, choose one
    that has minimum sum of squares of coins.
    Note: return combination of coins in ascending order.

    For example:
    >>> minimize_loss(1, []) == None
    >>> minimize_loss(0, [1]) == [] 
    >>> minimize_loss(5, [5, 1]) == [5] 
    >>> minimize_loss(4, [5, 6]) == [5]
    >>> minimize_loss(5, [1,1,1,1,1,5]) == [1,1,1,1,1] 
    """
    if sum(coins) < billed: return None
    if not billed: return []
    from itertools import combinations
    combs = []
    for i in range(len(coins)): combs += list(combinations(coins, i + 1))
    combs = list(filter(lambda x: sum(x) >= billed, combs))
    min_loss = sum(combs[0])
    for i in combs[1:]:
        if sum(i) < min_loss: min_loss = sum(i)
    combs = list(filter(lambda x: sum(x) == min_loss, combs))
    return sorted(list(sorted(combs, key=lambda x: sum(i**2 for i in x)))[0])


assert minimize_loss(1, []) == None
assert minimize_loss(0, [1]) == []
assert minimize_loss(5, [5, 1]) == [5] 
assert minimize_loss(4, [5, 6]) == [5]
assert minimize_loss(5, [1,1,1,1,1,5]) == [1,1,1,1,1] 
assert minimize_loss(56, [1,3,4]) == None
assert minimize_loss(56, [1,3,4,5,6,3,42,12,3]) == [1, 3, 3, 3, 4, 42]
assert minimize_loss(32, [8,8,7,31]) == [7, 31]



is_prime = lambda n: n > 1 and all(n%i != 0 for i in range(2, not))



def sort_by_digits(arr):
    """
    Write a function that sorts an array of integers
    by their digit's sum in ascending order. For negative numbers,
    ignore minus sign when calculating digit's sum.
    Note: if several integers have same digit's sum, sort according their decimal representation, also in ascending order.

    For example:
    >>> sort_by_digits([10,1,-2,11,3,-11]) == [1, 10, -11, -2, 11, 3]
    >>> sort_by_digits([]) == []
    """
    return sorted(sorted(arr), key=lambda x: (sum(int(i) for i in str(abs(x))), x))

assert sort_by_digits([10,1,-2,11,3,-11]) == [1, 10, -11, -2, 11, 3]
assert sort_by_digits([]) == []
assert sort_by_digits([1,1,2,-3,4,1,-24,6,-72,9,14]) == [1, 1, 1, 2, -3, 4, 14, -24, 6, -72, 9]
assert sort_by_digits([1,11,11,1,-1,-11,-11,-10]) == [-10, -1, 1, 1, -11, -11, 11, 11]
assert sort_by_digits([7,34,-43,-700,70,-601]) == [-700, -601, -43, 7, 34, 70]
assert sort_by_digits([-11,-10,1,-2,11,3]) == [-10, 1, -11, -2, 11, 3]


def ascii_cipher(string):
    """
    Given a string of characters, return a new string,
    where each character of a 'word' has been converted to reversed ascii value.
    Each character should be separated by -, and spaces should stay as they were before.
    Word is considered to be a substring, that is separated by spaces.
    Note: if ascii code ends with zeros, keep those zeros.
    
    Example:
    >>> ascii_cipher('Hi!') == '27-501-33'
    >>> ascii_cipher('1  d') == '94  001'
    >>> ascii_cipher('') == ''
    """
    return ' '.join([('-'.join([str(ord(j))[::-1] for j in i]) if i else i) for i in string.split(' ')])

assert ascii_cipher('w') == '911'
assert ascii_cipher('Hi!') == '27-501-33'
assert ascii_cipher('1  d') == '94  001'
assert ascii_cipher('') == ''
assert ascii_cipher('    ') == '    '
assert ascii_cipher('Hello  World!!!') == '27-101-801-801-111  78-111-411-801-001-33-33-33'


def the_highest(boxes):
    """
    You are given an array of boxes, where each box
    is represented as an array in a form of [length, width, height]
    where length, width and height are positive integers.
    Return the box with the highest volume.
    Note: if several boxes have the highest volume,
    return the box with the highest height.
    For boxes with same height, choose with the max length.
    If there is no boxes given, return None.

    >>> the_highest([]) == None
    >>> the_highest([[2,2,1],[1,2,2]]) == [1, 2, 2]
    """
    if not boxes: return None
    from numpy import prod
    boxes = sorted(boxes, key=lambda x: x[0],)
    boxes = sorted(boxes, key=lambda x: x[2])
    boxes = sorted(boxes, key=lambda x: prod(x))
    return boxes[-1]

assert the_highest([]) == None
assert the_highest([[2,2,1],[1,2,2]]) == [1, 2, 2]
assert the_highest([[1,2,3],[1,1,1]]) == [1, 2, 3]
assert the_highest([[1,1,1],[1,1,1],[1,1,1]]) == [1, 1, 1]
assert the_highest([[1,1,1],[2,2,2],[3,3,3]]) == [3, 3, 3]
assert the_highest([[3,4,6], [90,43,52]]) == [90, 43, 52]
assert the_highest([[100,100,1],[1,2,2]]) == [100, 100, 1]
assert the_highest([[100,1,1],[1,2,2]]) == [100, 1, 1]
assert the_highest([[2,2,1]]) == [2,2,1]
assert the_highest([[2,2,4], [1,4,4]]) == [2, 2, 4]



def string_to_hex(s):
    """
    Given a string "s", return its string representation in base 16.
    To represent it in base 16, you should convert each character's
    ascii code to base 16. Following that, each character in original
    string should be replaced by its hex value.
    Each character should be separated by '-', despite blank spaces,
    they should not be converted to base 16.

    Note: all character are in lowercase, e.g. 10 base 10 is "a" base 16.
    
    >>> string_to_hex("HELLO WORLD!") == "48-45-4c-4c-4f 57-4f-52-4c-44-21"
    >>> string_to_hex("! @ #") == "21 40 23"
    >>> string_to_hex("") == ""
    """
    return ' '.join('-'.join(hex(ord(j))[2:] for j in i) if i else i for i in s.split(' '))

assert string_to_hex("hello") == "68-65-6c-6c-6f"
assert string_to_hex("   ") == "   "
assert string_to_hex("! @ #") == "21 40 23"
assert string_to_hex("") == ""
assert string_to_hex("HELLO WORLD!") == "48-45-4c-4c-4f 57-4f-52-4c-44-21"



def starpoints(n):
    """
    You want draw a star on a Cartesian plot
    with 4 lines (2 on xy axis, 2 on diagonals).
    You are given a positive integer n,
    which is the length of the half of each of the 4 lines.
    Based on point (0, 0) return list of tuples (x, y),
    representing each of the 8 ends of 4 lines.
    Ordering is in clockwise order starting from the northest point.
    Note: round coordinates up to 2 floating points.
    
    >>> starpoints(1) == [(0, 1), (0.71, 0.71), (1, 0), (0.71, -0.71), (0, -1), (-0.71, -0.71), (-1, 0), (-0.71, 0.71)]
    """
    coords = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    res = []
    half_diag = round(((n**2)*.5)**.5, 2)
    for i in coords:
        if not (i[0] and i[1]): res += [(n * i[0], n * i[1])]
        else: res += [(half_diag * i[0], half_diag * i[1])]
    return res
    

assert starpoints(1) == [(0, 1), (0.71, 0.71), (1, 0), (0.71, -0.71), (0, -1), (-0.71, -0.71), (-1, 0), (-0.71, 0.71)]
assert starpoints(2) == [(0, 2), (1.41, 1.41), (2, 0), (1.41, -1.41), (0, -2), (-1.41, -1.41), (-2, 0), (-1.41, 1.41)]
assert starpoints(5) == [(0, 5), (3.54, 3.54), (5, 0), (3.54, -3.54), (0, -5), (-3.54, -3.54), (-5, 0), (-3.54, 3.54)]
assert starpoints(100) == [(0, 100), (70.71, 70.71), (100, 0), (70.71, -70.71), (0, -100), (-70.71, -70.71), (-100, 0), (-70.71, 70.71)]
assert starpoints(8900) == [(0, 8900), (6293.25, 6293.25), (8900, 0), (6293.25, -6293.25), (0, -8900), (-6293.25, -6293.25), (-8900, 0), (-6293.25, 6293.25)]

from sympy.ntheory import isprime
from sympy.ntheory import factorint



def is_smooth(n):
    """
    A number is "smooth" if its all digits are odds,
    or if number is composed with only 1 digit.
    Given a positive integer "n", return True if it is smooth, else False.

    Examples:
    >>> is_smooth(1) == True
    >>> is_smooth(888) == True
    >>> is_smooth(135) == True
    """
    if len(set(str(n))) == 1 or all(int(i) % 2 for i in str(n)): return True
    return False

assert is_smooth(1) == True
assert is_smooth(888) == True
assert is_smooth(135) == True
assert is_smooth(1358) == False
assert is_smooth(4) == True
assert is_smooth(991) == True
assert is_smooth(992) == False
assert is_smooth(444) == True



def pseudo_random(s):
    """
    Ascii value of a string is sum of ascii codes of characters.
    You are given a list of strings, and you need
    to randomly choose some of the strings.
    You want to imitate randomness of your choice, and to do
    that, find ascii codes of each word, and if sum of differences
    of ascii values of a chosen word with others is even,
    you decide to keep the word in returninglist, else exclude it.
    Also, keep the order of strings, as in the original array.

    Examples:
    >>> pseudo_random(["cat", "dog", "dogs"]) == ['cat', 'dog']
    >>> pseudo_random([""]) == []
    >>> pseudo_random([]) == []
    """
    ascii_codes = [sum(map(ord, i)) for i in s]
    res = []
    for i in range(len(s)):
        if sum(abs(ascii_codes[i] - ascii_codes[j]) for j in range(len(s))) % 2 == 0: res += [s[i]]
    return res


assert pseudo_random(["cat", "dog", "dogs"]) == ['dogs']
assert pseudo_random([""]) == ['']
assert pseudo_random([]) == []
assert pseudo_random(["1", "12", "123"]) == ['123']
assert pseudo_random(["123", "12", "1", "1234", "12345"]) == ['12', '1', '12345']
assert pseudo_random(["1", "12", "123", '321']) == ['1', '12', '123', '321']


def preprocess_str(s):
    """
    You are given a string s.
    Write a function that returns the preprocessed version of that string.
    The function should first remove the blank spaces.
    Then, it should convert the string to lowercase.
    Then, it should replace the non-alphabetic characters with spaces,
    and if there are substrings with same adjacent characters, compress to only one character.

    Examples:
    >>> preprocess_str("Thiiiis is a striiiing!!!") == "thisisastring "
    >>> preprocess_str("") == ""
    """
    import re
    s = s.replace(' ','')
    s = s.lower()
    s = re.sub(r'[^a-z]',' ',s)
    s = re.sub(r'(.)\1+',r'\1',s)
    return s


assert preprocess_str("Thiiiis is a striiiing!!!") == "thisisastring "
assert preprocess_str("") == ""
assert preprocess_str("!@#  !@#") == " "
assert preprocess_str("!!!!!!@#AAbA") == " aba"
assert preprocess_str("Hell o Wo r  ld!!!") == "heloworld "




def prime_factorization(n):
    """
    Given an integer n, return an array of its
    prime factors in ascending order.
    Note: for negative number, put -1 into an array.

    For example:
    >>> prime_factorization(1) == 0
    >>> prime_factorization(-113) == 0
    >>> prime_factorization(1000) == 0
    """
    from sympy.ntheory import factorint
    factors, res = factorint(n), []
    for i in factors: res += [i] * factors[i]
    return sorted(res)

assert prime_factorization(1) == []
assert prime_factorization(-113) == [-1, 113]
assert prime_factorization(1000) == [2, 2, 2, 5, 5, 5]
assert prime_factorization(0) == [0]
assert prime_factorization(999) == [3, 3, 3, 37]
assert prime_factorization(-777) == [-1, 3, 7, 37]




def xor(A, B):
    """
    You are given 2 arrays of integers, each of them having
    at least 2 integers. xor of an array is obtained by:
        1) find all adjecent pairs, e.g. pairs of [1,2,3] is (1,2) and (2,3)
        2) each pair will have an xor value (1 or 0).
        1 if only one of them is even, else 0.
        3) sum of xor values of all adjecent pairs, is an xor of an array.
    Return [a, b], where a is xor of A, and b is xor of B.

    For example:
    >>> xor([1,2,3], [4,5,6]) == [2, 2]
    >>> xor([1,3,7,3], [3,4,-1,3]) == [0, 2]
    """
    def xor_value(arr):
        pairs = [(arr[i], arr[i+1]) for i in range(len(arr)-1)]
        return sum(1 for i in pairs if (sum(i) % 2))
    return [xor_value(A), xor_value(B)]


assert xor([1,2,3], [4,5,6]) == [2, 2]
assert xor([1,3,7,3], [3,4,-1,3]) == [0, 2]
assert xor([1,2,3,4], [5,6,7,8]) == [3, 3]
assert xor([-8,9,0,1,7], [7,7]) == [3, 0]

def perfectly_squared(numbers):
    """
    Given an array of integers, return number of perfect squares squared.
    Note: for this problem, zero is considered to be a perdect square.

    Examples:
    >>> perfectly_squared([0,1,2,3,4]) == 9
    >>> perfectly_squared([]) == 0
    """
    return len([i for i in numbers if i >= 0 and not ((i ** .5) % 1) ]) ** 2

assert perfectly_squared([0,1,2,3,4]) == 9
assert perfectly_squared([]) == 0
assert perfectly_squared([0,1,2,3,4,9,16]) == 25
assert perfectly_squared([0,1,2,3,4,9,16, -5, -9]) == 25
assert perfectly_squared([-9,-1,-3,-4,-5, 0]) == 1


def prime_sum(arr):
    """
    Given an array of integers, return sum of prime numbers.
    
    Examples:
    >>> prime_sum([-7, 0, 1, 2, 3, 4, 5]) == 10
    >>> prime_sum([]) == 0
    """
    from sympy.ntheory import isprime
    return sum(i for i in arr if isprime(i))

assert prime_sum([-7, 0, 1, 2, 3, 4, 5]) == 10
assert prime_sum([]) == 0
assert prime_sum([10019369, 10019363, 10019357]) == 30058089



def can_sort(arr):
    """
    Given a list of non-negative integers arr, return True
    if it is possible to sort it in strictly increasing order
    by decreasing the values. You can decrease any integer,
    not lower than zero, or leave it as it is.
    Note: [2, 2] array is not in increasing order.

    Examples:
    >>> can_sort([2,3,1,99]) == False
    >>> can_sort([2,3,2,4,4]) == True
    >>> can_sort([1]) == True
    >>> can_sort([]) == True
    """
    n = 0
    for i in arr:
        if i < n: return False
        n += 1
    return True


assert can_sort([2,3,1,99]) == False
assert can_sort([2,3,2,4,4]) == True
assert can_sort([1]) == True
assert can_sort([]) == True
assert can_sort([0, 0]) == False
assert can_sort([99,99,99]) == True
assert can_sort([0]) == True

def biased_arithmetic_mean(arr):
    """
    Given an array of integers, return its arithmetc mean.
    If the mean is not a whole number, you should apply biased rounding.
    If the first digit after a floating point is even,
    round mean to its ceil, else to its floor.
    Note: return None if arr is empty.

    Examples:
    >>> biased_arithmetic_mean([2, 3]) == 2
    >>> biased_arithmetic_mean([2, 4, 5]) == 4
    """
    from math import ceil, floor
    if not arr: return None
    mean = sum(arr) / len(arr)
    if mean == int(mean): return mean
    return floor(mean) if int(str(mean).split('.')[1][0]) % 2 else ceil(mean)

assert biased_arithmetic_mean([2, 3]) == 2
assert biased_arithmetic_mean([2, 4, 5]) == 4
assert biased_arithmetic_mean([1, 1, 1]) == 1
assert biased_arithmetic_mean([]) == None
assert biased_arithmetic_mean([1,2,3]) == 2
assert biased_arithmetic_mean([0]) == 0
assert biased_arithmetic_mean([1,1,1,1,1,1,74]) == 12
assert biased_arithmetic_mean([1,1,1,1,72]) == 16



def reverse_digits(arr):
    """
    Given an array of non-negative integers,
    You need to return new array, where integers
    obtained from original array, by finding sum
    of the integer's digits sum, and reversing it.
    Note: reverse of 10, is 1.

    >>> reverse_digits([1,23,55]) == [1, 5, 1]
    >>> reverse_digits([]) == []
    """
    return [int(str(sum(map(int, str(i))))[::-1]) for i in arr]

assert reverse_digits([1,23,55]) == [1, 5, 1]
assert reverse_digits([]) == []
assert reverse_digits([20,10,40,50]) == [2, 1, 4, 5]
assert reverse_digits([5,1,3,77,452,4,1,3,42]) == [5, 1, 3, 41, 11, 4, 1, 3, 6]



def bin2dec(n):
    """
    Create a function that takes an string
    representing a binary number, and returns its decimal value.
    First character is representing sign, such that
    '1' means negative, '0' positive.
    Note: there is no sign for zero, so '0' is zero.
    It is guaranteed string will contain only '0's and '1's.

    Examples:
    >>> bin2dec('01') == 1
    >>> bin2dec('11101') == -13
    >>> bin2dec('010100') == 20
    """
    if n == '0': return 0
    return (1 if n[0] == '0' else -1) * int(n[1:], 2)

    
assert bin2dec('01') == 1
assert bin2dec('11101') == -13
assert bin2dec('010100') == 20
assert bin2dec('0') == 0
assert bin2dec('1101010101') == -341



def get_max_product(arr):
    """
    Given an array of integers, find the maximum product
    of any two integers in the array, and return them
    in array in ascending order. For several pairs,
    choose one that has maximum integer.

    Note: if arr has less than 2 items, return None.

    For example:
    >>> get_max_product([1]) == None
    >>> get_max_product([1, 2, 3, -3, -2]) == [2, 3]
    >>> get_max_product([1, 2, 3, -9, -8]) == [-9, -8]
    """
    if len(arr) < 2: return None
    from itertools import combinations
    combs = sorted(combinations(arr, 2), key=lambda x: x[0] * x[1])
    combs = list(filter(lambda x: x[0] * x [1] == combs[-1][0] * combs[-1][1], combs))
    return sorted(sorted(combs, key=max)[-1])

assert get_max_product([0]) == None
assert get_max_product([1]) == None
assert get_max_product([1, -6, -1]) == [-6, -1]
assert get_max_product([1, 2, 3, -3, -2]) == [2,3]
assert get_max_product([1, 1, 1, 1, 2, 3, 3, 3]) == [3,3]
assert get_max_product([1, 2, 3, 4]) == [3,4]
assert get_max_product([1, 2, 3, -9, -8]) == [-9, -8]
assert get_max_product([100, 2, 3, -9, -8]) == [3,100]


def scale(interval, n):
    """
    You are given a tuple "interval" containing 2 integers (a, b)
    and integer "n" > 1.
    Return list containing n values starting from a, and ending with b,
    equally distributed.
    Note: round values up to 2 floating points.

    Examples:
    >>> scale((1,1), 3) == [1, 1, 1]
    >>> scale((2,1), 4) == [2, 1.67, 1.34, 1]
    >>> scale((5, -1), 7) == [5, 4, 3, 2, 1, 0, -1]
    """
    if not n: return []
    step = (interval[1] - interval[0]) / (n - 1)
    res = [interval[0]]
    for _ in range(n-2): res += [round(res[-1] + step, 2)]
    return res + [interval[1]]

assert scale((1,1), 3) == [1, 1, 1]
assert scale((1,2), 2) == [1, 2]
assert scale((2,1), 4) == [2, 1.67, 1.34, 1]
assert scale((5, -1), 6) == [5, 3.8, 2.6, 1.4, 0.2, -1]
assert scale((5, -1), 7) == [5, 4, 3, 2, 1, 0, -1]


def reverse_sum(arr):
    """
    Given an array of non-negative integers,
    return reversed sum of reversed integers.

    >>> reverse_sum([12, 10, 32]) == 54
    >>> reverse_sum([]) == 0
    """
    return int(str(sum([int(str(i)[::-1]) for i in arr]))[::-1])

assert reverse_sum([12, 10, 32]) == 54
assert reverse_sum([]) == 0
assert reverse_sum([10,10,10]) == 3
assert reverse_sum([13,4,2,1,34,21]) == 39
assert reverse_sum([900000]) == 9



def weekday(date):
    """
    You are given string representing date in format of "dd/mm/yyyy".
    It is guaranteed year will start from year 0001.
    Note: if given date does not exist, return None.
    Return day of the week as a string.

    Examples:
    >>> weekday('07/08/0001') == "Tuesday"
    >>> weekday('29/02/2021') == None
    >>> weekday('16/07/4000') == "Sunday"
    """
    from datetime import datetime
    try: return datetime.strptime(date, '%d/%m/%Y').strftime('%A')
    except: return None

assert weekday('07/08/0001') == "Tuesday"
assert weekday('07/08/2020') == "Friday"
assert weekday('08/08/2020') == "Saturday"
assert weekday('09/08/2020') == "Sunday"
assert weekday('16/07/1998') == "Thursday"
assert weekday('16/07/4000') == "Sunday"
assert weekday('31/06/2020') == None
assert weekday('29/02/2021') == None


def largest_series(arr):
    """
    You will be given an array of integers.
    Find and return subarray with maximum
    number of integers, that form an arithmetic
    progression. For several subarrays with
    equal number of integers, return the most left subarray.
    Note: to form an arithmetic progression, you need
    at least 2 distinct integers.
    If there is no progression found, return None.

    Example:
    >>> largest_series([1,0,-1,2]) == [1, 0, -1]
    >>> largest_series([2,0,-2,2,5]) == [2, 0, -2]
    >>> largest_series([1,1,1]) == None
    """
    if len(arr) < 2: return None
    def is_progression(arr):
        step = arr[0] - arr[1]
        if not step: return False
        for i in range(1, len(arr) - 1):
            if arr[i] - arr[i+1] != step: return False
        return True
    res = None
    for i in range(len(arr) - 1):
        for j in range(i + 1):
            temp = arr[j:len(arr) - i + j]
            if is_progression(temp):
                if not res or len(temp) > len(res): res = temp
    return res
            

assert largest_series([1,4,2,-5,1,3,5]) == [1,3,5]
assert largest_series([1,0,-1,2]) == [1, 0, -1]
assert largest_series([1,0,-1,2,5]) == [1, 0, -1]
assert largest_series([1,1,1]) == None
assert largest_series([2,0,-2,2,5]) == [2, 0, -2]


def delete_character(n, s):
    """
    Given a string "s" and digit "n", obtain new string
    where all the characters which has a digit "n" in their ascii value,
    were removed. Return that string, e.g. given word "Hi" and n = 0,
    ascii value of 'i' is 105, which contains given digit. So you should return 'H'.

    Examples:
    >>> delete_character(0, "Hi") == "H"
    >>> delete_character(1, "") == ""
    >>> delete_character(1, "Hello World!!!") == "H W!!!"
    """
    return ''.join(i for i in s if str(n) not in str(ord(i)))

assert delete_character(0, "Hi") == "H"
assert delete_character(9, "leetcode") == "leetode"
assert delete_character(1, "") == ""
assert delete_character(1, "Hello World!!!") == "H W!!!"
assert delete_character(1, "eeeeeeee") == ""


def get_relative(n):
    """
    You will be given a positive integer and you have to return its relative.
    To find n's relative, sum its digits, reverse that sum, and return its
    reciprocal rounded up to 2 floating points.

    For example:
    >>> get_relative(5) == 0.2
    >>> get_relative(10000) == 1
    >>> get_relative(3) == 0.33
    """
    return round(1 / int(str(sum(int(i) for i in str(n)))[::-1]), 2)

assert get_relative(5) == 0.2
assert get_relative(15) == 0.17
assert get_relative(3) == 0.33
assert get_relative(1) == 1
assert get_relative(10000) == 1
assert get_relative(99999) == 0.02
assert get_relative(19) == 1
assert get_relative(91) == 1




def string_to_array(s):
    """
    You are given a string s, that might represent python array
    of integers. Your task is to return its array representation,
    or return None, if string is not valid array.
    String is said to be valid if you write it in
    python shell, and it will be accepted as an array of integers, or empty array.
    Note: for the sake of simplicity, string won't contain negative sign,
    and any special characters such as \n or \t.

    >>> string_to_array("[  1 ,  2 ,  3   ,   4,]") == [1, 2, 3, 4]
    >>> string_to_array("[1, 2, 3  4]") == None
    >>> string_to_array("[[,]") == None
    >>> string_to_array("[[]]") == None
    """
    arr = s.strip()
    if not arr: return None
    if arr[0] != '[' and arr[-1] != ']': return None
    arr = [i.strip() for i in arr[1:-1].split(',')]
    if not arr[-1]: arr = arr[:-1]
    for i in arr:
        if not i.isdigit(): return None
    return list(map(int, arr))



assert string_to_array("[1, 2, 3, 4,]") == [1, 2, 3, 4]
assert string_to_array("[1, 2, 3  4]") == None
assert string_to_array("[[,]") == None
assert string_to_array("[  1 ,  2 ,  3   ,   4,]") == [1, 2, 3, 4]
assert string_to_array("") == None
assert string_to_array("[]") == []
assert string_to_array("[1]") == [1]
assert string_to_array("[,]") == None
assert string_to_array("[[]]") == None


def lowest_number(arr):
    """
    Given an array of integers, return the "lowest" integer.
    To find the lowest integer, you need to obtain a special value
    for each integer, which is calculated by summing relative differences of its
    adjecent integers. Considering array [0, 3, 1, 4], special value
    for '1' will be (3-1) + (4-1), for '0' will be (3-0) etc.
    Integer with the greatest special value is considered to be the lowest.
    For several lowest integers, return with the lowest index.
    Note: if 'arr' has less than 2 items, return None.

    Examples:
    >>> lowest_number([0, 3, 1, 4]) == 1
    >>> lowest_number([-2, 3, 1, 4]) == -2
    >>> lowest_number([]) == None
    """
    if len(arr) < 2: return None
    res, special = 0, arr[1] - arr[0]
    if (arr[-2] - arr[-1]) > special:
        special, res = arr[-2] - arr[-1], -1
    for i in range(1, len(arr) - 1):
        if (arr[i-1] + arr[i+1] - 2 * arr[i]) > special:
            special, res = arr[i-1] + arr[i+1] - 2 * arr[i], i
    return arr[res]

assert lowest_number([0, 3, 1, 4]) == 1
assert lowest_number([-2, 3, 1, 4]) == -2
assert lowest_number([-2]) == None
assert lowest_number([]) == None
assert lowest_number([2,2]) == 2
assert lowest_number([2,1]) == 1


def to_remove(s):
    """
    We have to find the mininum number of characters to remove from the
    original string, to make it in a such way that its parity of the
    characters' ascii code will alternate. e.g. For string '1234' you do
    not have to remove any characters because parity is odd, even, odd, even.
    However, for '11234', you should return 1, as you need to remove 1 character.

    Examples:
    >>> to_remove("1234") == 0
    >>> to_remove("11234") == 1
    >>> to_remove("") == 0
    """
    if not s: return 0
    res, switch = 0, ord(s[0]) % 2
    for i in s[1:]:
        if (ord(i) % 2) == switch:
            res += 1
            continue
        switch = 0 if switch else 1
    return res

assert to_remove("1234") == 0
assert to_remove("11234") == 1
assert to_remove("") == 0
assert to_remove("1111111234444") == 9
assert to_remove("1") == 0
assert to_remove("Hello World!!!") == 6



def sorted_letters(s):
    """
    Given a string "s", return array of unique letters
    sorted by the frequency of the letters in ascending order,
    and if several letters have same frequencies, sort them
    based on their ascii code also in ascending order.
    Note: as only letters mentioned, ignore all non-alphabetic
    characters, and also capitalization is important.
    
    >>> sorted_letters('aabbc') == ['c', 'a', 'b']
    >>> sorted_letters('  1@#$34! ') == []
    """
    return sorted(sorted(list(set(i for i in s if i.isalpha()))), key=lambda x: s.count(x))

assert sorted_letters('aabbc') == ['c', 'a', 'b']
assert sorted_letters('  1@#$34! ') == []
assert sorted_letters('Alexander The Great!!!') == ['A', 'G', 'T', 'd', 'h', 'l', 'n', 't', 'x', 'a', 'r', 'e']
assert sorted_letters('AAAAlexander The Great!!!') == ['G', 'T', 'd', 'h', 'l', 'n', 't', 'x', 'a', 'r', 'A', 'e']
assert sorted_letters('') == []



def primes_within_sum(a, b):
    """
    Given 2 positive integers, where a <= b,
    return sum of primes, within range of [a, b] inclusive.

    >>> primes_within_sum(1,10) == 17
    >>> primes_within_sum(2,2) == 2
    >>> primes_within_sum(2,3) == 5
    """
    from sympy.ntheory import isprime
    print(
        sum(i for i in range(a, b + 1) if isprime(i))
    )
    return sum(i for i in range(a, b + 1) if isprime(i))

assert primes_within_sum(1,10) == 17
assert primes_within_sum(2,2) == 2
assert primes_within_sum(1,100) == 1060
assert primes_within_sum(100,200) == 3167
assert primes_within_sum(300,1000) == 67852
assert primes_within_sum(2,3) == 5
assert primes_within_sum(300,100000) == 454388262



def bs_to_pts(arr):
    from statistics import median, mean
    return mean(median(i) for i in arr)

assert bs_to_pts([[1, 2, 3]]) == 2
assert bs_to_pts([[9, 1, 2], [4, 4, 5]]) == 3


def find_difference(arr):
    """Write a function find_difference that takes a list of integers and return the              difference between the largest and smallest fibonacci numbers present in the list. It is      given that atleast two fibonacci numbers will be present in the list.
    Examples:
    find_difference([13, 5, 41, 34]) == 7
    find_difference([13, 34, 7, 13, 21]) == 21
    """
    arr = sorted(arr)
    fibs = [1,1]
    while (fibs[-1] + fibs[-2]) < arr[-1]: fibs+=[fibs[-1] + fibs[-2]]
    fibMax, fibMin = None, None
    for i in arr:
        if i in fibs:
            fibMin = i
            break
    for i in arr[::-1]:
        if i in fibs:
            fibMax = i
            break
    return fibMax - fibMin
    
assert find_difference([13, 5, 41, 34]) == 29
assert find_difference([13, 34, 7, 13, 21]) == 8


def play_game(board):
    """ Given a 2 x 2 board of positive integers, return True if the summation of the main diagonal is square and the other diagonal summation is prime.
    Otherwise, return False

    Examples:
    play_game([[0, 1],
            [2, 1]]) == True

    play_game([[2, 1],
            [2, 1]]) == False
    """
    from sympy.ntheory import isprime
    return (not (((board[0][0] + board[1][1]) ** .5) % 1)) and isprime(board[0][1] + board[0][1])
assert play_game([[0, 1],
            [2, 1]]) == True
            
assert play_game([[2, 1],
            [2, 1]]) == False

def scale(interval, n):
    """
    You are given a tuple "interval" containing 2 integers (a, b) and integer "n" > 1.
    Return list containing n values starting from a, and ending with b, equally distributed.
    Return None if any of the values are not integers.

    Examples:
    >>> scale((1,1), 3) == [1, 1, 1]
    >>> scale((2,1), 4) == None
    >>> scale((5, -1), 7) == [5, 4, 3, 2, 1, 0, -1]
    """
    if not n: return []
    elif n == 2: return [interval[0], interval[1]]
    step = (interval[1] - interval[0]) / (n - 1)
    if int(step) == step: step = int(step)
    if step and isinstance(step, float): return None
    res = [interval[0]]
    for _ in range(n-2): res += [res[-1] + step]   
    return res + [interval[1]]

assert scale((1,1), 3) == [1, 1, 1]
assert scale((1,2), 2) == [1, 2]
assert scale((2,1), 4) == None
assert scale((5, -1), 6) == None
assert scale((5, -1), 7) == [5, 4, 3, 2, 1, 0, -1]


def binary_search(arr, target, res=0):
    """
    You are given a sorted array of integers, and a target value as integer.
    Your task is to apply binary search algorithm, and return number
    of steps required to find the target using binary search algorithm.

    In binary search, you check the value in the middle (or, if even number
    of items, you check the pre_prelast value of the left half), and if that
    chosen value is target, return number of steps. If that value
    is greater, apply same thing to the left half, else right.
    Each array division is considered as 1 step.
    If target is not in arr, return None.

    >>> binary_search([], 2) == None
    >>> binary_search([1,2,3,4,5], 3) == 0
    >>> binary_search([1,2,3,4,5], 1) == 1
    >>> binary_search([1,2,3,4,5], 2) == 2
    """
    if not res and target not in arr: return None
    mid = int(len(arr) * .5) - (0 if len(arr) % 2 else 1)
    left, right = arr[:mid], arr[mid + 1:]
    if arr[mid] != target: return binary_search(right if target > arr[mid] else left, target, res + 1)
    return res


assert binary_search([], 2) == None
assert binary_search([1,2,3,4,5], 3) == 0
assert binary_search([1,2,3,4,5], 1) == 1
assert binary_search([-1,2,3,4,5], 2) == 2
assert binary_search([-1,2,3,4,5,6,7,8,9,10], 10) == 3
assert binary_search([-4, 5, 10], 2) == None
assert binary_search([-4, 5, 10], -4) == 1


def equalize(arr, avg):
    """
    Given an array of integers "arr", and integer "avg",
    find and return such x, that if you add that x into
    array and find the average, it will be equal to avg.

    >>> equalize([], 0) == 0
    >>> equalize([], 10) == 10
    >>> equalize([-1,-2,5], 3) == 10
    """
    if not arr: return avg
    return avg * (len(arr) + 1) - sum(arr)

assert equalize([], 0) == 0
assert equalize([], 10) == 10
assert equalize([-1,-2,5], 3) == 10
assert equalize([1,1,1,1,1,1,2], 3) == 16
assert equalize([1,1,1,1,1,1,2], 1) == 0
assert equalize([-10,-20,-30], -2) == 52
assert equalize([-1, 1], 1) == 3
assert equalize([-1, 1], 0) == 0


def success_score(days):
    """
    You are given an array of integers, that represents
    actions you've done for each day. There is a rule:
    your actions today, define your future. Success score
    for 1st day (arr[0]) is equal to arr[0], however,
    success score for rest of the days is equal to:
    arr[n] = arr[n-1] * arr[n].

    Return cumulative success score for given days.
    Note: return None for empty array.

    Examples:
    >>> success_score([]) == None
    >>> success_score([1,1,1]) == 3
    >>> success_score([1,-1,1]) == -1
    """
    if not days: return None
    return days[0] + sum(days[i+1] * days[i] for i in range(len(days[1:])))

assert success_score([]) == None
assert success_score([1,1,1]) == 3
assert success_score([1,-1,1]) == -1
assert success_score([3,4,2,3,5,1,3]) == 52
assert success_score([3,-4,2,3,-8,1,3]) == -40
assert success_score([3,-4,2,3,-2,1,3]) == -16
assert success_score([3,0,2,3,-2,1,3]) == 4
assert success_score([0, 2, 0]) == 0

def findMinPathSum(arr):
    """
    You are given an array of arrays "arr", which
    represents a squared matrix. Each entry is an
    integer. There are only 3 possible paths to
    go from top-left to bottom-right value:
        - go from top-left point to the bottom-left, then to the right till the end.
        - go from top-left point to the top-right, then to the bottom till the end.
        - go from top-left to the bottom-right (by diagonal).
    Path score is simply the sum of the values on the path, including start/end points.
    Return miminum path score.
    Note: return None for empty arr.

    >>> findMinPathSum([]) == None
    >>> findMinPathSum([[-1]]) == -1
    >>> findMinPathSum([[1,2,3],[4,5,6],[7,8,9]]) == 15
    >>> findMinPathSum([[1,2,3],[4,50,6],[7,8,9]]) == 21
    """
    from numpy import transpose as tr
    if not arr: return None
    paths = [
        sum(arr[i][len(arr)-i-1] for i in range(len(arr))),
        sum(tr(arr)[-1]) + sum(arr[0][:-1]),
        sum(tr(arr)[0]) + sum(arr[-1][1:])
    ]
    return min(paths)

assert findMinPathSum([]) == None
assert findMinPathSum([[-1]]) == -1
assert findMinPathSum([[1,2,3],[4,5,6],[7,8,9]]) == 15
assert findMinPathSum([[1,2,3],[4,50,6],[7,8,9]]) == 21
assert findMinPathSum([[1,2,3,45,67],[4,50,6,123,4],[7,8,9,-2,4],[43,-23,15,0,1],[66,32,-9,41,1]]) == 128



def make_the_cube(d, m):
    """
    You want to build a cube with dimenstions "n",
    and squared materials with length of "m",
    both given as positive integers,
    Return miminum number of materials needed to build the cube.
    Note: you may cut the materials, and use them for other
    sides, however you cannot join materials to build the side of the box.
    Return None, if you cannot build the box.

    >>> make_the_cube(2, 1) == None
    >>> make_the_cube(1, 1) == 6
    >>> make_the_cube(1, 2) == 2
    """
    if m < d: return None
    res = 0
    left = 0
    for _ in range(6):
        if d == m:
            res += 1
            continue
        if left:
            left -= 1
            continue
        left += (m//d)**2 - 1
        res += 1
    return res


assert make_the_cube(2, 1) == None
assert make_the_cube(1, 1) == 6
assert make_the_cube(2, 3) == 6
assert make_the_cube(2, 4) == 2
assert make_the_cube(2, 6) == 1




def odd_even_difference(n):
    """
    Create a function that takes an integer and returns the maximum
    difference between its closest even and odd neighbours.
    For instance, the closest odd and even neighbours of 5 are [3, 7, 4, 6],
    and the maximum possible difference is 7 - 3, which is 4.

    Note: difference is unsigned.

    Examples:
    >>> odd_even_difference(0) == 4
    >>> odd_even_difference(5) == 4
    >>> odd_even_difference(10) == 4
    """
    return 4

assert odd_even_difference(0) == 4
assert odd_even_difference(5) == 4
assert odd_even_difference(10) == 4
assert odd_even_difference(-4) == 4




def repeated_letters(txt):
    """
    Given a string txt, return such substring, that has
    maximum number of same alphabetical characters in a row.
    Capitalization is not important.
    For several substrings, return the most left substring.
    
    Note: if "txt" is empty, or there is not alphabetical characters, return empty string.

    Examples:
    >>> repeated_letters('') == ''
    >>> repeated_letters('123!@#  !@#') == ''
    >>> repeated_letters('aaAAa   aaaaa aa') == 'aaAAa'
    >>> repeated_letters('abc') == 'a'
    """
    if not txt: return ''
    subs = []
    i, curr = 0, ''
    for i in range(len(txt)):
        if not curr:
            if txt[i].isalpha(): curr = txt[i]
        else:
            if curr[0].lower() == txt[i].lower(): curr += txt[i]
            else:
                if curr[0] != ' ': subs += [curr]
                curr = txt[i]
    subs = list(filter(lambda x: len(set(x.lower())) == 1, subs + [curr]))
    subs = [i for i in subs if len(i) == len(max(subs, key=len))]
    return subs[0] if subs else ''



assert repeated_letters('') == ''
assert repeated_letters('123!@#  !@#') == ''
assert repeated_letters('aaAAa   aaaaa aa') == 'aaAAa'
assert repeated_letters('abc') == 'a'
assert repeated_letters(' ') == ''
assert repeated_letters('1 a 1') == 'a'



def squares(n):
    """
    You are given a positive integer n.
    Imagine a matrix with dimensions n x n.
    Return number of possible inner squares of side 3
    can be obtained from the matrix.

    Examples:
    >>> squares(1) == 0
    >>> squares(2) == 0
    >>> squares(3) == 1
    >>> squares(4) == 4
    """
    return 0 if n < 3 else (n - 2) ** 2
    
    
assert squares(1) == 0
assert squares(2) == 0
assert squares(3) == 1
assert squares(4) == 4
assert squares(5) == 9
assert squares(10000) == 99960004




def pre_prelast_name_finder(full_name):
    """
    You are given a full name of a person as a string.
    The pre_prelast word in the full name is considered to be a pre_prelast name.
    Return pre_prelast word, if there are more than 1 word, else return None.
    Note: word is a substring of characters, separated by a space.
    It is guaranteed to have only alphabetical characters and space.
    Ignore trailing spaces.

    Examples:
    >>> pre_prelast_name_finder('Bill     Gates   ') == 'Gates'
    >>> pre_prelast_name_finder('Bill') == None
    >>> pre_prelast_name_finder('Alexander the Great') == 'Great'
    >>> pre_prelast_name_finder('Alexander the Grea t') == 't'
    """
    words = full_name.split()
    return words[-1] if len(words) > 1 else None

assert pre_prelast_name_finder('Bill     Gates   ') == 'Gates'
assert pre_prelast_name_finder('Bill') == None
assert pre_prelast_name_finder('Alexander the Great') == 'Great'
assert pre_prelast_name_finder('Alexander the Grea t') == 't'
assert pre_prelast_name_finder('') == None
assert pre_prelast_name_finder('  ') == None

def remove_middle_name(name):
    """
    You are given a name of a person as a string.
    However, you do not know how many words are there.
    If there are 3 words in the given string, remove
    the middle name, while keeping all the spaces, and
    return it. If name does not contain 3 words, return the
    original string.
    Note: word is a substring of characters, separated by a space.
    It is guaranteed to have only alphabetical characters and space.

    Examples:
    >>> remove_middle_name(' Bill  William    Gates   ') == ' Bill      Gates   '
    >>> remove_middle_name('Bill') == 'Bill'
    >>> remove_middle_name('Alexander the Great') == 'Alexander  Great'
    >>> remove_middle_name('Alexander the Grea t') == 'Alexander the Grea t'
    """
    if len(name.split()) == 3:
        words = name.split(' ')
        i = 0
        for j in range(len(words)):
            if words[j]: i += 1
            if i == 2:
                words.pop(j)
                words.insert(j, '')
                break
        return ' '.join(words)
    return name

assert remove_middle_name(' Bill  William    Gates   ') == ' Bill      Gates   '
assert remove_middle_name('Bill') == 'Bill'
assert remove_middle_name('Alexander the Great') == 'Alexander  Great'
assert remove_middle_name('Alexander the Grea t') == 'Alexander the Grea t'
assert remove_middle_name('') == ''
assert remove_middle_name('  ') == '  '
assert remove_middle_name('    Bill   Bill   Bill  ') == '    Bill      Bill  '

def expand(s):
    """
    Given a string "s", return its expansion.
    To expand the string, you need to add a single space
    between each of the non-space characters, and need to
    replace each single space by double space.
    For empty input, return None.

    Example:
    >>> expand('') == None
    >>> expand('Hello World!') == 'H e l l o  W o r l d !'
    >>> expand('H') == 'H'
    >>> expand('H  H') == 'H    H'
    """
    if not s: return None
    return ' '.join([' '.join(list(i)) if i else i for i in s.replace(' ', '  ').split(' ')])

assert expand('') == None
assert expand('Hello World!') == 'H e l l o  W o r l d !'
assert expand('H') == 'H'
assert expand('H   H') == 'H      H'
assert expand('     ') == '          '




def divisors_sum(n):
    """
    Given a positive integer "n", return
    sum of all divisors of n, from 1 to n (both inclusive).

    For example:
    >>> divisors_sum(10) == 18
    >>> divisors_sum(100) == 217
    >>> divisors_sum(1) == 1
    """
    import math
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0: divs.extend([i,n/i])
    divs.extend([n])
    return sum(list(set(divs)))

assert divisors_sum(10) == 18
assert divisors_sum(100) == 217
assert divisors_sum(1) == 1
assert divisors_sum(13) == 14
assert divisors_sum(10000) == 24211
assert divisors_sum(9999999999) == 16203253248

def sum_geometric_progression(x, c, n):
    """
    Geometric progression is a sequence of integers where each term after
    the first is found by multiplying the previous one by a fixed value.
    You are given "x" and "c" as non-negative integers, and positive integer "n".
    "x" is starting value, and "c" is the fixed value. return array
    of geometric progression containing n elements.

    For example:
    >>> sum_geometric_progression(1, 2, 1) == 1
    >>> sum_geometric_progression(1, 2, 3) == 7
    >>> sum_geometric_progression(1, -1, 3) == 1
    >>> sum_geometric_progression(-1, 1, 3) == -3
    """
    res = [x]
    for i in range(n - 1): res += [res[-1] * c]
    return sum(res)

assert sum_geometric_progression(1, 2, 1) == 1
assert sum_geometric_progression(1, 2, 3) == 7
assert sum_geometric_progression(1, -1, 3) == 1
assert sum_geometric_progression(-1, 1, 3) == -3
assert sum_geometric_progression(-4, -4, 3) == -52



def my_sum(n):
    """
    Given an integer, return its sum of digits.
    Note: for negative integer, the first digit is negative.
    >>> my_sum(0) == 0
    >>> my_sum(-4) == -4
    >>> my_sum(-44) == 0
    """
    return sum([int(i) for i in str(abs(n))] + [2 * int(str(n)[:2]) if n < 0 else 0])

assert my_sum(0) == 0
assert my_sum(-4) == -4
assert my_sum(-44) == 0
assert my_sum(-91) == -8
assert my_sum(123) == 6



def minutes_to_km(light):
    """
    One light second is equal to 300K kilometers.
    Given light minutes as a non-negative integer,
    convert and return its distance equivalent in km.

    >>> minutes_to_km(0) == 0
    >>> minutes_to_km(1) == 18000000
    """
    return light * 18 * 10**6

assert minutes_to_km(0) == 0
assert minutes_to_km(1) == 18000000
assert minutes_to_km(10) == 180000000


def is_true_friend(msg):
    """
    You've received a message from a random friend
    from a social netwowrk. However, you also know
    that some accounts of your friends have been hacked, and 
    your goal is to figure it out based on their message.
    Friend is true, if the message received has odd
    number of characters, and even sum of ascii values
    of characters with odd ascii values.
    Return True if your friend is true, else False.
    Note: return None for empty string.

    Examples:
    >>> is_true_friend('') == None
    >>> is_true_friend('h i') == False
    >>> is_true_friend('hii') == True
    """
    return (len(msg) % 2 and sum(ord(i) for i in msg if ord(i) % 2) % 2 == 0) if msg else None

assert is_true_friend('') == None
assert is_true_friend('h i') == False
assert is_true_friend('hii') == True
assert is_true_friend('I need money') == False
assert is_true_friend('Just random string') == False



def find_missing_integer(arr):
    """
    Given an array of integers,
    return 'missing' integer of the array.
    To obtain missing integer, get number of
    odds in array, multiply it to the number
    of elements in array, and its remainder,
    when divided by mode of the array, is missing integer.
    For several modes, choose first to appear in array.
    Note: return None if given array is empty.

    Examples:
    >>> find_missing_integer([]) == None
    >>> find_missing_integer([1]) == 0
    >>> find_missing_integer([5, 5]) == 4
    """
    if not arr: return None
    mode = arr[0]
    for i in arr:
        if arr.count(i) > arr.count(mode): mode = i
    return (len([i for i in arr if i % 2]) * len(arr)) % mode

assert find_missing_integer([]) == None
assert find_missing_integer([1]) == 0
assert find_missing_integer([2, 1, 1, 9, 5, 5, 5]) == 2
assert find_missing_integer([1, 2]) == 0
assert find_missing_integer([1, 5, 5]) == 4
assert find_missing_integer([5, 5]) == 4


def sum_geometric_progression(x, c, n):
    """
    You are given "x" and "c" as integers, and positive integer "n".
    Geometric progression is a sequence of integers, starting from "x",
    and each of the next values in progression is previous value
    multiplied by "c", having "n" elements in total.
    'Untrackable' progressions are such progressions when you cannot
    recreate full progression given "n" and tail of the progression
    with more that 1 integer. For example: if x = 1, c = 0, n = 3,
    progression is [1, 0, 0]. Given [... 0, 0] and n = 3, you cannot
    recreate the full progression, bacause x can be any integer.
    If progression is not untrackable, return sum of integers in geometric
    progression containing "n" elements, else return None.
    [1,-3,9,-27] is an example of a progression where x = 1, c = -3, n = 4.
    
    For example:
    >>> sum_geometric_progression(-1, -1, 4) == 0
    >>> sum_geometric_progression(0, 3, 3) == None
    >>> sum_geometric_progression(1, -3, 4) == -20
    """
    if not x or not c: return None
    res = [x]
    for i in range(n - 1): res += [res[-1] * c]
    return sum(res)

assert sum_geometric_progression(1, 2, 1) == 1
assert sum_geometric_progression(1, 2, 3) == 7
assert sum_geometric_progression(1, -1, 3) == 1
assert sum_geometric_progression(-1, 1, 3) == -3
assert sum_geometric_progression(-4, -4, 3) == -52
assert sum_geometric_progression(-1, 0, 3) == None
assert sum_geometric_progression(0, 3, 3) == None
assert sum_geometric_progression(-1, -1, 4) == 0
assert sum_geometric_progression(-1, -1, 5) == -1
assert sum_geometric_progression(1, -3, 4) == -20


def multiply_array(a, b):
    """
    You are given 2 arrays of integers.
    If their length is equal, return new array
    is obtained by multiplying each of the integers
    of 'a' by a corresponding integer of 'b'.
    If they have different number of items, populate
    the deficient array with maximum integer from
    bigger array as many times as you need.

    Examples:
    >>> multiply_array([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]) == []
    >>> multiply_array([1], [1,2,3]) == [1, 6, 9]
    """
    if len(a) != len(b):
        if len(a) > len(b): a, b = b, a
        a += [max(b)] * (len(b) - len(a))
    return [i * j for i, j in zip(a, b)]

assert multiply_array([1, -2, 3, 4, 5], [2, 3, -4, 5, 6]) == [2, -6, -12, 20, 30]
assert multiply_array([1], [1,2,3]) == [1, 6, 9]
assert multiply_array([1,2,3],[1]) == [1, 6, 9]
assert multiply_array([1, 2, 3, 4], [2, 3, 4, 5, 6]) == [2, 6, 12, 20, 36]
assert multiply_array([], [1]) == [1]
assert multiply_array([], []) == []

def is_valid_word(word):
    """
    Given a string "word", return True if word is valid, else False.
    Properties of valid word:
        - contains only alphabetical characters.
        - only first letter can be in upper-case.
        - cannot have more that 3 vowels or consonants in a row.
    Return Note for empty string.
    Ignore capitalization.

    Examples:
    >>> is_valid_word('') == None
    >>> is_valid_word('Hello') == True
    >>> is_valid_word('helloworld') == True
    >>> is_valid_word('Hellllo World!') == False
    """
    if not word: return None
    curr, count = word[0], 1
    for i in range(len(word)):
        if not word[i].isalpha(): return False
        if i:
            if word[i].isupper(): return False
            if word[i].lower() == curr.lower():
                count += 1
                if count == 4: return False
            else:
                curr = word[i]
                count = 1
    return True

assert is_valid_word('') == None
assert is_valid_word('Hello') == True
assert is_valid_word('helloworld') == True
assert is_valid_word('Hellllo World') == False
assert is_valid_word(' ') == False
assert is_valid_word('!') == False
assert is_valid_word('A') == True
assert is_valid_word('a') == True
assert is_valid_word('h i') == False
assert is_valid_word('Ooonnn') == True
assert is_valid_word('OooNnn') == False
assert is_valid_word('Ooonnnn') == False
assert is_valid_word('Oooonnn') == False
    

def s_product(s1, s2):
    """
    You are given 2 strings.
    If their length is equal, return sum of the product of the
    ascii values of the each corresponding pairs (s1[i] * s2[i]),
    otherwise add the character with maximum ascii code from longer
    string to end of deficient string as many times as you need.

    Examples:
    >>> s_product('mike', 'blue') == 44742
    >>> s_product('a', '') == 9409
    >>> s_product('', '') == 0
    """
    s1, s2 = [ord(i) for i in s1], [ord(i) for i in s2]
    if len(s1) != len(s2):
        if len(s1) > len(s2): s1, s2 = s2, s1
        s1 += [max(s2)] * (len(s2) - len(s1))
    return sum([i * j for i, j in zip(s1, s2)])
    
assert s_product('mike', 'blue') == 44742
assert s_product('mike', 'fox') == 46622
assert s_product('fox', 'mike') == 46622
assert s_product('', '') == 0
assert s_product('a', '') == 9409
assert s_product('ABC', 'ABC') == 13070


def interval_probablity(arr, x):
    """
    Given an array of integers, return probability
    of getting integer 'x', when choosing random
    integer from 'arr' in interval of maximum and
    minimum integers (inclusive).
    For several miminum or maximumm values, choose
    first to occur in array. Round the probablity 
    up to 2 decimal points. If 'arr' is empty, return None.
    Note: probablity is a floating number from 0 to 1.

    Examples:
    >>> interval_probablity([], 1) == None
    >>> interval_probablity([1, 2], 1) == 0.5
    >>> interval_probablity([1, 1, 1], 1) == 0
    """
    if not arr: return None
    mini, maxi = arr.index(min(arr)), arr.index(max(arr)) + 1
    arr = arr[mini:maxi] if maxi > mini else arr[maxi-1:mini+1]
    return round(arr.count(x) / len(arr), 2) if arr else None

assert interval_probablity([], 1) == None
assert interval_probablity([1, 2, 1], 1) == .5
assert interval_probablity([1, 1, 1], 1) == 1
assert interval_probablity([1, 1, 2, 0, -1], 2) == .33
assert interval_probablity([-1, -1, 1, -1], 1) == .33
assert interval_probablity([0], 0) == 1
assert interval_probablity([2,1], 1) == .5
assert interval_probablity([1,2], 1) == .5
assert interval_probablity([1,3], 2) == 0


def odd_product(n):
    """
    Given integer 'n', find 3 closest odds smaller than n,
    and return largest product of any of possible pairs
    obtained from 3 closest odds.

    For example:
    >>> odd_product(4) == 3
    >>> odd_product(0) == 15
    """
    n -= 2 if n % 2 else 1
    odds = [n - 2 * i for i in range(3)]
    return max([odds[0]*odds[1], odds[0]*odds[2], odds[1]*odds[2]])

assert odd_product(4) == 3
assert odd_product(0) == 15
assert odd_product(5) == 3
assert odd_product(8) == 35
assert odd_product(100) == 99 * 97

def is_interesting(s):
    """
    Let's call a string interesting if there is a
    substring of the length of half of 's' or more,
    that reads the same forwards and backwards.
    For example, 'abc' is not interesting, however,
    'aabc' is interesting since the substring 'aa' is a palindrome.
    Ignore capitalization and return None for empty string.

    Examples:
    >>> is_interesting('') == None
    >>> is_interesting('abc') == False
    >>> is_interesting('aabc') == True
    """
    if s == '': return None
    s = s.lower()
    step = round(len(s)/2)
    for i in range(0, len(s) - step+1):
        if s[i:i+step] == s[i:i+step][::-1]: return True 
    return False

assert is_interesting('') == None
assert is_interesting('abc') == False
assert is_interesting('aabc') == True
assert is_interesting('aabbcc') == False
assert is_interesting('aabbbcc') == False
assert is_interesting('aabbbbcc') == True
assert is_interesting('!!!@#') == True

def max_sum(arr):
    """
    Given an array of integers, return such subarray,
    that has maximum sum of integers. For several
    candidates, choose shortest subarray, and if you
    still have several answers, choose the most left
    subarray. If 'arr' is empty, return None.

    >>> max_sum([]) == None
    >>> max_sum([1, 1, 1, -3, 2]) == [1, 1, 1]
    >>> max_sum([1, 1, -3, 2]) == [2]
    """
    if not arr: return None
    res = [arr[0]]
    for i in range(len(arr)):
        for j in range(len(arr) - i):
            if sum(arr[j:j+i+1]) > sum(res): res = arr[j:j+i+1]
    return res
assert max_sum([]) == None
assert max_sum([1, -3, 2]) == [2]
assert max_sum([1, 1, -3, 2]) == [2]
assert max_sum([1, 1, 1, -3, 2]) == [1,1,1]
assert max_sum([1, -3, -2, 8]) == [8]
assert max_sum([-2,1,-3,4,-1,2,1,-5,4]) == [4,-1,2,1]
assert max_sum([-2]) == [-2]

def iq(scores):
    """
    You need to get the IQ of the person,
    by looking at his IQ test results, which is
    given as an array of 10 integers between 0
    and 10 both inclusive. IQ starts at 155.
    Do following for each of the scores:
        - if it is less than 5, substract 7 from total IQ score
        - if it is more than 5, add 7
        - if it is 5, do nothing
    
    Return IQ score based on test results.
    Return None if scores do not have exactly 10 scores,
    or any of the scores are not within given range.

    >>> iq([0,2,1,4,3,4,0,0,2,1]) == 85
    >>> iq([9,5,5,5,5,5,5,5,5,1]) == 155
    >>> iq([6,7,6,3,5,1,2,4,5,1]) == 141
    """
    if len(scores) != 10 or list(filter(lambda x: x > 10 or x < 0, scores)): return None
    return 155 + sum(7 * (-1 if i < 5 else 1) for i in list(filter(lambda x: x != 5, scores)))

assert iq([0,2,1,4,3,4,0,0,2,1]) == 85
assert iq([9,5,5,5,5,5,5,5,5,1]) == 155
assert iq([6,7,6,3,5,1,2,4,5,1]) == 141
assert iq([10,10,10,10,10,6,7,8,9,6]) == 225
assert iq([0,1,2,3,4,5,6,7,8,9]) == 148
assert iq([0,1,2,3,4,5,6,7,8,9,10]) == None
assert iq([0]) == None
assert iq([0,1,2,3,4,5,6,7,8,11]) == None

def draw_dog(n):
    """
    A dog with a perfect body has proportions of Head:Body:Tail == 1 : 3 : 2
    A perfect dog drawn with head size of 1 is 'HBBBTT', size of 2 is 'HHBBBBBBTTTT' and so on.
    Given a positive integer 'n' which is a head size, return drawn dog that has a perfect body.
    
    Examples:
    >>> draw_dog(1) == 'HBBBTT'
    >>> draw_dog(2) == 'HHBBBBBBTTTT'
    """
    return ''.join([i * n for i in ['H','BBB','TT']])

assert draw_dog(1) == 'HBBBTT'
assert draw_dog(2) == 'HHBBBBBBTTTT'
assert draw_dog(3) == 'HHHBBBBBBBBBTTTTTT'
assert draw_dog(4) == 'HHHHBBBBBBBBBBBBTTTTTTTT'
assert draw_dog(5) == 'HHHHHBBBBBBBBBBBBBBBTTTTTTTTTT'

def count_intervowels(word):
    """
    Given a string, return number of vowels.
    Vowels are a, e, i, o, u and sometimes y.
    Let's assume that 'y' is considered as a vowel
    if any of the 2 adjacent neighbors are consonants.
    It is guaranteed 'word' will have only alphabetical characters.
    Note: do not consider 'y' as a consonant when checking neigbors,
    e.g. in word yyes, y's are not vowels.

    >>> count_intervowels('') == 0
    >>> count_intervowels('yyes') == 1
    >>> count_intervowels('myGym') == 2 
    """
    res = sum(1 for i in word if i.lower() in 'aeoiu')
    for i in range(len(word)):
        if word[i] not in 'Yy': continue
        if i:
            if word[i-1].lower() not in 'aeoiuy':
                res += 1
                continue
        if i < len(word) - 1:
            if word[i+1].lower() not in 'aeoiuy':
                res += 1
                continue
    return res

assert count_intervowels('') == 0
assert count_intervowels('yyes') == 1
assert count_intervowels('myGym') == 2
assert count_intervowels('HelloWorldMyDear') == 6
assert count_intervowels('cryyyy') == 1
assert count_intervowels('YYES') == 1
assert count_intervowels('MYGYM') == 2
assert count_intervowels('HELLOWORLDMYDEAR') == 6



def numbers_to_fair_string(arr):
    """
    Given an array of integers return a 'fair' string
    that contains all the integers in the list,
    separated by a comma. String is fair if it
    has equal amount of space for every integers.
    Space is the length of substring between commas,
    and it is determined by integer that takes maximum space.
    Fill empty spaces with spaces from the left of integer.
    Note: keep the order of integers in returning string.
    Return empty string for empty array.
    
    Examples:
    >>> numbers_to_fair_string([2, 4, 6, 8]) == "2,4,6,8"
    >>> numbers_to_fair_string([2, -4, 6, -8]) == " 2,-4, 6,-8"
    >>> numbers_to_fair_string([-31, 344]) == "-31,344"
    """
    if not arr: return ''
    res = [str(i) for i in arr]
    space = len(max(res, key=len))
    return ','.join([' ' * (space - len(i)) + i for i in res])

assert numbers_to_fair_string([2, 4, 6, 8]) == "2,4,6,8"
assert numbers_to_fair_string([]) == ""
assert numbers_to_fair_string([2, -4, 6, -8]) == " 2,-4, 6,-8"
assert numbers_to_fair_string([-31, 344]) == "-31,344"
assert numbers_to_fair_string([1,2,3,4,-9999]) == '    1,    2,    3,    4,-9999'

def next_decade(n, step):
    """
    Your are given integers 'n' and 'step'.
    Check if it is possible to make x steps
    from n to an integer divisible by 10. If it
    is possible return number steps needed to
    reach that integer, or None if not possible.
    For example n = 4, step = -2, you can make 2 steps
    to reach 0, which is divisible by 10, so return 2.

    >>> next_decade(4, -2) == 2
    >>> next_decade(4, 2) == 3
    >>> next_decade(4, 10) == None
    >>> next_decade(20, 0) == 0
    >>> next_decade(4, 0) == None
    """
    if not step:
        if not (n % 10): return 0
        else: return None
    if not (n % 10): return 0
    if not (step % 10): return None
    res = 0
    while n % 10:
        res += 1
        n += step
    return res

assert next_decade(4, -2) == 2
assert next_decade(4, 2) == 3
assert next_decade(4, 10) == None
assert next_decade(4, 13) == 2
assert next_decade(20, 0) == 0
assert next_decade(4, 0) == None
assert next_decade(-1, -111) == 9
assert next_decade(0, 0) == 0



def second_largest_prime(n):
    """
    Given an integer n, return the second largest prime less than n.
    Note: return None if there is no such prime.

    Examples:
    >>> second_largest_prime(-3) == None
    >>> second_largest_prime(3) == None
    >>> second_largest_prime(5) == 2
    """
    if n < 5: return None
    from sympy.ntheory import isprime
    res, count = None, 0
    while count < 2:
        n -= 1
        if isprime(n):
            count += 1
            res = n
    return res
    

assert second_largest_prime(-3) == None
assert second_largest_prime(3) == None
assert second_largest_prime(5) == 2
assert second_largest_prime(17) == 11
assert second_largest_prime(9999999) == 9999973


def min_sum(arr):
    """
    You are given an array of integers.
    Return minimum sum of a subarray
    with length of x, which is obtained by
    x = ((sum of all integers) modulo (number of integers)) + 1
    Return None for empty array.

    Examples:
    >>> min_sum([]) == None
    >>> min_sum([-3,4,1,5]) == None
    >>> min_sum([0,1,3,-1]) == None
    """
    if not arr: return None
    res = None
    x = (sum(arr) % len(arr)) + 1
    for i in range(len(arr) - x + 1):
        if not res: res = sum(arr[i:i+x])
        if sum(arr[i:i+x]) < res: res = sum(arr[i:i+x])
    return res

assert min_sum([]) == None
assert min_sum([-3,4,1,7]) == 1
assert min_sum([0,1,3,-1]) == 3
assert min_sum([1,1,1,1,1]) == 1
assert min_sum([-1,0,1,0,1]) == -1
assert min_sum([100]) == 100


def smaller_primes(n):
    """
    Given an integer 'n', return an integer,
    concatenated by primes smaller that 'n',
    e.g. primes [2, 3, 5] are formed into 235
    Return 0 if there are no primes less than 'n'.
    Note: primes should be in ascending order.
    
    Examples:
    >>> smaller_primes(-2) == 0
    >>> smaller_primes(6) == 235
    >>> smaller_primes(100) == 2357111317192329313741434753596167717379838997
    """
    if n <= 2: return 0
    from sympy.ntheory import isprime
    return int(''.join(str(i) for i in range(2, n) if isprime(i)))

assert smaller_primes(-2) == 0
assert smaller_primes(6) == 235
assert smaller_primes(100) == 2357111317192329313741434753596167717379838997
assert smaller_primes(30) == 2357111317192329
assert smaller_primes(15) == 23571113


def insert_sum(arr, target):
    """
    Given a list of integers, and a non-negative integer
    'target', insert sum of integers into 'arr' before
    index 'target', and return new obtained array.
    If 'target' is more than max index, insert it to the end.
    Return None for empty array.
    
    Examples:
    >>> insert_sum([],0) == None
    >>> insert_sum([1,2],0) == [3,1,2]
    >>> insert_sum([1,2],4) == [1,2,3]
    """
    if not arr: return None
    arr.insert(target, sum(arr))
    return arr
    

assert insert_sum([],0) == None
assert insert_sum([1,2],0) == [3,1,2]
assert insert_sum([1,2],4) == [1,2,3]
assert insert_sum([1,2],1) == [1,3,2]
assert insert_sum([1,2,3,4,5],3) == [1,2,3,15,4,5]

def multiply_array(a, b):
    """
    You are given 2 arrays of integers.
    If their length is equal, return new array
    obtained by multiplying each of the integers
    of 'a' by a corresponding integer of 'b'.
    If they have different number of items, populate
    the deficient array with maximum integer from
    bigger array as many times as you need to make
    it have same amount of integer as bigger one.

    Examples:
    >>> multiply_array([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]) == [2, 6, 12, 20, 30]
    >>> multiply_array([1], [1,2,3]) == [1, 6, 9]
    """
    if len(a) != len(b):
        if len(a) > len(b): a, b = b, a
        a += [max(b)] * (len(b) - len(a))
    return [i * j for i, j in zip(a, b)]

assert multiply_array([1, -2, 3, 4, 5], [2, 3, -4, 5, 6]) == [2, -6, -12, 20, 30]
assert multiply_array([1], [1,2,3]) == [1, 6, 9]
assert multiply_array([1,2,3],[1]) == [1, 6, 9]
assert multiply_array([1, 2, 3, 4], [2, 3, 4, 5, 6]) == [2, 6, 12, 20, 36]
assert multiply_array([], [1]) == [1]
assert multiply_array([], []) == []
assert multiply_array([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]) == [2, 6, 12, 20, 30]


def same_case(s):
    """
    Given a string 's', find the first letter's
    capitalization. Return the index of the
    second letter which has same capitalization.
    Return -1 if string does not contain any letters,
    or does not have 2 letters with same capitalization.
    Note: index is a non-negative integer.
    
    Examples:
    >>> same_case('') == -1
    >>> same_case('a B') == -1
    >>> same_case('p y t h o n') == 2
    """
    is_lower = None
    for i in range(len(s)):
        if s[i].isalpha():
            if is_lower is None:
                is_lower = True if s[i].islower() else False
                continue
            if is_lower is not None:
                if (s[i].islower() if is_lower else s[i].isupper()): return i
    return -1

assert same_case('') == -1
assert same_case('a B') == -1
assert same_case(' python ') == 2
assert same_case('Hello World!') == 6
assert same_case('A') ==-1

def transformation(n):
    """
    You are playing a game based on alphabet.
    Letter 'a' has a corresponding integer 1,
    2 for 'b', 3 for 'c' and so on.
    Steps to perform one transormation:
        
        0. for first transformation x = n; for next
            transformations, x = returned value of previous transformation
        1. multiply 'x' by 'n'
        2. (value_from_step_1 modulo 26) + 1
        3. return value_from_step_2

    Given a positive integer 'n', apply 'n' transformations,
    and return a letter representation of the result of the pre_prelast transformation.

    Examples:
    >>> transformation(1) == 'a'
    >>> transformation(2) == 'a'
    """
    x = n
    for _ in range(n): x = ((x * n) % 26) + 1
    return chr(96 + x)
    
assert transformation(1) == 'b'
assert transformation(2) == 'k'
assert transformation(3) == 'p'
assert transformation(4) == 'q'
assert transformation(99999) == 'p'

def count_intervowels(txt):
    """
    Given a string 'txt', return number of characters
    that are surrounded by vowels from both sides.
    Note: for this problem, 'y' is not a vowel.

    Examples:
    >>> count_intervowels('') == 0
    >>> count_intervowels('a A a') == 2
    >>> count_intervowels('oooo') == 2
    """
    if len(txt) < 2: return 0
    return sum(1 for i in range(1,len(txt)-1) if txt[i-1].lower() in 'aeiou' and txt[i+1].lower() in 'aeiou')

assert count_intervowels('') == 0
assert count_intervowels('a a a') == 2
assert count_intervowels('oooo') == 2
assert count_intervowels('!oyooyo1') == 2
assert count_intervowels('yooy') == 0

def complex_sorting(s):
    """
    Given a string 's', return an array of characters
    from 's', sorted in a complex way. Complex
    sorting implies sorting by type of characters.
    Ordering by types:
        1. Lowercase letters
        2. Uppercase letters
        3. Digits
        4. Any character except letters, digits and blank spaces
        5. Spaces
    Note: sort several characters in a group by ascii code in descending order.
    Return None for empty string.

    Examples:
    >>> complex_sorting('') == None
    >>> complex_sorting(' Hello! ') == ['o', 'l', 'l', 'e', 'H', '!', ' ', ' ']
    """
    if not s: return None
    alnum, special, blanks = '', '', 0
    for i in s:
        if i == ' ': blanks += 1
        elif i.isalnum(): alnum += i
        else: special += i
    return list(sorted(alnum)[::-1] + sorted(special)[::-1] + [' '] * blanks)

assert complex_sorting('') == None
assert complex_sorting(' Hello! ') == ['o', 'l', 'l', 'e', 'H', '!', ' ', ' ']
assert complex_sorting('!@#$%^&123456') == ['6', '5', '4', '3', '2', '1', '^', '@', '&', '%', '$', '#', '!']
assert complex_sorting('Complex sorting is fun!') == ['x', 'u', 't', 's', 's', 'r', 'p', 'o', 'o', 'n', 'n', 'm', 'l', 'i', 'i', 'g', 'f', 'e', 'C', '!', ' ', ' ', ' ']
assert complex_sorting('    ') == [' ', ' ', ' ', ' ']


def iq(scores):
    """
    You need to get the IQ of the person,
    by looking at his IQ test results, which is
    given as an array of 10 integers between 0
    and 10 both inclusive. IQ starts at 155.
    Do following for each of the scores:
        - if it is less than 5, substract 7 from total IQ score
        - if it is more than 5, add 7
        - if it is 5, do nothing
    
    Return IQ score based on test results.
    Return None if scores do not have exactly 10 scores,
    or any of the scores are not within given range.

    >>> iq([0,2,1,4,3,4,0,0,2,1]) == 85
    >>> iq([9,5,5,5,5,5,5,5,5,1]) == 155
    >>> iq([6,7,6,3,5,1,2,4,5,1]) == 141
    """
    if len(scores) != 10 or list(filter(lambda x: x > 10 or x < 0, scores)): return None
    return 155 + sum(7 * (-1 if i < 5 else 1) for i in list(filter(lambda x: x != 5, scores)))

assert iq([0,2,1,4,3,4,0,0,2,1]) == 85
assert iq([9,5,5,5,5,5,5,5,5,1]) == 155
assert iq([6,7,6,3,5,1,2,4,5,1]) == 141
assert iq([10,10,10,10,10,6,7,8,9,6]) == 225
assert iq([0,1,2,3,4,5,6,7,8,9]) == 148
assert iq([0,1,2,3,4,5,6,7,8,9,10]) == None
assert iq([0]) == None
assert iq([0,1,2,3,4,5,6,7,8,11]) == None

def numberOfMatrices(nums):
    """
    Given an array integers, return number of 2x2
    unique matrices can be formed using integers from 'nums'.
    Note: you can use each integer once.

    Examples:
    >>> numberOfMatrices([]) == 0
    >>> numberOfMatrices([1,1,1,1,1]) == 1
    >>> numberOfMatrices([1,1,1,1,2]) == 5
    """
    if len(nums) < 4: return 0
    from itertools import permutations
    return len(set(permutations(nums, 4)))

assert numberOfMatrices([]) == 0
assert numberOfMatrices([1,1,1,1,1]) == 1
assert numberOfMatrices([1,1,1,1,2]) == 5
assert numberOfMatrices([0,-1,0,-1,0,-1]) == 14
assert numberOfMatrices([0,1,2,3,4,5]) == 360

def reverse_factorial(n):
    """
    You are given a positive integer n.
    If it is a result of a factorial of
    integer 'x', return x, else return None.
    
    Examples:
    >>> reverse_factorial(1) == 1
    >>> reverse_factorial(120) == 5
    >>> reverse_factorial(3) == None
    """
    res, curr = 1, 1
    while curr <= n:
        curr = curr * res
        if curr == n: return res
        res += 1
    return None

assert reverse_factorial(1) == 1
assert reverse_factorial(120) == 5
assert reverse_factorial(3) == None
assert reverse_factorial(131) == None
assert reverse_factorial(362880) == 9



def is_nested_arr(arr):
    """
    Given an array of elements, return True
    if any of the elements is nested array,
    else return False.
    
    Examples:
    >>> is_nested_arr([]) == False
    >>> is_nested_arr([1,2,3,-1,[1,2,[1]]]) == True
    >>> is_nested_arr([1.2,3,5,'a']) == False
    """
    for i in arr:
        if isinstance(i, list):
            for j in i:
                if isinstance(j, list): return True

    return False

assert is_nested_arr([]) == False
assert is_nested_arr([1,2,3,-1,[1,2,[1]]]) == True
assert is_nested_arr([1.2,3,5,'a']) == False
assert is_nested_arr([1,2.3,[1,[]], {'a':'b'}]) == True
assert is_nested_arr([[],[]]) == False


def subarrays(arr):
    """
    Given a list of integers 'arr',
    return number of unique subarrays
    of length 2 or more.
    
    Examples:
    >>> subarrays([]) == 0
    >>> subarrays([1,1,2]) == 3
    """
    res = []
    if len(arr) < 2: return 0
    for i in range(2, len(arr) + 1):
        for j in range(len(arr) - i + 1):
            temp = [arr[j:i + j]]
            if temp not in res: res += [temp]
    return len(res)

assert subarrays([]) == 0
assert subarrays([1,1,2]) == 3
assert subarrays([1,1,1,2]) == 5
assert subarrays([-1,-2,-3,-3,-3]) == 9
assert subarrays([0]) == 0
assert subarrays([1,1]) == 1
assert subarrays([1,1,1]) == 2

def scale_the_line(x, y, k):
    """
    You are given integers 'x' and 'y', which
    represents a line on a Cartesian plot, drawn
    from (0, 0) to (x, y), and a non-zero integer k.
    Your task to is scale the line and return
    new (x, y) values as a tuple of floats/integers.
    For example, (x = 1, y = 1, k = 2) means you need
    to twice the magnitude of a line. After scaling,
    line ends at (2, 2). Negative k means decreasing the size.
    e.g. for (x = 1, y = 1, k = -3), return (0.33,0.33)
    Round coordinates up to 2 decimal points.

    Note: return None if point is given.

    Examples:
    >>> scale_the_line(0,0,1) == None
    >>> scale_the_line(1,1,1) == (1,1)
    >>> scale_the_line(1,1,2) == (2,2)
    >>> scale_the_line(1,1,-3) == (.33,.33)
    """
    if k < 0: k = 1/-k
    return (round(k * x, 2), round(k * y,2)) if x or y else None


assert scale_the_line(0,0,1) == None
assert scale_the_line(1,1,1) == (1,1)
assert scale_the_line(1,1,2) == (2,2)
assert scale_the_line(-1,-1,5) == (-5,-5)
assert scale_the_line(3,-1,3) == (9,-3)
assert scale_the_line(1,1,-3) == (.33,.33)




def remove_adjecent_duplicates(arr):
    """
    Given an nested array of integers, remove all adjecent
    duplicates in all arrays and return obtained array.

    Examples:
    >>> remove_adjecent_duplicates([]) == []
    >>> remove_adjecent_duplicates([1,1,2,1,2,3]) == [1,2,1,2,3]
    >>> remove_adjecent_duplicates([[1,1],[1,1,1]]) == [[1]]
    """
    res = []
    for i in arr:
        temp = i
        temp = remove_adjecent_duplicates(temp) if isinstance(temp, list) else i
        if res and res[-1] == temp: continue
        res += [temp]
    return res

assert remove_adjecent_duplicates([]) == []
assert remove_adjecent_duplicates([1,1,2,1,2,3]) == [1,2,1,2,3]
assert remove_adjecent_duplicates([1,1,2,1,[1,1],[1,1],[1,2]]) == [1,2,1,[1],[1,2]]
assert remove_adjecent_duplicates([[1,1],[1,1,1]]) == [[1]]
assert remove_adjecent_duplicates([[1,1],[1,1,1],[11,23],3,3,4,4,3,-4,-4,3]) == [[1], [11, 23], 3, 4, 3, -4, 3]


def perfect_factor(x):
    """
    Given a positive integer x, return its
    greatest factor that is a perfect square.
    
    >>> perfect_factor(0) == 0
    >>> perfect_factor(10) == 4
    """
    factors = []
    from functools import reduce
    for i in sorted(set(reduce(list.__add__, ([i, x//i] for i in range(1, int(x**0.5) + 1) if x % i == 0))))[::-1]:
        if (i ** .5).is_integer(): return i

assert perfect_factor(7) == 1
assert perfect_factor(8) == 4
assert perfect_factor(999999) == 9
assert perfect_factor(10**12) == 10**12
assert perfect_factor(1) == 1


def hashed_array(n):
    """
    Given a positive integer n, you need to return its hashed array.
    To obtain hashed array of an integer, get its binary as an
    array of integer, e.g. n = 10, and its binary array is [1, 0, 1, 0].
    Then, multiply each integer in binary array by the index of the element.
    Indexing starts at 1. [1, 0, 1, 0] becomes [1, 0, 3, 0].
    Return obtained array.

    Examples:
    >>> hashed_array(10) == [1, 0, 3, 0]
    >>> hashed_array(1000) == [1, 2, 3, 4, 5, 0, 7, 0, 0, 0]
    """
    hashed = list(map(int, list(bin(n)[2:])))
    return [hashed[i] * (i + 1) for i in range(len(hashed))]

assert hashed_array(1) == [1]
assert hashed_array(5) == [1, 0, 3]
assert hashed_array(10) == [1, 0, 3, 0]
assert hashed_array(1000) == [1, 2, 3, 4, 5, 0, 7, 0, 0, 0]
assert hashed_array(9999999) == [1, 0, 0, 4, 5, 0, 0, 0, 9, 0, 0, 12, 0, 14, 15, 0, 0, 18, 19, 20, 21, 22, 23, 24]

def factors(n):
    """
    Given an positive integer n, return a list of its factors in increasing order.

    Examples:
    >>> factors(20) == [1, 2, 4, 5, 10, 20]
    """
    from functools import reduce
    return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if not n % i))))

assert factors(20) == [1, 2, 4, 5, 10, 20]
assert factors(1) == [1]
assert factors(10) == [1, 2, 5, 10]
assert factors(17) == [1, 17]
assert factors(9999999999999) == [1, 3, 9, 53, 79, 159, 237, 477, 711, 4187, 12561, 37683, 265371653, 796114959, 2388344877, 14064697609, 20964360587, 42194092827, 62893081761, 126582278481, 188679245283, 1111111111111, 3333333333333, 9999999999999]



def rotate_word(word, n):
    """
    Consider alphabet as a circle of letters in clockwise
    order, so after letter 'z', again goes 'a', 'b' and so on.
    Given a 'word' of only alphabetical letters, and
    integer 'n', return rotated version of a 'word' by 'n' degrees.
    One degree is 1 clockwise shift, and consequently negative degree
    is 1 counterclockwise shift.

    Examples:
    >>> rotate_word('Abc', 1) == 'Bcd'
    >>> rotate_word('Abc', -1) == 'Zab'
    >>> rotate_word('Abc', 0) == 'Abc'
    """
    return ''.join(chr((((ord(i) - (97 if i.islower() else 65)) + n) % 26) + (97 if i.islower() else 65)) for i in word)


assert rotate_word('abc', 1) == 'bcd'
assert rotate_word('Abc', 1) == 'Bcd'
assert rotate_word('Abc', -1) == 'Zab'
assert rotate_word('Abc', 0) == 'Abc'
assert rotate_word('Hello', -26) == 'Hello'
assert rotate_word('Hello', 52) == 'Hello'
assert rotate_word('Hello', 5) == 'Mjqqt'


def str_to_dict(s):
    """
    You are given a string representation of
    python dictionary, where all keys are strings,
    and values are integers. Return it as dictionary.

    You are given "key=value" pairs as a string,
    separated by a single space, e.g. 'a=1 b=2'.
    Return its dictionary representation, where
    keys are strings, and values are integers.
    It's guaranteed that given string will have
    only valid "key=value" pairs separated by space,
    where 'key' contains alphabetical characters,
    and 'value' represents an integer.
    Note: return empty dictionary for empty string.

    Examples:
    >>> str_to_dict('a=1 b=2') == {'a': 1, 'b': 2}
    >>> str_to_dict('') == {}
    """
    return {i[0]:int(i[1]) for i in [i.split('=') for i in s.split()]}


assert str_to_dict('a=1 b=2') == {'a': 1, 'b': 2}
assert str_to_dict('') == {}
assert str_to_dict('a=1 b=2 c=-3') == {'a': 1, 'b': 2, 'c': -3}
assert str_to_dict('height=1 width=2 depth=19') == {'height': 1, 'width': 2, 'depth': 19}
assert str_to_dict('positive=1 negative=-1 zero=0') == {'positive': 1, 'negative': -1, 'zero': 0}

def str_to_dict(s):
    """
    You are given a string representation of a python
    dictionary, where all keys are strings, and values
    are integers. Return it as a dictionary. Tricky part
    is that string will also contain some extra spaces,
    and also person who wrote that string sometimes messes up
    and puts semicolons (;) instead of colons (:).
    It is guaranteed you will be given a valid string,
    that represent a python dictionary, where keys
    are strings, and values are integers.
    Note: strings are surrounded by a single quote.

    Examples:
    >>> str_to_dict(" { 'a' :   1  ,  'b' ;  2  }  ") == {'a': 1, 'b': 2}
    >>> str_to_dict("{    }") == {}
    """
    return eval(s.replace(';',':'))

assert str_to_dict(" { 'a' :   1  ,  'b' ;  2  }  ") == {'a': 1, 'b': 2}
assert str_to_dict("{    }") == {}
assert str_to_dict(" { 'a' : -1 , 'b': 2, 'c':0 }  ") == {'a': -1, 'b': 2, 'c': 0}
assert str_to_dict("{'height':1, 'width' ;  2, 'depth':19}") == {'height': 1, 'width': 2, 'depth': 19}
assert str_to_dict("{'positive';1, 'negative':-1, 'zero':0}") == {'positive': 1, 'negative': -1, 'zero': 0}


def min_split_array(arr):
    """
    Given an array of integers, split array into
    two parts in a such way that the difference
    of their sums is minimum, and return array
    containing 2 subarrays, while keeping the order.
    For several results, choose one with the longest left subarray.
    Subarray may have a length of 0.
    
    >>> min_split_array([]) == [[], []]
    >>> min_split_array([1]) == [[1], []]
    >>> min_split_array([3, 7, 2, 1]) == [ [1, 2], [3, 7] ]
    """
    res, curr = len(arr), abs(sum(arr))
    for i in range(len(arr)):
        if abs(sum(arr[:len(arr) - i - 1]) - sum(arr[len(arr)-i - 1:])) < curr:
            curr = abs(sum(arr[:len(arr) - i - 1]) - sum(arr[len(arr)-i - 1:]))
            res = len(arr) - i - 1
    return [arr[:res], arr[res:]]

    
assert min_split_array([]) == [[], []]
assert min_split_array([1]) == [[1], []]
assert min_split_array([3, 7, 2, 1]) == [[3, 7], [2, 1]]
assert min_split_array([1,0,1,0,1,0]) == [[1, 0, 1, 0], [1, 0]]
assert min_split_array([-1,0,1,0,-1]) == [[-1, 0, 1, 0, -1], []]


def first_non_repeated_letter(txt):
    """
    Given a string 'txt', return first alphabetical letter
    that isn't repeated in the entire sentence.
    Capitalization is not important.
    If there is not such letters, return None.

    Examples:
    >>> first_non_repeated_letter("") == None
    >>> first_non_repeated_letter("Abc") == 'A'
    >>> first_non_repeated_letter("aaBBCC") == None
    """
    txt_lowered = txt.lower()
    for i in range(len(txt_lowered)):
        if txt_lowered[i].isalpha() and txt_lowered[i] not in (txt_lowered[:i] + txt_lowered[i+1:]): return txt[i]       
    return None

assert first_non_repeated_letter("I like this test") == "l"
assert first_non_repeated_letter("aaBBCC") == None
assert first_non_repeated_letter("abc") == 'a'
assert first_non_repeated_letter("Abc") == 'A'
assert first_non_repeated_letter("") == None



def primed_primes(n):
    """
    Given an integer n, return an array of such primes
    that are less than or equal to n, and their digits sum is also prime.
    Note: return array in ascending order.

    >>> primed_primes(-1) == []
    >>> primed_primes(20) == [2, 3, 5, 7, 11]
    """
    from sympy.ntheory import isprime
    return [] if n < 2 else [i for i in range(2, n + 1) if isprime(i) and isprime(sum(map(int, str(i))))]

assert primed_primes(-1) == []
assert primed_primes(20) == [2, 3, 5, 7, 11]
assert primed_primes(100) == [2, 3, 5, 7, 11, 23, 29, 41, 43, 47, 61, 67, 83, 89]
assert primed_primes(40) == [2, 3, 5, 7, 11, 23, 29]
assert primed_primes(0) == []

def to_snake(s):
    """
    Snakes crawles in a zig-zag shape - from side to side.
    Given a string, return its snake version, which is formed
    by taking the most left character, then the most right,
    and so on, until you run out of characters.
    
    Examples:
    >>> to_snake("Hello")  == "Hoell"
    >>> to_snake(" Ruby ")  == "  Ryub"
    >>> to_snake("")  == ""
    """
    res, switch = '', 1
    while s:
        res += s[0] if switch else s[-1]
        s = s[1:] if switch else s[:-1]
        switch = not switch
    return res
    
assert to_snake("Hello")  == "Hoell"
assert to_snake(" Ruby ")  == "  Ryub"
assert to_snake("")  == ""
assert to_snake("Snakes are crazy!")  == "S!nyazkaersc  aer"
assert to_snake("zig-zag")  == "zgiagz-"


def minPosition(arr):
    """
    Given an array 'arr' of integers, return the minimum index of
    a value v, such that arr[i] < v < arr[j] for all (i, j) such that
    0 ≤ i < j ≤ arr.length. If such a value does not exist, return -1.
    Note: index is a non-negative integers, starting from 0.

    Examples:
    >>> minPosition([1, 2, 3]) == 1
    >>> minPosition([1, 1, 3, 4, 5]) == 2
    >>> minPosition([1, 0, -1]) == -1
    >>> minPosition([1, 2]) == -1
    """
    for i in range(1, len(arr) - 1):
        if all(arr[i] > a for a in arr[:i]) and all(arr[i] < b for b in arr[i+1:]):
            print(i)
            return i
    return -1

assert minPosition([1, 2, 3]) == 1
assert minPosition([1, 1, 3, 4, 5]) == 2
assert minPosition([1, 0, -1]) == -1
assert minPosition([1, 2]) == -1
assert minPosition([]) == -1
assert minPosition([1,2,2,9]) == -1
assert minPosition([1,2,3,9]) == 1
assert minPosition([0]) == -1



def frequency_in_matrix(matrix, k):
    """
    Given a matrix as a two-dimensional array of integers and positive integer k,
    return total number of values with a frequency greater than k.
    Valid matrix is a matrix that has x rows and y columns, where x and y are positive integers.
    
    Note: if matrix is not valid, return None.
    For example:
    >>> frequency_in_matrix([[1,1,3],[1,2,3],[1,2,3]], 3) == 1
    >>> frequency_in_matrix([], 3) == None
    >>> frequency_in_matrix([[1,1],[1,1,2]], 3) == None
    """
    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix): return None
    from collections import defaultdict
    freqs = defaultdict(int)
    for row in matrix:
        for i in row: freqs[i] += 1
    return sum(freqs[i] > k for i in freqs)



assert frequency_in_matrix([[1,1,3],[1,2,3],[1,2,3]], 3) == 1
assert frequency_in_matrix([[1,1,-3],[1,2,-3],[1,2,-3]], 1) == 3
assert frequency_in_matrix([[1,1,-3],[1,2,-3],[1,2,3]], 1) == 3
assert frequency_in_matrix([[1,1,3],[1,2,3],[1,2,3]], 2) == 2
assert frequency_in_matrix([[1,1,-3],[1,2,-3],[1,2,-3]], 4) == 0
assert frequency_in_matrix([], 3) == None
assert frequency_in_matrix([[1,1],[1,1,2]], 3) == None


def findMinPathSum(arr):
    """
    You are given an array of arrays "arr", which
    represents a squared matrix. Each entry is an
    integer. There are only 3 possible paths to
    go from top-left to bottom-right value:
        - go from top-left point to the bottom-left, then to the right till the end.
        - go from top-left point to the top-right, then to the bottom till the end.
        - go from top-left to the bottom-right (by diagonal).
    Path score is simply the sum of the values on the path, including start/end points.
    Return miminum path score.
    Note: return None for empty arr.

    >>> findMinPathSum([]) == None
    >>> findMinPathSum([[-1]]) == -1
    >>> findMinPathSum([[1,2,3],[4,5,6],[7,8,9]]) == 15
    >>> findMinPathSum([[1,2,3],[4,50,6],[7,8,9]]) == 21
    """
    from numpy import transpose as tr
    if not arr: return None

    paths = [
        sum(arr[i][i] for i in range(len(arr))),
        sum(tr(arr)[-1]) + sum(arr[0][:-1]),
        sum(tr(arr)[0]) + sum(arr[-1][1:])
    ]
    return min(paths)

assert findMinPathSum([]) == None
assert findMinPathSum([[-1]]) == -1
assert findMinPathSum([[1,2,3],[4,5,6],[7,8,9]]) == 15
assert findMinPathSum([[1,2,3],[4,50,6],[7,8,9]]) == 21
assert findMinPathSum([[1,   2, 3, 45,67],
                       [4,  50, 6,123, 4],
                       [7,   8, 9, -2, 4],
                       [43,-23,15,  0, 1],
                       [66, 32,-9, 41, 1]]) == 61

def matrix_cipher(arr):
    """
    You are given a matrix as a nested lists of integers.
    Each integer is an ascii value of a character.
    You should read the matrix in zig-zag order,
    and return obtained string. Zig-zag order is
    when you start from the top left corner, read
    the row to the right, then go down by 1 row, read the row
    to the left, and so on, until you read each of the cells.
    Note: return None for empty 'arr'.

    Examples:
    >>> matrix_cipher([]) == ''
    >>> matrix_cipher([]) == matrix_cipher([[104, 101, 108],[33, 111, 108]]) == 'hello!'
    """
    arr = [arr[i][::-1] if i % 2 else arr[i] for i in range(len(arr))]
    return ''.join(chr(j) for i in arr for j in i)

assert matrix_cipher([[104, 101, 108],[33, 111, 108]]) == 'hello!'
assert matrix_cipher([]) == ''
assert matrix_cipher([[65,66,67,68],[72,71,70,69]]) == 'ABCDEFGH'
assert matrix_cipher([[ord(i)] for i in 'PYTHON']) == 'PYTHON'
assert matrix_cipher([[48,49,50,51,52],[57,56,55,54,53]]) == '0123456789'




def digit_repetition(arr):
    """
    Given an array of integers, return the digit
    as integer that occurs most frequently among integers.
    For several results return the greater digit.
    Return None for empty array.

    Examples:
    >>> digit_repetition([]) == None
    >>> digit_repetition([1,0]) == 1
    >>> digit_repetition([11, 22, -12]) == 2
    """
    if not arr: return None
    digits = ''.join(str(i) for i in arr).replace('-', '')
    digits = [(i, digits.count(i)) for i in set(digits)]
    return int(sorted(digits, key=lambda x: (x[1], x[0]))[-1][0])

assert digit_repetition([]) == None
assert digit_repetition([1,0]) == 1
assert digit_repetition([1,0,-1, 22, 3,3,3,1]) == 3
assert digit_repetition([11, 22, -12]) == 2
assert digit_repetition([-123, 321, -1123]) == 1

def min_sum(arr):
    """
    You are given an array of integers.
    Return minimum sum of a subarray
    with length of x, which is obtained by
    x = ((sum of all integers) modulo (number of integers)) + 1
    Return None for empty array.

    Examples:
    >>> min_sum([]) == None
    >>> min_sum([-3,4,1,7]) == 1
    >>> min_sum([0,1,3,-1]) == 3
    """
    if not arr: return None
    res = None
    x = (sum(arr) % len(arr)) + 1
    for i in range(len(arr) - x + 1):
        if not res: res = sum(arr[i:i+x])
        if sum(arr[i:i+x]) < res: res = sum(arr[i:i+x])
    return res

def min_sum(arr):
    """
    You are given an array of integers.
    Return minimum sum of a subarray
    with length of x, which is obtained by
    x = ((sum of all integers) modulo (number of integers)) + 1
    Return None for empty array.

    Examples:
    >>> min_sum([]) == None
    >>> min_sum([-3,4,1,7]) == 1
    >>> min_sum([0,1,3,-1]) == 3
    """
    if arr:
        x = sum(arr)%len(arr)+1
        return min([sum(arr[i:i+x]) for i in range(len(arr)-x+1)])

assert min_sum([90,-1,-1,-1,-1]) == -2

def hashed_array(n):
    """
    Given a non-zero integer n, you need to return its hashed array.
    To obtain hashed array of an integer, get its binary as an
    array of integer, e.g. n = 10, and its binary array is [1, 0, 1, 0].
    Then, multiply each integer in binary array by the index of the element.
    Indexing starts at 1. [1, 0, 1, 0] becomes [1, 0, 3, 0].
    Note: for negative integers, find hashed array of its positive
    equivalent, and return its reverse.

    Return obtained array.

    Examples:
    >>> hashed_array(10) == [1, 0, 3, 0]
    >>> hashed_array(-10) == [0, 3, 0, 1]
    >>> hashed_array(1000) == [1, 2, 3, 4, 5, 0, 7, 0, 0, 0]
    """
    is_neg = True if n < 0 else False
    if is_neg: n *= -1
    hashed = list(map(int, list(bin(n)[2:])))
    hashed = [hashed[i] * (i + 1) for i in range(len(hashed))]
    return hashed[::-1] if is_neg else hashed

assert hashed_array(1) == [1]
assert hashed_array(5) == [1, 0, 3]
assert hashed_array(10) == [1, 0, 3, 0]
assert hashed_array(1000) == [1, 2, 3, 4, 5, 0, 7, 0, 0, 0]
assert hashed_array(9999999) == [1, 0, 0, 4, 5, 0, 0, 0, 9, 0, 0, 12, 0, 14, 15, 0, 0, 18, 19, 20, 21, 22, 23, 24]
assert hashed_array(-10) == [0, 3, 0, 1]
assert hashed_array(-5) == [3, 0, 1]





def rotate_word(word, n):
    """
    Consider alphabet as a circle of letters in clockwise
    order, so after letter 'z', again goes 'a', 'b' and so on.
    Given a 'word' of only alphabetical letters, and
    integer 'n', return rotated version of a 'word' by 'n' degrees.
    One degree is 1 clockwise shift, and consequently negative degree
    is 1 counterclockwise shift.
    Note: keep capitalization of characters.

    Examples:
    >>> rotate_word('Abc', 1) == 'Bcd'
    >>> rotate_word('Abc', -1) == 'Zab'
    >>> rotate_word('Abc', 0) == 'Abc'
    """
    return ''.join(chr((((ord(i) - (97 if i.islower() else 65)) + n) % 26) + (97 if i.islower() else 65)) for i in word)

assert rotate_word('abc', 1) == 'bcd'
assert rotate_word('Abc', 1) == 'Bcd'
assert rotate_word('Abc', -1) == 'Zab'
assert rotate_word('ABC', -1) == 'ZAB'
assert rotate_word('aBC', -1) == 'zAB'
assert rotate_word('Abc', 0) == 'Abc'
assert rotate_word('Hello', -26) == 'Hello'
assert rotate_word('Hello', 52) == 'Hello'
assert rotate_word('Hello', 5) == 'Mjqqt'


def find_wisest_people(n, people):
    """
    The princess, to whom you are very good friend, is preparing to take
    the throne. You're really excited and want to help her in any possible way,
    so she asks you for help. She asks you to find out the wisest people in the
    kingdom. You are given a non-negative integer 'n', which is amount of people
    you need to find, and also given a list of 'people' where each person is a tuple of (a, b),
    where 'a' is age of the person, and 'b' is IQ score, both integers. Wisdom of a person is a * b.
    Return first 'n' wisest people as an array of tuples (as in 'people'), while keeping
    the order as in list 'people'. For several wisest people, choose first to appear
    in 'people'. If n >= len(people), return the input.

    >>> find_wisest_people(0, [(1, 1)]) == []
    >>> find_wisest_people(2, [(1, 1), (2, 0.5), (3, 1)]) == [(3, 1), (1, 1)] 
    >>> find_wisest_people(10, [(1, 1), (2, 0.5), (3, 1)]) == [(1, 1), (2, 0.5), (3, 1)]
    """
    return people if len(people) <= n else sorted(people, key=lambda x: x[0] * x[1], reverse=True)[:n]

assert find_wisest_people(0, [(1, 1)]) == []
assert find_wisest_people(2, [(1, 1), (2, 0.5), (3, 1)]) == [(3, 1), (1, 1)] 
assert find_wisest_people(10, [(1, 1), (2, 0.5), (3, 1)]) == [(1, 1), (2, 0.5), (3, 1)]
assert find_wisest_people(2, [(50, 2), (50, 3), (1, 1000)]) == [(1, 1000), (50, 3)]
assert find_wisest_people(2, [(50, 2), (50, 3), (50000, -1000)]) == [(50, 3), (50, 2)]


def closest_normal(n):
    """
    A 'normal' integer is an integer with 'x' digits,
    where 'x' is the sum of its digits. Given a positive
    integer n, return the greatest 'normal' integer,
    which is less than or equal to n.
 
    Examples:
    >>> closest_normal(1) == 1
    >>> closest_normal(2) == 1
    >>> closest_normal(100) == 20
    """
    while True:
        if len(str(n)) == sum(map(int, str(n))): return n
        else: n -= 1

assert closest_normal(1) == 1
assert closest_normal(2) == 1
assert closest_normal(100) == 20
assert closest_normal(999999) == 600000
assert closest_normal(88796) == 50000



def smallest_float(n):
    """
    Given a positive integer n > 9, return
    the smallest float you can form by
    using digits of n (only once).
    Note: even though '.1' in python is considered as a float,
    for this problem, float without an integer part is not a valid float.

    Examples:
    >>> smallest_float(10) == 0.1
    >>> smallest_float(111) == 1.11
    >>> smallest_float(101) == 0.11
    """
    digits = ''.join(sorted(str(n)))
    return float(digits[0] + '.' + digits[1:])

assert smallest_float(10) == 0.1
assert smallest_float(111) == 1.11
assert smallest_float(101) == 0.11
assert smallest_float(10101) == 0.0111
assert smallest_float(9991) == 1.999
assert smallest_float(9821) == 1.289

def is_perfect(n):
    """
    A perfect number is an integer > 1, that is equal to the sum of its positive divisors.
    Positive divisor is a such integer x that is: 0 < x < n, and divides n.
    Given an integer n, return True if it is perfect, else False.
    
    >>> is_perfect(-100) == False
    >>> is_perfect(6) == True
    """
    if n < 6: return False
    import math
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: divs.extend([i,n/i])
    return sum(set(divs)) == n

assert is_perfect(-100) == False
assert is_perfect(6) == True
assert is_perfect(10009) == False
assert is_perfect(13) == False
assert is_perfect(137438691328) == True
assert is_perfect(33550336) == True



def is_all_odd(n):
    """
    You will be given a positive integer.
    You must return True if it's all odd numbers and False otherwise.
    """


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

# Given 1->2->3->4, reorder it to 1->4->2->3.
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
def reorderList(head: ListNode) -> None:
    size, temp = 0, head
    while temp: size, temp = size + 1, temp.next
    temp = head
    for i in range(int((size + 1) / 2) - 1): temp = temp.next
    tail, temp.next = temp.next, None
    current = tail
    prev = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    tail = prev
    temp = head
    while tail:
        temp_temp = temp.next
        temp.next = tail
        temp = tail
        tail = temp_temp


def is_valid_word(word):
    """
    Given a string "word", return True if word is valid, else False.
    Properties of valid word:
        - contains only alphabetical characters.
        - only first letter can be in upper-case.
        - cannot have more that 3 vowels or consonants in a row.
    Return None for empty string.
    Note: for this problems, vowers are a, e, o, i and u

    Examples:
    >>> is_valid_word('') == None
    >>> is_valid_word('Hello') == True
    >>> is_valid_word('helloworld') == True
    >>> is_valid_word('Hellllo World!') == False
    """
    if not word: return None
    curr, count = word[0].lower() in 'aeiou', 1
    for i in range(len(word)):
        if not word[i].isalpha(): return False
        if i:
            if word[i].isupper(): return False
            if curr:
                if word[i].lower() in 'aeiou':
                    count += 1
                    if count == 4: return False
                else: curr, count = 0, 1
            else:
                if word[i].lower() not in 'aeiou':
                    count += 1
                    if count == 4: return False
                else: curr, count = 1, 1
    return True


def is_fully_odd(n):
    """
    Given a positive integer, return True,
    if it is a 'fully odd' integer, else False.

    Properties of fully odd integers:
        - integer is odd
        - sum of digits is odd
        - number of digits is odd
        - number of unique digits is odd
        - contains only odd digits
    
    Examples:
    >>> is_fully_odd(753) == True
    >>> is_fully_odd(13) == False
    """
    return all([sum(map(int, str(n))) % 2, len(str(n)) % 2, len(set(str(n))) % 2, all(int(i) % 2 for i in str(n))])

assert is_fully_odd(1) == True
assert is_fully_odd(13) == False
assert is_fully_odd(243) == False
assert is_fully_odd(753) == True
assert is_fully_odd(773) == False
assert is_fully_odd(223) == False
assert is_fully_odd(23) == False
assert is_fully_odd(101) == False
assert is_fully_odd(111) == True
assert is_fully_odd(44) == False
assert is_fully_odd(7) == True
assert is_fully_odd(13) == False
assert is_fully_odd(27) == False



def matrix_perimeter(arr):
    """
    Given a matrix as a 2D array of a positive integers,
    return perimeter of a matrix. Perimeter of a matrix
    is sum of its values on edges (same as for squares).
    Return 0 for empty arr.
    Note: count 1 cell only once.

    >>> matrix_perimeter([]) == 0
    >>> matrix_perimeter([[1]]) == 1
    >>> matrix_perimeter([[1],[1],[1]]) == 3
    >>> matrix_perimeter([[1,2,3],[4,5,6],[7,8,9]]) == 40
    """
    if not arr: return 0
    for i in range(len(arr)):
        if i in [0, len(arr) - 1]: continue
        arr[i] = arr[i] if len(arr[i]) < 3 else [arr[i][0]] + [arr[i][-1]]
    return sum(j for i in arr for j in i)
        

assert matrix_perimeter([]) == 0
assert matrix_perimeter([[1]]) == 1
assert matrix_perimeter([[1],[1],[1]]) == 3
assert matrix_perimeter([[1,2,3],[4,5,6],[7,8,9]]) == 40
assert matrix_perimeter([[1,2,3,1],[4,4,5,6],[65,7,8,9]]) == 106



def between_extreme(arr):
    """
    Given an array of integers, return such subarray,
    that is obtained by finding the minimum and maximum
    integers. e.g. given [3,9,4,5,1,5] you should return [9,4,5,1],
    as 9 is maximum, and 1 is minimum integer. For several
    max/min integers choose one that appears first. e.g.
    given [1,1,1,1], max in first integer, and minimum is also first integer,
    so you should return [1]. Return empty array for empty input.

    >>> between_extreme([]) == []
    >>> between_extreme([3,9,4,5,1,5]) == [9,4,5,1]
    >>> between_extreme([3,9,4,5,1,100,5]) == [1,100]
    >>> between_extreme([1,1,1,1]) == [1]
    """
    if not arr: return []
    min_i = arr.index(min(arr))
    max_i = arr.index(max(arr))
    if max_i < min_i: min_i, max_i = max_i, min_i
    return arr[min_i:max_i+1]

assert between_extreme([]) == []
assert between_extreme([3,9,4,5,-6,5]) == [9,4,5,-6]
assert between_extreme([3,9,4,5,1,100,5]) == [1,100]
assert between_extreme([1,1,1,1]) == [1]
assert between_extreme([0]) == [0]
assert between_extreme([1,1,1,1,0]) == [1, 1, 1, 1, 0]
assert between_extreme([1,1,1,2,0]) == [2, 0]
assert between_extreme([1,1,1,1,2]) == [1, 1, 1, 1, 2]
assert between_extreme([1,1,1,-8,2]) == [-8, 2]



def counting_roots(txt, root):
    """
    Create a function that takes a string 'txt' and string 'root',
    and returns number of words in 'txt' that has text 'root' in the word.
    Word is a string of characters, separates by space.
     
    Examples:
    >>> counting_roots('', 'root') == 0
    >>> counting_roots('count', 'root') == 0
    >>> counting_roots('counting counter on Counter', 'count') == 3
    """
    return sum(1 for i in txt.split() if root.lower() in i.lower())

assert counting_roots('', 'root') == 0
assert counting_roots('count', 'root') == 0
assert counting_roots('counting counter on Counter', 'count') == 3
assert counting_roots('AcToR is acting on action movie actively', 'ACT') == 4
assert counting_roots('formula and reforms', 'form') == 2



def find_wisest_people(n, people):
    """
    The princess, to whom you are very good friend, is preparing to take
    the throne. You're really excited and want to help her in any possible way,
    so she asks you for help. She asks you to find out the wisest people in the
    kingdom. You are given a non-negative integer 'n', which is amount of people
    you need to find, and also given a list of 'people' where each person is a tuple of (a, b),
    where 'a' is age of the person, and 'b' is IQ score, both integers/floats. Wisdom of a person is a * b.
    Return first 'n' wisest people as an array of tuples (as in 'people'), sorted by
    their wisdom in descending order, For several candidacies with the same wisdom,
    give preference to those with a greater index in 'people', and also keep order of reversed 'people'.
  
    >>> find_wisest_people(0, [(1, 1)]) == []
    >>> find_wisest_people(2, [(1, 1), (2, 0.5), (3, 1)]) == [(3, 1), (1, 1)] 
    >>> find_wisest_people(10, [(1, 1), (2, 0.5), (3, 1)]) == [(3, 1), (1, 1), (2, 0.5)]
    """
    return sorted(people[::-1], key=lambda x: x[0] * x[1], reverse=True)[:n]

assert find_wisest_people(0, [(1, 1)]) == []
assert find_wisest_people(2, [(1, 1), (2, 0.5), (3, 1)]) == [(3, 1), (2, 0.5)]
assert find_wisest_people(10, [(1, 1), (2, 0.5), (3, 1)]) == [(3, 1), (2, 0.5), (1, 1)]
assert find_wisest_people(2, [(50, 2), (50, 3), (1, 1000)]) == [(1, 1000), (50, 3)]
assert find_wisest_people(2, [(50, 2), (50, 3), (50000, -1000)]) == [(50, 3), (50, 2)]


def largestKnot(arr):
    """
    You can make a knot of size 'n', only if there is a such
    array/subarray that contains 'n' integers and there is no
    adjecent same integers. e.g. the largest knot you can make
    given [1,2,3,4,1,1,1] is [1,2,3,4,1] because it is the
    longest subarray, that does not contain any adjecent duplicates.
    Given array of integer, return such subarray, with which you
    can build the largest knot. For several possible answers,
    choose the most left subarray. Return None for empty string.

    Examples:
    >>> largestKnot([]) == None
    >>> largestKnot([1,1,1,1]) == [1]
    >>> largestKnot([1,2,3,4,1,1,1]) == [1,2,3,4,1]
    """
    if not arr: return None
    res = []
    for i in range(len(arr)):
        for j in range(i + 1):
            curr = arr[j:j + len(arr) - i]
            if all(curr[i] != curr[i+1] for i in range(len(curr) - 1)) and len(curr) > len(res): res = curr
    return res

assert largestKnot([]) == None
assert largestKnot([1,1,1,1]) == [1]
assert largestKnot([1,2,3,4,1,1,1]) == [1,2,3,4,1]
assert largestKnot([1,2,3,5,5,3,4,6,7,5,4,4,3,5]) == [5, 3, 4, 6, 7, 5, 4]
assert largestKnot([0]) == [0]



def verbalize(arr):
    """
    Given an array of integers, return array of their string
    representations. String representation of an integer
    should contain all the digits verbalized and separated by space.
    For negative integer, put minus at the beginning. See examples below:
    Note: characters are in lowercase.

    Examples:
    >>> verbalize([]) == []
    >>> verbalize([23,-23,0]) == ['two three', 'minus two three', 'zero']
    """
    def to_str(n):
        digits = ['zero','one','two','three','four','five','size','seven','eight','nine']
        return ('minus ' if n < 0 else '') + ' '.join(digits[int(i)] for i in str(abs(n)))
    return list(map(to_str, arr))

assert verbalize([]) == []
assert verbalize([23,-23,0]) == ['two three', 'minus two three', 'zero']
assert verbalize([-4552, 4, 45]) == ['minus four five five two', 'four', 'four five']
assert verbalize([1,2,3,4,5,6,7,8,9,0]) == ['one', 'two', 'three', 'four', 'five', 'size', 'seven', 'eight', 'nine', 'zero']
assert verbalize([1234567890]) == ['one two three four five size seven eight nine zero']



def get_max_length(s):
    """
    Given a string 's', return the max length of such
    substring that is between any of the upper case characters.
    e.g. given ' A B B A ' return 5, as the longest
    substring that is between upper case characters
    is ' B B ' with the length of 5. Return 0 if there is
    no such substrings.

    Examples:
    >>> get_max_length('') == 0
    >>> get_max_length('A') == 0
    >>> get_max_length('AB') == 0
    >>> get_max_length(' A B B A ') == 5
    """
    caps = list(filter(lambda x: x.isupper(), s))
    if len(caps) < 2: return 0
    return len(s[s.index(caps[0]) + 1:-s[::-1].index(caps[-1]) - 1])


assert get_max_length('') == 0
assert get_max_length('A') == 0
assert get_max_length('AB') == 0
assert get_max_length(' A B B A ') == 5
assert get_max_length('HelloWorld') == 4



def perfect_factor(x):
    """
    Given a positive integer x, return its
    greatest factor that is a perfect square.
    
    >>> perfect_factor(7) == 1
    >>> perfect_factor(8) == 4
    >>> perfect_factor(9) == 9
    """
    from functools import reduce
    for i in sorted(set(reduce(list.__add__, ([i, x//i] for i in range(1, int(x**0.5) + 1) if x % i == 0))))[::-1]:
        if (i ** .5).is_integer(): return i

def perfect_factor(x):
    """
    Given a positive integer x, return its
    greatest factor that is a perfect square.
    
    >>> perfect_factor(7) == 1
    >>> perfect_factor(8) == 4
    >>> perfect_factor(9) == 9
    """
    for divisor in [i for i in range(x, 0, -1) if not x % i]:
        if (divisor ** .5).is_integer(): return divisor


assert perfect_factor(7) == 1
assert perfect_factor(8) == 4
assert perfect_factor(999999) == 9
assert perfect_factor(10**6) == 10**6
assert perfect_factor(1) == 1
assert perfect_factor(9) == 9

def extract_odd(n):
    """
    Given an integer 'n', return such odd integer
    that is obtained by taking digits from left
    part to the last digit that is odd (inclusive).
    Return None if there is no odd digits found. See examples below.

    Examples:
    >>> extract_odd(44) == None
    >>> extract_odd(4434) == 443
    >>> extract_odd(-44) == None
    >>> extract_odd(-441232) == -44123
    """
    n_temp = str(n)
    for i in range(len(n_temp) - 1, -1, -1):
        if n_temp[i] == '-': continue
        if int(n_temp[i]) % 2: return int(n_temp[:i+1])
    

assert extract_odd(44) == None
assert extract_odd(4434) == 443
assert extract_odd(-44) == None
assert extract_odd(-441232) == -44123
assert extract_odd(1111) == 1111
assert extract_odd(2111) == 2111
assert extract_odd(-445) == -445
assert extract_odd(-44566) == -445
assert extract_odd(0) == None




def expand_elements(arr, length):
    """
    You are given an array of positive integers 'arr',
    and a positive integer 'length'. If 'length'
    is less than len(arr), return None, else
    expand 'arr' by adding zeros to the sides of
    original integers, starting from the left, until
    length of arr is equal to 'length'.
    
    >>> expand_elements([], 3) == [0, 0, 0]
    >>> expand_elements([1], 3) == [0, 1, 0]
    >>> expand_elements([1, 2], 3) == [0, 1, 2]
    >>> expand_elements([1,2,3], 9) == [0, 0, 1, 0, 0, 2, 0, 3, 0]
    """
    if length < len(arr): return None
    temp = arr.copy()
    i = 0
    while len(temp) < length:
        if not i: temp.insert(i, 0)
        elif temp[i]: temp.insert(i + 1, 0)
        i += 1
        if i == len(temp): i = 0
    return temp

assert expand_elements([], 3) == [0, 0, 0]
assert expand_elements([1], 3) == [0, 1, 0]
assert expand_elements([1, 2], 3) == [0, 1, 2]
assert expand_elements([1,2,3], 3) == [1, 2, 3]
assert expand_elements([1,2,3], 9) == [0, 0, 1, 0, 0, 2, 0, 3, 0]
assert expand_elements([1], 10) == [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
assert expand_elements([1,4,6,2], 14) == [0, 0, 1, 0, 0, 4, 0, 0, 6, 0, 0, 2, 0, 0]
assert expand_elements([1,2,3,4], 3) == None

def move_pieces(arr):
    """
    You are given an array of integers.
    Find unique ways to rearrange 'arr'
    in a such way that the cumulative absolute
    differences between each adjancent integers is maximum.
    For example, [1, 2, 3] can be rearranged in 4 ways,
    [1,3,2], [2,1,3], [2,3,1] and [3,1,2] - their cumulative
    difference is 3, which is maximum cumulative difference possible.
    Note: there is at least 1 way which is input.
    Return None if 'arr' is empty.

    >>> move_pieces([]) == None
    >>> move_pieces([1]) == 1
    >>> move_pieces([1,2]) == 2
    >>> move_pieces([1,2,3]) == 4
    """
    if not arr: return None
    from itertools import permutations
    perms = [sum(abs(x[i] - x[i+1]) for i in range(len(x) - 1)) for x in list(permutations(arr))]
    return len(list(filter(lambda x: x == max(perms), perms)))

assert move_pieces([]) == None
assert move_pieces([1]) == 1
assert move_pieces([1,2]) == 2
assert move_pieces([1,2,3]) == 4
assert move_pieces([1,2,0,-3,-6]) == 4
assert move_pieces([9,4,5,-6,-4,1]) == 8


from sympy.ntheory import isprime
from sympy.ntheory import factorint


def prime_factorial(n):
    """
    Given an integer 'n', return the product of
    all integers that are <= 'n' that are prime
    or contain any prime digit. Return None if n < 2.
    
    Examples:
    >>> prime_factorial(-2) == None
    >>> prime_factorial(2) == 2
    >>> prime_factorial(5) == 2 * 3 * 5
    >>> prime_factorial(15) == 2 * 3 * 5 * 7 * 11 * 12 * 13 * 15
    """
    if n < 2: return None
    res = 1
    from sympy.ntheory import isprime
    for i in range(2, n + 1):
        if any(isprime(int(n)) for n in str(i)) or isprime(i): res *= i
    return res


assert prime_factorial(-2) == None
assert prime_factorial(2) == 2
assert prime_factorial(5) == 2 * 3 * 5
assert prime_factorial(10) == 210
assert prime_factorial(100) == 20027131012117612765521537423605317166695504528044730749209775478651171520038222282353750835200000000000000000
assert prime_factorial(15) == 2 * 3 * 5 * 7 * 11 * 12 * 13 * 15


def diverse_submatrix(matrix):
    """
    Given a squared matrix of integers, find and return
    the largest squared submatrix such that all its
    elements are different. For several results,
    give priority to a matrix that is located at the
    top, and if you still have several matrices,
    choose the most left matrix. Return None for empty 'matrix'.

    >>> diverse_submatrix([]) == None
    >>> diverse_submatrix([[1]]) == [[1]]
    >>> diverse_submatrix([[1,2,3],[1,4,5],[1,4,5]]) == [[2,3],[4,5]]
    """
    if not matrix: return None
    res = matrix
    for i in range(len(matrix), 0, -1):
        temp_x, temp_y = 0, 0
        for j in range((len(matrix) - i + 1)**2):
            curr = [[n for n in row[temp_x:temp_x + i]] for row in matrix[temp_y // (len(matrix) - i + 1): temp_y // (len(matrix) - i + 1) + i]]
            if (i ** 2) == len(set([j for i in curr for j in i])): return curr
            temp_x, temp_y = temp_x + 1, temp_y + 1
            if temp_x == (len(matrix) - i + 1): temp_x  = 0

assert diverse_submatrix([]) == None
assert diverse_submatrix([[1]]) == [[1]]
assert diverse_submatrix([[-1,-1],[-1,-1]]) == [[-1]]
assert diverse_submatrix([[1,2],[3,-4]]) == [[1, 2], [3, -4]]
assert diverse_submatrix([[1,2,3],[1,4,5],[1,4,5]]) == [[2,3],[4,5]]
assert diverse_submatrix([[1,2,3],[1,2,5],[1,4,9]]) == [[2, 5], [4, 9]]
assert diverse_submatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def extract_odd(n):
    """
    You are given an integer 'n'. Imagine
    you've converted it to string. You task is
    to find such odd digit that is located at the
    most right side of a string, e.g. for '4434', it
    would be 3. then slice everything starting from the
    beginning till that found odd (inclusive), and return its
    integer representation, so for '4434' return 443.
    Return None if there is no odd digits found.

    Examples:
    >>> extract_odd(44) == None
    >>> extract_odd(4434) == 443
    >>> extract_odd(-44) == None
    >>> extract_odd(-441232) == -44123
    """
    n_temp = str(n)
    for i in range(len(n_temp) - 1, -1, -1):
        if n_temp[i] == '-': continue
        if int(n_temp[i]) % 2: return int(n_temp[:i+1])


def expand_elements(arr, length):
    """
    You are given an array of positive integers 'arr',
    and a positive integer 'length'. If 'length'
    is less than len(arr), return None, else
    expand 'arr' by adding zeros to the sides of
    original integers, starting from the left, until
    length of arr is equal to 'length'. For example:
    arr = [1, 2], length = 7. We have 2 original integers
    and 3 spaces to fill (2 on sides and 1 in-between). We start
    filling from left to right: [1,2] -> [0,1,2] -> [0,1,0,2] -> [0,1,0,2,0].
    Now we have only 5 items, we need 2 more, so we go again.
    [0,1,0,2,0] -> [0,0,1,0,2,0] -> [0,0,1,0,0,2,0]

    >>> expand_elements([], 3) == [0, 0, 0]
    >>> expand_elements([1], 3) == [0, 1, 0]
    >>> expand_elements([1, 2], 7) == [0,0,1,0,0,2,0]
    >>> expand_elements([1,2,3], 9) == [0, 0, 1, 0, 0, 2, 0, 3, 0]
    """
    if length < len(arr): return None
    temp = arr.copy()
    i = 0
    while len(temp) < length:
        if not i: temp.insert(i, 0)
        elif temp[i]: temp.insert(i + 1, 0)
        i += 1
        if i == len(temp): i = 0
    return temp




def counting_roots(txt, root):
    """
    You are given strings 'txt' and 'root'.
    Family of words are words that is based on same root, e.g.
    words 'count' and 'counter' are from same family with root 'count'.
    Return number of words in 'txt' that belong to family 'root' (string given as an argument).
    Note: word is a group of characters separated by space.
    Ignore capitalization.
     
    Examples:
    >>> counting_roots('', 'root') == 0
    >>> counting_roots('count', 'root') == 0
    >>> counting_roots('counting counter on Counter', 'count') == 3
    """
    return sum(1 for w in list(txt.split()) if root.lower() in w.lower())


assert counting_roots('', 'root') == 0
assert counting_roots('count', 'root') == 0
assert counting_roots('counting counter on Counter', 'count') == 3
assert counting_roots('AcToR is acting on action movie actively', 'ACT') == 4
assert counting_roots('formula and reforms', 'form') == 2



def is_short_duplicate(s1, s2):
    """
    String 's1' is a short duplicate of 's2' if
    string 's2' is a substring of a string formed
    by repeating string 's1' as many times required.
    For example, for s1 = 'ok', and s2 = 'kokok', you should
    return True, as you can repeat 's1' 3 times -> 'okokok', which
    contains 's2'. Capitaliation is important.
    Note: empty string is a short duplicate of any string.
    
    Examples:
    >>> is_short_duplicate('', '') == True
    >>> is_short_duplicate('', 'word') == True
    >>> is_short_duplicate('ok', 'kokok') == True
    >>> is_short_duplicate('lol', 'lolol') == False
    """
    return s1 == '' or s2 in s1 * len(s2)

assert is_short_duplicate('', '') == True
assert is_short_duplicate('', 'word') == True
assert is_short_duplicate('ok', 'kokok') == True
assert is_short_duplicate('lol', 'lolol') == False
assert is_short_duplicate('ok ', 'kokok') == False
assert is_short_duplicate('abc', 'bc') == True
assert is_short_duplicate('abc', 'bcabcab') == True
assert is_short_duplicate('abc', 'bcabcaba') == False

def reverse_odds(arr):
    """
    You are given an array of integers 'arr'.
    'Reversed pair' of arr[i] is arr[len(arr) - i - 1].
    Read through each integer (not index),
    and if it is odd, reverse it with its 'reversed pair'.
    e.g given [1, 2, 3, 4, 6], return [6, 2, 3, 4, 1].
    If both 'reversed pairs' are odds, you need
    to reverse twice, (or keep the original order).
    Note: you should apply reversing to every integer
    only once, for instance, arr = [1, 2]: 1 is odd, so we
    reverse -> [2,1]. We've applied reversing to 1,
    and need to apply for 2. 2 is even, so we return [2,1].

    Examples:
    >>> reverse_odds([]) == []
    >>> reverse_odds([1]) == [1]
    >>> reverse_odds([1,2]) == [2,1]
    >>> reverse_odds([1,2,3,4,5]) == [1, 2, 3, 4, 5]
    """
    for i in range(len(arr) // 2):
        if (arr[i] % 2 + arr[len(arr) - i - 1] % 2) % 2:
            arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
    return arr

assert reverse_odds([]) == []
assert reverse_odds([1]) == [1]
assert reverse_odds([1,2]) == [2,1]
assert reverse_odds([1,2,3,4,5]) == [1, 2, 3, 4, 5]
assert reverse_odds([1,3,-5,-6,-3,7,8]) == [8, 3, -5, -6, -3, 7, 1]
assert reverse_odds([-2,-4,-6,8,0]) == [-2,-4,-6,8,0]
assert reverse_odds([1, 2, 3, 4, 6]) == [6, 2, 3, 4, 1]



from datetime import datetime

def car_scratches_to_date(s):
    """
    There is a maniac who scratches valid dates on cars.
    Maniac scratches year in a format of 4 integers,
    month as a lowercase string, and day as 2 integers.
    However the order of year, month and day is random.
    e.g. it can be '2020 september 04' or '  04 2020 september  '.
    Given a string, representing a valid maniac's scratch, return
    python datetime object of the scratched date.

    Examples:
    >>> car_scratches_to_date('2020 september 04') == datetime(2020, 9, 4)
    >>> car_scratches_to_date('  04 2020 september  ') == datetime(2020, 9, 4)
    """
    months = ['january','february','march','april','may','june','july','august','september','october','november','december']
    date = sorted(s.split())
    return datetime(int(date[1]), months.index(date[2]) + 1, int(date[0]))

from datetime import datetime
assert car_scratches_to_date('2020 september 04') == datetime(2020, 9, 4)
assert car_scratches_to_date('  04 2020 september  ') == datetime(2020, 9, 4)
assert car_scratches_to_date(' september 2020 04    ') == datetime(2020, 9, 4)
assert car_scratches_to_date(' january 1956 14    ') == datetime(1956, 1, 14)
assert car_scratches_to_date('14  january 1956     ') == datetime(1956, 1, 14)



def special_integers(arr):
    """
    Given an array of integers, obtain new array by getting
    'special integers', while keeping the original order.
    An integer x in array is special if you can obtain x by
    multuplying or dividing every integer in array by any integer.

    Examples:
    >>> special_integers([]) == []
    >>> special_integers([0,1,2,3]) == [0]
    >>> special_integers([1,2,3,6]) == [1,6]
    >>> special_integers([-1,2,2,4,8]) == [-1,2,2,4,8]
    """
    res = []
    for i in arr:
        temp = []
        if not i:
            res.append(i)
            continue
        for j in arr:
            if j and (not j % i or not i % j): temp.append(1)
            else:
                temp.append(0)
                break
        if all(temp): res.append(i)
    return res
   

assert special_integers([]) == []
assert special_integers([0,1,2,3]) == [0]
assert special_integers([1,2,3,6]) == [1,6]
assert special_integers([-1,2,2,4,8]) == [-1,2,2,4,8]
assert special_integers([1,13,26]) == [1, 13, 26]

'''

#Here is an example of how to test printing to stdout.
from io import StringIO
from unittest.mock import patch
​
def foo():
    #Prints hello world.
    print("Hello World!")
​
def check_candidate():
    with patch('sys.stdout', new=StringIO()) as fakeOutput:
        foo()
        assert fakeOutput.getvalue() == "Hello World!\n"

##############################

def get_name_and_age():
    '''
    This function will first display "Name:" to Stdout and accept a string from Stdin.
    Then will display "Age:" to Stdout and accept a string from Stdint.
    Finally function prints: "Nice to meet you {name}!\nYou are {age} years old!"
    '''
    name = input("Name:")
    age = input("Age:")
    print(f"Nice to meet you {name}!\nYou are {age} years old!")
def check_candidate():
    from io import StringIO
    from unittest.mock import patch
    fake_input = iter(['HUMAN', '1000']) #Inputs in order to be passed through input().
    def se(args=None):
        if args is not None:
            print(args) #Prints the stdout part of input, so it can be caught too.
        #This gets called every time the mocked object is called, with the same arguments.
        return next(fake_input) #Returns the next fake input each time it is called.
​
    with patch("builtins.input", side_effect=se):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            get_name_and_age()
            data = fake_output.getvalue()
    assert data == 'Name:\nAge:\nNice to meet you HUMAN!\nYou are 1000 years old!\n'
check_candidate()
######################

#PROMPT
​
​
# Language: Python 3
# Task: Synthesize function
​
def remind_me(dir_path):
    '''
    You get back from vacation and you want to remind yourself what you were working on.
    
    You are given a path to a directory 'dir_path' as a string.
    Find all python files in the directory recursively.
    Order the files from most recently modified to least recently modified.
    Print the results to Stdout in the following format:
​
    {filename1}
    last modified: {MM-DD-YYYY}
    {last line of filename1}
    {filename2}
    ...
    
    Note: the final line should end with a newline '\n'
    '''
​
#TEST
def test_candidate():
    from pyfakefs.fake_filesystem_unittest import Patcher
    from io import StringIO
    from unittest.mock import patch
    
    with patch('sys.stdout', new=StringIO()) as fakeOutput:
        with Patcher() as patcher:
            import os
            from datetime import datetime
            filelist = []
            lastlines = []
            last_modifieds = []
            #Make some fake dirs.
            os.makedirs("/foo/bar")
            os.makedirs("/foo/foo2/foo3")
​
            #Make some fake files.
            with open("/foo/a.txt", "w") as f:
                f.write("end of a")
            os.utime("/foo/a.txt", (1,1))
            with open("/foo/bar/b.txt", "w") as f:
                f.write("end of b")
            os.utime("/foo/bar/b.txt", (2,2))
            with open("/foo/bar/q.txt", "w") as f:
                f.write("end of q")
            os.utime("/foo/bar/q.txt", (2000000,2))
            with open("/foo/foo2/c.py", "w") as f:
                f.write("beginning of c\n")
                f.write("end of c")
                filelist.append("/foo/foo2/c.py")
            os.utime("/foo/foo2/c.py", (5*10**5,5*10**5))
            with open("/foo/foo2/foo3/d.py", "w") as f:
                f.write("end of d")
                filelist.append("/foo/foo2/foo3/d.py")
            os.utime("/foo/foo2/foo3/d.py", (5*10**10,5*10**10)) #Sets the date modified for testing purposes.
            #Grab last modified dates.
            for filepath in filelist:
                last_modifieds.append(os.path.getmtime(filepath))
                with open(filepath, "r") as f:
                    lastlines.append(list(f.readlines())[-1])
            results = list(zip(filelist, lastlines, last_modifieds))
            results = sorted(results, key=lambda x:x[-1], reverse=True) #Reverse sort by date modifed.
            output = []
            for path, line, t in results:
                name = os.path.split(path)[-1]
                output.append(name)
                dt_object = datetime.fromtimestamp(t)
                s = str(dt_object.strftime("%m-%d-%Y"))
                output.append(f"last modified: {s}")
                output.append(line)
            output = "\n".join(output)+"\n"
            remind_me("/foo")
            result = fakeOutput.getvalue()
    assert result == output
​
#SOLUTION
# Language: Python 3
# Task: Synthesize function
​
def remind_me(dir_path):
    '''
    You get back from vacation and you want to remind yourself what you were working on.
    
    You are given a path to a directory 'dir_path' as a string.
    Find all python files in the directory recursively.
    Order the files from most recently modified to least recently modified.
    Print the results to Stdout in the following format:
​
    {filename1}
    last modified: {MM-DD-YYYY}
    {last line of filename1}
    {filename2}
    ...
    
    Note: the final line should end with a newline '\n'
    '''
    import os
    from datetime import datetime
    file_list = []
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            if filename.endswith('.py'):
                f_path = os.path.join(dirpath, filename)
                file_list.append(f_path)
    file_list = sorted(file_list, key=lambda x: os.path.getmtime(x))
    file_list.reverse()
    for file_path in file_list:
        name = os.path.split(file_path)[-1]
        print(name)
        last_modified = str(datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%m-%d-%Y'))
        print(f"last modified: {last_modified}")
        with open(file_path, "r") as f:
            print(list(f.readlines())[-1])
#######################
def foo(x):
    '''
    Input x, if x is not a string raise a ValueError.
    Otherwise capitalize the first letter of x and return it.
    '''
    if not isinstance(x, str):
        raise ValueError
    return x[0].capitalize() + x[1:]
 
def check_candidate(): 
    import unittest
    class SampleTest(unittest.TestCase):
        def test_exceptions(self):
            with self.assertRaises(ValueError):
                foo(1)
            with self.assertRaises(ValueError):
                foo(2.0)
            with self.assertRaises(ValueError):
                foo([])
            with self.assertRaises(ValueError):
                foo(None)
​
    SampleTest().test_exceptions()
    assert foo("abv") == "Abv"
​
check_candidate()

###########################
https://faker.readthedocs.io/en/master/index.html
##########################
def foo(url):
    '''
    Counts the number of characters in the HTML code of a given 'url'.
    '''
    import requests
    stuff = requests.get(url)
    return len(stuff.text)
​
def check_candidate():
    def fake_request(url):
        class FakeRequest(object):
            def __init__(self): 
                self.text ='''
            HTML!!!!
            '''
        if url == "http://www.python.org":
            o = FakeRequest()
            return FakeRequest()
        else:
            raise ValueError
    from unittest.mock import patch
    with patch("requests.get", new=fake_request):
        assert foo("http://www.python.org") == 34
check_candidate()
#######################

import sys
import unittest
from unittest.mock import MagicMock, patch
sys.modules['cv2'] = MagicMock()
import foo
class TestFoo(unittest.TestCase):
     @patch('cv2.imread')
     def test_load_image(self, imread):
         foo.load_image('test')
         assert imread.called

##################
def test():
	input_str = "hello"
	copy_input_str = "".join([c for c in input_str])
	assert foo(input_str) == "goodbye"

####################

def test_foo(bar):
    id_bar_foo = id(bar)
    bar = bar.upper()
    return id_bar_foo, id(bar)
bar = "Hello"
id_bar = id(bar)
id_bar_foo, id_up_foo = test_foo(bar)
assert bar == "Hello" and id_bar == id_bar_foo and id_bar != id_up_foo
##########################
