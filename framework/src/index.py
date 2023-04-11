
# Hàm này không gọi hàm nào khác
def independentFunction(a):
    return (a)

# Hàm này gọi hàm foo nên khi test bằng unit test cần phải mock
def functionThatCallOther(a):
    result = foo(a)
    return result


def foo(a):
    return a 


def check_triangle(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return false
    return true

def check_prime_number(n):
    #flag = 0 => không phải số nguyên tố
    #flag = 1 => số nguyên tố
    flag = 1;
    if (n <2):
        flag = 0
        return flag  #Số nhỏ hơn 2 không phải số nguyên tố => trả về 0
    
    #Sử dụng vòng lặp while để kiểm tra có tồn tại ước số nào khác không
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break #Chỉ cần tìm thấy 1 ước số là đủ và thoát vòng lặp
    return flag

def print_Prime(n):
    for i in range(2,n):
        if check_prime_number(i):
            print(i)
