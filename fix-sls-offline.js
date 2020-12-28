let fs = require('fs');
let lineNumber = 6;
let data = fs.readFileSync('node_modules/hapi/lib/defaults.js').toString().split("\n");
data.splice(lineNumber, 0, `Os.tmpDir = Os.tmpdir;`);
let text = data.join("\n");

fs.writeFile('node_modules/hapi/lib/defaults.js', text, (err) => {
  if (err) return console.log(err);
});
