function sortTableStrCol(n){
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("table");
    switching = true;
    dir = "asc";

    while(switching){
        switching = false;
        rows = table.rows;

        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("td")[n];
            y = rows[i + 1].getElementsByTagName("td")[n];

            if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount ++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}

function sortTableIntCol(n){
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("table");
    switching = true;
    dir = "asc";

    while(switching){
        switching = false;
        rows = table.rows;

        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("td")[n];
            y = rows[i + 1].getElementsByTagName("td")[n];

            if (dir == "asc") {
                if (Math.floor(x.innerHTML) > Math.floor(y.innerHTML)) {
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (Math.floor(x.innerHTML) < Math.floor(y.innerHTML)) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount ++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}

function sortTableIntRow(n){
    var table, cols, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("table1");
    switching = true;
    dir = "asc";

    while(switching){
        switching = false;
        cols = document.getElementById("table1").rows[n].cells

        for (i = 1; i < (cols.length- 1); i++) {
            shouldSwitch = false;
            x = cols.item(i)
            y = cols.item(i+1)

            if (dir == "asc") {
                if (Math.floor(x.innerHTML) > Math.floor(y.innerHTML)) {
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (Math.floor(x.innerHTML) < Math.floor(y.innerHTML)) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            for (j=0;j<table.rows.length;j++){
                copie = table.rows[j].cells[i].innerHTML
                table.rows[j].cells[i].innerHTML = table.rows[j].cells[i+1].innerHTML;
                table.rows[j].cells[i+1].innerHTML=copie;
            }
            switching = true;
            switchcount ++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}

function sortTableStrRow(n){
    var table, cols, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("table");
    switching = true;
    dir = "asc";

    while(switching){
        switching = false;
        cols = document.getElementById("table1").rows[n].cells

        for (i = 1; i < (cols.length- 1); i++) {
            shouldSwitch = false;
            x = cols.item(i)
            y = cols.item(i+1)

            if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            cols[i].parentNode.insertBefore(cols[i+1], cols[i]);
            switching = true;
            switchcount ++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}


function sortTableStr(n,x) {
    console.log("Am intrat in sortTable");
    var table, rows, switching, i, j, x, shouldSwitch, dir, switchcount = 0, copie,idTable;
    idTable=x.parentNode.parentNode.parentNode.id;
    table = document.getElementById(idTable);
    switching = true;
  
    dir = "asc"; 
    while (switching) {
  
      switching = false;
  
      x = table.rows[n].cells
      for (i = 1 ; i < (x.length - 1); i++) {
        shouldSwitch = false;
        if (dir == "asc") {
  
          if (x[i].innerHTML.toLowerCase() > x[i+1].innerHTML.toLowerCase()) {
            shouldSwitch= true;
            break;
          }
        } else if (dir == "desc") {
          if (x[i].innerHTML.toLowerCase() < x[i+1].innerHTML.toLowerCase()) {
            shouldSwitch = true;
            break;
          }
        }
      }
      
  
      if (shouldSwitch) {
  
        //interschimbare coloane
        for (j=0;j<table.rows.length;j++){
            copie = table.rows[j].cells[i].innerHTML
            table.rows[j].cells[i].innerHTML = table.rows[j].cells[i+1].innerHTML;
            table.rows[j].cells[i+1].innerHTML=copie;
        }
  
  
        switching = true;
        switchcount ++;      
      } else {
        if (switchcount == 0 && dir == "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
  }

  function sortTableInt(n,x) {
    console.log("Am intrat in sortTable");
    var table, rows, switching, i, j, x, shouldSwitch, dir, switchcount = 0, copie,idTable;
    idTable=x.parentNode.parentNode.parentNode.id;
    table = document.getElementById(idTable);
    switching = true;
  
    dir = "asc"; 
    while (switching) {
  
      switching = false;
  
      x = table.rows[n].cells
      for (i = 1 ; i < (x.length - 1); i++) {
        shouldSwitch = false;
        if (dir == "asc") {
  
          if (x[i].innerText > x[i+1].innerText) {
            shouldSwitch= true;
            break;
          }
        } else if (dir == "desc") {
          if (x[i].innerText < x[i+1].innerText) {
            shouldSwitch = true;
            break;
          }
        }
      }
      
  
      if (shouldSwitch) {
  
        //interschimbare coloane
        for (j=0;j<table.rows.length;j++){
            copie = table.rows[j].cells[i].innerHTML
            table.rows[j].cells[i].innerHTML = table.rows[j].cells[i+1].innerHTML;
            table.rows[j].cells[i+1].innerHTML=copie;
        }
  
  
        switching = true;
        switchcount ++;      
      } else {
        if (switchcount == 0 && dir == "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
  }