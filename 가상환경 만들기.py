# 가상환경을 만드는 이유
# 여러 프로젝트를 개발할 때 프로젝트마다 패키지의 버전 문제가 있을 수 있다. 
# 이를 해결하기 위해서 가상환경을 만들어 각 프로젝트마다 패키징을 한다. 
# 가상환경 : 독립된 공간을 만들어 주는 기능 

# 가상환경 폴더 생성 
# python -m venv 가상환경이름
# powershell 기준입니다. 

python -m venv env
cd env
./Scrpits/Activate.ps1 
# (env) PS C:\project\example>

# 만약에 실행이 되지 않는다면 powershell을 관리자 권한으로 실행후 다시 실행합니다. 
# Set-ExecutionPolicy Unrestricted -> 코드 실행 

