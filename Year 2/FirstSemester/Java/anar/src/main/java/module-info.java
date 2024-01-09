module com.example.anar {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;

    opens com.example.anar to javafx.fxml;
    exports com.example.anar;
    exports com.example.anar.Domain;
    opens com.example.anar.Domain to javafx.base, javafx.fxml;
}