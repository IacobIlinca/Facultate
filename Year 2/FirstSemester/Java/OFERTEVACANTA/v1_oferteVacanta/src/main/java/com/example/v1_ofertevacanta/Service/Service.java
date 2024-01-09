package com.example.v1_ofertevacanta.Service;

import com.example.v1_ofertevacanta.Domain.*;
import com.example.v1_ofertevacanta.Repository.*;

public class Service {
    private static Service service = null;
    private Repository<Hotel, Double> repoHotel;
    private Repository<Location, Double> repoLocation;
    private Repository<SpecialOffer, Double> repoOffer;
    private Repository<Client, Long> repoClient;
    private Repository<Reservation, Double> repoReservation;

    public synchronized static Service getInstance(DBLocationRepository repoLocation, DBHotelRepository repoHotel, DBOfferRepository repoOffer, DBClientRepository repoClient, DBReservationRepository repoReservation) {
        if (service == null)
            service = new Service(repoHotel, repoLocation, repoOffer,repoClient, repoReservation);
        return service;
    }

    public Service(Repository<Hotel, Double> repoHotel, Repository<Location, Double> repoLocation, Repository<SpecialOffer, Double> repoOffer,Repository<Client, Long> repoClient, Repository<Reservation, Double> repoReservation) {
        this.repoHotel = repoHotel;
        this.repoLocation = repoLocation;
        this.repoOffer = repoOffer;
        this.repoClient = repoClient;
        this.repoReservation = repoReservation;
    }

    public Iterable<Hotel> getAllHotels() {
        return repoHotel.findAll();
    }


    public Iterable<Location> getAllLocations() {
        return repoLocation.findAll();
    }

    public Iterable<SpecialOffer> getAllOffers() {
        return repoOffer.findAll();
    }

    public Iterable<Client> getAllClients() {
        return repoClient.findAll();
    }

    public Iterable<Reservation> getAllReservations(){
        return repoReservation.findAll();
    }

}
