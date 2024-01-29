import streamlit as st
import time
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np

# 메뉴 구현
# pip install streamlit-option-menu
# from streamlit_option_menu import option_menu




with st.sidebar:
    choice = option_menu("Menu", ["출력", "폼", "차트"],
    icons=['view-stacked', 'ui-checks', 'bar-chart'],
    menu_icon="app-indicator", default_index=0,
    styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#08c7b4"},
    }
    )


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
    # 초기 세팅
    


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

#    st.markdown("---")
#    st.header("오디오 출력")
#    audio_file = open('sample_audio.mp3', 'rb')
#    st.audio( audio_file.read() , format='audio/mp3')


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

st.sidebar.header("모듈 설치")
code = '''
streamlit 설치
pip install streamlit
import streamlit as st

streamlit 실행
streamlit run sample.py

사이드 메뉴 설치
pip install streamlit-option-menu
from streamlit_option_menu import option_menu

차트 설치
import pandas as pd
import numpy as np

메뉴 왼쪽 icons 참고
https://icons.getbootstrap.com/

lang chain 설치
'''
st.sidebar.code(code)


# 메뉴에 따라 내용이 다르게 나옴 
if choice == "출력":
    view()
elif choice == "폼":
    form()
else:
    chart()






