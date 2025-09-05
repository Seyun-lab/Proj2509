노션: 
https://www.notion.so/gyeoul-deep-room/Team-1-25e27bc8ba1480c9ac04e6bc1ac39528?source=copy_link

````markdown
# Proj2509  
미니프로젝트 1  

---

## 📂 깃허브 레포지토리
- [Proj2509 Repository](https://github.com/Seyun-lab/Proj2509.git)

---

## ⚙️ 로컬 환경 설정
- 편집기: **Git Bash** (없으면 설치)  
- 주의: **경로에 한글 ❌**

---

## 📥 깃허브에서 프로젝트 내려받기 (Clone)
```bash
git clone https://github.com/Seyun-lab/Proj2509.git
````

---

## 🌿 브랜치 이동

```bash
cd Proj2509
git checkout Seyun-lab
```

---

## 🛠️ 코드 작업 & 커밋 & 푸시

1. 작업한 코드 저장 (**Commit**)
2. 원격 저장소에 푸시 (**Push**)

---

## 🔁 병합 요청 (Pull Request)

1. GitHub 웹사이트 접속
2. **Pull Request** 클릭
3. `base: main ← compare: dev-본인이름` 선택
4. 팀장이 확인 후 **Merge**

---

## 🐍 아나콘다 장고 환경 설정

1. 아나콘다 활성화
2. 설치 확인

   ```bash
   python -m django --version
   ```
3. 현재 폴더에 프로젝트 생성

   ```bash
   django-admin startproject mainapp 폴더명
   ```
4. 앱 생성

   ```bash
   python manage.py startapp myapp
   ```
5. DB 초기화 (manage.py 경로에서 실행)

   ```bash
   python manage.py migrate
   ```
6. 서버 실행

   ```bash
   python manage.py runserver 192.168.0.15:8000
   ```
7. 원격 테이블 구조 가져오기

   ```bash
   python manage.py inspectdb > aa.py
   ```
8. DB 수정 시 (models.py 관련)

   ```bash
   python manage.py makemigrations
   ```

---

## 🗄️ DB 서버 연결 방법

1. CMD\_CLI 접속

   ```bash
   mariadb -h 127.0.0.1 -u root -p
   ```
2. 주요 명령어

   ```sql
   show 테이블명;
   use 데이터베이스이름;
   desc 테이블명;
   ```
3. 종료

   ```sql
   quit;
   ```

