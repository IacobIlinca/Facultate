package com.example.spital.repository.memory;

import com.example.spital.domain.Entity;
import com.example.spital.domain.Pat;
import com.example.spital.repository.Repository;
import com.example.spital.utils.ConcreteObservable;
import com.example.spital.utils.events.PatEvent;

import java.util.HashMap;
import java.util.Map;

import static com.example.spital.utils.events.ChangeEvent.ADD;
import static com.example.spital.utils.events.ChangeEvent.UPDATE;

public abstract class InMemoryRepo<ID, E extends Entity<ID>> implements Repository<ID, E> {
    private Map<ID, E> entities = new HashMap<>();

    @Override
    public E findOne(ID id) throws IllegalArgumentException {
        if (id == null)
            throw new IllegalArgumentException("Id cannot be null!");
        else {
            E entity = null;
            for (E ent : entities.values()) {
                if (ent.getId().equals(id)) {
                    entity = ent;
                }
            }
            return entity;
        }
    }

    @Override
    public Iterable<E> getAll() {
        return entities.values();
    }

    @Override
    public void save(E entity) {
        if (entity == null)
            throw new IllegalArgumentException("Entity cannot be null!");
        if (entities.containsKey(entity.getId())){
            throw new IllegalArgumentException("Entity already exists!");
        }
        entities.put(entity.getId(),entity);

    }

    @Override
    public void update(E entity) {
        if (entity == null)
            throw new IllegalArgumentException("Entity cannot be null!");
        if (!entities.containsKey(entity.getId())){
            throw new IllegalArgumentException("Entity doesn t exists!");
        }
        entities.put(entity.getId(),entity);

    }

    @Override
    public void delete(ID id) {
        if (id == null)
            throw new IllegalArgumentException("Id cannot be null!");
        entities.remove(id);
    }
}
