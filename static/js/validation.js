
//to show and hide the password of customer sign up

function showPassword() {
    var pass = document.getElementById("password");
    var eye1 = document.getElementById("hide1");
    var eye2 = document.getElementById("hide2");


    if (pass.type === 'password') {
        pass.type = "text";
        eye1.style.display = "inline";
        eye2.style.display = "none";
    }

    else {
        pass.type = "password";
        eye1.style.display = "none";
        eye2.style.display = "inline";
    }

}

//validation for customer sign up
const lastName = document.getElementById("lastName")
const firstName = document.getElementById("firstName")
const password = document.getElementById("password")
const formCustomer = document.getElementById("SignUpCustomerForm")
const errorMani = document.getElementById("errorCustomer")
const email = document.getElementById("email1")
const phone = document.getElementById("telephone")


formCustomer.addEventListener('submit', (e) => {
    let messages = []

    if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value))) {
        messages.push('Email is not valid')
    }

    if (firstName.value.length < 2) {
        messages.push('First name must be at least 2 characters')
    }

    if (lastName.value.length < 2) {
        messages.push('Last name must be at least 2 characters')
    }

    if (password.value.length <= 6) {
        messages.push('Password must be loger than 6 characters')
    }


    if (messages.length > 0) {
        e.preventDefault()
        errorMani.innerText = messages.join(', ')
    }

})

// // validation for editing profile page
// function updateMyProfile() {
//     // alert("Your details were updated");
//     isValidData();

// }
function checkeAllServices() {
    let services = document.getElementsByClassName('service');
    let prices = document.getElementsByClassName('price');
    for (let i = 0; i < services.length; i++) {
        if (services[i].value != '') {
            checkProperPrice(prices[i]);
        }
    }
    for (let i = 0; i < prices.length; i++) {
        if (prices[i].value != '') {
            checkProperService(services[i]);
        }
    }
}
function isValidData() {
    checkeAllServices();
    const numOfInvalid = document.getElementsByClassName('invalidInput').length;
    if (numOfInvalid > 0) {
        alert('Your details have not been updated successfully.Please fix the price list - if you are adding a service you have to add price too and the opposite');
        document.getElementsByClassName('invalidInput')[0].focus();
    }
    else {
        alert('Your details have been updated successfully ');
    }
}
function checkProperService(ServiceElement) {
    if (ServiceElement.value == '') {
        ServiceElement.className += " invalidInput";
    }
    else {
        ServiceElement.className = 'service';
    }
}


function checkProperPrice(priceElement) {
    if (priceElement.value == '') {
        priceElement.className += " invalidInput";
    }
    else {
        priceElement.className = 'price';
    }
}