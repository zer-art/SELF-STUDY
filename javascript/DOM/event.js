button = document.getElementById('button');

button.onclick = () => {
  console.log('Button clicked!');
  alert('Button clicked!');
}

const themeButton = document.getElementById('theme');

themeButton.addEventListener("click" , ()=>{
    document.body.style.backgroundColor = 'black';
    document.body.style.color = 'white';
    console.log('Theme changed!');
    alert('Theme changed!');
})
