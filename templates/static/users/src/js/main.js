
const inputs = document.querySelectorAll('input[type="radio"]')
const myDiv = document.getElementById('form')

inputs.forEach(radioButton => {
    radioButton.addEventListener('change', function() {
        if (this.checked) {
            myDiv.style.display = 'block'
        }
    })
})
