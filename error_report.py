import json

with open('/Users/gulden/Downloads/python_odevleri (1)/inputs/odev2_logs.json') as file:
    data = json.load(file)

level_counts = {}
error_by_service = {}
highest_error_messages = 0
top_error_service = ""
service_error_message = {}
added = {}
error_alerts = []

for item in data:
    ts = item["ts"]
    level = item["level"]
    service = item["service"]
    msg = item["msg"]
    code = item["code"]
    level_counts[level] = level_counts.get(level, 0) + 1

    if level == "ERROR":
        error_by_service[service] = error_by_service.get(service, 0) + 1

for key, value in error_by_service.items():
    if value > highest_error_messages:
        highest_error_messages = value
        top_error_service = {key: highest_error_messages}

for item in data:
    ts = item["ts"]
    level = item["level"]
    service = item["service"]
    msg = item["msg"]
    code = item["code"]

    if level == "ERROR":
        if service not in service_error_message:
            added[service] = []

    if service not in service_error_message:
        service_error_message[service] = [msg]
    else:
        if msg not in service_error_message[service]:#unique kullanılmıştır.

            service_error_message[service].append(msg)

for key, value in error_by_service.items():
    if value >= 2:
        error_alerts.append({key: value})

print(level_counts)
print(error_by_service)
print(f"The service that generates the most error messages {top_error_service}")
print(service_error_message)
print(error_alerts)