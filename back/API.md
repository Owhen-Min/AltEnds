AltEnds/
│
├── back/                          # 기본 프로젝트 파일
│   ├── settings.py                # 설정 파일
│   ├── urls.py                    # URL 라우팅
│   ├── wsgi.py                    # WSGI 진입점
│   └── requirements.txt           # Python 패키지 의존성
│
├── accounts/                      # 사용자 계정 관련 앱
│   ├── models.py                  # 데이터베이스 모델
│   ├── adapters.py                # 어댑터
│   ├── exception_handlers.py      # 예외 처리기
│   ├── forms.py                   # 폼
│   ├── models.py                  # 유저 모델
│   ├── serializers.py             # 시리얼라이저
│   ├── signals.py                 # 신호
│   └── views.py                   # API 엔드포인트
│
├── communityarticles/             # 커뮤니티 관련 앱
│   ├── models.py                  # 데이터베이스 모델
│   ├── serializers.py             # 직렬화기
│   ├── urls.py                    # URL 라우팅
│   └── views.py                   # API 엔드포인트
│
├── moviearticles/                 # 영화 기사 관련 앱
│   ├── models.py                  # 데이터베이스 모델
│   ├── serializers.py             # 직렬화기
│   ├── urls.py                    # URL 라우팅
│   └── views.py                   # API 엔드포인트
│
├── media/                         # 미디어 파일
│   ├── movies/                    # 영화 포스터
│   ├── profilepictures/           # 프로필 사진
│   └── static/                    # 정적 파일
│
└── README.md                      # 프로젝트 설명서