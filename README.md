# Prompt Manager

Python & Git 기초 과제

AI 프롬프트를 등록하고 관리하는 콘솔 프로그램입니다.

## 개발 환경

- Python 3.10 이상
- Git
- VS Code
## 작성자

- 이름: 오주연
- GitHub: https://github.com/jjjoy1114/A1_1_prompt_manager

# Prompt Manager (나만의 프롬프트 관리 프로그램)

Python & Git 기초 과제 - 터미널에서 메뉴 번호를 입력해 AI 프롬프트를 저장·검색·관리하는 콘솔 프로그램입니다. 외부 라이브러리 없이 Python 기본 문법만 사용했습니다.

## 실행 방법

터미널에서 `python prompt_manager.py` 를 실행합니다. (Python 3.10 이상 필요)

## 기능 목록

1. 프롬프트 추가 (제목/내용/카테고리, 빈 값·중복 제목 방지)
2. 프롬프트 목록 보기 (제목/카테고리/즐겨찾기 표시)
3. 카테고리별 조회
4. 프롬프트 검색 (제목·내용 키워드)
5. 프롬프트 상세 보기
6. 즐겨찾기 관리 (추가/해제 토글)
7. 즐겨찾기 목록
8. Markdown 내보내기 (보너스1)
0. 종료

프롬프트는 `prompts.json`에 저장되어 프로그램을 종료한 뒤에도 유지됩니다. (보너스1)

## 등록된 프롬프트 카테고리

텍스트 생성, 이미지 생성, 영상 생성, 페르소나, 자동화, 기타

## 작성자

- 이름: 오주연
- GitHub: https://github.com/jjjoy1114/A1_1_prompt_manager

## 파일 구성

- prompt_manager.py : 실행 코드
- prompts.json : 프롬프트 저장 데이터
- README.md : 설명 문서
- .gitignore : Git 추적 제외 설정
