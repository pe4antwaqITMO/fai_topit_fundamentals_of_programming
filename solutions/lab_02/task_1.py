import copy


a = 10
b = a
print(a,b)
print(id(a),id(b))
a += 1
print(a,b)
print(id(a),id(b))


first = [10, 20]
second = first
print(first,second)
print(id(first),id(second))
second.append(30)
print(first,second)
print(id(first),id(second))

second = list(first)

print(first,second)
print(id(first),id(second))

print(first == second, first is second)
second.append(40)
print(first,second)


config1 = {"name": "Prod", "users": ["Admin"], "params": [80, True]}
config2 = config1
config2["params"][0] = 443
print(config1['params'], config2['params'])

config3 = copy.deepcopy(config1)
config3["params"][0] = 8080
print(config1['params'],config3['params'])

assert config1['params'] is not config3['params'], 'error'
