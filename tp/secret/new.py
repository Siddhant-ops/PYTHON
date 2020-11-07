print("\n================================================================================================\n")


# lines = ["You have woken up in a mysterious maze",
#          "The building has 5 levels",
#          "Scans show that the floors increase in size as you go down"]

# from time import sleep

# for line in lines:          # for each line of text (or each message)
#     for c in line:          # for each character in each line
#         print(c, end='')    # print a single character, and keep the cursor there.
#         sleep(0.1)          # wait a little to make the effect look good.
#     print('')


from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
        key_file.close()


# generate_key();


def load_key():
    return open("secret.key", "rb").read()


def encrypt_message(message):
    key = load_key()
    print(f"My initial message is : {message}")
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    print("\n==================================================\n")

    print(f"my encrypted message is {encrypted_message}")


print(encrypt_message("hello"))


def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    decoded_message = decrypted_message.decode()

    print("\n==================================================\n")

    print(f"my decrypted message is {decoded_message}")


decrypt_message(encrypt_message)

