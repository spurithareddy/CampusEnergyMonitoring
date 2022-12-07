var app = require('express')();
var express= require('express');
var http = require('http').Server(app);
var io = require('socket.io')(http);
var port = process.env.PORT || 3000;
var mysql = require('mysql');
app.use(express.static(__dirname +'/public'));
app.get('/', function(req, res){
  res.sendFile(__dirname+'/microgrid.html');
});
var pool    =    mysql.createPool({
      connectionLimit   :   100,
      host              :   'localhost',
      user              :   'root',
      password          :   'Ponnu @123mysql',
      database          :   'gnits',
      debug             :   false
});

/*

console.log("connected");

var connect = mysql.createConnection({
      host:"localhost",
     database: 'gnits',
username: 'test',
password: 'check'});
var initial_result;
connect.query('select * from mdata', function(err, result) {
if(err)

    console.log(err);

 console.log("inside on");
    io.emit('changed',result);
 
});



});*/
io.on('connection',function(socket){  
    console.log("A user is connected");
   pool.getConnection(function(err,connection){
        if (err)
         console.log(err);
	 
	 
	 //new code
	 
	 connection.query("select sum(Energy) as con  from mdata ", function(err, result) {
          //console.log("inside chart meter3");    
          //console.log(result);
          io.emit('guage',result);
 
    });


connection.query("select sum(Energy) as con from mdata where meter_ID=2", function(err, result) {
          //console.log("inside chart meter3");    
          //console.log(result);
          io.emit('enm2',result);
 
    });
connection.query("select sum(Energy) as con from mdata where meter_ID=3", function(err, result) {
          //console.log("inside chart meter3");    
          //console.log(result);
          io.emit('enm3',result);
 
    }); connection.query("select sum(Energy) as con from mdata where meter_ID=4", function(err, result) {
          //console.log("inside chart meter3");    
          //console.log(result);
          io.emit('enm4',result);
 
    }); connection.query("select sum(Energy) as con from mdata where meter_ID=5", function(err, result) {
          //console.log("inside chart meter3");    
          //console.log(result);
          io.emit('enm5',result);
 
    }); connection.query("select sum(Energy) as con from mdata where meter_ID=6", function(err, result) {
          //console.log("inside chart meter3");    
          //console.log(result);
          io.emit('enm6',result);
 
    }); connection.query("select sum(Energy) as con from mdata where meter_ID=7", function(err, result) {
          //console.log("inside chart meter3");    
          //console.log(result);
          io.emit('enm7',result);
 
    }); connection.query("select sum(Energy) as con from mdata where meter_ID=8", function(err, result) {
          //console.log("inside chart meter3");    
          //console.log(result);
          io.emit('enm8',result);
 
    }); connection.query("select sum(Energy) as con from mdata where meter_ID=9", function(err, result) {
          //console.log("inside chart meter3");    
          //console.log(result);
          io.emit('enm9',result);
 
    }); connection.query("select sum(Energy) as con from mdata where meter_ID=10", function(err, result) {
          //console.log("inside chart meter3");    
          //console.log(result);
          io.emit('enm10',result);
 
    }); connection.query("select sum(Energy) as con from mdata where meter_ID=11", function(err, result) {
          //console.log("inside chart meter3");    
          //console.log(result);
          io.emit('enm11',result);
 
    });
	 
	 //here instead of 'like %00:0:00' which indicates 12 am we have to use dynamic time settings
	 //the data emitted here is present day's present time's values hence this data must be caught by realtime data meters.
connection.query("select * from mdata where tstamp like '%00:00:00'", function(err, result) {
     
          //console.log("inside on");    
          //console.log(result);
          io.emit('gnits_meter_data',result);
		  
    });
	
    //connection.query("select * from mdata where tstamp like '%-01-30%:00:00'", function(err, result) {
		
		//here conditions must be such that tstamp and the meter_ID must be the values selected by the user in "Meter Data of a Day" pagez
     connection.query("select * from mdata where meter_ID=3", function(err, result) {
          //console.log("inside chart meter data of day");    
          //console.log(result);
          io.emit('a_block_history',result);
		  
    }); 
	
	
	connection.query("select * from mdata", function(err, result) {
          //console.log("inside chart meter data of day");    
          //console.log(result);
          io.emit('meters_data',result);
		  
    }); 
	

connection.query("select * from mdata where meter_ID=2", function(err, result) {
         // console.log("inside chart meter2");    
          //console.log(result);
          io.emit('meter_2_data',result);
		  
    }); 

connection.query("select * from mdata where meter_ID=3", function(err, result) {
         // console.log("inside chart meter3");    
          //console.log(result);
          io.emit('meter_3_data',result);
		  
    }); 

connection.query("select * from mdata where meter_ID=4", function(err, result) {
         // console.log("inside chart meter4");    
          //console.log(result);
          io.emit('meter_4_data',result);
		  
    }); 

connection.query("select * from mdata where meter_ID=5", function(err, result) {
          //console.log("inside chart meter5");    
          //console.log(result);
          io.emit('meter_5_data',result);
		  
    }); 

connection.query("select * from mdata where meter_ID=6", function(err, result) {
         // console.log("inside chart meter6");    
          //console.log(result);
          io.emit('meter_6_data',result);
		  
    }); 

connection.query("select * from mdata where meter_ID=7", function(err, result) {
          //console.log("inside chart meter7");    
          //console.log(result);
          io.emit('meter_7_data',result);
		  
    }); 

connection.query("select * from mdata where meter_ID=8", function(err, result) {
          //console.log("inside chart meter8");    
          //console.log(result);
          io.emit('meter_8_data',result);
		  
    }); 

connection.query("select * from mdata where meter_ID=9", function(err, result) {
          //console.log("inside chart meter9");    
          //console.log(result);
          io.emit('meter_9_data',result);
		  
    }); 	
});

});

http.listen(port, function(){
  console.log('listening on *:' + port);
});

 
 
