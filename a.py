my_str = "hello world"
my_str_as_bytes = str.encode(my_str)
print(my_str_as_bytes) # ensure it is byte representation
my_decoded_str = my_str_as_bytes.decode()
print(my_decoded_str) # ensure it is strin
