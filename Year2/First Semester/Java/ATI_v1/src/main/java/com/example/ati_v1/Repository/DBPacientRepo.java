package com.example.ati_v1.Repository;

import com.example.ati_v1.Domain.Pacient;
import com.example.ati_v1.Domain.Pat;
import com.example.ati_v1.Domain.Tip;
import com.example.ati_v1.Domain.Ventilatie;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DBPacientRepo implements Repository<Pacient, String> {
    private String url;
    private String username;
    private String password;

    public DBPacientRepo(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Pacient save(Pacient entity) {
        return null;
    }

    @Override
    public Pacient delete(String s) {
        return null;
    }

    @Override
    public Pacient findOne(String s) {
        return null;
    }

    @Override
    public Pacient update(Pacient entity) {
        return null;
    }

    @Override
    public Iterable<Pacient> findAll() {
        List<Pacient> pacienti = new ArrayList<>();

        String query = "SELECT * from pacient";
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query);
            ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                String CNP = resultSet.getString("cnp");
                Integer varsta = resultSet.getInt("varsta");
                Ventilatie prematur = Ventilatie.valueOf(resultSet.getString("prematur"));
                String diagnostic_principal = resultSet.getString("diagnostic_principal");
                Integer gravitate = resultSet.getInt("gravitate");

                Pacient pacient=new Pacient(CNP,varsta,prematur,diagnostic_principal,gravitate);
                pacienti.add(pacient);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return pacienti;
    }

}
