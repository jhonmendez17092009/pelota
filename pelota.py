# input

h = int(input("digite el valor de h: "))

# processing

q = h/5
n = 0

while h >= q:

    h = 0.9 * h

    n = n + 1

# output

print("la pelota rebota le quinta parte en el rebote " + str (n))