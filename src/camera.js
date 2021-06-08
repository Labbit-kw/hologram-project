// dom
const recordButton = document.querySelector(".record-button")
const stopButton = document.querySelector(".stop-button")
const playButton = document.querySelector(".play-button")
const downloadButton = document.querySelector(".download-button")

// 비디오 플레이어
const previewPlayer = document.querySelector("#preview")
const recordingPlayer = document.querySelector("#recording")

let recorder;
let recordedChunks; // 데이터 담는 용도

// functions
function videoStart(){
    navigator.mediaDevices.getUserMedia({ video: true, audio: true})
        .then(stream => {
            previewPlayer.srcObject = stream;
            startRecording(previewPlayer.captureStream())
        })
}

function startRecording(stream){
    recordedChunks = [];
    recorder = new MediaRecorder(stream);
    recorder.ondataavailable = (e) => { recordedChunks.push(e.data)}; // 이벤트에 데이터를 담아서 . 녹화된 내용이 여기에 담김
    recorder.start();
 }

 function stopRecording(){
    previewPlayer.srcObject.getTracks().forEach(track => track.stop()) //배열이기 때문에 이렇게 사용 16:40초 내용 언급
    recorder.stop();
 }

 function playRecording(){
    const recordedBlob = new Blob(recordedChunks, {type: "video/webm"}); // 파라미터 : (비디오 데이터가 담긴 배열, 확장자)
    recordingPlayer.src = URL.createObjectURL(recordedBlob);
    recordingPlayer.play();
    downloadButton.href = recordingPlayer.src;
    downloadButton.download = `recording_${new Date()}.webm`;

 }

// 이벤트 처리
recordButton.addEventListener("click", videoStart);
stopButton.addEventListener("click", stopRecording);
playButton.addEventListener("click", playRecording);