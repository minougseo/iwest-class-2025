
import os
import requests

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