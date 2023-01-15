def isbn10_validation(num):
    if len(num) != 10:
        return False
    isbn = list(reversed([int(i) for i in str(num)]))
    sum = 0
    for i, val in enumerate(isbn, 1):
        sum += i*val
    if sum % 11 == 0:
        return True
    else:
        return False
    # print(sum)


def isbn13_validation(num):
    if len(num) != 13:
        return False
    isbn = list(reversed([int(i) for i in str(num)]))
    odd_digits = isbn[-1::-2]
    even_digits = isbn[-2::-2]
    odd_sum = sum(odd_digits)
    even_sum = 0
    for i in even_digits:
        even_sum += i*3
    if (even_sum+odd_sum) % 10 == 0:
        return True
    else:

        return False
    # print(odd_sum+even_sum)


if __name__ == "__main__":
    isbn10_validation("0716703440")
    isbn13_validation("9780716703440")
