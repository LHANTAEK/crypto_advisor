# Crypto Investment Advisor Bot
[English](README_EN.md) | [한국어](README.md)

이 프로젝트는 CrewAI와 chatGPT API를 활용하여 암호화폐 시장의 트렌드를 분석하고 투자 인사이트를 제공하는 AI 챗봇 입니다.
![image](https://github.com/user-attachments/assets/cca82c68-19f0-4143-b2b8-4dd84dd9532e)
[서비스 링크](https://huggingface.co/spaces/HANTAEK/cryptocurrency_analyst_chatbot)

## 주요 기능

이 애플리케이션은 다음과 같은 핵심 기능을 제공합니다.
- 실시간 암호화폐 시장 트렌드 분석
- AI 기반의 투자 인사이트 제공
- Gradio 웹 인터페이스를 통한 사용자 친화적 상호작용

## 설치 방법

프로젝트 설치를 위한 **두 가지 방법**을 제공합니다. Docker를 사용한 간편 설치와 Poetry를 사용한 로컬 개발 환경 설치 중 선택하실 수 있습니다.

### 사전 요구사항 (공통)

프로젝트를 실행하기 위해 다음의 API 키가 필요합니다.

1. OpenAI API 키
   - [OpenAI 웹사이트](https://platform.openai.com/signup)에서 회원가입 후 API 키를 발급받으세요.
   - API 키는 [API Keys](https://platform.openai.com/account/api-keys) 페이지에서 생성할 수 있습니다.

2. Tavily API 키
   - [Tavily 웹사이트](https://tavily.com/)에서 회원가입을 진행하세요.
   - 회원가입 후 대시보드에서 API 키를 발급받을 수 있습니다.

발급받은 API 키는 프로젝트 루트 디렉토리에 `.env` 파일을 생성하여 다음과 같이 설정하세요.
Docker에 들어가는 환경변수는 큰따옴표(""), 작은따옴표('')를 쓰지 않습니다. 주의해서 설정해주세요.

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### **방법 1**: Docker를 사용한 간편 설치

이 방법은 별도의 Python 환경 설정 없이 애플리케이션을 바로 실행할 수 있습니다.

1. Docker 설치
   - Windows/Mac: [Docker Desktop](https://www.docker.com/products/docker-desktop) 설치
   - Linux: 패키지 매니저를 통해 Docker 설치

2. 프로젝트 클론
```bash
git clone [repository-url]
cd [repository-name]
```

3. Docker 이미지 빌드
```bash
docker build -t crypto-advisor .
```

4. Docker 컨테이너 실행
```bash
docker run -p 7860:7860 --env-file .env crypto-advisor
```

### **방법 2**: Poetry를 사용한 로컬 개발 환경 설치

이 방법은 개발 및 커스터마이징을 위한 완전한 개발 환경을 제공합니다.

1. Python 3.11 설치
   - [Python 공식 웹사이트](https://www.python.org/downloads/)에서 Python 3.11 설치

2. Poetry 설치
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. 프로젝트 클론 및 의존성 설치
```bash
git clone [repository-url]
cd [repository-name]
poetry install
```

4. 애플리케이션 실행
```bash
poetry run python app.py
```

## 실행 확인

설치 방법과 관계없이 애플리케이션이 성공적으로 실행되면 아래와 같이 진행해주세요.

1. 웹 브라우저에서 `http://localhost:7860` 접속
2. "Crypto Investment Advisor Bot" 인터페이스 확인
3. 암호화폐 관련 질문이나 분석하고 싶은 주제 입력
4. AI의 분석 결과 및 투자 인사이트 확인


## 문제 해결

자주 발생하는 문제와 해결 방법

1. Docker 실행 시 포트 충돌
   - 다른 포트를 사용: `docker run -p 7861:7860 --env-file .env crypto-advisor`

2. Poetry 설치 문제
   - 가상 환경 재생성: `poetry env remove python` 후 `poetry install` 재실행


## 기여 방법

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request
