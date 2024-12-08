var width, height;
var xCenter, yCenter;

const MAX_RADIUS = 15;
const NUM_POINTS = 100;
const DEPTH = 600;

var ctx;

var points = new Array(NUM_POINTS);

function init() {
    var canvasElement = document.getElementById("myCanvas");
    ctx = canvasElement.getContext("2d");

    width = canvasElement.width;
    height = canvasElement.height;
    xCenter = width/2;
    yCenter = height/2;

    for (let i = 0; i < NUM_POINTS; i++) {
        points[i] = new ThreeDPoint();
    }

    projection();
}

function projection() {
    ctx.fillStyle = "#000000";
    ctx.rect(0, 0, width, height);
    ctx.fill();

    for (let i = 0; i < NUM_POINTS; i++) {
        points[i].z --;
        if ( points[i].z > 0) {
            points[i].update();
            points[i].draw(ctx);
        }
    }

    requestAnimationFrame(projection);
}

function map(inputNum, minInput, maxInput, minOutput, maxOutput) {
    return (inputNum - minInput) * (maxOutput - minOutput) / (maxInput - minInput) + minOutput;
}