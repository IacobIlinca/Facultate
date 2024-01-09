package com.example.v1_ofertevacanta.Service;

import com.example.v1_ofertevacanta.Domain.Client;
import com.example.v1_ofertevacanta.Domain.Hotel;
import com.example.v1_ofertevacanta.Domain.Location;
import com.example.v1_ofertevacanta.Domain.SpecialOffer;
import com.example.v1_ofertevacanta.Repository.*;

public class Service {
    private static Service service = null;
    private Repository<Hotel, Double> repoHotel;
    private Repository<Location, Double> repoLocation;
    private Repository<SpecialOffer, Double> repoOffer;
    private Repository<Client, Long> repoClient;

    public synchronized static Service getInstance(DBLocationRepository repoLocation, DBHotelRepository repoHotel, DBOfferRepository repoOffer, DBClientRepository repoClient) {
        if (service == null)
            service = new Service(repoHotel, repoLocation, repoOffer,repoClient);
        return service;
    }

    public Service(Repository<Hotel, Double> repoHotel, Repository<Location, Double> repoLocation, Repository<SpecialOffer, Double> repoOffer,Repository<Client, Long> repoClient) {
        this.repoHotel = repoHotel;
        this.repoLocation = repoLocation;
        this.repoOffer = repoOffer;
        this.repoClient = repoClient;
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
}
