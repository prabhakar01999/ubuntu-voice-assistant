function get_speech(){
    document.getElementById("info").value = "Wait for 5 seconds."
    let {PythonShell} = require('python-shell')
    var path = require('path')
    var options = {
        scriptPath : path.join(__dirname, '/../engine/'),
        pythonPath : '/home/prabhakar/anaconda3/bin/python'

    }
    let speech = new PythonShell('Assistant.py',options)
    speech.on('message', function(message){
        swal(message);  
    }) 
}