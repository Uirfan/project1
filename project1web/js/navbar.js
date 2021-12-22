function includeNavbar() {
  let aab;
 if(localStorage.getItem("userId")){

   aab='<li" class="nav-item"><a onclick="signout()" id="signOut" class="nav-link active" role="button" aria-current="page">Sign Out</a></li>'};

  document.body.innerHTML += `<nav class="navbar navbar-expand-lg navbar-dark bg-dark ">
    <div class="container-fluid ">
      <a class="navbar-brand" href="#">
        <img src="img/logo.png" width="27" height="35" alt="" loading="lazy"
      />  Clan Business Mullet</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse " id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 ">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
`+ aab +
  `
        </ul>
      </div>
    </div>
  </nav>`

}