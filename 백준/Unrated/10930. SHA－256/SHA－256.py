import hashlib

data = input()
encode_data = data.encode()
result = hashlib.sha256(encode_data).hexdigest()
print(result)
