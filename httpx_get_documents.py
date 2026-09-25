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

open_credit_card_account_payload = {
    "userId": response_create_data['user']['id']
}

open_credit_card_account_response = httpx.post(
    'http://localhost:8003/api/v1/accounts/open-credit-card-account',
    json=open_credit_card_account_payload
)

open_credit_card_account_response_data = open_credit_card_account_response.json()

# print(open_credit_card_account_response)

get_tariff_document_response = httpx.get(
    f"http://localhost:8003/api/v1/documents/tariff-document/"
    f"{open_credit_card_account_response_data['account']['id']}"
)

get_tariff_document_response_data = get_tariff_document_response.json()

print('tariff document response:', get_tariff_document_response_data)
print('tariff document status code:', get_tariff_document_response.status_code)

get_contract_document_response = httpx.get(
    f"http://localhost:8003/api/v1/documents/contract-document/"
    f"{open_credit_card_account_response_data['account']['id']}"
)

get_contract_document_response_data = get_contract_document_response.json()

print('contract document response:', get_contract_document_response_data)
print('contract document status code:', get_contract_document_response.status_code)