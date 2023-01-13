# post请求

import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
}

# data = {
# 	'kw': 'spider'
# }

# # post请求的参数 必须要进行编码
# data = urllib.parse.urlencode(data).encode('utf8')

# # 要放在请求定制的对象中
# request = urllib.request.Request(url=url, data=data, headers=headers)
#
# # 发送请求
# response = urllib.request.urlopen(request)
#
# content = response.read().decode('utf8')

while True:
	words = input('请输入要翻译的语句:')
	data = {
		'kw': words
	}
	data = urllib.parse.urlencode(data).encode('utf8')
	# 要放在请求定制的对象中
	request = urllib.request.Request(url=url, data=data, headers=headers)

	# 发送请求
	response = urllib.request.urlopen(request)

	content = response.read().decode('utf8')
	obj = json.loads(content)
	# print('翻译结果为:', dict(obj).get('v'))
	for item in obj.get('data'):
		print(item.get('v'), end='\t')
	print()

# 把str -> json对象
# obj = json.loads(content)
# print(obj)


