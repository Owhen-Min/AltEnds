# FrontEnd

## 1. 프로젝트 소개
---
이 프로젝트는 영화 데이터 API와 대체 결말 생성 기능을 제공하는 웹 애플리케이션의 FrontEnd 부분입니다. 사용자는 다양한 영화에 대한 대체 결말을 생성하고, 커뮤니티에 공유할 수 있습니다.

## 2. 기술 스택
---
- **Vue.js**: 프론트엔드 프레임워크
- **Vue Router**: 페이지 라우팅
- **Vuex**: 상태 관리
- **Axios**: HTTP 요청 라이브러리
- **CSS/SCSS**: 스타일링
- **Webpack**: 모듈 번들러
## 3. 설치 방법
---
### 프로젝트 디렉터리로 이동
``` bash
cd front
```
### 의존성 설치
``` bash
npm install
```
### 개발 서버 시작
```bash
npm run dev
```
## 4. API와의 연동
---
이 프로젝트에서는 **Axios**를 사용하여 백엔드 API와 데이터를 주고받습니다. 주요 API는 영화 데이터 및 커뮤니티 관련 데이터에 접근하거나 조작하는 데 사용됩니다. 아래는 프로젝트에서 사용하는 주요 API 목록과 기능 설명입니다.

---
#### **1. API 연동 예시**

1. **Axios 기본 설정**
    
    - 프로젝트에서 Axios를 사용하기 위해 기본 설정을 구성합니다. 이 설정을 통해 모든 API 요청에 공통 헤더를 추가하거나 기본 URL을 지정할 수 있습니다.
```javascript
    import axios from 'axios';
    
    const apiClient = axios.create({
	  baseURL: 'http://<백엔드 서버 주소>',
	  headers: {
		'Content-Type': 'application/json',
	  },
	});
	export default apiClient;
```
2. **API 호출 예제**
    - 영화 목록 조회:
```javascript
    import apiClient from '@/utils/apiClient';
    
    const fetchMovies = async () => {
      try {
        const response = await apiClient.get('/api/v1/movies/');
        console.log(response.data);
	  } catch (error) {
	    console.error('Failed to fetch movies:', error);
	  }
	};
	
	fetchMovies();
```

    - 영화 상세 정보 조회:
```javascript
    const fetchMovieDetail = async (moviePk) => {
      try {
        const response = await apiClient.get(`/api/v1/movies/${moviePk}/`);
        return response.data;
      } catch (error) {
        console.error('Failed to fetch movie details:', error);
      }
	};
```
        
    - 댓글 생성: 
```javascript
    const createComment = async (endingPk, commentData) => {
      try {
        const response = await apiClient.post(
          `/api/v1/movies/altends/${endingPk}/comments/`,
          commentData
        );
        return response.data;
      } catch (error) {
        console.error('Failed to create comment:', error);
      }
    };
```