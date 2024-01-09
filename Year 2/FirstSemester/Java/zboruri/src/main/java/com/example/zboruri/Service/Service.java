package com.example.zboruri.Service;

import com.example.zboruri.Domain.Client;
import com.example.zboruri.Domain.Ticket;
import com.example.zboruri.Domain.Zbor;
import com.example.zboruri.Repository.DBClientRepo;
import com.example.zboruri.Repository.DBTicketRepo;
import com.example.zboruri.Repository.DBZborRepo;
import com.example.zboruri.Repository.Repository;

public class Service {
    private static Service service = null;
    private Repository<Client, String> repoClient;
    private Repository<Zbor, Long> repoZbor;
    private Repository<Ticket, Long> repoTicket;

    public synchronized static Service getInstance(DBClientRepo repoClient, DBZborRepo repoZbor, DBTicketRepo repoTicket) {
        if (service == null)
            service = new Service(repoClient, repoZbor, repoTicket);
        return service;
    }

    public Service(Repository<Client, String> repoClient, Repository<Zbor, Long> repoZbor, Repository<Ticket, Long> repoTicket) {
        this.repoClient = repoClient;
        this.repoZbor = repoZbor;
        this.repoTicket = repoTicket;
    }

    public Iterable<Client> getAllClienti() {
        return repoClient.findAll();
    }
    public Iterable<Zbor> getAllZboruri() {
        return repoZbor.findAll();
    }

}
