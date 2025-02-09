for i in range(2,1000):
    count = 0
    for j in range(2,i-1):
         if (i % j) == 0:
             count += 1
    if count == 0:
        print(f"prime found! {i} is a prime number.")

