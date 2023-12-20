with open('20200126.txt', 'r', encoding='utf-8') as f:
    # 读取文件内容
    text = f.read()

# 将文本编码为 UTF-8
text_utf8 = text.encode('utf-8')

# 将编码后的文本写入新的文件
with open('new.txt', 'w', encoding='utf-8') as f:
    f.write(text_utf8)