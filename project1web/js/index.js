

async function createUser() {
  let userFirstName = document.getElementById("createFirstName").value;
  let userLastName = document.getElementById("createUserLastName").value;
   let userName = document.getElementById("createUserName").value; 
   let userPassword = document.getElementById("createPassword").value; 
   let userisManager = document.getElementById("createIsManager").value; 

  const userValidateJSON = {
    firstName: userFirstName,
    lastName: userLastName,
    userName: userName,
    password: userPassword,
    isManager: userisManager
  };
  let response = await fetch(url + "/user/create", {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    body: JSON.stringify(userValidateJSON),
  });
  let responseBody = await response.json();

  if (responseBody.Message == "Invalid Information") {
    alert("Invalid credentials");
  } else {
    localStorage.setItem("userId", responseBody.userId);
    localStorage.setItem("isManager", responseBody.isManager);
    localStorage.setItem("firstName", responseBody.firstName);
    localStorage.setItem("lastName", responseBody.lastName);
  
    if (responseBody.isManager) {
      location.href = "manager.html";
    } else {
      localStorage.setItem("isEmployee", "true");  
      location.href = "employee.html";
    }
  }
}
  async function fetchUsers(getP) {
    const rqjson = {
      userValidateJSON: getP
    };
    let response = await fetch(url + "/users/get", {
      method: "POST",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
      body: JSON.stringify(rqjson),
    });
    let responseBody = await response.json();
    return responseBody;
    
  }
  async function validateUser() {
    let userNameInput = document.getElementById("inputUserName").value;
    let passwordInput = document.getElementById("inputPassword").value;
  
    const userValidateJSON = {
      userName: userNameInput,
      password: passwordInput,
    };
    let response = await fetch(url + "/user/validate", {
      method: "POST",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
      body: JSON.stringify(userValidateJSON),
    });
    let responseBody = await response.json();
  
    if (responseBody.Message == "Invalid Information") {
      alert("Invalid credentials");
    } else {
      localStorage.setItem("userId", responseBody.userId);
      localStorage.setItem("isManager", responseBody.isManager);
      localStorage.setItem("firstName", responseBody.firstName);
      localStorage.setItem("lastName", responseBody.lastName);
    
      if (responseBody.isManager) {
        location.href = "manager.html";
      } else {
        localStorage.setItem("isEmployee", "true");  
        location.href = "employee.html";
      }
    }
  }

  document.getElementById("signInButton").addEventListener('click',validateUser);
