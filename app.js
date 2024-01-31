let mediaRecorder;
let audioChunks = [];

document.getElementById("startRecord").addEventListener("click", () => {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.ondataavailable = event => {
                audioChunks.push(event.data);
            };
            mediaRecorder.onstop = async () => {
                const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                const formData = new FormData();
                formData.append("audio", audioBlob, "recording.wav");
                
                // 오디오 파일을 서버로 전송
                await fetch("/upload-audio/", { method: "POST", body: formData });
            };

            audioChunks = [];
            mediaRecorder.start();
            document.getElementById("stopRecord").disabled = false;
            document.getElementById("startRecord").disabled = true;
        })
        .catch(error => console.error("Error accessing media devices.", error));
});

document.getElementById("stopRecord").addEventListener("click", () => {
    mediaRecorder.stop();
    document.getElementById("stopRecord").disabled = true;
    document.getElementById("startRecord").disabled = false;
});
