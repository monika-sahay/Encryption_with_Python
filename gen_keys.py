from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


private_key = rsa.generate_private_key(
    public_exponent = 65537,
    key_size= 2048
)
priv_pem = private_key.private_bytes(
    encoding = serialization.Encoding.PEM,
    format= serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

print(priv_pem)