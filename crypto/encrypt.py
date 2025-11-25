# crypto/encrypt.py
import os
from ctypes import CDLL, c_char_p, create_string_buffer

_here = os.path.dirname(__file__)
dll_name = os.path.join(_here, "encrypt.dll")

# Carrega a DLL
_lib = CDLL(dll_name)

# Assinatura da função: void encrypt_password(const char* input, char* output)
_lib.encrypt_password.argtypes = [c_char_p, c_char_p]
_lib.encrypt_password.restype = None

def encrypt(password: str) -> str:
    if password is None:
        raise ValueError("password is None")
    out = create_string_buffer(65)  # 64 hex + null
    _lib.encrypt_password(password.encode('utf-8'), out)
    return out.value.decode('ascii')
