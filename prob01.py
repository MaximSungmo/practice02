# 문제1. 파이썬 경로명 s = &#39;/usr/local/bin/python&#39; 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.

s = '/usr/local/bin/python'

# 디렉토리 경로명 분리
s_list = s.split(sep='/')

# 공백 리스트 제거
s_trimed_list = [x for x in s_list if x]
print(s_trimed_list)

print(s.rsplit("/",1))





