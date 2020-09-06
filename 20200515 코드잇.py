def introduce(name, age, nationality="한국"):
    print(f"내 이름은 {name}, 나이는 {age}살, 국적은 {nationality}입니다.")
    return "하이하이"

print(introduce("임지아",30))

def is_evenly_divisible(number):
    return number % 2 == 0 


# 테스트
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))



def calculate_change(payment, cost):
    change = payment - cost
    a = change // 50000
    b = (change % 50000) // 10000
    c = (change % 10000) // 5000
    d = (change % 5000) // 1000

    print("50000원 지폐 : {}장".format(a))
    print("10000원 지폐 : {}장".format(b))
    print("5000원 지폐 : {}장".format(c))
    print("1000원 지폐 : {}장".format(d))


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)