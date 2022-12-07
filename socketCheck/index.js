var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var port = process.env.PORT || 8080;
var mysql = require('mysql');
app.get('/', function(req, res){
  res.sendFile( 'C:/Users/Siri/Sample_codes/socketCheck/index.html');
});


   


io.on('connection', function(socket){


	/*var connect = mysql.createConnection({
      database: 'gnits',
	  username: 'root',
     password: 'Ponnu @123mysql'});
	var initial_result;
	 connect.query('select * from mdata', function(err, result) {
		 if(err)

    console.log(err);	*/	
   socket.emit('changed',"hi"); 

    });



});

http.listen(port, function(){
  console.log('listening on *:' + port);
});
