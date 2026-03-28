
let images = [

"/static/images/lujuria.jpeg",
"/static/images/mica.jpeg",
"/static/images/yepex.jpeg",
"/static/images/esteban.jpeg",
"/static/images/pao.jpeg",
"/static/images/danier.jpeg"


]

let index = 0
let img = document.getElementById("carousel")

setInterval(()=>{

img.style.opacity = 0

setTimeout(()=>{

index++

if(index >= images.length){
index = 0
}

img.src = images[index]
img.style.opacity = 1

},500)

},3000)