function isManager() {
    if(localStorage.getItem('isManager') ===  "true"){
        return;
    }
    else {
        location.href = "index.html";
    }
}

async function Stats(){
    let accepted = await fetchReimbursements("accepted","get");
    let rejected =await fetchReimbursements("rejected","get");
    let pending = await fetchReimbursements("pending","get");

    function maxAmount(res){
      let amount = 0
      for(let data of res){
        if( amount < data.expenseAmount){
          amount =  data.expenseAmount
        }
      
      }
      return amount
    }

    function getAmount(args){
      let amount = Number(0);
     for(let data of args){
         amount += Number(data.expenseAmount);   
    }
    return amount;
   }
 
    document.getElementById("stats").innerHTML += `
    <h3>Statistics</h3> 
    <div id="viewStats" class="row">
    <div class="col">
    <div class="card" style="width: 18rem;">
    <ul class="list-group list-group-flush">
      <li class="list-group-item">Accepted: ` + accepted.length +`</li>
      <li class="list-group-item">Rejected: ` + rejected.length+`</li>
      <li class="list-group-item">Pending: ` + pending.length +`</li>
    </ul>
  </div>
    </div>
    <div class="col">
    <div class="alert alert-success" role="alert">
    <h6>Accepted Amount:<h6>
  <h1>$`+ getAmount(accepted) + `<h1>
 </div>
    </div>
    <div class="col">
    <div class="alert alert-danger" role="alert">
    <h6>Rejected Amount:<h6>
    <h1>$`+getAmount(rejected)+`<h1>
  </div>
    </div>
    <div class="col">
    <div class="alert alert-info" role="alert">
    <h6>Pending Amount:<h6>
    <h1>$`+getAmount(pending)+`<h1>
  </div>
    </div>
  </div>
  <div class="row"> <div class="col">
  <div class="alert alert-dark" role="alert">
  <h6>Highest Accepted Expense:<h6>
<h1>$`+ maxAmount(accepted) + `<h1>
</div> <div class="alert alert-dark" role="alert">
<h6>Highest Rejected Expense:<h6>
<h1>$`+ maxAmount(rejected) + `<h1>
</div></div>
  `}

  async function viewReimbursements(getP,attachTo) {
    document.getElementById(attachTo).innerHTML = ""
   let responseBody = await fetchReimbursements(getP,"get");
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

   
async function updateReimbursement(id){
    {
      const rqjson = {
        reimbursementId: id,
        status: document.getElementById("inputGroupSelect01").value,
        rejectReason: document.getElementById("exampleFormControlTextarea1").value,
      };
    
      let response = await fetch(url + "/reimbursement/update", {
        method: "POST",
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
        },
        redirect: "follow",
        body: JSON.stringify(rqjson),
      });
      let responseBody = await response.json();
      viewReimbursements("pending","tableContainer")
    }
  }
  