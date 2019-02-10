dict1 = {}
print(type(dict1))

# list 와 달리 순서 상관없이 key-value 형식으로 추가가능
dict1[5] = 25
dict1[2] = 4
dict1[3] = 9
print(dict1)
print(dict1[3])

family = {}

family['mom'] = 'grace'
family['dad'] = 'chris'
family['son'] = 'young'
family['daughter'] = 'kay'

print(family)
print(family['dad'])
print(family['son'])

# 사전의 key 모두 받아오기
print(family.keys())

# 사전 요소 확인
print('son' in family.keys())
print(type(family.keys())) # dict_keys

# key_list
family_keys = list(family.keys())
print(family_keys)
print(type(family_keys)) # list

# 사전의 value 모두 받아오기
print(family.values())
print(type(family.values())) # dict_values



