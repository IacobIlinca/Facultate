module com.example.examenpractic {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;

    opens com.example.examenpractic to javafx.fxml;
    exports com.example.examenpractic;
    exports com.example.examenpractic.Domain;
    opens com.example.examenpractic.Domain to javafx.base, javafx.fxml;
}