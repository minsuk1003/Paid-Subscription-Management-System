from data import service_data

for category in service_data:
    print(category)
    for service in service_data[category]:
        print(service, end="\t")
    print('\n')

    