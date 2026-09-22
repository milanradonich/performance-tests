import time

import httpx

create_user_payload = {

        "email": f"user_{time.time()}@fake.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string",
        "phoneNumber": "string"

}
with httpx.Client(base_url='http://localhost:8003/api/v1') as client:
    create_user_response = client.post(
        "/users",
        json=create_user_payload
    )

    response_create_data = create_user_response.json()
    user_id = response_create_data["user"]["id"]

    open_deposit_payload = {
        "userId": user_id,
    }

    open_deposit_response = client.post(
        "/accounts/open-deposit-account",
        json=open_deposit_payload
    )

    open_deposit_data = open_deposit_response.json()

print("Status code:", open_deposit_response.status_code)
print("Deposit account:", open_deposit_data)
