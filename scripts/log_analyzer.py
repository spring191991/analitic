def analyze_logs(logs):
    balance=0
    i=0
    for log in logs:
        if log["status"] == "COMPLETED":
            balance += log["data"]["balance"]
        if log["status"] == "FAILED":
            i += 1
    return {"sum": balance, "errors": i}
print(analyze_logs(api_logs))
