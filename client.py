from util import SimpleClient

client = SimpleClient(port=8000)
print("available functions: ")
print(client.list_functions())

print("2 + 3 = " + str(client.add(2, 3)))
print("5 + 2 = " + str(client.add(5, 2)))
