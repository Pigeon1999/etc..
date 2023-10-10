# 가상환경을 만드는 이유
# 여러 프로젝트를 개발할 때 프로젝트마다 패키지의 버전 문제가 있을 수 있다. 
# 이를 해결하기 위해서 가상환경을 만들어 각 프로젝트마다 패키징을 한다. 
# 가상환경 : 독립된 공간을 만들어 주는 기능 

# 1. 가상환경 폴더 생성 
# python -m venv 가상환경이름
# powershell 기준입니다. 

python -m venv env
& ./Scrpits/Activate.ps1 

# 2. 이 상태에서 패키지를 설치한다면 (가상환경명)\Lib\site-packages 안에 패키지가 저장됩니다

# 3. 패키지 목록 관리하기 
# 가상 환경에 설치된 패키지는 목록을 저장해 두었다가 나중에 다시 설치할 수 있습니다.

# pip freeze로 저장하기 
pip freeze > requirements.txt

# pip install로 설치하기 
pip install -r requirements.txt

# pip uninstall로 삭제하기 
pip uninstall -r requirements.txt

# 4. 가상 환경 비활성화하기
deactivate

# 5. 가상 환경 삭제하기 
sudo rm -rf 가상환경이름
