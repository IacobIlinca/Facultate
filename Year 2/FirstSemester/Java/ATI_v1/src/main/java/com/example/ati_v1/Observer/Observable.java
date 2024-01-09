package com.example.ati_v1.Observer;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Observable {
    private List<Observer> observerList = new ArrayList<>();

    public void addObserver(Observer obs){
        observerList.add(obs);
    }
    public void removeObserver(Observer obs){
        observerList.remove(obs);
    }

    public List<Observer> getObserverList(){
        return observerList;
    }

    protected void notification() throws IOException {
        for(Observer obs : observerList){
            obs.update();
        }
    }
}

