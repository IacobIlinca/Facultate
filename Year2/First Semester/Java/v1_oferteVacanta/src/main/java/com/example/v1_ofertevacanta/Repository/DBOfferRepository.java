package com.example.v1_ofertevacanta.Repository;

import com.example.v1_ofertevacanta.Domain.SpecialOffer;

import java.sql.*;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class DBOfferRepository implements Repository<SpecialOffer, Double> {
    private String url;
    private String username;
    private String password;

    public DBOfferRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }


    @Override
    public SpecialOffer save(SpecialOffer entity) {
        return null;
    }

    @Override
    public SpecialOffer delete(Double aDouble) {
        return null;
    }

    @Override
    public SpecialOffer findOne(Double aDouble) {
        return null;
    }

    @Override
    public SpecialOffer update(SpecialOffer entity) {
        return null;
    }

    @Override
    public Iterable<SpecialOffer> findAll() {
        List<SpecialOffer> offers = new ArrayList<>();

        String query = "SELECT * from offer";
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement(query);
             ResultSet resultSet = statement.executeQuery()
        ) {
            while (resultSet.next()) {
                Double id = resultSet.getDouble("offer_id");
                Double idHotel = resultSet.getDouble("hotel_id");
                LocalDate startDate = resultSet.getDate("start_date").toLocalDate();
                LocalDate endDate = resultSet.getDate("end_date").toLocalDate();
                int percent = resultSet.getInt("percents");
                SpecialOffer specialOffer = new SpecialOffer(id, idHotel, startDate, endDate, percent);
                offers.add(specialOffer);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return offers;
    }

}
