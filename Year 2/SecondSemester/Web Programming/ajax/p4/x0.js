var playerTurn = true; // Variabilă care indică rândul jucătorului

// Funcție care se apelează când se face click pe o celulă din tabel
function cellClicked(row, col) {
    var cell = $("table tr:eq(" + row + ") td:eq(" + col + ")"); // Găsește celula pe care s-a făcut click
    if (cell.text() == "") { // Verifică dacă celula este goală
        if (playerTurn) { // Dacă este rândul jucătorului
            cell.text("X"); // Adaugă X în celulă
            sendMove(row, col); // Trimite mutarea la server
        }
        playerTurn = !playerTurn; // Schimbă rândul jucătorului
    }
}

// Funcție care trimite mutarea la server
function sendMove(row, col) {
    $.ajax({
        url: "http://localhost/server.php", // Adresa scriptului PHP care gestionează mutările
        type: "POST",
        data: { row: row, col: col }, // Datele care trebuie trimise la server
        dataType: "json",
        success: function(response) {
            if (response.gameover) { // Dacă jocul s-a terminat
                showMessage(response.message); // Afișează un mesaj corespunzător
            } else { // Dacă jocul nu s-a terminat
                var cell = $("table tr:eq(" + response.row + ") td:eq(" + response.col + ")"); // Găsește celula în care trebuie să facă mutarea calculatorul
                cell.text("0"); // Adaugă 0 în celulă
                playerTurn = !playerTurn; // Schimbă rândul jucătorului
            }
        }
    });
}

// Funcție care afișează un mesaj
function showMessage(message) {
    swal({
        title: message,
        icon: "info",
        button: "OK",
    }).then(() => {
        location.reload(); // Reîncarcă pagina pentru a începe un nou joc
    });
}
