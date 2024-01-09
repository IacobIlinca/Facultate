module com.example.zboruri {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;

    opens com.example.zboruri to javafx.fxml;
    exports com.example.zboruri;
    exports com.example.zboruri.Domain;
    opens com.example.zboruri.Domain to javafx.base, javafx.fxml;
}