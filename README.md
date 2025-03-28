# Django Project Setting Use Guide

<details> 
<summary>1. Django 소개</summary>

## 1. Django 란?

Django는 파이썬으로 작성된 무료 오픈 소스 웹 프레임워크로, 신속한 개발과 간편한 유지보수를 목표로 합니다. MTV(Model-Template-View) 아키텍쳐를 기반으로 하여 웹 애플리케이션을 쉽게 구축할 수 있는 언어

## 2. Django의 특징

- **빠른 개발** : 재사용 가능한 컴포넌트와 다양한 도구 제공.
- **배터리 포함**: 많은 기능(ORM, 인증, 관리 패널 등) 기본 제공.
- **보안**: SQL 인젝션, XSS, CSRF 등 보호 기능 내장.
- **확장성**: 다양한 플러그인과 패키지로 기능 확장 제공.
- **강력한 커뮤니티**: 활발한 커뮤니티와 풍부한 문서화.

## 3. Django 설치

### 3.1. Python 및 pip 설치

Django는 Python으로 작성되므로, Python과 pip 설치가 필수임

### Ubuntu (Linux)

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### macOS

```bash
brew install python
```

### Windows

1. [Python 다운로드 페이지](https://www.python.org/downloads/)에서 Python 설치 프로그램을 다운로드.
2. 설치 시 "Add Python to PATH" 옵션을 선택

### 3.2. 가상 환경 설정

가상 환경을 만들고 활성화

```bash
pip install virtualenv
virtualenv myenv
source myenv/bin/activate # Linux/Mac
# myenv\Scripts\activate # Windows
```

### 3.3. Django 설치

가상 환경이 활성화된 상태에서 Django를 설치합니다.

```bash
pip install django
```

## 4. Django 프로젝트 생성

새로운 Django 프로젝트를 생성합니다.

```bash
django-admin startproject myproject
cd myproject
```

## 5. 개발 서버 실행

개발 서버를 실행하여 프로젝트가 제대로 생성되었는지 확인

```bash
python manage.py runserve
```

웹 브라우저에 http://127.0.0.1:8000/에 접속하여 Django 환영 페이지를 확인

## 6. 애플리케이션 실행

Django 프로젝트 내에서 애플리케이션을 생성

```bash
python manage.py startup myapp
```

## 7. 데이터베이스 마이그레이션

Django 기본 데이터베이스를 설정하고 마이그레이션 실행

```bash
python manage.py migrate
```

## 8. 관리자 계정 생성

Django의 관리자 패널에 접근할 수 있도록 관리자 계정을 생성

```bash
python manage.py createsuperuser
```

## 9. 관리자 패널 실행

개발 서버를 다시 실행하고, http://127.0.0.1:8000/admin에 접속해 관리자 패널에 로그인

</details>

<details>
  <summary> 2. Django 공략 순서</summary>
 
 ### 1. **Django 설치**
  - Python 및 pip 설치 
  - 가상 환경 설정
  - Django 설치

### 2. **Django 프로젝트 생성**

- 새로운 Django 프로젝트 생성

### 3. **개발 서버 실행**

- 기본 개발 서버 실행

### 4. **애플리케이션 생성**

- Django 애플리케이션 생성

### 5. **모델 정의**

- 데이터베이스 모델 정의
- 마이그레이션 파일 생성 및 적용

### 6. **어드민 설정**

- 관리자 패널에 모델 등록
- 관리자 계정 생성

### 7. **뷰(View) 작성**

- 비즈니스 로직 및 데이터 처리

### 8. **템플릿 작성**

- HTML 템플릿 작성 및 렌더링

### 9. **URL 설정**

- URL 패턴 정의 및 연결

### 10. **정적 파일 및 미디어 파일 설정**

- CSS, JavaScript, 이미지 파일 관리

### 11. **테스트 작성**

- 유닛 테스트 및 통합 테스트 작성

### 12. **배포 준비**

- 설정 파일 조정
- 배포 환경 설정

### 13. **배포**

- 실제 서버에 배포

### 14. **모니터링 및 유지보수**

- 로그 관리 및 성능 모니터링
</details>

<details>
  <summary>3. Django Popular Library</summary>
  <br>
  
  1. **Django REST Framework (DRF)** 
    - RESTful API를 쉽게 구축할 수 있도록 도와주는 강력한 라이브러리, 인증, 권한 부여, 적절한 기능을 제공
  2. **Django AIIauth**
    - 사용자 인증 및 등록을 위한 라이브러리로, 소셜 로그인 기능을 지원, 다양한 인증 방식(이메일, 소셜 미디어 등)을 제공
  3. **Django Celery**
    - 비동기 작업 큐를 처리하기 위한 라이브러리로, 백그라운드 작업을 쉽게 관리
  4. **Django Crispy Forms**
    - Django 폼을 더욱 아릅답게 렌더링할 수 있도록 도와주는 라이브러리로, 다양한 CSS 프레임워크와 통합이 가능 
  5. **Django Debug Toolbar**
    - 개발 중 유용한 디버깅 정보를 제공하는 도구로, SQL 쿼리, 요청/응답 시간 등을 시각적으로 보여주는 라이브러리 
  6. **Django Compressor**
    - CSS 및 JavaScript 파일을 압축하고 최적화하여 웹 페이지 로딩 속도를 개선하는 데 도움을 주는 라이브러리 
  7. **Django Guardian**
    - 객체 수준의 권한 권리를 지원하는 라이브러리로, 사용자가 특정 객체에 대한 권한을 가질 수 있도록 설정할 수 있음
  8. **Django Storages**
    - 다양한 스토리지 백엔드(AWS S3, Google Cloud Storage)와 통합하여 파일 업로드 및 관리를 쉽게 할 수 있도록 해주는 라이브러리 
  9. **Django Filter**
    - Django 쿼리셋을 필터링할 수 있는 API를 제공하여, 사용자 정의 필터를 쉽게 구현할 수 있게 해줌
  10. **Django Haystack** 
    - 검색 기능을 쉽게 구현할 수 있도록 도와주는 라이브러리로, Elasticsearch, Solr 등 다양한 검색엔진과 통함할 수 있음
  11. **Django Rest Auth** 
    - Django REST framework와 함께 사용할 수 있는 인증 및 사용자 관리 라이브러리
  12. **Django Simple History**
    - Django 모델의 변경 이력을 기록하여 추적할 수 있게 도와주는 라이브러리
  13. **Django Environ**
    - 환경 변수를 쉽게 관리할 수 있도록 도와주는 라이브러리로, 설정 파일을 더 깔끔하게 유지할 수 있음
  14. **Django ImageKit** 
    - 이미지 처리 및 최적화를 위한 라이브러리로, 다양한 이미지 변환 기능을 제공

</details>
