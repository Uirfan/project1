function isEmployee() {
    if(localStorage.getItem('isEmployee') === "true" ){
        return;
    }
    else {
        location.href = "index.html";
    }
}

async function showReimbursementById(attachTo){
    document.getElementById(attachTo).innerHTML = ""
    let responseBody = await fetchReimbursements(Number(localStorage.getItem("userId")),"getByUserId");
    document.getElementById(attachTo).setAttribute("style","overflow-x:auto");
    document.getElementById(attachTo).innerHTML =
      `<table class="table table-hover"><thead>
      <tbody id="`+attachTo+`child">
       <tr>
       <th scope="col">ID</th>
       <th scope="col">User ID</th>
       <th scope="col">Expense Name</th>
       <th scope="col">Expense Amount</th>
       <th scope="col">Date</th>
       <th scope="col">Status</th>
  
       </tr>
      </tbody>
      </thead>`;
  
      for(let responses of responseBody){
        document.getElementById(attachTo+"child").innerHTML +=`
        <tr role="button" onclick="viewReimbursement(`+responses.reimbursementId+`)" data-toggle="tooltip" data-placement="top" title="Click to view" data-bs-toggle="modal" data-bs-target="#exampleModal" >
          <td scope="row">`+responses.reimbursementId+`</td>
          <td>`+responses.userId+`</td>
          <td>`+responses.expenseName+`</td>
          <td>`+responses.expenseAmount+`</td>
          <td>`+responses.date+`</td>
          <td>`+responses.status+`</td>
          </tr>`
      }
  
    }

async function createReimbursement(){

  if(Number(document.getElementById("expenseAmount").value) <= 0){
    alert("Expense Amount must be a positive number")
    return
  }
  const rqjson = {
    userId: Number(localStorage.getItem("userId")),
    expenseName: document.getElementById("expenseName").value,
    expenseReason: document.getElementById("expenseReason").value,
    expenseAmount: Number(document.getElementById("expenseAmount").value)


  };
  let response = await fetch(url + "/reimbursement/create",{
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    body: JSON.stringify(rqjson),
  });
  let responseBody = await response.json();
  showReimbursementById("tableContainer");
  return responseBody

}