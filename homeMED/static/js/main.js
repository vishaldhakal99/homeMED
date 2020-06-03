const signInBtn = document.querySelector("#signIn");
const signUpBtn = document.querySelector("#signUp");
const signInForm = document.querySelector("#signInForm");
const signUpForm = document.querySelector("#signUpForm");

signUpForm.classList.add("hidden");
signInBtn.addEventListener("click", (e) => {
  e.preventDefault();
  signUpForm.classList.add("hidden");
  signInForm.classList.remove("hidden");
});
signUpBtn.addEventListener("click", (e) => {
  e.preventDefault();
  signUpForm.classList.remove("hidden");
  signInForm.classList.add("hidden");
});
