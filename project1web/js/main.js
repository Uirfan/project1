
const url = "http://127.0.0.1:5000";



async function fetchReimbursements(getP,method) {
    const rqjson = {
      reimbursements: getP
    };
    let response = await fetch(url + "/reimbursement/"+ method ,{
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


async function viewReimbursement(id){
    let reimbursements = await fetchReimbursements(id,"get");
    let reimbursement = reimbursements[0] 
    document.getElementById("saveChanges").innerHTML = "";
    document.getElementById("checkReimbursements").innerHTML = `
    <ul class="list-group list-group-flush" id="reimbursementId">
    <li class="list-group-item">Reimbursement ID: `+reimbursement.reimbursementId+`</li>
    <li class="list-group-item">User ID: `+reimbursement.userId+`</li>
    <li class="list-group-item">Expense Name: `+reimbursement.expenseName+`</li>
    <li class="list-group-item">Expense Amount: `+reimbursement.expenseAmount+`</li>
    <li class="list-group-item">Expense Reason: `+reimbursement.expenseReason+`</li> 
  `;
  if(reimbursement.status ==="pending" & localStorage.getItem("isManager") === "true"){document.getElementById("checkReimbursements").innerHTML += `<li class="list-group-item"><div class="input-group mb-3">
  <label class="input-group-text" for="inputGroupSelect01">Status</label>
  <select class="form-select" id="inputGroupSelect01">
    <option selected value="accepted">Accept</option>
    <option value="rejected">Reject</option>
  </select>
</div></li>
<li class="list-group-item"><div class="mb-3">
<label for="exampleFormControlTextarea1" class="form-label">Reason</label>
<textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
</div></li>


</ul>`;
   
 document.getElementById("saveChanges").innerHTML = `<button type="button" id="saveButton" class="btn btn-primary" data-bs-dismiss="modal" onclick="updateReimbursement(`+reimbursement.reimbursementId+`);">Save</button>`;
}
 else {
  document.getElementById("checkReimbursements").innerHTML += `<li class="list-group-item">Status: `+reimbursement.status+`</li>
  <li class="list-group-item">Reject Reason: `+reimbursement.rejectReason+`</li>
  <li class="list-group-item">Status Date: `+reimbursement.statusDate+`</li> </ul>`
 }


    
}

function signout(){
  localStorage.clear();
  location.href = "index.html";
}