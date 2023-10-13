var sound1 = new Audio();
var src1 = document.createElement("source");
src1.type = "audio/mpeg"
src1.src = "audio/C.mp3";
sound1.appendChild(src1);

var sound2 = new Audio();
var src2 = document.createelement("source");
src2.type = "audio/mpeg";
src2.src = "audio/E.mp3";
sound2.appendChild(src2);

sound.play(); sound2.play();