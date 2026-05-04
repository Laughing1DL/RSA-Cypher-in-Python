# RSA Encryption (Pure Python, No Libraries)

This project is a simple educational implementation of the RSA encryption algorithm written entirely in Python, without using external cryptography libraries.

It demonstrates the core mathematical concepts behind RSA, including key generation, encryption, and decryption.

--------------------------------------------------------------------------------- 

### Features
RSA key pair generation
Encryption of text messages
Decryption of ciphertext
Implementation of:
Euclidean Algorithm (GCD)
Extended Euclidean Algorithm
Modular inverse
Euler’s Totient function

--------------------------------------------------------------------------------- 

## How It Works

RSA is based on the mathematical difficulty of factoring large numbers.

--------------------------------------------------------------------------------- 

### Key Steps:

Choose two prime numbers p and q
Compute:
n = p * q
φ(n) = (p-1)(q-1)

Choose public exponent e such that:
gcd(e, φ(n)) = 1

Compute private key d:
d = e⁻¹ mod φ(n)
Public key = (e, n)
Private key = (d, n)

--------------------------------------------------------------------------------- 

### Functions Overview

#### mcd(a, b):

Computes the greatest common divisor using the Euclidean algorithm.

#### coprime(mcd_testing):

Checks if two numbers are coprime.

#### egcd(a, b):

Extended Euclidean algorithm.

#### modinv(a, m): 

Finds modular inverse of a modulo m.

#### phi_operation(p, q):

Computes Euler's Totient function.

#### keygen(p, q):

Generates public and private keys.

#### cypher(message, public_key):

Encrypts a string into a list of integers.

#### decypher(ciphertext, private_key):

Decrypts a list of integers back into a string.

--------------------------------------------------------------------------------- 

### Example Usage: 
public, private = keygen(61, 53)

encrypted = cypher("Hello!!", public)
print("Encrypted:", encrypted)

decrypted = decypher(encrypted, private)
print("Decrypted:", decrypted)

--------------------------------------------------------------------------------- 

### Example Output
Encrypted: [3000, 1313, 745, 745, 2185, 1853, 1853]
Decrypted: Hello!!

--------------------------------------------------------------------------------- 

### Important Notes
This implementation is for educational purposes only.
It is not secure for real-world use because:
Uses small prime numbers
Lacks padding (e.g., OAEP)
Processes characters individually
Real cryptographic systems use optimized libraries and much larger keys (2048+ bits).

--------------------------------------------------------------------------------- 

### Concepts Covered
Number theory
Modular arithmetic
Cryptography basics
Public-key encryption

--------------------------------------------------------------------------------- 

## Possible Improvements
Add prime number generation
Support larger keys
Implement padding (OAEP)
Encrypt full blocks instead of characters
Add CLI or GUI interface

--------------------------------------------------------------------------------- 

## Requirements
Python 3.x
No external libraries required
