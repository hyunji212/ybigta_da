const num = document.getElementById("number");
let number = parseInt(num.innerText);

function plus(){
  const plusbtn = document.getElementById("plusbtn"); 
  number += 1;
  num.innerText = number;

}

function extract(){
  const minusbtn = document.getElementById("minusbtn"); 
  number -= 1;
  num.innerText = number;

}

plusbtn.addEventListener("click", plus);
minusbtn.addEventListener("click", extract); 