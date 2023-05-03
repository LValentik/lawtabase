document.getElementById("search-button").addEventListener("click", function() {
    var query = document.getElementById("search").value;
    var quer2 = document.getElementById("legislative").value;
    console.log("You searched for: " + query + quer2);
    alert("You searched for: " + query + quer2);
  });