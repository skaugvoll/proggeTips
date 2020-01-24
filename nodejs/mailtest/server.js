
var express = require("express"),
  bodyParser = require("body-parser"),
  nodemailer = require("nodemailer");

// setup
  var app = express();
var port = 8080;


// apply middlewear
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


// endpoint
app.get("/mail", async () => {
  var transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
           user: '',
           pass: ''
       }
   });

   const mailOptions = {
    from: 'sender@email.com', // sender address
    to: 'x@gmail.com', // list of receivers
    subject: 'Subject of your email', // Subject line
    html: '<h1>Lets go</h1><ul><li>1</li><li>2</li></ul>'// plain text body
  };

  transporter.sendMail(mailOptions, function (err, info) {
    if(err)
      console.log(err)
    else
      console.log(info);
 });


});
app.listen(port, function(req, res) {
  console.log("Server is running at port: ", port);
});






