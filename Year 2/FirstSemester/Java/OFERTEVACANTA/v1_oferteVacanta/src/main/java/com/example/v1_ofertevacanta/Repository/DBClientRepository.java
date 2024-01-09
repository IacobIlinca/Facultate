package com.example.v1_ofertevacanta.Repository;

import com.example.v1_ofertevacanta.Domain.Client;
import com.example.v1_ofertevacanta.Domain.Hobby;

import java.sql.*;

public class DBClientRepository implements Repository<Client, Long> {
    private String url;
    private String username;
    private String password;

    public DBClientRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Client save(Client entity) {
        return null;
    }

    @Override
    public Client delete(Long aLong) {
        return null;
    }

    @Override
    public Client findOne(Long aLong) {
        String query = "SELECT * FROM client WHERE id_client=?";
        Client client = null;
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(query)
        ) {
            statement.setLong(1, aLong);
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                String nameClient = resultSet.getString("client_name");
                int fidelityGrade = resultSet.getInt("fidelity_grade");
                int age = resultSet.getInt("age");
                Hobby hobby= Hobby.valueOf(resultSet.getString("hobby"));
                client=new Client(aLong,nameClient,fidelityGrade,age,hobby);
                client.setId(aLong);
            }


        } catch (SQLException e) {
            e.printStackTrace();
        }
        return client;
    }

    @Override
    public Client update(Client entity) {
        return null;
    }

    @Override
    public Iterable<Client> findAll() {
        return null;
    }
}
