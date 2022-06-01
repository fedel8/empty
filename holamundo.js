//una vez inicializado el server con
//node holamundo.js
// se puede ver desde el browser
//cargando la página http://localhost:8888/
console.log("Hola Mundo");
var http = require("http");

var chain = "holis";

function onRequest(request, response, response1) {
  console.log("Peticion Recibida.");
  response.writeHead(200, {"Content-Type": "text/html"});
  response.write("Holass Mundosss\n");
  response.write(chain);
  response.end();
//  response1.write(chain);
//  response1.end();
}

http.createServer(onRequest).listen(8888);

console.log("Servidor Iniciado.");

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("What is your name ? ", function(name) {
    rl.question("Where do you live ? ", function(country) {
        console.log(`${name}, is a citizen of ${country}`);
        chain = `${name}, is a citizen of ${country}`;
//        rl.close();
    });
});

rl.on("close", function() {
    console.log("\nBYE BYE !!!");
    process.exit(0);
});




