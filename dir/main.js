// Function that display value
function dis(val) {
document.getElementById("operator").value += val
}

function myFunction(event) {
if (event.key == '0' || event.key == '1' 
    || event.key == '2' || event.key == '3'
    || event.key == '4' || event.key == '5' 
    || event.key == '6' || event.key == '7'
    || event.key == '8' || event.key == '9' 
    || event.key == '+' || event.key == '-'
    || event.key == '*' || event.key == '/')
    document.getElementById("operator").value += event.key;
}

var cal = document.getElementById("calc");
cal.onkeyup = function (event) {
if (event.keyCode === 13) {
    console.log("Enter");
    let x = document.getElementById("operator").value
    console.log(x);
    solve();
}
}

// Function that evaluates the digit and return result
function solve() {
let x = document.getElementById("operator").value
let y = math.evaluate(x)
document.getElementById("result").value +=" = "+ y
}

// Function that clear the display
function clr() {
document.getElementById("result").value = ""
}