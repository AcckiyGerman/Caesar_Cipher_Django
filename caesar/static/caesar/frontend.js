/*binding canvas*/
var canvas = document.getElementById('canvas');
var scene = canvas.getContext('2d');
scene.font = "12pt Arial";

/*binding handlers on submit buttons*/
$('#encode').on('click', function(){ sendRequest('/encode/') });
$('#decode').on('click', function(){ sendRequest('/decode/') });

/*collect and validate data from fields*/
function collectData(){
    var input_text = $('.input_text').val();
    var rotate = $('#rotate').val();
    if ( isNaN(rotate) ){ alert('Сдвиг должен быть числом!'); return }
    if ( !input_text ){ alert('Пожалуйста, введите сообщение!'); return }
    return { input_text: input_text, rotate: rotate };
}

function sendRequest(adress){
    var data = collectData();
    if ( !data ){ return }
    $.ajax({
        type: 'GET',
        url: adress,
        data: { json_data: JSON.stringify(data) },
        dataType: 'text',
        cache: false,
        success: onResponse
    })
}

function onResponse(response){
    var data = JSON.parse(response);
    console.log(data);
    // placing data into the proper fields:
    $('.output_text').text( data['output_text'] );
    $('.restored_text_box').text( data['restored_text'] );
    $('.probably_rotate').text( data['probably_rotate']);
    drawDiagram(data['frequency_dict']);
    $('#iframe')[0].contentWindow.location.reload(true);
}

function drawDiagram(frequencyDict) {
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
    for (var i=1; i<maxVal; i++){
        //scene.fillRect(0, i*step, canvas.width, 1);
    }
    //drawing pikes
    var width = canvas.width / symbols.length;
    if (width > 20){ width = 20; }
    symbols.forEach(function(symbol, number) {
        val = frequencyDict[symbol];
        var xPos = number * width;
        scene.fillStyle = "orange";
        scene.fillRect(xPos, canvas.height, width - 3, -val*step);
        scene.fillStyle = "black";
        scene.fillText(symbol, xPos, canvas.height - 5);
    })
}