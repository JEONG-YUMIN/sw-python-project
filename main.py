import json
from datetime import date, datetime


# 데이터를 저장할 파일 이름
FILE_NAME = "study_data.json"


# 저장된 데이터 불러오기
def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        # 저장 파일이 없으면 빈 과목 목록으로 시작
        return {"subjects": []}


# 데이터 저장하기
def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# 날짜 입력받기
def input_date(message):
    while True:
        text = input(message)

        try:
            input_day = datetime.strptime(text, "%Y-%m-%d").date()
            return input_day
        except ValueError:
            print("날짜 형식이 잘못되었습니다. 예: 2026-06-20")


# 0 이상의 숫자 입력받기
def input_number(message):
    while True:
        try:
            number = float(input(message))

            if number < 0:
                print("0 이상의 숫자를 입력하세요.")
            else:
                return number

        except ValueError:
            print("숫자만 입력하세요.")


# 과목 등록하기
def add_subject(data):
    print("\n[과목 등록]")

    name = input("과목명을 입력하세요: ")
    exam_date = input_date("시험 날짜를 입력하세요 (예: 2026-06-20): ")
    target_time = input_number("목표 공부 시간을 입력하세요: ")
    done_time = input_number("현재까지 공부한 시간을 입력하세요: ")

    subject = {
        "name": name,
        "exam_date": str(exam_date),
        "target": target_time,
        "done": done_time
    }

    data["subjects"].append(subject)
    save_data(data) 

    print(f"{name} 과목이 등록되었습니다.")


# 오늘 공부한 시간 추가하기
def add_study_time(data):
    subjects = data["subjects"]

    if len(subjects) == 0:
        print("아직 등록된 과목이 없습니다.")
        return

    print("\n[등록된 과목]")
    for i, subject in enumerate(subjects):
        print(f"{i + 1}. {subject['name']}")

    choice = input("공부 시간을 추가할 과목 번호를 선택하세요: ")

    try:
        index = int(choice) - 1

        if index < 0 or index >= len(subjects):
            print("잘못된 번호입니다.")
            return

        add_time = input_number("오늘 추가로 공부한 시간을 입력하세요: ")

        # 기존 공부 시간에 오늘 공부한 시간을 더함
        subjects[index]["done"] += add_time

        save_data(data)

        print(f"{subjects[index]['name']} 과목에 {add_time}시간이 추가되었습니다.")

    except ValueError:
        print("번호는 숫자로 입력하세요.")


# 공부 현황 보기
def show_status(data):
    subjects = data["subjects"]

    if len(subjects) == 0:
        print("아직 등록된 과목이 없습니다.")
        return

    today = date.today()

    print("\n===== 공부 현황 =====")

    recommended_subject = ""
    max_priority = -1

    for subject in subjects:
        name = subject["name"]
        exam_date = datetime.strptime(subject["exam_date"], "%Y-%m-%d").date()
        target = subject["target"]
        done = subject["done"]

        # 시험 날짜에서 오늘 날짜를 빼서 D-day 계산
        dday = (exam_date - today).days

        # 목표 공부 시간에서 현재 공부 시간을 빼서 부족 시간 계산
        shortage = target - done
        if shortage < 0:
            shortage = 0

        # 진행률 계산
        if target == 0:
            progress = 100
        else:
            progress = (done / target) * 100

        if progress > 100:
            progress = 100

        # 진행률을 막대 형태로 표현
        bar_count = int(progress // 10)
        bar = "█" * bar_count + "-" * (10 - bar_count)

        print(f"\n[{name}]")

        if dday > 0:
            print(f"시험까지 D-{dday}")
        elif dday == 0:
            print("시험이 오늘입니다.")
        else:
            print(f"시험일이 {-dday}일 지났습니다.")

        print(f"진행률: [{bar}] {progress:.1f}%")
        print(f"목표: {target}시간 / 현재: {done}시간 / 부족: {shortage}시간")

        # 하루 평균 필요한 공부 시간 계산
        if dday > 0:
            daily_needed = shortage / dday
            print(f"시험 전까지 하루 평균 {daily_needed:.1f}시간 더 공부하면 됩니다.")
        else:
            daily_needed = shortage

        # 추천 기준: 부족 시간과 남은 날짜를 함께 고려
        if shortage > 0:
            if dday > 0:
                priority = shortage / dday
            else:
                priority = shortage + 100

            if priority > max_priority:
                max_priority = priority
                recommended_subject = name

    print("\n===== 추천 =====")

    if recommended_subject == "":
        print("모든 과목이 목표 공부 시간을 달성했습니다.")
    else:
        print(f"현재 가장 우선적으로 공부할 과목은 {recommended_subject}입니다.")
        print("부족한 시간과 시험까지 남은 날짜를 함께 고려해서 추천했습니다.")


# 등록된 과목 목록 보기
def show_subjects(data):
    subjects = data["subjects"]

    if len(subjects) == 0:
        print("아직 등록된 과목이 없습니다.")
        return

    print("\n===== 등록된 과목 목록 =====")

    for i, subject in enumerate(subjects):
        print(f"{i + 1}. {subject['name']}")
        print(f"   시험 날짜: {subject['exam_date']}")
        print(f"   목표 공부 시간: {subject['target']}시간")
        print(f"   현재 공부 시간: {subject['done']}시간")


# 메인 함수
def main():
    data = load_data()

    while True:
        print("\n===== 시험 D-day와 공부 시간 관리 프로그램 =====")
        print("1. 과목 등록")
        print("2. 오늘 공부 시간 추가")
        print("3. 공부 현황 보기")
        print("4. 등록된 과목 목록 보기")
        print("5. 종료")

        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            add_subject(data)

        elif choice == "2":
            add_study_time(data)

        elif choice == "3":
            show_status(data)

        elif choice == "4":
            show_subjects(data)

        elif choice == "5":
            print("프로그램을 종료합니다.")
            break

        else:
            print("1, 2, 3, 4, 5 중에서 선택하세요.")


main()