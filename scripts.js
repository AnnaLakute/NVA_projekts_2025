function aprekins(){
let vards = document.getElementById("vards").value;
let x = parseInt(document.getElementById('x').value); 
let y = parseInt(document.getElementById("y").value);
if (!vards.match(/^\S[a-zA-Zā-žĀ-Ž\s]*$/)){
 alert("Ievadiet vārdu ar burtiem!"); 
  return;
}
  
  if(vards == "" || isNaN(x) ||isNaN(y)){
    console.log("Jāaizpilda visi lauki!");
    alert("Jāaizpilda visi lauki!");
    return    // return vajadzīgs lai pārskata atkārtoti funkciju, citādāk turpinās rēķināt
  }
  
let z = x + y; 
console.log("logaritma vērtība: " + z);
document.getElementById("rezultats").innerText = vards + " tavs rezultāts " + x + " + " +  y + " = " + z;
}

function atnemsana(){
let vards = document.getElementById("vards").value;
  let x = parseInt(document.getElementById('x').value); 
let y = parseInt(document.getElementById("y").value);

let z = x - y; 
document.getElementById("rezultats").innerText = vards + " tavs rezultāts " + x + " - " +  y + " = " + z;
}

function reizinasana(){
let vards = document.getElementById("vards").value;
  let x = parseInt(document.getElementById('x').value); 
let y = parseInt(document.getElementById("y").value);

let z = x * y; 
document.getElementById("rezultats").innerText = vards + " tavs rezultāts " + x + " * " +  y + " = " + z;
}

function dalisana(){
let vards = document.getElementById("vards").value;
  let x = parseInt(document.getElementById('x').value); 
let y = parseInt(document.getElementById("y").value);

let z = x / y; 
document.getElementById("rezultats").innerText = vards + " tavs rezultāts " + x + " / " +  y + " = " + z;
}

window.onload = function () {
//  alert("Paziņojums");
};

/*function zimetuzcanva() {
  const canva = document.getElementById("zimejums"); //Iegūst kanvu pēc ID
  const conteksts = canva.getContext("2d"); //Iegūst 2D zīmējumu

  //Taisnstūris
  //conteksts.fillStyle = "red";
  //conteksts.fillRect(20, 20, 150, 100);

  //conteksts.strokeStyle = "pink";
 // conteksts.strokeRect(100, 10, 50, 100);

  //Aplis
  conteksts.beginPath();
  conteksts.arc(100, 200, 50, 0, 2 * Math.PI); //x,y, raduis,
  conteksts.fillStyle = "green";
  conteksts.fill();
  conteksts.lineWidth = 15;
  conteksts.strokeStyle = "black";
  conteksts.stroke();

  //Zīmēt tekstu
  conteksts.font = "30px Arial";
  conteksts.fillStyle = "orange";
  conteksts.fillText("Šveiki, Kanva", 250, 50);

  //sazīmēt līnijas

  conteksts.beginPath();
  conteksts.moveTo(50, 150);
  conteksts.lineTo(150, 400);
  conteksts.lineWidth = 10;
  conteksts.strokeStyle = "blue";
  conteksts.stroke();
}*/

function taisnsturis() {
  const canva = document.getElementById("zimejums"); //Iegūst kanvu pēc ID
  const conteksts = canva.getContext("2d"); //Iegūst 2D zīmējumu

  //Taisnstūris
  conteksts.fillStyle = "red";
  conteksts.fillRect(20, 20, 150, 100);

  conteksts.strokeStyle = "pink";
  conteksts.strokeRect(100, 10, 50, 100);
}

function aplis() {
  const canva = document.getElementById("zimejums"); //Iegūst kanvu pēc ID
  const conteksts = canva.getContext("2d"); //Iegūst 2D zīmējumu

  conteksts.beginPath();
  conteksts.arc(100, 200, 50, 0, 2 * Math.PI); //x,y, raduis,
  conteksts.fillStyle = "green";
  conteksts.fill();
  conteksts.lineWidth = 15;
  conteksts.strokeStyle = "black";
  conteksts.stroke();
}
function teksts() {
  const canva = document.getElementById("zimejums"); //Iegūst kanvu pēc ID
  const conteksts = canva.getContext("2d"); //Iegūst 2D zīmējumu

  //Zīmēt tekstu
  conteksts.font = "30px Arial";
  conteksts.fillStyle = "orange";
  conteksts.fillText("Šveiki, Kanva", 250, 50);
}

function linija() {
  const canva = document.getElementById("zimejums"); //Iegūst kanvu pēc ID
  const conteksts = canva.getContext("2d"); //Iegūst 2D zīmējumu
  //sazīmēt līnijas

  conteksts.beginPath();
  conteksts.moveTo(50, 150);
  conteksts.lineTo(150, 400);
  conteksts.lineWidth = 10;
  conteksts.strokeStyle = "blue";
  conteksts.stroke();
}

function clearall() {
  var canvas = document.getElementById("zimejums");
  var context = canvas.getContext("2d");
  context.clearRect(0, 0, canvas.width, canvas.height);
}
