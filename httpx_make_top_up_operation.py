import time
import httpx

# Шаг 1: создаём пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Шаг 2: открываем дебитовый счёт
open_debit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}
open_debit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-debit-card-account",
    json=open_debit_card_account_payload
)
open_debit_card_account_response_data = open_debit_card_account_response.json()

# Шаг 3: пополняем дебитовый счет
make_top_up_operation_payload = {
  "status": "COMPLETED",
  "amount": 1500,
  "cardId": open_debit_card_account_response_data["account"]["cards"][0]["id"],
  "accountId": open_debit_card_account_response_data["account"]["id"]
}
make_top_up_operation_response = httpx.post(
    "http://localhost:8003/api/v1/operations/make-top-up-operation",
    json=make_top_up_operation_payload
)
make_top_up_operation_response_data = make_top_up_operation_response.json()

# Вывод результатов в консоль
print("Make top up operation status code:", make_top_up_operation_response.status_code)
print("Make top up operation response:", make_top_up_operation_response_data)
