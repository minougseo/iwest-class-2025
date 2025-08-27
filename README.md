# iwest-class-2025

## 프로젝트 개요

이 프로젝트는 OpenAI API를 활용하여 간단한 챗봇 및 대화형 AI 예제를 구현합니다. Python 환경에서 API 키 관리, 대화 메시지 관리, 반복 대화 기능 등을 실습할 수 있습니다.

## 폴더 및 파일 설명

- `hello_ai_01.py` : OpenAI API를 사용해 단일 질문-응답 챗봇 예제
- `hello_ai_02.py` : 사용자와 반복적으로 대화하는 챗봇 예제 (대화 히스토리 유지)
- `utils.py` : (추가 유틸리티 함수 작성 시 사용)
- `requirements.txt` : 필요한 Python 패키지 목록

## 가상환경 생성 및 활성화 가이드 (macOS 기준)

```bash
# 가상환경 생성 (예: .venv 폴더)
python3 -m venv .venv

# 가상환경 활성화
source .venv/bin/activate

# 가상환경 비활성화
deactivate
```

## 설치 및 실행 방법

1. 가상환경을 활성화합니다.
2. 필요한 패키지를 설치합니다:
   ```bash
   pip install -r requirements.txt
   ```
3. `.env` 파일을 생성하고 아래와 같이 OpenAI API 키를 입력합니다:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
4. 예제 파일 실행:
   ```bash
   python hello_ai_01.py
   python hello_ai_02.py
   ```

## 사용법

- `hello_ai_01.py` : 실행하면 OpenAI 챗봇의 응답이 출력됩니다.
- `hello_ai_02.py` : 실행 후 "Human:" 프롬프트에 질문을 입력하면 AI가 답변합니다. 종료하려면 빈 입력 또는 "quit" 입력.

## 기타 참고사항

- OpenAI API 키는 https://platform.openai.com/ 에서 발급받을 수 있습니다.
- macOS 기준 명령어입니다. Windows는 `Scripts\activate`를 사용하세요.

## 라이선스 및 문의

- 라이선스: MIT
- 문의: minougseo@gmail.com
