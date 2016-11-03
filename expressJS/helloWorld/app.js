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
*/
app.get('/', function(req, res) {
  res.send('Hello World!');
});

/*
What this does is that it starts the server, and makes it listen to
port 3000. and when it has started up, it prints to the console a msg.
*/
app.listen(3000, function() {
  console.log('Hello world server listening on port 3000!');
});
