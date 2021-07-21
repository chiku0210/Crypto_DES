from hashlib import sha256
from random import randint


def convert_message_to_int(M):
    return int(sha256(M.encode()).hexdigest(), 16)

# generate signature
def gen_public_sig(X, M): #X is password, M is message

    g = 2  # Genrator Function
    p = 11  # prime number


    m = convert_message_to_int(M)

    y = pow(g, m, p)
    r = randint(0, p - 1)
    h = pow(g, r, p)
    b = randint(0,1)
    s = (r+b*m)%(p-1)

    tup = (y, s, r, h, b)

    return tup

# verify
def verify(t):

    y, s, r, h, b = t

    g = 2  # Genrator Function
    p = 11  # prime number

    # c = hashThis(t1, t2, t3)

    if (pow(g, s, p) == (pow(y, b, p) * h) % p):
        return True
    return False


# print(verify(gen_public_sig(123, 'hi')))