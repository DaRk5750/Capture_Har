import json

# Load the HAR file
with open("captured_data.har", "r") as har_file:
    har_data = json.load(har_file)

# file = open('captur.txt','w')

# for log in har_data:
#     if 'responseStatus' in log:
#         file.write(str(log) + '\n')

total_count = 0
count_2xx = 0
count_4xx = 0
count_5xx = 0

for log in har_data:
    if 'responseStatus' in log:
        status_code = log['responseStatus']
        total_count += 1

        if 200 <= status_code < 300:
            count_2xx += 1
        elif 400 <= status_code < 500:
            count_4xx += 1
        elif 500 <= status_code < 600:
            count_5xx += 1

# Display the results
print("Total Status Code Count:", total_count)
print("Total 2XX Status Code Count:", count_2xx)
print("Total 4XX Status Code Count:", count_4xx)
print("Total 5XX Status Code Count:", count_5xx)


