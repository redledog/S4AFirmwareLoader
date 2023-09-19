# S4ALoader

avrdude (https://github.com/avrdudes/avrdude/) 가 필요합니다.
다운로드 후 avrdude.exe 가 포함된 폴더의 경로를 환경변수에 추가해야합니다. -- 내부에 추가 완료

killian441 의 avr_multiloader 를 사용했습니다.
https://github.com/killian441/avr_multiloader

module 설치를 위해 아래와 같이 터미널에 입력합니다.

pip install -r requirements.txt

빌드
DEBUG용 pyinstaller -F main.py
PRODUCT용 pyinstaller -w -F main.py