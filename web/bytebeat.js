let audioCtx = null;
let scriptNode = null;
let isPlaying = false;
let t = 0;

const toggleBtn = document.getElementById("toggleBtn");
const formulaInput = document.getElementById("formulaInput");

function createAudioEngine() {
  audioCtx = new (window.AudioContext || window.webkitAudioContext)({ sampleRate: 8000 });
  scriptNode = audioCtx.createScriptProcessor(1024, 0, 1);

  scriptNode.onaudioprocess = function (event) {
    const outputBuffer = event.outputBuffer.getChannelData(0);
    let evalFunc;
    try {
      evalFunc = new Function("t", "return (" + formulaInput.value + ") & 255;");
    } catch (e) {
      return;
    }

    for (let i = 0; i < outputBuffer.length; i++) {
      try {
        const u8Sample = evalFunc(t);
        outputBuffer[i] = (u8Sample / 128.0) - 1.0;
        t++;
      } catch (err) {
        outputBuffer[i] = 0;
      }
    }
  };
  scriptNode.connect(audioCtx.destination);
}

toggleBtn.addEventListener("click", () => {
  if (!audioCtx) createAudioEngine();
  if (isPlaying) {
    audioCtx.suspend();
    toggleBtn.textContent = "Start Audio";
    toggleBtn.style.background = "#238636";
    isPlaying = false;
  } else {
    audioCtx.resume();
    toggleBtn.textContent = "Stop Audio";
    toggleBtn.style.background = "#da3633";
    isPlaying = true;
  }
});