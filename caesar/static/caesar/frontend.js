var canvas = document.getElementById('canvas');
var scene = canvas.getContext('2d');
scene.font = "14pt Arial";

/*binding handlers on submit buttons*/
$('#encode').on('click', function(){ sendRequest('/encode/') });
$('#decode').on('click', function(){ sendRequest('/decode/') });

function sendRequest(adress){
    $.ajax({
        type: 'GET',
        url: adress,
        data: {
            'inputText': $('.inputText').val(),
            'rotate': $('#rotate').val()
        },
        dataType: 'text',
        cache: false,
        success: onResponse
    })
}

function onResponse(response){
    var data = JSON.parse(response);
    $('.outputText').val(data['outputText']);
    $('.unravelText').val(data['unravelText']);
    var frequencyDict = data['frequencyDict'];
    drawDiagram(frequencyDict);
}

function drawDiagram(frequencyDict){

}