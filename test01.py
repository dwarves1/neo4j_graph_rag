import os
from dotenv import load_dotenv
from langchain_neo4j import Neo4jGraph

# 1. 환경 변수 로드
load_dotenv()

# 2. 값 로드 확인 (디버깅용)
uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USERNAME")
pwd = os.getenv("NEO4J_PASSWORD")

print(f"DEBUG: URI={uri}, USER={user}, PWD={'****' if pwd else 'None'}")

if not uri or not user or not pwd:
    raise ValueError(".env 파일에서 환경 변수를 읽어오지 못했습니다. 파일 위치를 확인하세요.")

# 3. 객체 생성
try:
    graph = Neo4jGraph( 
        url=uri, 
        username=user, 
        password=pwd,
    )
    print("연결 성공!")
except Exception as e:
    print(f"연결 실패: {e}")