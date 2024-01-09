package com.example.spital.repository.file;

import com.example.spital.domain.Pacient;
import com.example.spital.domain.Pat;
import com.example.spital.domain.Type;

import java.util.List;

public class PacientRepo extends AbstractFileRepo<Integer, Pacient> {
    public PacientRepo(String filename) {
        super(filename);
    }

    @Override
    public Pacient extractEntity(List<String> attr) {
        Integer id = Integer.parseInt(attr.get(0));
        Integer varsta = Integer.parseInt(attr.get(1));
        String prematur = attr.get(2);
        String diagnostic = attr.get(3);
        Integer gravitate = Integer.parseInt(attr.get(4));
        return new Pacient(id,varsta,prematur,diagnostic,gravitate);
    }

    @Override
    protected String createEntityAsString(Pacient entity) {
        return entity.getId() + ";" + entity.getVarsta() + ";" + entity.getPrematur() + ";" + entity.getDiagnostic()
                + ";" + entity.getGravitate();
    }
}
