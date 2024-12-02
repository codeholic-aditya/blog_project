# import hashlib
# id=""
# hashcode=hashlib.sha256(id.encode('utf-8')).hexdigest()
# print(hashcode[:20])


# import datetime
# date=datetime.datetime.now()
# print(date)



import base64

input_string = "Hello, World!"

input_bytes = input_string.encode('utf-8')

encoded_bytes = base64.b64encode(input_bytes)

encoded_string = encoded_bytes.decode('utf-8')

print(encoded_string)

decoded_bytes = base64.b64decode(encoded_string)

decoded_string = decoded_bytes.decode('utf-8')

print(decoded_string)