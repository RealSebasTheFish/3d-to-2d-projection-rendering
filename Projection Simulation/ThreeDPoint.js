class ThreeDPoint {
    constructor() {
        this.x = -xCenter + Math.random() * 2 * xCenter;
        this.y = -yCenter + Math.random() * 2 * yCenter;
        this.z = 100 + Math.random() * DEPTH-100;

        this.radius = MAX_RADIUS;

        this.scaleProjected = 0;
        this.xProj = 0;
        this.yProj = 0;

        let r = parseInt( Math.floor(Math.random() * 255) );
        let g = parseInt( Math.floor(Math.random() * 255) );
        let b = parseInt( Math.floor(Math.random() * 255) );
        this.color = "rgb(" + r + "," + g + "," + b + ")";
    }

    update() {
        this.scaleProjected = DEPTH / (DEPTH + this.z);

        this.xProj = (this.x * this.scaleProjected) + xCenter;
        this.yProj = (this.y * this.scaleProjected) + yCenter;

        this.radius = map(this.z, 0, DEPTH, MAX_RADIUS, 0);
    }

    draw(ctx) {
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.xProj, this.yProj, this.radius, 0, Math.PI*2, true);
        ctx.fill();
    }
}