---

---
# BackEnd
---
## 0. INDEX
---
1. 기술 스택
2. 설치 및 실행 방법
3. 구성 요소 설명
4. 환경 변수 설정
5. 기타 참고 사항

## 1. 기술 스택
---
이 Django 프로젝트는 다음과 같은 기술 스택과 라이브러리를 사용합니다:

#### **1) 프레임워크 및 언어**

- Python 3
- Django 4.2.16 (웹 프레임워크)
- Django REST Framework (API 설계 및 관리)
- SQLite3 (기본 데이터베이스)

#### **2)인증 및 권한 관리**

- `dj-rest-auth`: RESTful 인증 및 권한 처리
- `django-allauth`: 소셜 인증 및 사용자 관리
- `rest_framework.authtoken`: 토큰 기반 인증

#### **3) 환경 변수 관리**

- `python-decouple`: `.env` 파일을 통한 환경 변수 관리

#### **4) CORS 설정**

- `django-cors-headers`: 프론트엔드와의 CORS 정책 처리

#### **5) 이미지 및 파일 관리**

- `Pillow`: 이미지 처리 및 업로드 지원

#### **6) 기타 사용한 라이브러리**

- `openai`: OpenAI API 연동 (대체 결말 생성 기능)
- `django-environ`: 환경 설정 파일 관리

## 2. 설치 및 실행 방법
---
이 프로젝트를 로컬 환경에서 실행하려면 다음 단계를 따르세요:

#### **1. 프로젝트 클론**

GitHub 또는 프로젝트 저장소에서 코드를 클론합니다:

```bash
git clone <your-repository-url>
cd <project-directory>
```

#### **2. 가상환경 설정**

Python 가상환경을 생성하고 활성화합니다:

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
source venv\Scripts\activate     # Windows
```

#### **3. 의존성 설치**

`requirements.txt` 파일을 통해 필요한 패키지를 설치합니다:

```bash
pip install -r requirements.txt
```

#### **4. 환경 변수 설정**

`.env` 파일을 생성하고 다음과 같은 내용을 추가하세요:

```.env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

#### **5. 데이터베이스 설정**

데이터베이스를 마이그레이션합니다:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### **6. 로컬 서버 실행**

개발 서버를 실행합니다:

```bash
python manage.py runserver
```

서버가 실행되면 http://127.0.0.1:8000에서 프로젝트를 확인할 수 있습니다.

## 3. 구성 요소 설명
---

## 4. 환경 변수 설정
---

## 5. 기타 참고 사항