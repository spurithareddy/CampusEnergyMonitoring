var mysql=require('mysql')
var http = require('http');
var port = process.env.PORT || 8080;
http.createServer(function(req,res)
{
}).listen(8080);
var con=mysql.createConnection({
   host:"localhost",
   user:"root",
   password:"Ponnu @123mysql",
   database:"gnits"
});

con.connect(function(err){
  if(err) throw err;
  console.log("Node connected to mysql server")
});
con.query('select * from mdata',function(err,rows,fields)
{
	if(err)throw err;
	console.log(rows[0]);
});
con.end();

