//get elements
const videoEl = document.querySelector("video")
const picEl = document.querySelector(".oval")
const nav = document.querySelector("nav")

//add event listener


//add event to page
window.addEventListener("scroll", () => {
    if(window.pageYOffset > 60) {
        nav.classList.add("scrolled");
    }else{
        nav.classList.remove("scrolled")
    }
})

// adding function

function detail() {
    alert("coming soon, thank you")
}

// validation of contact form

// create a function to handle the validation
(function(){
    // use stirct to place restriction
    'use strict'

    // fetch the form from HTML page and store it in the variable form
    var forms = document.querySelectorAll(".needs-validation")

    // call the stored form using(Array.protptype.slice.call)
    Array.prototype.slice.call(forms)

    // loop over the form and prevent submission
    .forEach(function(form) {
        form.addEventListener('submit', function(event){
            if(!form.checkValidity()){
                event.preventDefault()
                event.stopPropagation()
            }
            form.classList.add('was-validated')
        },false)
        
    });
})();