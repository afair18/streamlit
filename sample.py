import streamlit as st
import time
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np





# 사이드바 메뉴
with st.sidebar:
    choice = option_menu("Menu", ["세팅","출력", "폼", "차트","MYSQL","기타기능","langchain"],
    icons=['gear','view-stacked', 'ui-checks', 'bar-chart','database-check','cpu','robot'],
    menu_icon="app-indicator", default_index=0,
    styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#08c7b4"},
    }
    )



# 모듈세팅 및 기본설치
def setting():
    st.header("모듈 설치")
    code = '''
    #streamlit 설치
    pip install streamlit
    import streamlit as st

    #streamlit 실행
    streamlit run sample.py

    #사이드 메뉴 설치
    pip install streamlit-option-menu
    from streamlit_option_menu import option_menu

    #차트 설치
    import pandas as pd
    import numpy as np

    #메뉴 왼쪽 icons 참고
    https://icons.getbootstrap.com/

    #MYSQL 설치+사용
    pip install mysql-connector-python
    import mysql.connector


    lang chain 설치
    '''
    st.code(code)
    st.markdown("---")

#기본출력
def view():
    # 출력부분
        
    st.title("텍스트 출력")
    st.header("Header")
    st.subheader("subheader")
    st.write('Hello, *World!* :sunglasses:')
    st.caption('Balloons. Hundreds of them...')
    st.latex(r''' e^{i\pi} + 1 = 0 ''')
    st.write(['st', 'is <', 3]) 
    code = '''
    import streamlit as st
    st.write('Hello, *World!* :sunglasses:')
    '''
    st.code(code)

    st.markdown("---")

    st.header("테이블출력")
    import pandas as pd
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40],
    }))

    code = '''
    import pandas as pd

    st.write('테이블출력 예제')
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40],
    }))
    '''
    st.code(code)

    st.markdown("---")
    st.header("컬럼 출력")
    col1,col2 = st.columns([2,3])
    # 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

    with col1 :
        # column 1 에 담을 내용
        st.title('here is column1')
    with col2 :
        # column 2 에 담을 내용
        st.title('here is column2')
        st.checkbox('this is checkbox1 in col2 ')


    # with 구문 말고 다르게 사용 가능 
    col1.subheader(' i am column1  subheader !! ')
    col2.checkbox('this is checkbox2 in col2 ') 
    #=>위에 with col2: 안의 내용과 같은 기능을합니다


    st.markdown("---")
    st.header("탭 출력")
    # 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
    tab1, tab2= st.tabs(['Tab A' , 'Tab B'])

    with tab1:
    #tab A 를 누르면 표시될 내용
        st.subheader('hello')
        
    with tab2:
    #tab B를 누르면 표시될 내용 
        st.subheader('hi')

    st.markdown("---")
    st.header("사이드바")

    


    # 사이드바에 체크박스, 버튼등 추가할 수 있습니다! 


    # st.markdown("---")
    # st.header("로딩상태 출력")
    # latest_iteration = st.empty()
    # bar = st.progress(0)
    # for i in range(100):
    #   latest_iteration.text(f'Iteration {i+1}')
    #   bar.progress(i + 1)
    #   time.sleep(0.05)
    # st.balloons()

    # st.markdown("---")
    # st.header("웨이팅 출력")
    # with st.spinner('Wait for it...'):
    #   time.sleep(5)
    #   st.success('Done!')


    st.markdown("---")
    st.header("이미지 출력")
    img = Image.open('sample_img.jpg')
    st.image(img)


#    st.markdown("---")
#    st.header("동영상 출력")
#    video_file = open('sample_movie.mp4', 'rb')
#    st.video(video_file)

    st.markdown("---")
    st.header("오디오 출력")
    audio_file = open('sample_audio.mp3', 'rb')
    st.audio( audio_file.read() , format='audio/mp3')

    st.markdown("---")
    # CSS를 사용해 버튼 스타일 정의
    st.header("css 버튼 출력+파이썬 변수")
    button_style = """
    <style>
    .custom-button {
        display: inline-block;
        padding: 0.5rem 1rem;
        font-size: 1rem;
        color: white;
        background-color: gray;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .custom-button:hover {
        background-color: black;
    }
    </style>
    """

    # Streamlit 페이지에 CSS 적용
    st.markdown(button_style, unsafe_allow_html=True)


    py_variable = "파이썬 변수"
    # HTML 버튼 생성
    button_html = f'<button onclick="handleClick()" class="custom-button">{py_variable}</button>'
    st.markdown(button_html, unsafe_allow_html=True)

#==================================================================================================

# 폼 출력
def form():
    st.markdown("---")
    st.header("텍스트 입력 폼")
    # 1. 이름 입력 받기
    name = st.text_input('이름을 입력하세요!')

    if name != '' :
        st.subheader(name + '님 안녕하세요??')
    # 2. 입력 글자 갯수 제한
    address = st.text_input('주소를 입력하세요!', max_chars=10)

    # 여러 행을 입력가능하도록
    message = st.text_area('메세지를 입력하세요', height=3)
    st.subheader(message)

    st.markdown("---")
    st.header("비밀번호 입력폼")
    # 비밀번호 입력
    password = st.text_input('비밀번호 입력', type='password')
    st.write(password)


    st.markdown("---")
    st.header("체크박스 선택")
    # 체크박스 선택
    agree = st.checkbox('동의합니다')
    if agree :
        st.write('동의하셨습니다.')
    else :
        st.write('동의하지 않았습니다.')
    st.markdown("---")
    st.header("라디오 버튼")
    # 라디오버튼 선택예제

    options = ['Option 1', 'Option 2', 'Option 3']
    selected_option = st.radio('Select an option', options)
    st.write('You selected:', selected_option)

    st.markdown("---")
    st.header("숫자입력 폼")
    # 4. 숫자 입력, 정수
    st.number_input('숫자 입력', 1, 100)
    # 5. 숫자 입력, 실수
    st.number_input('실수 입력', 1.0, 100.0)

    st.markdown("---")
    st.header("날짜입력 폼")
    # 6. 날짜 입력
    my_date = st.date_input('약속날짜') # 디폴트로 오늘 날짜가 찍혀 있다.
    st.write(my_date)

    # 요일 찍기
    st.write( my_date.weekday() )
    st.write( my_date.strftime('%A') )


    st.markdown("---")
    st.header("멀티 셀렉트")
    # 멀티세렉트
    option_list = ['짜장면', '짬뽕', '탕수육']
    option = st.multiselect('메뉴를 선택하세요', option_list)
    st.write(option)


    st.markdown("---")
    st.header("슬라이더 선택")
    age = st.slider('나이', 1, 120, 30, 5)
    st.text('제가 선택한 나이는 {} 입니다.'.format(age))

    # csv 저장시 utf-8로 저장
    st.markdown("---")
    st.header("익스펜더")
    df = pd.read_csv('sample_csv.csv')
    with st.expander('데이터프레임 보기') :
        st.dataframe(df)


    st.markdown("---")
    st.header("시간 입력폼")
    my_time = st.time_input('시간 선택')
    st.write(my_time)


    st.markdown("---")
    st.header("색상 입력폼")
    color = st.color_picker('색을 선택하세요')
    st.write(color)

#차트 출력
def chart():
    # 차트 출력
    # 바차트
    chart_data = pd.DataFrame(
    {
        "col1": list(range(20)) * 3,
        "col2": np.random.randn(60),
        "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
    }
    )

    st.bar_chart(chart_data, x="col1", y="col2", color="col3")


    #영역차트
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)


    # 라인차트
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)


    # scatter 차트
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.scatter_chart(chart_data)

    # 지도
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    st.map(df)


    # ploty 차트
    import plotly.express as px

    st.subheader("Define a custom colorscale")
    df = px.data.iris()
    fig = px.scatter(
        df,
        x="sepal_width",
        y="sepal_length",
        color="sepal_length",
        color_continuous_scale="reds",
    )

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    with tab2:
        st.plotly_chart(fig, theme=None, use_container_width=True)


def mysql():
    st.header("MYSQL 접속")
    code = '''
    import mysql.connector
    # MySQL 데이터베이스 연결 설정
    db = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )

    # MySQL 커서 생성
    cursor = db.cursor()
    '''
    st.code(code)
    st.markdown("---")

    st.header("MYSQL 데이터 추가")
    code = '''
    new_data = st.text_input("새로운 데이터 입력:")
    if st.button("추가"):
        insert_query = "INSERT INTO your_table_name (column_name) VALUES (%s)"
        cursor.execute(insert_query, (new_data,))
        db.commit()
        st.success("데이터가 추가되었습니다.")
    '''
    st.code(code)
    st.markdown("---")

    st.header("MYSQL 데이터 조회")
    code = '''
    # 데이터 조회
    cursor.execute("SELECT * FROM your_table_name")
    result = cursor.fetchall()
    for row in result:
        st.write(row)
    '''
    st.code(code)
    st.markdown("---")

    st.header("MYSQL 데이터 수정")
    code = '''
    # 데이터 수정
    update_data = st.text_input("수정할 데이터 입력:")
    if st.button("수정"):
        update_query = "UPDATE your_table_name SET column_name = %s WHERE column_name = %s"
        cursor.execute(update_query, (update_data, update_data))
        db.commit()
        st.success("데이터가 수정되었습니다.")
    '''
    st.code(code)
    st.markdown("---")


def etc():
    st.header("웹페이지 파싱")
    code = '''
    import requests
    from bs4 import BeautifulSoup

    # 네이버 금융에서 종목코드 넣으면 가격정보 가져오기

    codes = ['096530', '010130'] # 종목코드 리스트
    prices = [] # 가격정보가 담길 리스트

    for code in codes:
        url = 'https://finance.naver.com/item/main.nhn?code=' + code
        response = requests.get(url)

        response.raise_for_status()

        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        today = soup.select_one('#chart_area > div.rate_info > div')
        price = today.select_one('.blind')
        prices.append(price.get_text())
        print(prices)
'''
    st.code(code)

    import requests
    from bs4 import BeautifulSoup

    # 네이버 금융에서 종목코드 넣으면 가격정보 가져오기
    
    codes = ['096530', '010130'] # 종목코드 리스트
    prices = [] # 가격정보가 담길 리스트

    for code in codes:
        url = 'https://finance.naver.com/item/main.nhn?code=' + code
        response = requests.get(url)
        response.raise_for_status()

        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        today = soup.select_one('#chart_area > div.rate_info > div')
        price = today.select_one('.blind')
        prices.append(price.get_text())
        #print(prices)
    st.write("실행결과")
    st.write(prices)
    

    st.header("네이버 자동로그인")
    code = '''
    import pyperclip
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import time

    # 웹드라이버 열기 (네이버 메인 화면)
    driver = webdriver.Chrome()
    driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

    time.sleep(3)   # 3초 시간 지연

    # 로그인 창에 아이디/비밀번호 입력
    loginID = "네이버아이디"
    pyperclip.copy(loginID)
    driver.find_element(By.XPATH, '//*[@id="id"]').send_keys(Keys.CONTROL + 'v') # 붙여넣기


    loginPW = "네이버비번"
    pyperclip.copy(loginPW)
    driver.find_element(By.XPATH, '//*[@id="pw"]').send_keys(Keys.CONTROL + 'v') # 붙여넣기


    time.sleep(1)

    # 로그인 버튼 클릭
    driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
    time.sleep(2)

    #로그인 후 '새로운 환경' 알림에서 '나중에 하기' 클릭
    driver.find_element(By.XPATH, '//*[@id="new.dontsave"]').click()

    while(True):
        pass
    '''
    st.code(code)



    st.header("엑셀,워드 다루기")
    code = '''
    import os
    import openpyxl as op #엑셀 모듈
    from docx import Document #워드 모듈

    from openpyxl.styles.fonts import Font
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.style import WD_STYLE_TYPE
    from docx.shared import Cm, Inches
    from docx.oxml.ns import qn
    from docx.shared import Pt



    # 현재 파일 경로
    path = os.path.dirname(os.path.abspath(__file__))

    wb = op.load_workbook(f"{path}/excel.xlsx") #워크북 객체 생성(파일명 : test.xlsx)
    ws = wb.active #활성화 되어있는 시트 설정


    #Sheet의 Cell 속성 사용하기
    data1 = ws.cell(row=1, column=2).value

    #엑셀 인덱스(Range) 사용하기
    data2 = ws["C1"].value


    #위 결과 출력
    print("cell(1,2) : ", data1)
    print('Range("C1"):', data2)



    # 엑셀의 D4 셀에 C의 합(sum 함수 이용)을 넣고 저장
    ws["D4"].value = "=SUM(A4:C4)"
    font_format = Font(size=15, name='굴림', color = 'FF0000',bold = True,italic = True)
    ws["D4"].font = font_format

    # 새로운 시트 생성 ws = wb.create_sheet("연습")
    wb.save(f"{path}/excel.xlsx") # 엑셀 저장

    # 엑셀의 값을 데이터에 넣기
    data = []
    for row in ws.rows:
        data.append(row[1].value) # B열 엑셀 데이터를 리스트에 추가

    print(data)


    # 워드문서 만들기

    # 불러오기
    doc = Document()

    # 글씨입력
    doc.add_heading('제목 입니다', level=1)
    para = doc.add_paragraph('문단에 들어갈 내용입니다.') #문단 추가


    #이미지삽입
    doc.add_picture(f'{path}/excelimg.jpg', width=Cm(10)) #이미지 삽입



    #표만들기
    table = doc.add_table(rows=2, cols=3) #표 추가
    table.style = doc.styles['Table Grid']
    cell = table.cell(0, 1) #0행 1열
    cell.text = '표에 들어갈 내용입니다.' #표에 내용 추가

    #저장하기
    doc.save(f'{path}/word.docx')
    '''
    st.code(code)

def langchain():
    st.header("Langchain")
    
    code = '''
    from langchain.chat_models import ChatOpenAI
    import openai
    import os

    # OpenAI API 키 설정
    os.environ['OPENAI_API_KEY'] = "키값"
    
    # Langchain을 사용하여 모델 연결
    llm = ChatOpenAI(temperature=0,               # 창의성 (0.0 ~ 2.0) 
                 max_tokens=2048,             # 최대 토큰수
                 model_name='gpt-3.5-turbo',  # 모델명
                )

    # 질의내용
    question = '미국의 수도는 뭐야?'

    # 질의
    st.write((f'[답변]: {llm.predict(question)}'))



    # 사용가능한 모델 목록
    openai.api_key = "키값"
    model_list = sorted([m['id'] for m in openai.Model.list()['data']])
    for m in model_list:
        st.write(m)


    # 템플릿 사용
    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain
    template = '{area1} 와 {area2} 의 시차는 몇시간이야?'
    prompt = PromptTemplate(template=template, input_variables=['area1', 'area2'])
    chain = LLMChain(prompt=prompt, llm=llm)
    st.write(chain.run(area1='서울', area2='파리'))
    '''
    st.code(code)

    from streamlit.components.v1 import html

    # HTML + JavaScript 코드
    HTML_CODE = """
    <button id="startRecord">녹음 시작</button>
    <button id="stopRecord" disabled>녹음 정지</button>
    <p id="recognitionResult">인식된 텍스트가 여기에 표시됩니다...</p>

    <script>
    var recognition;
    document.getElementById("startRecord").addEventListener("click", function() {
        if ('webkitSpeechRecognition' in window) {
            recognition = new webkitSpeechRecognition();
            recognition.lang = 'ko-KR'; // 한국어 설정
            recognition.continuous = false; // 단일 결과
            recognition.interimResults = false; // 중간 결과 미표시

            recognition.onstart = function() {
                document.getElementById("recognitionResult").textContent = "인식 중...";
            };

            recognition.onresult = function(event) {
                var transcript = event.results[0][0].transcript;
                document.getElementById("recognitionResult").textContent = transcript;
            };

            recognition.onerror = function(event) {
                document.getElementById("recognitionResult").textContent = "인식 에러: " + event.error;
            };

            recognition.onend = function() {
                document.getElementById("startRecord").disabled = false;
                document.getElementById("stopRecord").disabled = true;
            };

            recognition.start();
            document.getElementById("startRecord").disabled = true;
            document.getElementById("stopRecord").disabled = false;
        } else {
            document.getElementById("recognitionResult").textContent = "이 브라우저에서는 음성 인식이 지원되지 않습니다.";
        }
    });

    document.getElementById("stopRecord").addEventListener("click", function() {
        if (recognition) {
            recognition.stop();
        }
    });
    </script>
    """


    HTML_CODE = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.5.12/cropper.min.css" />
    <style>
        img {
            max-width: 100%;
        }
        .container {
            margin-top: 20px;
        }
    </style>
    input type="file" id="imageInput" accept="image/*">
<div class="container">
    <img id="image" style="display:none;">
</div>
<button id="cropButton">Crop</button>

<script src="https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.5.12/cropper.min.js"></script>
<script>
    let image = document.getElementById('image');
    let input = document.getElementById('imageInput');
    let cropButton = document.getElementById('cropButton');
    let cropper;

    input.addEventListener('change', function(e) {
        const files = e.target.files;
        if (files && files.length > 0) {
            const fileReader = new FileReader();

            fileReader.onload = function() {
                image.src = this.result;
                image.style.display = 'block';

                if (cropper) {
                    cropper.destroy();
                }

                cropper = new Cropper(image, {
                    aspectRatio: 16 / 9,
                    viewMode: 1,
                });
            };

            fileReader.readAsDataURL(files[0]);
        }
    });

    cropButton.addEventListener('click', function() {
        if (!cropper) {
            return;
        }

        const canvas = cropper.getCroppedCanvas();
        if (!canvas) {
            return;
        }

        canvas.toBlob(function(blob) {
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'cropped-image.png';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }, 'image/png');
    });
    </script>
    """

    # Streamlit 앱에서 HTML 코드 삽입
    st.title('Streamlit 음성 인식 예제')
    html(HTML_CODE, height=200)

# 메뉴에 따라 내용이 다르게 나옴 
if choice == "출력":
    view()
elif choice == "폼":
    form()
elif choice == "차트":
    chart()
elif choice == "MYSQL":
    mysql()
elif choice == "세팅":
    setting()
elif choice == "기타기능":
    etc()
elif choice == "langchain":
    langchain()
else:
    view()






