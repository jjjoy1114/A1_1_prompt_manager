"""
나만의 프롬프트 관리 프로그램 (Prompt Manager)
- 콘솔 기반 프롬프트 저장/검색/관리 프로그램
- 외부 라이브러리 없이 Python 기본 문법만 사용
- 보너스1: JSON 저장·불러오기 / 카테고리별 Markdown 내보내기
"""

import json
from pathlib import Path

DATA_FILE = Path("prompts.json")
EXPORT_DIR = Path("exports")

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

DEFAULT_PROMPTS = [
    {
        "title": "MagSafe 거치대 제품컷 - 매트블랙 라이프스타일",
        "content": "A sleek matte black metallic MagSafe phone mount, set up as a minimal stand on a clean light-wood cafe table. An iPhone is magnetically attached to it. A cup of iced Americano and an aesthetic journal in the softly blurred background. Warm sunlight filtering through a window, bright and cozy vibe, lifestyle tech accessory photography, 8k, photorealistic --ar 9:16",
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "MagSafe 거치대 제품컷 - 스타라이트 크림 카페",
        "content": "A sleek, minimalist MagSafe smartphone mount in a soft starlight cream color, set up as a desk stand on a white marble cafe table. An iPhone is magnetically attached. Next to it is a beautifully poured latte and an open aesthetic journal. Soft natural sunlight filtering through a large window, cozy and aesthetic cafe background, photorealistic, 8k, high-end product photography.",
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "MagSafe 거치대 제품컷 - 카라비너 고리 키링 연출",
        "content": "[연출 지시] 첨부 이미지의 고리(카라비너) 부분을 이용해 가방 고리에 키링처럼 매단 모습. 제품 원형 변경 절대 금지, 포인트 색상 등 색상 변경 가능. A sleek matte black metallic MagSafe phone mount clipped to a bag, lifestyle tech accessory photography, 8k, photorealistic --ar 9:16",
        "category": "이미지 생성",
        "favorite": False,
    },
]

prompts = []


def load_prompts():
    """prompts.json이 있으면 읽고, 없으면 기본 데이터로 새로 만든다."""
    global prompts
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            prompts = json.load(f)
    else:
        prompts = [dict(p) for p in DEFAULT_PROMPTS]
        save_prompts()


def save_prompts():
    """현재 prompts 목록을 JSON 파일에 저장한다."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)


def input_required(message):
    """빈 값이면 다시 입력받는다."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("입력값이 비어있습니다. 다시 입력해주세요.")


def select_category():
    """카테고리를 번호로 선택하거나 직접 입력한다."""
    print("\n카테고리 선택:")
    for i, name in enumerate(CATEGORIES, start=1):
        print(f"{i}) {name}")
    choice = input_required("선택: ")
    if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
        selected = CATEGORIES[int(choice) - 1]
        if selected == "기타":
            return input_required("카테고리를 직접 입력하세요: ")
        return selected
    return choice


def is_duplicate_title(title):
    """같은 제목이 이미 있는지 확인한다."""
    return any(p["title"].lower() == title.lower() for p in prompts)


def star(favorite):
    return " ⭐" if favorite else ""


def print_prompt_line(index, prompt):
    print(f"{index}. [{prompt['category']}] {prompt['title']}{star(prompt['favorite'])}")


def show_menu():
    print(f"\n=== 나만의 프롬프트 관리 (총 {len(prompts)}개) ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. Markdown 내보내기")
    print("0. 종료")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input_required("제목: ")
    if is_duplicate_title(title):
        print("이미 같은 제목의 프롬프트가 있습니다. 다른 제목을 사용해주세요.")
        return
    content = input_required("내용: ")
    category = select_category()
    prompts.append({"title": title, "content": content, "category": category, "favorite": False})
    save_prompts()
    print("\n프롬프트가 추가되었습니다!")


def show_prompt_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, start=1):
        print_prompt_line(i, p)
    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category():
    print("\n=== 카테고리별 조회 ===")
    category = select_category()
    matched = [p for p in prompts if p["category"] == category]
    if not matched:
        print(f"\n[{category}] 카테고리의 프롬프트가 없습니다.")
        return
    print(f"\n[{category}] 카테고리 프롬프트:")
    for i, p in enumerate(matched, start=1):
        print(f"{i}. {p['title']}{star(p['favorite'])}")
    print(f"\n총 {len(matched)}개의 프롬프트")


def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input_required("검색어: ").lower()
    matched = [p for p in prompts if keyword in p["title"].lower() or keyword in p["content"].lower()]
    if not matched:
        print("\n검색 결과가 없습니다.")
        return
    print("\n검색 결과:")
    for i, p in enumerate(matched, start=1):
        print_prompt_line(i, p)
    print(f"\n{len(matched)}개의 프롬프트를 찾았습니다.")


def get_index_by_number(message):
    """번호를 입력받아 유효하면 인덱스를, 아니면 None을 돌려준다."""
    value = input(message).strip()
    if not value.isdigit():
        print("숫자를 입력해주세요.")
        return None
    number = int(value)
    if 1 <= number <= len(prompts):
        return number - 1
    print("잘못된 번호입니다.")
    return None


def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    idx = get_index_by_number("번호 입력: ")
    if idx is None:
        return
    p = prompts[idx]
    line = "─" * 30
    print(line)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {'⭐' if p['favorite'] else '없음'}")
    print(line)
    print("내용:")
    print(p["content"])
    print(line)


def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    idx = get_index_by_number("프롬프트 번호 입력: ")
    if idx is None:
        return
    p = prompts[idx]
    p["favorite"] = not p["favorite"]
    save_prompts()
    if p["favorite"]:
        print(f"'{p['title']}' 프롬프트를 즐겨찾기에 추가했습니다!")
    else:
        print(f"'{p['title']}' 프롬프트를 즐겨찾기에서 해제했습니다!")


def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    favorites = [p for p in prompts if p["favorite"]]
    if not favorites:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return
    for i, p in enumerate(favorites, start=1):
        print_prompt_line(i, p)
    print(f"\n총 {len(favorites)}개의 즐겨찾기")


def export_markdown():
    print("\n=== Markdown 내보내기 ===")
    if not prompts:
        print("내보낼 프롬프트가 없습니다.")
        return
    EXPORT_DIR.mkdir(exist_ok=True)
    grouped = {}
    for p in prompts:
        grouped.setdefault(p["category"], []).append(p)
    for category, items in grouped.items():
        safe_name = category.replace("/", "_").replace(" ", "_")
        file_path = EXPORT_DIR / f"{safe_name}.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {category}\n\n")
            for p in items:
                mark = " ⭐" if p["favorite"] else ""
                f.write(f"## {p['title']}{mark}\n\n")
                f.write(f"{p['content']}\n\n")
    print(f"Markdown 파일을 {EXPORT_DIR}/ 폴더에 저장했습니다!")
    print(f"생성된 카테고리 파일 수: {len(grouped)}개")


def main():
    load_prompts()
    print("\n환영합니다! 나만의 프롬프트 관리 프로그램입니다.")
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_prompt_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "8":
            export_markdown()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 다시 입력해주세요.")


if __name__ == "__main__":
    main()
    