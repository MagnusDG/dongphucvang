document.addEventListener("touchstart", function(){}, true)




/*==================== CHANGE BACKGROUND HEADER ====================*/ 
window.addEventListener('scroll',function(){
    let header=this.document.querySelector("header");
    let windowPosition = window.scrollY>0;
    header.classList.toggle("navbar_on_scrolled",windowPosition);
})
