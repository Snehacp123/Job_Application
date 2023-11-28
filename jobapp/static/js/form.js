
const form = document.getElementById("Form");
// The form elements
const firstnames = document.getElementById("firstname");
const lastnames = document.getElementById("lastname");
const phno = document.getElementById("mob");
const emailvalue = document.getElementById("email");
const givenDate1 = document.getElementById("dob");
const select_jobrole = document.getElementById("Job-role");
const select_qualification = document.getElementById("qualification");
const select_experience_year = document.getElementById("selectyearopt");
const select_experience_month = document.getElementById("selectmonthopt");

// Add an event listener to the form element. When the form is submitted, the validateFirstName, validateLastName, validatePhoneNumber, validateEmail, validateDate, validateJobrole, validateQualification, validateExperienceYear, and validateExperienceMonth functions will be called.
form.addEventListener('submit', (event) => {

    validateFirstName(event);
    validateLastName(event);
    validatePhoneNumber(event);
    validateEmail(event);
    validateDate(event);
    validateJobrole(event);
    validateQualification(event);
    validateExperienceYear(event);
    validateExperienceMonth(event);
    // Scroll to the top of the page.
    window.scrollTo(0,0);
});

// validation for firstname
function validateFirstName(event){
    if(firstnames.value.trim() === null || firstnames.value.trim() === "" ){
        document.getElementById("validateFirstName").innerHTML = "First name should not be empty"
        event.preventDefault();
        return false;
    }
    if(firstnames.value.trim().length < 3 || firstnames.value.trim().length > 25){
        document.getElementById("validateFirstName").innerHTML = "First name must be between 3 and 25 characters" ;
        event.preventDefault();
        return false;

    }else {
        document.getElementById("validateFirstName").innerHTML = ""
        return true;
    }
}
// Add an event listener to the first name input element. When the value of the input element changes, the validateFirstName function will be called.
firstnames.addEventListener('change',(event) => {
    validateFirstName(event);
});


// validation for lastname
function validateLastName(event){
    if(lastnames.value.trim() === null || lastnames.value.trim() === "" ){
        document.getElementById("validateLastName").innerHTML = "Last name should not be empty"
        event.preventDefault();
        return false;
    }
    if(lastnames.value.trim().length < 1 || lastnames.value.trim().length > 25){
        document.getElementById("validateLastName").innerHTML = "Last name must be between 1 and 25 characters" ;
        event.preventDefault();
        return false; 
    }else {
        document.getElementById("validateLastName").innerHTML = ""
        return true;
    }
}
// Add an event listener to the last name input element. When the value of the input element changes, the validateLastName function will be called.
lastnames.addEventListener('change',(event) => {
    validateLastName(event);
});

// validation for phonenumber
function validatePhoneNumber(event){   
    const phonepattern = /^\d{10}$/ ;
    if(phno.value.trim() === null || phno.value.trim() === ""){
        document.getElementById("validatePhoneNumber").innerHTML = "Phone number should not be empty";
        event.preventDefault();
        return false;
    }
    if(!phonepattern.test(phno.value.trim())){
        document.getElementById("validatePhoneNumber").innerHTML = "Please enter a 10-digit phone number";
        event.preventDefault();
        return false; 
        
    }else{
        document.getElementById("validatePhoneNumber").innerHTML = "";
        return true;
    }
}
// Add an event listener to the phonenumber input element. When the value of the input element changes, the phonenumber function will be called.
phno.addEventListener('change',(event) => {
    validatePhoneNumber(event);
});

// validation for email
function validateEmail(event){
    const emailpattern =/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/

    if(emailvalue.value.trim() === ""){
        document.getElementById("validateEmail").innerHTML = "Email should not be empty";
        event.preventDefault();
        return false;
    }if(!emailpattern.test(emailvalue.value.trim())){
            document.getElementById("validateEmail").innerHTML = "Please enter a valid email address";
            event.preventDefault();
            return false; 
    }
    else{
        document.getElementById("validateEmail").innerHTML = "";
        return true; 
    }
}
// Add an event listener to the email address input element. When the value of the input element changes, the validateEmail function will be called.
emailvalue.addEventListener('change',(event) => {
    validateEmail(event);
});


// validation for date of birth
function validateDate(event) {
    const givenDate = document.getElementById("dob").value;
    console.log("givendate=", givenDate);
    const date1 = new Date();
    console.log("date1=", date1);
    const date2 = new Date(givenDate);
    console.log("date2=", date2);
    const timeDiff = (date1 - date2) / (1000 * 60 * 60 * 24 * 365.25);
    if (timeDiff >= 18) {
        document.getElementById("validateDate").innerHTML = "";
        return true;
    }
    else {
        document.getElementById("validateDate").innerHTML = "Age must be at least 18 years old";
        event.preventDefault();
        return false;
    }
}

// Add an event listener to the date of birth input element. When the value of the input element changes, the validateDate function will be called.
givenDate1.addEventListener('change', (event) => {
    validateDate(event);

});

// validation for job role
function validateJobrole(event){
    if(select_jobrole.value === "" || select_jobrole.value === null)
    {
        document.getElementById("validatejobrole").innerHTML = "Please select a job role"
        event.preventDefault()
        return false;
    }else{
        document.getElementById("validatejobrole").innerHTML = "";
        return true;
    }

}
// Add an event listener to the job role select element. When the value of the select element changes, the validateJobrole function will be called.
select_jobrole.addEventListener('change',(event) => {
    validateJobrole(event);
});

// validation for qualification
function validateQualification(event){
    
    if(select_qualification.value === "" || select_qualification.value === null)
    {
        document.getElementById("validateQualification").innerHTML = "Please select a qualification"
        event.preventDefault()
        return false;
    }
    else{
        document.getElementById("validateQualification").innerHTML = "";
        return true;
    }
}
// Add an event listener to the Qualification select element. When the value of the select element changes, the validate Qualification function will be called.
select_qualification.addEventListener('change',(event) => {
    validateQualification(event);
});

// validation for experience in year
function validateExperienceYear(event){   
    if(select_experience_year.value === "" || select_experience_year.value === null)
    {
        document.getElementById("validateExperienceYear").innerHTML = "Please select Experience"
        event.preventDefault()
        return false;
    }
    else{
        document.getElementById("validateExperienceYear").innerHTML = "";
        return true;
    }
}
// Add an event listener to the experience select element. When the value of the select element changes, the validateexperienceyear function will be called.
select_experience_year.addEventListener('change',(event) => {
    validateExperienceYear(event);
});
// validation for experience in months
function validateExperienceMonth(event){
    
    if(select_experience_month.value === "" || select_experience_month.value === null)
    {
        document.getElementById("validateExperienceMonth").innerHTML = "Please select Experience"
        event.preventDefault()
        return false;
    }else{
        document.getElementById("validateExperienceMonth").innerHTML = "";
        return true;
    }
}
// Add an event listener to the experience month select element. When the value of the select element changes, the validateExperienceMonth function will be called.
select_experience_month.addEventListener('change',(event) => {
    validateExperienceMonth(event);
});


// This function is used to prevent the user from going back to the previous page.
function preventbackbutton()
{
    window.history.forward();
}
        // This function is called immediately after the page loads.
        setTimeout("preventbackbutton()", 0);
        window.onunload=function(){null};
