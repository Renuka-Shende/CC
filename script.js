const fname = document.getElementById('fname')
const email = document.getElementById('email')
const phone = document.getElementById('phone')
const message = document.getElementById('message')
const form = document.getElementById('form')
const errorElement = document.getElementById('error')

//The Contact form array for get details from user
form.addEventListener('submit', (e) => {
    let messages =[]
    if (fname.value === '' || fname.value == null){
        messages.push('Name is required')
    }
    if (email.value === '' || email.value == null){
        messages.push('Email required')
    }
    if(phone.value.length <=8 || phone.value.length >= 11 || phone.value.length === '' || phone.value.length == null){
        messages.push('Irish phone number required (e.g 0859999999)')
    }
    if (message.value === '' || message.value == null){
        messages.push('Please leave us a message, we are happy to help.')
    }

    if(messages.length > 0){
        
        errorElement.innerText = messages.join(', ')
        e.preventDefault()
        return;

    } 
   
    
    document.getElementById("show").style.display="block";
    document.getElementById("form").style.display="none";
    
    
    
})
    