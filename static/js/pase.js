const card = document.querySelector(".card")

// giro automático al aparecer
setTimeout(()=>{

card.classList.add("flip")

},2000)


// click para girar
card.addEventListener("click", ()=>{

card.classList.toggle("flip")

})


// hover para desktop
card.addEventListener("mouseenter", ()=>{

card.classList.add("flip")

})

card.addEventListener("mouseleave", ()=>{

card.classList.remove("flip")

})