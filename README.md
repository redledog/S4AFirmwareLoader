# S4A Firmware Loader

avrdude (https://github.com/avrdudes/avrdude/) 가 포함되어 있습니다.
<br>
~~다운로드 후 avrdude.exe 가 포함된 폴더의 경로를 환경변수에 추가해야합니다.~~ -- 프로그램 내부에 포함. 따라서 환경변수에 추가할 필요 없음.
<br>
<hr>
killian441 의 avr_multiloader 를 사용했습니다.
<br>
(https://github.com/killian441/avr_multiloader)
<hr>
module 설치를 위해 아래와 같이 터미널에 입력합니다.
<br>
<code>pip install -r requirements.txt</code>
<br>
<h3>빌드</h3>
DEBUG용 <code>pyinstaller main_debug.spec</code>
<br>
PRODUCT용 <code>pyinstaller main.spec</code>
