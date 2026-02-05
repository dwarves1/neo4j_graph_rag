1. uv 설치
- macOS 및 Linux: curl -LsSf https://astral.sh/uv/install.sh | sh
- Windows: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

### Neo4j GraphRAG 프로젝트 설정
#### 1. 프로젝트 디렉토리 생성 및 초기화
uv init neo4j-graphrag
cd neo4j-graphrag

#### 2. 가상환경 생성
# Python 3.12 기반 가상환경 생성
uv venv .venv --python=3.12

# 가상환경 활성화 (Windows)
.venv\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source .venv/bin/activate

# 가상환경 활성화시에 오류 발생하면 권한부여 해야함
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

#### 3. 필요한 패키지 설치
# langchain-neo4j 설치
uv add langchain-neo4j

# 추가 필요한 패키지들 (예시)
uv add python-dotenv langchain langchain-openai langchain-google-genai

#### 4. git 설정
git config --global user.name "본인영문이름"
git config --global user.email "본인이메일@example.com"

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/계정명/저장소명.git
git push -u origin main