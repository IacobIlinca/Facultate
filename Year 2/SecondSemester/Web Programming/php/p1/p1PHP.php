<?php
// Verificați dacă utilizatorul a trimis un formular de căutare
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // Preiați valorile introduse de utilizator
  $plecare = $_POST["plecare"];
  $destinatie = $_POST["destinatie"];
  $directe = isset($_POST["directe"]);

  // Realizați validările necesare pentru a preveni SQL injection
  $plecare = validateInput($plecare);
  $destinatie = validateInput($destinatie);

  // Interacționați cu baza de date pentru a obține trenurile potrivite
  $trenuri = cautaTrenuri($plecare, $destinatie, $directe);

  // Afișați rezultatele căutării
  if (!empty($trenuri)) {
    echo "<h2>Rezultate căutare trenuri:</h2>";
    echo "<table>";
    echo "<tr><th>Număr tren</th><th>Tip tren</th><th>Localitate plecare</th><th>Localitate sosire</th><th>Ora plecare</th><th>Ora sosire</th></tr>";
    foreach ($trenuri as $tren) {
      echo "<tr>";
      echo "<td>".$tren['nr_tren']."</td>";
      echo "<td>".$tren['tip_tren']."</td>";
      echo "<td>".$tren['localitate_plecare']."</td>";
      echo "<td>".$tren['localitate_sosire']."</td>";
      echo "<td>".$tren['ora_plecare']."</td>";
      echo "<td>".$tren['ora_sosire']."</td>";
      echo "</tr>";
    }
    echo "</table>";
  } else {
    echo "<p>Nu au fost găsite trenuri conform căutării.</p>";
  }
}

// Funcție pentru validarea datelor introduse de utilizator
function validateInput($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  // Poate fi adăugată orice altă validare specifică
  return $data;
}

// Funcție pentru interacțiunea cu baza de date

  function cautaTrenuri($plecare, $destinatie, $directe) {
    // Configurați conexiunea la baza de date - înlocuiți valorile aici cu cele adecvate pentru configurația dvs.
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "trenuridb";
  
    // Creează conexiunea
    $conn = new mysqli($servername, $username, $password, $dbname);
  
    // Verifică dacă există erori de conexiune
    if ($conn->connect_error) {
      die("Conexiunea la baza de date a eșuat: " . $conn->connect_error);
    }
  
    // Construiește interogarea bazată pe cerințele utilizatorului
    $sql = "SELECT * FROM trenuri WHERE localitate_plecare = ? AND localitate_sosire = ?";
    if ($directe) {
      $sql .= " AND tip_tren = 'direct'";
    }
  
    // Pregătește declarația interogării cu parametrii
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ss", $plecare, $destinatie);
  
    // Execută interogarea
    $stmt->execute();
  
    // Obține rezultatele interogării
    $result = $stmt->get_result();
  
    // Stochează rezultatele într-un array
    $trenuri = array();
    while ($row = $result->fetch_assoc()) {
      $trenuri[] = $row;
    }
  
    // Închide declarația și conexiunea la baza de date
    $stmt->close();
    $conn->close();
  
    return $trenuri;

}
?>



