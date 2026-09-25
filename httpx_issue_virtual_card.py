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

# print(open_debit_card_account_response_data)

issue_virtual_card_payload = {
  "userId": response_create_data['user']['id'],
  "accountId": open_debit_card_account_response_data['account']['id']
}

issue_virtual_card_response = httpx.post(
    'http://localhost:8003/api/v1/cards/issue-virtual-card',
    json=issue_virtual_card_payload
)

issue_virtual_card_response_data = issue_virtual_card_response.json()

print(issue_virtual_card_response_data)
print(issue_virtual_card_response.status_code)

