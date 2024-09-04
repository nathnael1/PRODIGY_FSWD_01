document.addEventListener("DOMContentLoaded", function() {
document.getElementById("fullName").addEventListener("input", function(event) { 
    localStorage.setItem("fullName",event.target.value)
})
document.getElementById("email").addEventListener("input", function(event) { 
    localStorage.setItem("email",event.target.value)
})
const fullName = localStorage.getItem("fullName");
const email = localStorage.getItem("email");
if(fullName) {
    document.getElementById("fullName").value = fullName;
}
if(email) {
    document.getElementById("email").value = email;
}

})