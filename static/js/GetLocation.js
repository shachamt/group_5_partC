function GetLocation() {
    if (navigator.geolocation) {
        console.log("in get location");
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        document.getElementById("p").innerHTML = "Geolocation is not supported by this browser.";
    }
}


function showPosition(position) {
    var x = document.getElementById("p");
    var y = document.getElementById("locate");
    x.innerHTML = "Your In <br>" + "Latitude: " + position.coords.latitude +
        "<br>Longitude: " + position.coords.longitude;
    y.innerHTML = "try me again";
    console.log(position);
}
 //get location for manicutrist sign up
function GetLocationMani() {
    if (navigator.geolocation) {
        console.log("in get location");
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        document.getElementById("p1").innerHTML = "Geolocation is not supported by this browser.";
    }
}

//writes the position in the form
function showPosition(position) {
    var x = document.getElementById("p1");
    var y = document.getElementById("buttonLocationMani");
    console.log(position);
    document.getElementById("Latitude").value = position.coords.latitude;
    document.getElementById("Longitude").value = position.coords.longitude;

}

function sandMani() {
    alert("Your details have been sent to the manicurist and she will contact you in the next 12 hours");
}


//to show and hide the password of manicurist sign up
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

//validation for manicurist sign up
    const lastName = document.getElementById("lastName")
    const firstName = document.getElementById("firstName")
    const password = document.getElementById("password")
    const formMani = document.getElementById("SignUpManicuristForm")
    const errorMani = document.getElementById("errorMani")
    const email = document.getElementById("email")
    const phone = document.getElementById("telephone")

    formMani.addEventListener('submit', (e) => {
        let messages = []

        if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value))) {
        messages.push ('Email is not valid')
        }

        if(firstName.value.length <2) {
            messages.push ('First name must be at least 2 characters')
        }

        if(lastName.value.length <2) {
            messages.push ('Last name must be at least 2 characters')
        }

        if(password.value.length <=6) {
            messages.push ('Password must be loger than 6 characters')
        }


        if (messages.length>0) {
            e.preventDefault()
            errorMani.innerText = messages.join (', ')
        }

    })

