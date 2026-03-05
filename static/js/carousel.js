
let images = [

"/static/images/lujuria1.png",
"/static/images/lujuria2.jpg",
"/static/images/lujuria3.webp"

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