# Proj2509
미니프로젝트1
<깃허브> 레포지토리: https://github.com/Seyun-lab/Proj2509.git
⚙️ 로컬 환경 설정
편집기: Git Bash (없으면 설치)
(* 경로에 한글X)
✅ 깃허브에서 프로젝트 내려받기 (Clone)
git clone https://github.com/Seyun-lab/Proj2509.git
✅ 본인 이름의 브랜치로 이동 
cd Proj2509
git checkout Seyun-lab  
🛠️ 코드 작업 & 커밋 & 푸시
✅ 작업한 코드 저장 (Commit)
✅ 원격 저장소에 푸시 (Push)


🔁 병합 요청 (Pull Request)
GitHub 웹사이트 접속 (https://github.com/Seyun-lab/Acorn_From0714.git)

 → Pull Request 클릭


base: main ← compare: dev-본인이름 선택


팀장이 확인 후 Merge



<아나콘다에 장고 환경설정>
아나콘다 활성화
설치 확인
python -m django --version

4. 현재 폴더에 바로 만들고 싶다면
5.
django-admin startproject mainapp 폴더명
python manage.py startapp myapp
6. 
manage.py 있는 경로에서 실행 
python manage.py migrate 
7. 서버 런
python manage.py runserver 192.168.0.15:8000
8. 원격 table 구조 얻기 : python manage.py inspectdb > aa.py
9.  DB 수정할때마다 python manage.py makemigrations (models.py와 관련있다)

<DB 서버 연결 방법>
CMD_CLI 들어가는 법
mariadb -h 127.0.0.1 -u root -p
show 테이블명;  
use 데이터베이스이름;
desc 테이블명;
끝낼때 꼭 quit; 

















