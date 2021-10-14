import json

inp = input() 
json_data = json.loads(inp)
ans, ans_name, mn = 0, '', 999999

for item in json_data["Subscriptions"]:
    price = int(item["price"])
    discount = int(item["discount"])
    ans = int(price * (100 - discount) / 100)
    if mn > ans:
        mn = ans
        ans_name = str(item["name"])

print('Name: ' + ans_name + '\nPrice: ' + str(mn))


