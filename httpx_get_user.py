import time

import httpx

create_user_payload = {

        "email": f"user_{time.time()}@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string",
        "phoneNumber": "string"

}

response_create = httpx.post('http://localhost:8003/api/v1/users', json=create_user_payload)
response_create_data = response_create.json()

print("Create user response:", response_create_data)
print("Status code", response_create.status_code)

response_get = httpx.get(f'http://localhost:8003/api/v1/users/{response_create_data['user']['id']}')
response_get_data = response_get.json()
print("Get user response:", response_get_data)
print("Status code", response_get.status_code)


