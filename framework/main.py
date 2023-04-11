from src.index import independentFunction
from src.index import check_triangle, print_Prime


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    if check_triangle(a,b,c):
        print("La tam giac hop le")
    else:
        print("Khong phai la tam giac")
    n = int(input())
    print_Prime(n)
    
    
    independentFunction(1)
