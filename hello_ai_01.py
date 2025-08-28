
# os, dotenv, openai 라이브러리 임포트
import os
from dotenv import load_dotenv
from openai import OpenAI

# .env 파일에서 환경변수를 불러옵니다.
load_dotenv()

# 환경변수에서 OPENAI_API_KEY 값을 가져옵니다. 없으면 None을 반환합니다.
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", default=None) or None

# 명시적으로 api key를 지정하지 않으면,
# OpenAI 내부에서 알아서 OPENAI_API_KEY 환경변수 값을 찾습니다.
client = OpenAI(api_key=OPENAI_API_KEY)

def create_chat_completion(client: OpenAI) -> str:
    """
    OpenAI 클라이언트를 사용하여 챗봇 응답을 생성합니다.

    Args:
        client (OpenAI): OpenAI API 클라이언트 객체

    Returns:
        str: 챗봇의 응답 메시지
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            # 역할(role): system, user, assistant 등 지정
            {"role": "system", "content": "당신은 서부발전의 서민욱 대리입니다."},
            {"role": "user", "content": "자기 소개를 해주세요. 이름 3행시도 해주세요."},
        ],
    )
    print("response.usage : ", response.usage)  # 토큰 사용량 출력
    return response.choices[0].message.content  # 챗봇 응답 반환

# 챗봇 응답을 출력합니다.
print(create_chat_completion(client))

