@echo off
chcp 65001 > nul
echo 모든 프로젝트의 빌드 데이터를 삭제 합니다.
 --rmi all 옵션은 compose 파일에 정의된 모든 이미지를 삭제합니다.
 -v 옵션은 볼륨(데이터)까지 삭제하고 싶을 때 추가하세요.
docker-compose down --rmi all
echo.
echo 삭제 완료되었습니다.
pause