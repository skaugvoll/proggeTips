/*
Think of this as a import statement, that imports the express library
*/
var express = require('express');

/*
Create a express object from the "import"
*/
var app = express();

/*
app.METHOD("PATH", function(req,res) {what to do});
METHOD = one of the HTTP request methods (get,post,push,ect.)
PATH = a string representation of the URL path. ex. '/secondpage'
function (req,res) {what to do} = what to do when a request is sendt to path

What this does, is that it "listens" for a http - request
to the path "/" - wich is the same as "/index". but shorthand.

req = request sendt to the express server
res = the respons to be sendt from the express server.

In order to send files, we need to pass in the path to the file.
To be able to do this, we need to import the 'path'-library

We will also need to use a function called .sendFile(), and not .send()
to send a file back to the client.
.sendFile(PATHtoFile), to skip having to write out the entire file path,
we can use node.js "__dirname", "function".
__dirname can be used instead of filepath, it gets replased with the
path to the file you are writing in. and then you can concatonate
it with the missing path to your file.

*/
var path = require('path');



/*------------------Make routes-----------------*/
//make route to index
app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname + '/templates/index.html'));
});

app.get('/ellen', function(req, res) {
  res.sendFile(path.join(__dirname + '/templates/ellen.html'));
})

/*
What this does is that it starts the server, and makes it listen to
port 3000. and when it has started up, it prints to the console a msg.
*/
app.listen(3000, function() {
  console.log('Hello world server listening on port 3000!');
});
