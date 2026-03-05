const canvas = document.getElementById("confetti")
const ctx = canvas.getContext("2d")

canvas.width = window.innerWidth
canvas.height = window.innerHeight

let pieces = []

for(let i=0;i<150;i++){

pieces.push({

x:Math.random()*canvas.width,
y:Math.random()*canvas.height,
size:Math.random()*6+2,
speed:Math.random()*3+1

})

}

function draw(){

ctx.clearRect(0,0,canvas.width,canvas.height)

pieces.forEach(p=>{

ctx.fillStyle = ["#ff004c","#ffffff","#ffcc00"][Math.floor(Math.random()*3)]

ctx.fillRect(p.x,p.y,p.size,p.size)

p.y += p.speed

if(p.y > canvas.height){
p.y = 0
}

})

requestAnimationFrame(draw)

}

draw()