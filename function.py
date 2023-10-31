from data import *
import re

# 사용자 첫 방문 함수
def first_process():
    print("유료 구독제 통합 관리 시스템에 오신 것을 환영합니다!", end="\n\n")

    maximum = input("월 최대 금액을 설정하세요.\n")
    maximum = int(re.findall(r'\d+', maximum)[0])

    tutorial = input("먼저 내가 구독한 플랫폼을 등록하세요. (Y or N 입력)\n")

    if tutorial in ('Y', 'y'):
        first_add_service()
    
    print()

    return maximum

# 사용자 선택 함수
def select(maximum):
    print("무엇을 하시겠습니까?\n")
    print("1) 대표적인 유료 구독 플랫폼 확인하기")
    print("2) 내가 구독한 플랫폼 확인하기")
    print("3) 구독 플랫폼 등록, 해지하기")
    print("4) 시스템 종료하기\n")

    num = int(input("번호를 입력하세요 : "))
    print('\n')

    if num == 1:
        print_service()
    elif num == 2:
        my_service(maximum)
    elif num == 3:
        modify_service(maximum)
    elif num == 4:
        exit()
    else:
        print("잘못된 입력입니다. 다시 입력하세요.")

# 전체 유료 구독 서비스 출력 함수
def print_service():
    for category in service_data:
        print(category)
        for service in service_data[category]:
            print(service, end="\t")
        print('\n')

# 내가 유료 구독한 서비스 출력 함수
def my_service(maximum):
    print("다음은 현재 유료 구독한 플랫폼입니다.\n")
    for service in my_data:
        print(f"{service} : {my_data[service]}원")
    print(f"\n총 구독 플랫폼 수는 {len(my_data)}개입니다.")
    print(f"월별 총 지출 금액은 {sum(my_data.values())}원입니다.\n")

    if maximum < sum(my_data.values()):
        print(f"설정한 월별 최대 금액을 {sum(my_data.values()) - maximum}원 초과했습니다. 불필요한 구독을 해지하여 금액을 줄여야 합니다.\n")

# 유료 구독 서비스 첫 등록 함수
def first_add_service():
    i = 1
    for category in service_data:
        print(f"{i}) {category}", [service for service in service_data[category].keys()], sep='\n', end='\n\n')
        i += 1
        cnt = 0
        
        while True:
            if cnt == 0:
                name = input("다음 카테고리에서 유료 구독한 플랫폼을 하나만 입력하세요. (없으면 N 입력)\n")
            else:
                name = input("구독한 플랫폼이 더 있다면, 하나만 입력하세요. (없으면 N 입력)\n")
            if name in ('N', 'n'):
                break
            else:
                cost = input("해당 플랫폼에서 월별 지출되는 비용을 입력하세요.\n")
                cost = int(re.findall(r'\d+', cost)[0])
                my_data[name] = cost
                cnt += 1
        
        print('\n')
    
    print("초기 등록이 끝났습니다!\n")

# 구독 플랫폼 등록, 해지 함수
def modify_service(maximum):
    my_service(maximum)

    enr_can = input("구독 플랫폼 등록 or 해지 (등록, 해지)\n")
    if enr_can == "등록":
        name = input("새로 등록할 플랫폼을 입력하세요.\n")
        cost = input("월별 지출되는 비용을 입력하세요.\n")
        cost = int(re.findall(r'\d+', cost)[0])
        my_data[name] = cost

    elif enr_can == "해지":
        while True:
            name = input("해지할 플랫폼을 입력하세요.\n")
            try:
                del my_data[name]
                break
            except:
                print("다시 입력하세요")
                continue
    
    my_service(maximum)