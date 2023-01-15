
def parse_int(num):
    return [int(i) for i in str(num)]


def cc_validaiton(c_num):
    if len(str(c_num)) != 16:
        return False
    validation(c_num)


def imei_validaiton(imei_num):
    if len(str(imei_num)) != 15:
        return False
    validation(imei_num)


def validation(num):
    num = parse_int(num)
    odd_digits = num[-1::-2]
    even_digits = num[-2::-2]
    odd_sum = sum(odd_digits)
    even_sum = 0
    for i in even_digits:
        if i*2 > 9:
            even_sum += int(str(i*2)[0]) + int(str(i*2)[1])
        else:
            even_sum += (i*2)
    if (odd_sum+even_sum) % 10 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(validation(5590490208098960))
    print(validation("661828289361090"))
    print(validation("351162962088848"))
