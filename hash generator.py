"""
This app will generate SHA-256 hashes for input strings or files
"""
import hashlib

def generate_hash(input_string):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the bytes of the input string
    sha256_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    return sha256_hash.hexdigest()
def generate_file_hash(file_path):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Open the file in binary mode and read it in chunks
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    # Get the hexadecimal representation of the hash
    return sha256_hash.hexdigest()

def hash_generator():
    # Get user input for string or file
    choice = input("Do you want to hash a string or a file? (Enter 'string' or 'file'): ").strip().lower()
    if choice == 'string':
        user_input = input("Enter the string to hash: ")
        print("SHA-256 Hash:", generate_hash(user_input))
    elif choice == 'file':
        file_path = input("Enter the file path to hash: ")
        try:
            print("SHA-256 Hash:", generate_file_hash(file_path))
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")
    else:
        print("Invalid choice. Please enter 'string' or 'file'.")
if __name__ == "__main__":
    hash_generator()