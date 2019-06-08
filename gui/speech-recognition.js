function get_speech(){
    document.getElementsById("info").value = "Speak after 5 seconds"
    var python = require("python-shell")
    var path = require("path")
    var options = {
        scriptPath : path.join(__dirname, '/../engine/'),
        pythonPath : '/home/prabhakar/anaconda3/bin/python'

    }
    var speech = new python("Assistant.py",options);

    speech.end(function(err,code,message){
        swal("Click button to speak.")
        document.getElementsById("info").value = "Ready to take input again";
    }) 
}