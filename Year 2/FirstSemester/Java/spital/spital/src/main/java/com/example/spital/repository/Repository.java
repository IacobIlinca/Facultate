package com.example.spital.repository;

import com.example.spital.domain.Entity;

public interface Repository<ID,E extends Entity<ID>> {
    E findOne(ID id) throws IllegalArgumentException;
    Iterable<E> getAll();
    void save(E entity);
    void update(E entity);
    void delete(ID id);
}
