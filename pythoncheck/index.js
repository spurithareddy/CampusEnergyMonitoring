
const express = require('express');
const app = express();



const port = process.env.PORT || 3000;
app.listen(port, function () {
  console.log('myapp listening on port ' + port);
});

const path = require('path')
const {spawn} = require('child_process')

/**
 * Run python script, pass in `-u` to not buffer console output
 * @return {ChildProcess}
 */
 app.get('/', function (req, res) {
    

function runScript(){
  return spawn('python', [
    "-u",
    path.join(__dirname, 'dataset.py'),

  ]);
}

const subprocess = runScript()

// print output of script
subprocess.stdout.on('data', (data) => {
  console.log(`data:${data}`);
  res.send(data);
});
subprocess.stderr.on('data', (data) => {
  console.log(`${data}`);
});
subprocess.on('close', () => {
  console.log("Closed");
});

 });