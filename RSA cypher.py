# RSA Encryption without libraries

def mcd (a, b):
    while b != 0:
        z = a
        a = b
        b = z%b
    return a

def coprime(mcd_testing):
    if mcd_testing == 1:
        return True
    else:
        return False

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def phi_operation(p, q):
    result = (p-1)*(q-1)
    return result

def keygen(p, q):
    n = p * q
    phi = phi_operation(p, q)
    e = 65537
    if mcd(e, phi) != 1:
        e = 3

    d = modinv(e, phi)
    return (e, n), (d, n)

def cypher(message, public_key):
    e, n = public_key
    encrypted_list = []
    for char in message:
        m = ord(char)
        c = pow(m, e, n)
        encrypted_list.append(c)
    return encrypted_list


def decypher(ciphertext, private_key):
    d, n = private_key
    for values in ciphertext:
        x = chr(values)
        print(x)
    return (ciphertext, d, n)

def decypher(ciphertext, private_key):
    d, n = private_key
    decrypted_message = ""
    for c in ciphertext:
        m = pow(c, d, n)
        decrypted_message += chr(m)
    return decrypted_message

public, private = keygen(61, 53)
c = cypher("Hello!!", public)
print(c)
r = decypher([3000, 1313, 745, 745, 2185, 1853, 1853], private)
print(r)