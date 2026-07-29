document.addEventListener("DOMContentLoaded",function(){

console.log("Cloud Data Redundancy Removal System Loaded");

const alerts=document.querySelectorAll(".alert");

alerts.forEach(function(alert){

setTimeout(function(){

alert.classList.remove("show");

},3000);

});

});