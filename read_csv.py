import csv
with open('./private_config.csv', 'r') as csv_file:
        secrets = csv.reader(csv_file, delimiter=",")
        for row in secrets:
            AWS_ACCESS_KEY_ID = row[0]
            AWS_SECRET_ACCESS_KEY = row[1]
            AWS_STORAGE_BUCKET_NAME = row[2]

print(AWS_ACCESS_KEY_ID)
