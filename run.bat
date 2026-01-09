@echo off
chcp 65001 > nul
echo 모든 프로젝트를 실행합니다.
docker-compose up -d
echo.
echo 완료되었습니다.
pause