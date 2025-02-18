from zapv2 import ZAPv2

target = 'http://localhost:5000'  # Replace with your target URL
zap = ZAPv2(apikey='')  # Replace with API key if applicable

print(f"Accessing target: {target}")
zap.urlopen(target)

print("Starting Spider...")
scan_id = zap.spider.scan(target)
while int(zap.spider.status(scan_id)) < 100:
    print(f"Spider progress: {zap.spider.status(scan_id)}%")
print("Spider completed.")

print("Starting Active Scan...")
scan_id = zap.ascan.scan(target)
while int(zap.ascan.status(scan_id)) < 100:
    print(f"Active Scan progress: {zap.ascan.status(scan_id)}%")
print("Active Scan completed.")

print("Alerts:")
for alert in zap.core.alerts():
    print(alert)
