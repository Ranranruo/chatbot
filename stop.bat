@echo off
chcp 65001 > nul
echo 모든 프로젝트를 중지 합니다.
docker-compose down
echo.
echo 중지 완료 되었습니다.
pause