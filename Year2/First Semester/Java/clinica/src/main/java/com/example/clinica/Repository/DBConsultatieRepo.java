package com.example.clinica.Repository;

import com.example.clinica.Domain.Consultatie;
import com.example.clinica.Domain.Sectie;

import java.sql.*;
import java.time.LocalDate;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;

public class DBConsultatieRepo implements Repository<Consultatie, Long> {
    private String url;
    private String username;
    private String password;

    public DBConsultatieRepo(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Consultatie save(Consultatie entity) {
        String query = "INSERT INTO consultatie(id, medic_id, cnp_pacient,nume_pacient,data,ora) VALUES(?, ?, ?,?,?,?)";
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement = connection.prepareStatement(query)
        ) {
            statement.setLong(1, entity.getId());
            statement.setLong(2, entity.getIdMedic());
            statement.setLong(3, entity.getCNPPacient());
            statement.setString(4, entity.getNumePacient());
            statement.setDate(5, Date.valueOf(entity.getData()));
            statement.setTime(6, Time.valueOf(entity.getOra()));
            statement.executeUpdate();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return entity;
    }

    @Override
    public Consultatie delete(Long aLong) {
        return null;
    }

    @Override
    public Consultatie findOne(Long aLong) {
        return null;
    }

    @Override
    public Consultatie update(Consultatie entity) {
        return null;
    }

    @Override
    public Iterable<Consultatie> findAll() {
        List<Consultatie> consultatii = new ArrayList<>();

        String query = "SELECT * from consultatie";
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(query);
             ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                Long id = resultSet.getLong("id");
                Long idMedic = resultSet.getLong("medic_id");
                Long cnpPacient = resultSet.getLong("cnp_pacient");
                String numePacient = resultSet.getString("nume_pacient");
                LocalDate data = resultSet.getDate("data").toLocalDate();
                LocalTime ora = resultSet.getTime("ora").toLocalTime();
                Consultatie consultatie = new Consultatie(id, idMedic,cnpPacient,numePacient,data, ora);
                consultatii.add(consultatie);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return consultatii;
    }
}
