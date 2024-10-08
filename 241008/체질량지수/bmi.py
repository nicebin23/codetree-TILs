h, w = map(int, input().split())
b = w/(h/100)**2
print(int(b))
if b >= 25 :
    print("Obesity")