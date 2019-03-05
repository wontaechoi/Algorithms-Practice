def solution(phone_book):
    num_hash = {}
    for num in phone_book:
        num_hash[num] = 1
    for num in phone_book:
        for n in num_hash:
            if num!=n:
                if num in n[:len(num)]:
                    return False
    answer = True
    return answer