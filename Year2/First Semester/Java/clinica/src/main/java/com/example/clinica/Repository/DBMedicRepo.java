package com.example.clinica.Repository;

import com.example.clinica.Domain.Medic;
import com.example.clinica.Domain.Sectie;
import com.example.clinica.Domain.Tip;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DBMedicRepo implements Repository<Medic, Long> {
    private String url;
    private String username;
    private String password;

    public DBMedicRepo(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Medic save(Medic entity) {
        return null;
    }

    @Override
    public Medic delete(Long aLong) {
        return null;
    }

    @Override
    public Medic findOne(Long aLong) {
        return null;
    }

    @Override
    public Medic update(Medic entity) {
        return null;
    }

    @Override
    public Iterable<Medic> findAll() {
        List<Medic> medici = new ArrayList<>();

        String query = "SELECT * from medic";
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(query);
             ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                Long id = resultSet.getLong("id");
                Long idSectie = resultSet.getLong("id_sectie");
                String nume = resultSet.getString("nume");
                Integer vechime = resultSet.getInt("vechime");
                Tip type = Tip.valueOf(resultSet.getString("rezident"));
                Medic medic = new Medic(id,idSectie, nume, vechime, type);
                medici.add(medic);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return medici;
    }
}
