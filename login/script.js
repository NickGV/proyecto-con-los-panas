const loginForm = document.querySelector(".login-container form");

if (loginForm) {
  loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const inputs = loginForm.querySelectorAll('input');
    const username = inputs[0].value;
    const password = inputs[1].value;

    const errorMessage = validateLoginFields(username, password);
    if (errorMessage) {
      showError(errorMessage, loginForm);
    } else {
      console.log("Login successful:", username);
    }
  });
}

function validateLogin(username, password) {
  if (username.trim().length === 0) {
    return "Please enter a username";
  }
  if (password.length === 0) {
    return "Please enter a password";
  }
  return "";
}

function validateLoginFields(username, password) {
  if (username.trim().length === 0) {
    return "Username cannot be empty";
  }
  if (password.trim().length === 0) {
    return "Password cannot be empty";
  }
  return "";
}

const registerForm = document.querySelector("#form-register");

if (registerForm) {
  registerForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const inputs = registerForm.querySelectorAll('input');
    const fullName = inputs[0].value;
    const email = inputs[1].value;
    const password = inputs[2].value;
    const confirmPassword = inputs[3].value;

    const errorMessage = validateSignUp(fullName, email, password, confirmPassword);
    if (errorMessage) {
      showError(errorMessage, registerForm);
    } else {
      console.log("Sign up successful:", fullName, email);
      // Aquí puedes agregar la lógica para enviar los datos al servidor
    }
  });
}

function validateSignUp(fullName, email, password, confirmPassword) {
  if (fullName.trim().length < 3) {
    return "Full name must be at least 3 characters long";
  }
  if (!isValidEmail(email)) {
    return "Please enter a valid email address";
  }
  if (password.length < 6) {
    return "Password must be at least 6 characters long";
  }
  if (password !== confirmPassword) {
    return "Passwords do not match";
  }
  return "";
}

function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function showError(message, form) {
  let errorDiv = form.querySelector('.error-message');
  if (!errorDiv) {
    errorDiv = document.createElement("div");
    errorDiv.className = "error-message";
    form.insertBefore(errorDiv, form.firstChild);
  }
  errorDiv.textContent = message;
  
  setTimeout(() => {
    errorDiv.remove();
  }, 3000);
}
