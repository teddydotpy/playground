"use strict";

var gl;
var points = [];
var axis = 0;
var theta = [ 0, 0, 0 ];

var thetaLoc;

var modeViewMatrix, projectionMatrix;
var modelViewMatrixLoc, projectionMatrixLoc;

var colors = [vec4(Math.random(), Math.random(), Math.random(), 1,0)]
        
window.onload = function init(){
        
    //Setting up webGl
    var canvas = document.getElementById( "gl-canvas" );
    gl = WebGLUtils.setupWebGL( canvas );
    if ( !gl ) { alert( "WebGL isn't available" ); }


// This section of code was copied from https://webglfundamentals.org/webgl/lessons/webgl-resizing-the-canvas.html
// To get my canvas to look nice in full screen

    const canvasToDisplaySizeMap = new Map([[canvas, [1024, 1024]]]);
 
    function onResize(entries) {
      for (const entry of entries) {
        let width;
        let height;
        let dpr = window.devicePixelRatio;
        if (entry.devicePixelContentBoxSize) {
          // NOTE: Only this path gives the correct answer
          // The other paths are imperfect fallbacks
          // for browsers that don't provide anyway to do this
          width = entry.devicePixelContentBoxSize[0].inlineSize;
          height = entry.devicePixelContentBoxSize[0].blockSize;
          dpr = 1; // it's already in width and height
        } else if (entry.contentBoxSize) {
          if (entry.contentBoxSize[0]) {
            width = entry.contentBoxSize[0].inlineSize;
            height = entry.contentBoxSize[0].blockSize;
          } else {
            width = entry.contentBoxSize.inlineSize;
            height = entry.contentBoxSize.blockSize;
          }
        } else {
          width = entry.contentRect.width;
          height = entry.contentRect.height;
        }
        const displayWidth = Math.round(width * dpr);
        const displayHeight = Math.round(height * dpr);
        canvasToDisplaySizeMap.set(entry.target, [displayWidth, displayHeight]);
      }
    }



function resizeCanvasToDisplaySize(canvas) {
    // Get the size the browser is displaying the canvas in device pixels.
   const [displayWidth, displayHeight] = canvasToDisplaySizeMap.get(canvas);
   
    // Check if the canvas is not the same size.
    const needResize = canvas.width  != displayWidth || 
                       canvas.height != displayHeight;
   
    if (needResize) {
      // Make the canvas the same size
      canvas.width  = displayWidth;
      canvas.height = displayHeight;
    }
   
    return needResize;
}

// ---------------------------------------------------------------------------------------------------------------- //

    var cubebuffer = createcubebuffer(50);
    

    var program = initShaders(gl, "vertex-shader", "fragment-shader");
    gl.useProgram( program );

    var vBuffer = gl.createBuffer();
    gl.bindBuffer( gl.ARRAY_BUFFER, vBuffer );
    gl.bufferData( gl.ARRAY_BUFFER, flatten(cubebuffer), gl.STATIC_DRAW );

    var vPosition = gl.getAttribLocation( program, "vPosition" );
    gl.vertexAttribPointer( vPosition, 3, gl.FLOAT, false, 0, 0 );
    gl.enableVertexAttribArray( vPosition );

    thetaLoc = gl.getUniformLocation(program, "theta");

    render();
    resizeCanvasToDisplaySize(gl.canvas); //Taken from https://webglfundamentals.org/webgl/lessons/webgl-resizing-the-canvas.html

}

function render(){
    gl.clear( gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
    gl.viewport( 0, 0, gl.canvas.width, gl.canvas.height );
    theta[axis] += 2.0;
    gl.uniform3fv(thetaLoc, theta);

    gl.drawArrays( gl.TRIANGLES, 0, 36);
    requestAnimFrame(render);
}

//I was unable to finish sorry I really did try


