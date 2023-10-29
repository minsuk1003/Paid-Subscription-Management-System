from function import *

print("유료 구독제 통합 관리 시스템에 오신 것을 환영합니다!", end="\n\n")

print()
print("무엇을 하시겠습니까?")
print("1) 전체 유료 구독 플랫폼 확인하기")
print("2) 내가 구독한 플랫폼과 비용 확인하기")
print("3) 내가 구독한 플랫폼과 비용 추가하기")
print("4) 시스템 종료하기")

num = int(input("번호를 입력하세요 : "))

if num == 1:
    print_service()
elif num == 2:
    pass
elif num == 3:
    exit()