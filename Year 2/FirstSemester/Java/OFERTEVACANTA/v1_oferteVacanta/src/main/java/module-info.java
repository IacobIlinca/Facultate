module com.example.v1_ofertevacanta {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;

    opens com.example.v1_ofertevacanta to javafx.fxml;
    exports com.example.v1_ofertevacanta;
    exports com.example.v1_ofertevacanta.Domain;
    opens com.example.v1_ofertevacanta.Domain to javafx.base, javafx.fxml;
}