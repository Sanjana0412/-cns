import socket
from xor_cipher import xor_encrypt_decrypt

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5002

def send_single_message(msg: str, key: str) -> str:
   
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_HOST, SERVER_PORT))

    encrypted_msg = xor_encrypt_decrypt(msg, key)
    payload = f"{encrypted_msg}|||{key}"
    client.send(payload.encode())

    encrypted_ack = client.recv(1024).decode()
    ack = xor_encrypt_decrypt(encrypted_ack, key)

    client.close()
    return ack

