function createsquarebuffer(size){
    var k = size / 100;
    var points = [];
    var vertexPoints = [
        vec3(-k, k, 1,0),
        vec3(-k,-k, 1.0),
        vec3(k, -k, 1.0),
        vec3(k, k, 1.0),
    ]
    points = cubefaces(vertexPoints[0], vertexPoints[1], vertexPoints[2], vertexPoints[3]);
    return points;
}

function createcubebuffer(size){
    var k = size / 100;
    var points = [];
    var hold = [];
    var vertexPoints = [
        vec4(-k , -k , k, 1.0),
        vec4(-k , k , k, 1.0),
        vec4(k , k , k, 1.0),
        vec4(k , -k , k, 1.0),
        vec4(-k , -k , -k, 1.0),
        vec4(-k , k , -k, 1.0),
        vec4(k , k , -k, 1.0),
        vec4(k , -k , -k, 1.0)
    ]

    hold.push(cubefaces(vertexPoints[1], vertexPoints[0], vertexPoints[3], vertexPoints[2]));
    hold.push(cubefaces(vertexPoints[2], vertexPoints[3], vertexPoints[7], vertexPoints[6]));
    hold.push(cubefaces(vertexPoints[3], vertexPoints[0], vertexPoints[4], vertexPoints[7]));
    hold.push(cubefaces(vertexPoints[6], vertexPoints[5], vertexPoints[1], vertexPoints[2]));
    hold.push(cubefaces(vertexPoints[4], vertexPoints[5], vertexPoints[6], vertexPoints[7]));
    hold.push(cubefaces(vertexPoints[5], vertexPoints[4], vertexPoints[0], vertexPoints[1]));

        for(var i = 0; i < hold.length; i++){
            for(var j = 0; j < hold[i].length; j++){
                points.push(hold[i][j]);
            }
        }

    return points;
    
}

function cubefaces(a, b, c, d){
    var points = [];
    var indecis = [a, b, c, a, c, d];
    for ( var i = 0; i < indecis.length; ++i ) {
        points.push(indecis[i]);
    }
    return points;
}