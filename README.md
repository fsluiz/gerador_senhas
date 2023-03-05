# gerador_senhas
This Python code generates a random password with a specified length.

To run the code, open a Python environment or IDE and run the file. The user will be prompted to enter the desired password length.

The password is generated using a combination of uppercase and lowercase letters, digits, and special characters. The list of characters is defined by the chars variable, which is a string that contains ASCII letters, digits, and several special characters such as "!@#$%&*()_+?".

The random.SystemRandom() method is used to generate a cryptographically secure random number, which ensures that the password is truly random and not predictable.

Finally, the password is printed to the console as a string using the join() method to concatenate the randomly chosen characters.

Note that this code is for educational purposes only and should not be used for real-world password generation, as it does not provide any security features such as hashing or salting.
