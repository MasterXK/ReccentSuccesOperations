import json


def get_info(json_path: str) -> list[dict]:
    try:
        with open(json_path, encoding="UTF-8") as json_file:
            json_content = json.load(json_file)

    except json.JSONDecodeError:
        return []

    except FileNotFoundError:
        return []

    if type(json_content) is list:
        return json_content

    return []


def get_transaction_sum(transaction: dict) -> float:
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])

    raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
