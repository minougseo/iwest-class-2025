import os
from dotenv import load_dotenv
from tasks import create_email_body

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", default=None) or None

email_body = create_email_body(
    받는사람="서민욱 대리",     # keyword parameters
    용건="8월 업무보고",
    핵심내용="우리 휴가 언제 가냐",
    api_key=OPENAI_API_KEY
)
print(email_body)