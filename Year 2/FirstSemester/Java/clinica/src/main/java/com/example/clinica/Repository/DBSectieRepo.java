package com.example.clinica.Repository;

import com.example.clinica.Domain.Sectie;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DBSectieRepo implements Repository<Sectie, Long> {

    private String url;
    private String username;
    private String password;

    public DBSectieRepo(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Sectie save(Sectie entity) {
        return null;
    }

    @Override
    public Sectie delete(Long aLong) {
        return null;
    }

    @Override
    public Sectie findOne(Long aLong) {
        return null;
    }

    @Override
    public Sectie update(Sectie entity) {
        return null;
    }

    @Override
    public Iterable<Sectie> findAll() {
        List<Sectie> sectii = new ArrayList<>();

        String query = "SELECT * from sectie";
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(query);
             ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                Long id = resultSet.getLong("id");
                String nume = resultSet.getString("nume");
                Long idMedic = resultSet.getLong("sef_de_sectie");
                Float pret = resultSet.getFloat("pret_per_consultatie");
                Integer duarat = resultSet.getInt("durata_maxima_consultatie");
                Sectie sectie = new Sectie(id, nume, idMedic, pret, duarat);
                sectii.add(sectie);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return sectii;

    }
}
