# 사용할 Python환경
FROM python:3.14.2

# 컨테이너 내부의 작업 폴더를 /app으로 정합니다.
WORKDIR /app

# 의존성 목록 파일을 먼저 복사합니다.
COPY requirements.txt .

# 필요한 패키지들을 컨테이너에 설치합니다.
RUN pip install -r requirements.txt

# 나머지 소스 코드들을 전부 복사합니다.
COPY . .

# 서버를 실행합니다.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

