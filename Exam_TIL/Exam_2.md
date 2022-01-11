# 개발환경

## 가상환경과 패키지 관리
- `Anaconda`, `VirtualEnv`, ... 
  - 독립적인 개발환경을 구성할 수 있습니다. 

- 패키지 관리
  - `pip`: 파이썬 패키지 관리 도구
  - `conda`: 아나콘다 패키지 관리 도구

  1. 패키지 설치

  ```
    prompt> pip install 패키지명
    prompt> conda install 패키지명
  ```

  2. 패키지 확인

  ```
    prompt> pip list
    prompt> pip show 패키지명
    prompt> conda list
  ```

  3. 패키지 업데이트

  ```
    prompt> pip install --upgrade 패키지명
  ```

  4. 패키지 삭제 

  ```
    prompt> pip uninstall 패키지명
  ```

> 주피터에서 명령어 실행
  - 외부 명령어: 파이썬 명령어가 아닌, 주피터가 실행중인 운영체제한 대한 명령어를 의미 합니다. 
    - windows, linux 계열의 명령어를 주피터 내에서 사용이 가능합니다.
  - `!`는 외부 명령어를 의미 합니다.

# 웹(프론트앤드)

## HTTP
- Hyper Text Transfer Protocol
  - HTML 파일을 전송하는 네트워크 규칙
  - 하이퍼-텍스트 즉, 문자를 전송하기 위한 네트워크 표준

- HTTP 헤더
  - 요청헤더(Request Header)
    - 첫번째 라인(start-line): request-line

    ```
      Method  SP  URL/URI  SP  HTTP version
    ```
  - 응답헤더(Response Header)
    - 첫번째 라인(start-line): response-line

    ```
      HTTP version  SP  Status-Code  SP  Status-String
    ```
### Method

- GET
  - 전달하려는 데이터를 URL/URI을 통해서 전달
  - 보안에 취약하다
  - 데이터의 크기에 제한이 있습니다.(헤더의 크기를 넘을 수 없습니다)

- POST
  - FORM을 통해서 전달할 수 있다. 
  - 보안이 강화된 형태
  - 데이터의 크기에 제한 없이 전달이 가능

### 상태코드

- 1xx
- 2xx
  - 200 OK: 요청이 잘 처리가 된 경우
- 3xx
- 4xx
  - 요청 오류(클라이언트측 오류)
  - 401 Unauthorized(인증오류)
  - 403 Fobbiden(권한이 없는 접근)
  - 404 Not Found(리소스를 찾을 수 없는 경우)
- 5xx
  - 서버측 오류(요청을 처리하다가 오류가 발생하는 경우)
  - 500 Internel Server Error

## HTML
- Hyper-Text Markup Language
  - 문서의 구조를 표현하기 위해 제일 처음 고안(By. 팀버너스리)
  - 언어라고 부르기는 어렵다
    - 제어문이 없다( JavaScript가 대신 )

- 요소(Element)
  - 태그, 내용, 속성
  - 계층적 구조 표현
    - 최상위 요소: HTML(모든 HTML 문서의 최상위 요소는 항상 `HTML`이다)
    - HEAD: 화면에 표현되지 않는 요소들로 구성
    - BODY: 화면에 보여지는 모든 요소들로 구성

- 태그
  - 문서를 표현하기 위한 태그들: p/Paragraph, h/Heading, a/anchor, img/Image, table, ol/Ordered List, ul/Unordered List
  - 배치에 따른 분류: 블록기반의 태그, 인라인 기반의 태그
  - 익명 태그: div, span

- 속성
  - 일반 속성: 태그에 종속적인 속성
    - 태그마다 서로 다른 속성을 갖게 됩니다. 
    - img 태그의 대표적인 속성: width, height, src
    - a 태그의 대표적인 속성: href, target
  - 글로벌 속성: 모든 태그에 공통적으로 사용 가능한 속성
    - id와 class가 대표적인 글로벌 속성
      - id와 class의 차이는? 
        - id는 유일한 값, class는 중복 가능한 값
    - 스타일 속성
    - 이벤트 속성

## CSS

- 셀렉터
  - 전체 선택자: *(와일드 카드)
  - 태그 선택자: 태그이름
  - id 선택자: #id이름
  - class 선택자: .class이름
  - 하위 선택자: 공백
  - 자식 선택자: `>`

## JavaScript
- `자바`와는 아무런 상관이 없습니다!
- 인터프리터 언어
  - 웹 에서 자바스크립트가 실행될 때는 웹 브라우저가 인터프리터 역할을 해준다. 
  - 웹이 아니라면? node.js를 통해서 실행이 가능

- DOM(Document Object Model)
  - HTML 문서를 하나의 객체로써 다룰 수 있게 해준다.
  - `document` 객체를 이용해서 요소에 접근하는 방법
    - 요소를 직접 선택
      - `document.getElementByTagName`
      - `document.getElementById`
      - `document.getElementByClassName`
      - ... 
    - 계층 구조를 이용한 접근
      - DOM에서는 요소도 하나의 속성
      - `childeNode, parentNode, ...`을 통해서 계층적 접근이 가능

- BOM(Browser Object Model)
  - 현재 사용하고 있는 브라우저 또한 객체이다. 

# 웹(백엔드)
- 웹 에서 장고의 역할은?
  - `웹 프레임워크`의 역할을 수행
    - 결국엔 쉽고 빠르게 웹 사이트를 개발할 수 있게 도와주는 도구
    - 자주 사용되는 구성 요소들을 미리 갖춰놓은 웹 개발 도구
    - `MVC`( Model, View, Controller ) 구성을 제공하는 대표적인 개발 도구

- 장고에서 프로젝트 생성 하는 방법

```
prompt> django-admin startproject 프로젝트이름
```

- 장고에서 앱을 생성 하는 방법

```
prompt> python manage.py startapp 앱이름
```

## Model
- `데이터 베이스`를 처리하기 위한 구성요소
  - `ORM`(Object Relational Mapping)
    - 장고의 객체와 DB의 테이블을 연결
    - SQL을 직접 사용하지 않아도 DB를 제어할 수 있다. 
    - 클래스의 이름 => 테이블의 이름
    - 속성 => 테이블의 컬럼

- Model에서 정의된 클래스를 DB에 반영하는 방법

```
prompt> python manage.py makemigrations app_name
...

prompt> python manage.py migrate
...
```

- 디비 테이블에서 사용하는 키(Key)
  - 클래스에서 속성을 정의할 때 키를 정의할 수 있습니다.
  - `Primary Key`
    - 유일한 값(중복 불가)
    - 자료를 식별하는 용도로 사용
  - `Foreign Key`
    - 테이블과 테이블의 관계를 설정
    - 외부 테이블을 참조하기 위해서 사용

## View
- 화면에 보여지는 부분을 처리
- 장고에서 `view`를 담당하는 기능은 `템플릿` 이다. 
  - 장고에서는 일반적으로 `MTV` 라는 용어를 사용 하기도 합니다.
    - `Model`, `Template`, `View`

## Controller
- 장고에서 `Controller` 역할을 담당하는 모듈이 `views`이다.
- URL 요청과 `views`를 연결해주는 역할을 담당하는 기능은?
  - `URLconf` -> `Urls.py`에서 요청 URL에 따른 Views와 연결

- 사용자가 URL을 통해서 요청할 수 있는 `Action` 4가지
  - `CRUD` => `Create`, `Read`, `Update`, `Delete`
  - 생성, 읽고, 수정, 삭제
  - CRUD에 맞춰서 기능을 새로 정의할 수 있도록 하면 됩니다.
    - `CRUD는 백엔드에서 기본적으로 제공되는 기능이다?`
      - 기본적으로 기능을 제공하지는 않습니다. 
      - URL 요청을 크게 4가지로 분류를 할 수 있는 것이고, 기능은 개발자가 직접 구현