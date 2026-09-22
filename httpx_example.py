import httpx

response_get = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response_get.status_code)
print(response_get.json())


data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response_post = httpx.post("https://jsonplaceholder.typicode.com/todos")

print(response_post.status_code)
print(response_post.json())


headers = {"Authorization": "Bearer my_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.status_code)
print(response.json())

params = {"userId": 1}

response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.request.url)
print(response.status_code)
print(response.json())

files = {'file': open('test_file.txt', 'rb')}
response = httpx.post('http://httpbin.org/post', files=files)

print(response.status_code)
print(response.json())

with httpx.Client(
        base_url='https://jsonplaceholder.typicode.com',
        headers={"Authorization": "Bearer my_token"}
) as client:
    response_1 = client.get("/todos/1")
    response_2 = client.get("/todos/2")

    client.close()

print(response_1.json())
print(response_1.request.headers)
print(response_2.json())


try:
    response = httpx.get('https://jsonplaceholder.typicode.com/incorrect_url')
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print("Ошибка:", {e})


try:
    response = httpx.get('https://httpbin.org/deley/5', timeout=2)
except httpx.ReadTimeout as e:
    print("Запрос превысил лимит по времени:", {e})

