window.onload = function () {
  //alert("Paziņojums");
  var navLink = document.querySelectorAll(".topnav a");
  console.log(navLink);
  navLink.forEach(function (link) {
    link.addEventListener("click", function (link) {
      navLink.forEach(function (link) {
        link.classList.remove("active");
      });
      this.classList.add("active");
    });
  });
};

function atjaunotIetvaru(which) {
  document.getElementById("lapas_saturs").innerHTML =
    "<" +
    'object id="lapas" type="text/html" data="' +
    which.href +
    '"></' +
    "object>";
}

let age = 19;
console.log(age);
if (age < 18) {
  console.log("Nepilngadīgs");
} else if (age >= 18 && age < 65) {
  console.log("Pilngadīgs");
} else {
  console.log("Seniors");
}

for (let i = 0; i < 10; i = i + 2) {
  if (i == 4 || i == 6) {
    console.log("i= četri");
  }
  console.log(i);
}

let j = 0;
while (j <= 10) {
  console.log("While rezultāts" + j);
  j++;
}

let k = 1;
do {
  console.log("DO WHILE: " + k);
  k++;
} while (k <= 10);

let skaitlis = [6, 3, 7, 5, 3, 8, 0];

let summa = 0;
for (let i = 0; i < skaitlis.length; i++) {
  summa = summa + skaitlis[i];
  console.log(i + " vērtība =" + skaitlis[i]);
}
console.log("Atbilde: " + summa);
console.log(skaitlis);

//
//Patstāvīgais darbs Nr.2
//

function collas() {
  let cl = parseInt(document.getElementById("cl").value);
  let cm = cl * 2.54;
  var teksts;
  let virsraksts = "@AnnaLākute mājas lapas konvertora rezultāts";
  let saturs = "Šis ir automātiski ģenerēts teksts!";
  let rezultats = "Jūsu šodienas iegūtais rezultāts ir ";
  let datums = new Date().toLocaleDateString("lv-LV"); // Formatēts datums latviešu valodā

  console.log("centimetros: " + cm);
  teksts = document.getElementById("rezultats2").innerText = cm;
  return `${virsraksts}\n\n${saturs}\n\n${rezultats}, ka ${cl} collas ir tik pat cik ${teksts} centimetri.\n\nIzveidots: ${datums}`;
}

function lejuplade() {
  let cl = document.getElementById("cl").value;
  if (cl === "") {
    console.log(
      "Lai varētu veikts lejuplādi, ir jāveic aprēķins ievadot collas!"
    );
    alert("Lai varētu veikts lejuplādi, ir jāveic aprēķins ievadot collas!");
    return; // return vajadzīgs lai pārskata atkārtoti funkciju, citādāk turpinās rēķināt
  }

  let datnesNosaukums = "rezultats.txt";
  let teksts = collas();
  let datne = document.createElement("a");

  //
  //
  //

  datne.setAttribute(
    "href",
    "data:text/csv;charset=utf8," + encodeURIComponent(teksts)
  );
  datne.innerText = "Lejulādēt datus";
  datne.setAttribute("download", datnesNosaukums);

  datne.style.display = "none";
  document.body.appendChild(datne);

  datne.click();

  document.body.removeChild(datne);
}

function aprekins() {
  let vards = document.getElementById("vards").value;
  let x = parseInt(document.getElementById("x").value);
  let y = parseInt(document.getElementById("y").value);
  if (!vards.match(/^\S[a-zA-Zā-žĀ-Ž\s]*$/)) {
    alert("Ievadiet vārdu ar burtiem!");
    return;
  }

  if (vards == "" || isNaN(x) || isNaN(y)) {
    console.log("Jāaizpilda visi lauki!");
    alert("Jāaizpilda visi lauki!");
    return; // return vajadzīgs lai pārskata atkārtoti funkciju, citādāk turpinās rēķināt
  }

  let z = x + y;
  console.log("logaritma vērtība: " + z);
  document.getElementById("rezultats").innerText =
    vards + " tavs rezultāts " + x + " + " + y + " = " + z;
}

function atnemsana() {
  let vards = document.getElementById("vards").value;
  let x = parseInt(document.getElementById("x").value);
  let y = parseInt(document.getElementById("y").value);

  let z = x - y;
  document.getElementById("rezultats").innerText =
    vards + " tavs rezultāts " + x + " - " + y + " = " + z;
}

function reizinasana() {
  let vards = document.getElementById("vards").value;
  let x = parseInt(document.getElementById("x").value);
  let y = parseInt(document.getElementById("y").value);

  let z = x * y;
  document.getElementById("rezultats").innerText =
    vards + " tavs rezultāts " + x + " * " + y + " = " + z;
}

function dalisana() {
  let vards = document.getElementById("vards").value;
  let x = parseInt(document.getElementById("x").value);
  let y = parseInt(document.getElementById("y").value);

  let z = x / y;
  document.getElementById("rezultats").innerText =
    vards + " tavs rezultāts " + x + " / " + y + " = " + z;
}

//window.onload = function () {
//  alert("Paziņojums");
//};

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
