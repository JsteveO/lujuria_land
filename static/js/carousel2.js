let images = [
"/static/images/todos.jpeg",
"/static/images/chicas.jpeg",
"/static/images/chicas2.jpeg",
"/static/images/diablas.jpeg",
"/static/images/bony.jpeg",
"/static/images/sal.jpeg",
"/static/images/chicas3.jpeg",
"/static/images/chicas4.jpeg"
]

let index = 0

let bgLeft = document.querySelector(".bg-left")
let bgRight = document.querySelector(".bg-right")

setInterval(() => {

    index++

    if(index >= images.length){
        index = 0
    }

    // Imagen izquierda
    bgLeft.style.backgroundImage = `
        linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
        url(${images[index]})
    `

    // Imagen derecha (puedes usar otra lógica si quieres)
    bgRight.style.backgroundImage = `
        linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
        url(${images[(index + 1) % images.length]})
    `

}, 3000)