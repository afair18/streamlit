import streamlit as st
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

# Streamlit 앱에서 HTML 코드 삽입
st.title('Streamlit 음성 인식 예제')
html(HTML_CODE, height=200)
