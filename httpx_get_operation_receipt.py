import json

import httpx

import time

create_user_payload = {

    "email": f"user_{time.time()}@example.com",
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

    open_credit_card_account_payload = {
        "userId": user_id
    }

    open_credit_card_account_response = client.post(
        "/accounts/open-credit-card-account",
        json=open_credit_card_account_payload
    )

    open_credit_card_account_data = open_credit_card_account_response.json()

    make_purchase_operation_payload = {
        "status": "IN_PROGRESS",
        "amount": 77.99,
        "category": "taxi",
        "cardId": open_credit_card_account_data['account']['cards'][0]['id'],
        "accountId": open_credit_card_account_data['account']['id']
    }

    make_purchase_operation_response = client.post(
        '/operations/make-purchase-operation',
        json=make_purchase_operation_payload
    )

    make_purchase_operation_data = make_purchase_operation_response.json()

    get_operation_receipt_response = client.get(
        f'/operations/operation-receipt/{make_purchase_operation_data['operation']['id']}'
    )

    get_operation_receipt_response_data = get_operation_receipt_response.json()

print("Чек по операции:", json.dumps(get_operation_receipt_response_data, indent=2))
print("Status code:", get_operation_receipt_response.status_code)
