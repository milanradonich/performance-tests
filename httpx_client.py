"""
import httpx

import time

create_user_payload = {

        "email": f"user_{time.time()}@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string",
        "phoneNumber": "string"

}

response_create = httpx.post('http://localhost:8003/api/v1/users', json=create_user_payload)
response_create_data = response_create.json()
"""
import os

import httpx

import time

client = httpx.Client(
    base_url='http://localhost:8003',
    timeout=60,
    headers={"Authorization": "Bearer..."}
)

payload = {

        "email": f"user_{time.time()}@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string",
        "phoneNumber": "string"

}

response = client.post('/api/v1/users', json=payload)

print("response:", response.text)
print("headers:", response.request.headers)

