let images = [

"/static/images/lujuria.jpeg",
"/static/images/todos.jpeg",
"/static/images/chicas.jpeg",
"/static/images/chicas1.jpeg",
"/static/images/chicas2.jpeg",
"/static/images/diablas.jpeg"


]

let pase = 0
let img = document.getElementById("carousel2")

setInterval(()=>{

img.style.opacity = 0

setTimeout(()=>{

pase++

if(pase >= images.length){
index = 0
}

img.src = images[pase]
img.style.opacity = 1

},500)

},3000)