package com.example.v1_ofertevacanta.Repository;



import com.example.v1_ofertevacanta.Domain.Entity;

import java.util.Map;
import java.util.Optional;

public interface Repository<E, ID> {
    E save(E entity);

    E delete(ID id);

    E findOne(ID id);

    E update(E entity);

    Iterable<E> findAll();


}
