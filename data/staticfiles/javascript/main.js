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