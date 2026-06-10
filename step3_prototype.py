
# 과목 등록, 등록된 과목 목록 보기

# 여러 과목 정보를 저장할 리스트
# 과목 하나는 딕셔너리로 저장하고, 여러 과목은 이 리스트 안에 저장한다.
subjects = []


# 과목을 새로 등록하는 함수
def add_subject():
    print("\n[과목 등록]")

    # 사용자에게 과목 정보를 입력받는다.
    name = input("과목명을 입력하세요: ")
    exam_date = input("시험 날짜를 입력하세요 (예: 2026-06-20): ")
    target_time = float(input("목표 공부 시간을 입력하세요: "))
    done_time = float(input("현재까지 공부한 시간을 입력하세요: "))

    # 입력받은 과목 정보를 딕셔너리 형태로 저장한다.
    subject = {
        "name": name,              # 과목명
        "exam_date": exam_date,    # 시험 날짜
        "target": target_time,     # 목표 공부 시간
        "done": done_time          # 현재까지 공부한 시간
    }

    # 새 과목 딕셔너리를 전체 과목 리스트에 추가한다.
    subjects.append(subject)

    print(f"{name} 과목이 등록되었습니다.")


# 등록된 과목 목록을 보여주는 함수
def show_subjects():
    # 등록된 과목이 없을 경우 안내 문구를 출력하고 함수 종료
    if len(subjects) == 0:
        print("아직 등록된 과목이 없습니다.")
        return

    print("\n===== 등록된 과목 목록 =====")

    # subjects 리스트에 저장된 과목들을 하나씩 출력한다.
    # enumerate를 사용하면 번호와 과목 정보를 함께 가져올 수 있다.
    for i, subject in enumerate(subjects):
        print(f"{i + 1}. {subject['name']}")
        print(f"   시험 날짜: {subject['exam_date']}")
        print(f"   목표 공부 시간: {subject['target']}시간")
        print(f"   현재 공부 시간: {subject['done']}시간")


# 프로그램이 계속 실행되도록 반복문을 사용한다.
while True:
    print("\n===== 시험 공부 관리 프로그램 =====")
    print("1. 과목 등록")
    print("2. 등록된 과목 목록 보기")
    print("3. 종료")

    # 사용자에게 메뉴 번호를 입력받는다.
    choice = input("메뉴를 선택하세요: ")

    # 1번을 선택하면 과목 등록 함수 실행
    if choice == "1":
        add_subject()

    # 2번을 선택하면 등록된 과목 목록 출력
    elif choice == "2":
        show_subjects()

    # 3번을 선택하면 반복문을 종료하고 프로그램 종료
    elif choice == "3":
        print("프로그램을 종료합니다.")
        break

    # 1, 2, 3이 아닌 값을 입력한 경우 안내 문구 출력
    else:
        print("1, 2, 3 중에서 선택하세요.")