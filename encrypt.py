


from cryptography.fernet import Fernet
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

# Usage:
encrypt_file("./_internal/cred.json", b'mtevl27w0WsbYu6V_JAd8ApbFhB9Gx0XvWc56UsQeDA=')