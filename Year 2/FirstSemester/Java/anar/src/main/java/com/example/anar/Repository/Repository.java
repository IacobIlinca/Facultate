package com.example.anar.Repository;

public interface Repository <E, ID> {
    E save(E entity);

    E delete(ID id);

    E findOne(ID id);

    E update(E entity);

    Iterable<E> findAll();

}
