// Get the timer and button elements
const timerDiv = document.getElementById("timer");

let timer;
let seconds = 0;

// Function to format time as HH:MM:SS
function formatTime(seconds) {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const secs = seconds % 60;
  return `${String(hours).padStart(2, "0")}:${String(minutes).padStart(
    2,
    "0"
  )}:${String(secs).padStart(2, "0")}`;
}

// Function to update the timer display
function updateTimer() {
  timerDiv.textContent = formatTime(seconds);
}

// Function to start the timer
function startTimer() {
  if (!timer) {
    timer = setInterval(() => {
      seconds++;
      updateTimer();
    }, 1000);
  }
}

// Function to stop the timer
function stopTimer() {
  if (timer) {
    clearInterval(timer);
    timer = null;
  }
}

startTimer()