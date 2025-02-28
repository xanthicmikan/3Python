#Use re module
import re

text = '''根 據 規 則 移 除 空 白 ( 笑 )'''

regex= re.compile(r'[\u4E00-\u9FFF\uFF00-\uFFFF\u0021-\u002F\n]|[a-zA-Z0-9]+')
arr = re.findall(regex, text)
text = ' '.join(arr)

regex= re.compile(r'(?<=[^a-zA-Z0-9\u0021-\u002E])(\x20)(?=[^a-zA-Z0-9\u0021-\u002E])')
text = re.sub(regex, '', text)

regex= re.compile(r'(\x20)(?=[\(\%\uFF00-\uFFFF])')
text = re.sub(regex, '', text)

text = text.replace(' . ','.')
print(text)