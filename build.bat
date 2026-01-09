@echo off
chcp 65001 > nul
echo 모든 프로젝트를 빌드합니다.
docker-compose build
echo.
echo 완료되었습니다.
pause