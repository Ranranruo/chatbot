@echo off

REM ===================================
REM Client 서버 실행
REM ===================================
cd client-server-latest
start cmd /k "npm i && npm run dev -- --host 0.0.0.0"

REM ===================================
REM Python 서버 실행
REM ===================================
cd ../ai-server-latest
call venv/Scripts/activate
start uvicorn app.chat.main:app --host 0.0.0.0 --port 8000

REM ===================================
REM Spring Boot 서버 실행
REM ===================================
cd ../
start java -jar backend-server-latest.jar

REM ===================================
REM MariaDB Docker 컨테이너 실행
REM ===================================
REM 컨테이너 이름: my-mariadb
REM 호스트 포트: 3300, 데이터 볼륨: ..\database\mariadb_data
cd database
docker rm -f my-mariadb
docker build -t my-mariadb .
docker run --name my-mariadb -p 3300:3306 -v maria-data:/var/lib/mysql my-mariadb



pause