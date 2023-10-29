from data import service_data

# 유료 구독 서비스 출력 함수
def print_service():
    for category in service_data:
        print(category)
        for service in service_data[category]:
            print(service, end="\t")
        print('\n')