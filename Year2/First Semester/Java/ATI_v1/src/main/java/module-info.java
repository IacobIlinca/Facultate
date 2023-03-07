module com.example.ati_v1 {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;

    opens com.example.ati_v1 to javafx.fxml;
    exports com.example.ati_v1;
    exports com.example.ati_v1.Domain;
    opens com.example.ati_v1.Domain to javafx.base, javafx.fxml;
}