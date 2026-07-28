import json
def analyze_logs(logs):
    balance=0
    i=0
    for log in logs:
        if log["status"] == "COMPLETED":
            balance += log["data"]["balance"]
        if log["status"] == "FAILED":
            i += 1
    return {"sum": balance, "errors": i}

with open('scripts/api_responses.json', 'r', encoding='utf-8') as file:
    loaded_logs = json.load(file)

report = analyze_logs(loaded_logs)

print("--- Аналитический отчет по логам ---")
print(f"Успешно обработано на сумму: {report['sum']} руб.")
print(f"Обнаружено критических ошибок: {report['errors']}")
