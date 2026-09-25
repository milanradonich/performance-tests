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

# print("Create user response:", response_create_data)
# print("Status code", response_create.status_code)

open_debit_card_account_payload = {
    "userId": response_create_data['user']['id']
}

open_debit_card_account_response = httpx.post(
    'http://localhost:8003/api/v1/accounts/open-debit-card-account',
    json=open_debit_card_account_payload
)

open_debit_card_account_response_data = open_debit_card_account_response.json()

make_top_up_operation_payload = {
    "status": "COMPLETED",
    "amount": 1555,
    "cardId": open_debit_card_account_response_data['account']['cards'][0]['id'],
    "accountId": open_debit_card_account_response_data['account']['id']
}

make_top_up_operation_response = httpx.post(
    'http://localhost:8003/api/v1/operations/make-top-up-operation',
    json=make_top_up_operation_payload
)

make_top_up_operation_data = make_top_up_operation_response.json()

print(make_top_up_operation_data)
print(make_top_up_operation_response.status_code)