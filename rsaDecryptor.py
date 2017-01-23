#RSA 5-digit Decryptor Program

print('Welcome to the RSA Decryptor! Enter the value of q')
p = int(input())

print('Enter the  value of q')
q = int(input())

n = p * q

print('Your RSA modulus n is ' + str(n)+'.')

print('Enter a value for e, the 2nd part of the public key')
e = int(input())

print('Your public key is ' + str(n) + ',' + str(e))

d = ((p - 1) * (q - 1) * (e - 1) + 1) / 3 

print('enter the 2nd part of the private key d')
privateKey = int(input())

if privateKey == d:
    print('You are correct! Beginning decryption...')

    print('Enter the first number')
    firstNumber = int(input())

    print('Enter the second number')
    secondNumber = int(input())

    print('Enter the third number')
    thirdNumber = int(input())

    print('Enter the fourth number')
    fourthNumber = int(input())

    print('Enter the fifth number')
    fifthNumber = int(input())

    firstNumberDecrypted = (firstNumber**privateKey) % n

    secondNumberDecrypted = (secondNumber**privateKey) % n

    thirdNumberDecrypted = (thirdNumber**privateKey) % n
 
    fourthNumberDecrypted = (fourthNumber**privateKey) % n

    fifthNumberDecrypted = (fifthNumber**privateKey) % n

    print('Your decrypted message is ' + str(firstNumberDecrypted) + ' ' + str(secondNumberDecrypted) + ' ' + str(thirdNumberDecrypted) + ' ' + str(fourthNumberDecrypted) + ' ' + str(fifthNumberDecrypted))
    
else:
    print('Your guess is wrong. Bye bye!')
