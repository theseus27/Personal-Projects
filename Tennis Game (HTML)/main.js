var canvas, canvasContext;
var ballX = 50;
var ballSpeedX = 5;

window.onload = function() {
  console.log("Hello world!");
  canvas = document.getElementById('gameCanvas');
  canvasContext = canvas.getContext('2d');

  // 100 ms = 1 s, will run fps times per second
  var framesPerSecond = 30;
  setInterval(function() {
    moveEverything();
    drawEverything();
  }, 1000/framesPerSecond);
}

function moveEverything() {
  ballX += ballSpeedX;

  if (ballX > 790 || ballX < 10) {
    ballSpeedX *= -1;
  }
}

function drawEverything() {
  //Objects drawn 'last' will be drawn on top of older objects
  canvasContext.fillStyle = 'black';
  canvasContext.fillRect(0, 0, canvas.width, canvas.height);

  canvasContext.fillStyle = 'white';
  canvasContext.fillRect(0, 200, 10, 150);

  canvasContext.fillStyle = 'red';
  canvasContext.fillRect(ballX, 100, 10, 10);
}
