text = "蓝盟"
encoded = text.encode('utf-8') # UTF-8编码
print(encoded) # 输出: b'\xe4\xb8\xad\xe6\x96\x87'
decoded = encoded.decode('utf-8') # 解码回原始文本
print(decoded) # 输出: 中文
str_utf8 = text
byte_length = len(str_utf8.encode('utf-8'))
print(byte_length)  ## 输出字节长度