

function funkcija() {
    document.write("Viss")
}

function raadiChatu(dati){
    var jaunaRinda="<br/>"
    var chats = "";
    var vieta = document.getElementById("chats")
    for(var rinda of dati["chats"]){
        chats+=rinda+jaunaRinda
    }
    vieta.innerHTML=chats
}

async function lasi(){
    const atbilde = await fetch("/chats/lasi")
    const datuObj = await atbilde.json()
    raadiChatu(datuObj)
    await new Promise(resolve => setTimeout(resolve,5000))
    await lasi()
}

async function suuti(){ 
    name = document.getElementById("name").value
    zinjasElem = document.getElementById("zinja")
    zinja = zinjasElem.value
  if(zinja ==  "") {return};
    zinjasElem.value=""
    const atbilde = await fetch("/chats/suuti", { 
        method:'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({"chats":name + " : " + zinja})
    })
    const datuObj = await atbilde.json()
    raadiChatu(datuObj)
}


document.getElementById("zinja").addEventListener("keyup",function(event){
  if (event.keyCode==13){suuti();}
})