@echo off
chcp 65001 > nul
echo 현재 빌드된 이미지 목록을 조회합니다.
docker ps
echo.
echo 완료되었습니다.
pause