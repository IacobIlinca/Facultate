package com.example.spital.repository.file;

import com.example.spital.domain.Pat;
import com.example.spital.domain.Type;
import com.example.spital.utils.ConcreteObservable;
import com.example.spital.utils.events.PatEvent;

import java.util.List;

public class PatRepo extends AbstractFileRepo<Integer, Pat> {
    public PatRepo(String filename) {
        super(filename);
    }

    @Override
    public Pat extractEntity(List<String> attr) {
        Integer id = Integer.parseInt(attr.get(0));
        Type tip = Type.valueOf(attr.get(1));
        String ventilatie = attr.get(2);
        Integer pacientId = Integer.parseInt(attr.get(3));
        return new Pat(id,tip,ventilatie,pacientId);
    }

    @Override
    protected String createEntityAsString(Pat entity) {
        return entity.getId()+";" + entity.getTip() + ";" + entity.getVentilatie() + ";" + entity.getPacientId();
    }
}
