import os
from dotenv import load_dotenv
from tasks import create_email_body, summerize_meeting

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", default=None) or None

# email_body = create_email_body(
#     받는사람="서민욱 대리",     # keyword parameters
#     용건="8월 업무보고",
#     핵심내용="우리 휴가 언제 가냐",
#     api_key=OPENAI_API_KEY
# )
# print(email_body)

# read + text mode
file = open("./회의록/20250828.txt", "rt", encoding="utf-8")
회의록 = file.read() # 파일의 전체 내용을 읽어서, 문자열로 반환
file.close()

요약내용 = summerize_meeting(회의록=회의록, api_key=OPENAI_API_KEY)
print("## 요약내용 ##")
print(요약내용)