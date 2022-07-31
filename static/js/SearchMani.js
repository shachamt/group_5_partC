const slideValue=document.querySelector("span");
const inputslider=document.querySelector("#pricerange");
inputslider.oninput=(()=>{
    let value=inputslider.value;
    slideValue.textContent=value;
    slideValue.style.left=(value/2)+"%";
    slideValue.classList.add("show");
});
inputslider.onblur =(()=>{
    slideValue.classList.remove("show");
   });