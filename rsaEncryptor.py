#RSA 5-digit Encryptor Program

print('Welcome to the RSA Encryptor! Enter a value for a prime number p')
p = int(input())

print('Enter a value for another prime number q')
q = int(input())

n = p * q

print('Your RSA modulus n is ' + str(n)+'.')

print('Enter a value for e, the 2nd part of the public key')
e = int(input())

print('Your public key is ' + str(n) + ',' + str(e))

d = str(((p - 1) * (q - 1) * (e - 1) + 1) / 3 )
print(d)

print('Enter your first number')
firstNumber = int(input())

print('Enter your second number')
secondNumber = int(input())

print('Enter your third number')
thirdNumber = int(input())

print('Enter your fourth number')
fourthNumber = int(input())

print('Enter your fifth number')
fifthNumber = int(input())

firstNumberEncrypted = (firstNumber**e) % n

secondNumberEncrypted = (secondNumber**e) % n

thirdNumberEncrypted = (thirdNumber**e) % n
 
fourthNumberEncrypted = (fourthNumber**e) % n

fifthNumberEncrypted = (fifthNumber**e) % n

print('Your encrypted message is ' + str(firstNumberEncrypted) + ' ' + str(secondNumberEncrypted) + ' ' + str(thirdNumberEncrypted) + ' ' + str(fourthNumberEncrypted) + ' ' + str(fifthNumberEncrypted))
