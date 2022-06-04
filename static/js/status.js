window.onload = showPercentage();

function showPercentage(){
    var receivedVal = document.getElementById("receivedVal").innerHTML;
    confirm(receivedVal);
}


function greet(){
    const greets = ["Hello there,", "Welcome back,","Hola, "];

    const random = Math.floor(Math.random() * months.length);
    // greet_it = (random, months[random]);

    document.getElementById("name").innerHTML = "<p> + greets[random] + </p>";

}