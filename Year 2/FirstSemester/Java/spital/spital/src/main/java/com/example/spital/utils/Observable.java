package com.example.spital.utils;


import com.example.spital.utils.events.Event;

public interface Observable <E extends Event>{
    void addObserver(Observer<E> observer);
    void removeObserver(Observer<E> observer);
    void notifyObservers(E event);
}
