
import os
import requests
from openai import OpenAI
from openai.types.shared.chat_model import ChatModel

def make_response(
        user_content: str,
        system_content: str | None = None,
        model: str | ChatModel = "gpt-4o-mini",
        temperature: float = 0.25,
        api_key: str | None = None,
) -> str:
    messages =[]
    if system_content: # 빈 문자열도 아니고, None 도 아닐 때
        messages.append({"role": "system", "content": system_content})
    messages.append({"role": "user", "content": user_content})
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content

def download_file(
        file_url: str,
        filepath: str | None = None, # default parameter, 옵션 인자는 디폴트 값을 넣어줘야함
) -> None:
    res = requests.get(file_url)
    print("res ok :", res.ok)

    if filepath is None:
        filepath = os.path.basename(file_url) # / 제일끝 추출

    file_content = res.content

    dir_path = os.path.dirname(filepath)
    os.makedirs(dir_path, exist_ok=True)  # 파일을 저장할 경로 지정

    # 주의 : 같은 경로의 경로일 경우, 덮어쓰기가 됩니다.
    with open(filepath, "wb") as f:
        f.write(file_content)
        print("saved", filepath)