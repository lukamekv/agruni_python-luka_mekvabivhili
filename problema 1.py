import random
import math

def ricxvi(n):
    counter = 0
    for _ in range(n):
        a = random.random()
        b = random.random()
        if math.sqrt(a**2 + b**2) <= 1:
            counter += 1
    return 4 * counter / n



for n in [10, 1_000, 100_000, 10_000_000]:
    print(ricxvi(n))

    # დასკვნა: რაც უფრო მეტ წერტილს ვიღებთ მით უფრო ვუახლოვდებით π-ის მნიშვნელობას. შეცდომა მცირდება დაახლოებით √n-ის პროპორციულად თუმცა რადგან შემთხვევით წერტილებს ვაძლევთ შედეგი განსხვავდება.