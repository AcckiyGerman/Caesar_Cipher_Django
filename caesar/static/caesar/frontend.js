/*binding canvas*/
var canvas = document.getElementById('canvas');
var scene = canvas.getContext('2d');
scene.font = "14pt Arial";

/*binding handlers on submit buttons*/
$('#encode').on('click', function(){ sendRequest('/encode/') });
$('#decode').on('click', function(){ sendRequest('/decode/') });

/*this func will collect and validate data from fields*/
function collectData(){
    var inputText = $('.inputText').val();
    if ( !inputText ){ alert('Пожалуйста, введите сообщение!'); return }
    var rotate = $('#rotate').val();
    if ( isNaN(rotate) ){ alert('Сдвиг должен быть числом!'); return }
    return { inputText: inputText, rotate: rotate };
}

function sendRequest(adress){
    var data = collectData();
    if ( !data ){ return }  // Nothing to send.
    $.ajax({
        type: 'GET',
        url: adress,
        data: { jsonData: JSON.stringify(data) },
        dataType: 'text',
        cache: false,
        success: onResponse
    })
}

function onResponse(response){
    var data = JSON.parse(response);
    // placing data into the proper fields:
    $('.outputText').val( data['outputText'] );
    $('.unravelText').val( data['unravelText'] );
    drawDiagram(data['frequencyDict']);
}

function drawDiagram(frequencyDict) {
    //clearing canvas
    scene.clearRect(0, 0, canvas.width, canvas.height);
    //finding max frequency value and sorting symbols
    var symbols = new Array();
    var maxVal = 0;
    for (var s in frequencyDict){
        symbols.push(s);
        var val = frequencyDict[s];
        if (val > maxVal){
            maxVal = val;
        }
    }
    symbols.sort();
    //drawing lines
    scene.fillStyle = "blue";
    var step = canvas.height / maxVal;
    for (i=0; i<maxVal; i++){
        scene.fillRect(0, i*step, canvas.width, 1);
    }
    //drawing pikes
    var width = canvas.width / symbols.length;
    symbols.forEach(function(symbol, number) {
        val = frequencyDict[symbol];
        var xPos = number * width;
        scene.fillStyle = "orange";
        scene.fillRect(xPos, canvas.height, width - 5, -val*step);
        scene.fillStyle = "black";
        scene.fillText(symbol, xPos + 7, canvas.height - 5);
    })
}
