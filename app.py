from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <head>
            <title>음성 인식</title>
        </head>
        <body>
            <h1>음성을 입력하세요</h1>
            <button id="start-btn">음성 인식 시작</button>
            <p id="text">인식된 음성이 여기에 표시됩니다...</p>
            <script>
                var startBtn = document.getElementById('start-btn');
                var textParagraph = document.getElementById('text');
                
                // 음성 인식 인스턴스 생성
                var recognition = new webkitSpeechRecognition();
                recognition.continuous = false; // 연속적으로 인식하지 않고 한 번만 인식
                recognition.lang = 'ko-KR'; // 한국어 설정
                
                // 음성 인식 시작 이벤트
                recognition.onstart = function() {
                    textParagraph.textContent = '인식을 시작합니다...';
                };
                
                // 음성 인식 결과 이벤트
                recognition.onresult = function(event) {
                    var transcript = event.results[0][0].transcript;
                    textParagraph.textContent = '인식된 텍스트: ' + transcript;
                };
                
                // 에러 처리
                recognition.onerror = function(event) {
                    textParagraph.textContent = '인식 에러: ' + event.error;
                };
                
                // 음성 인식 시작 버튼 클릭 이벤트
                startBtn.onclick = function() {
                    recognition.start();
                };
            </script>
        </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
