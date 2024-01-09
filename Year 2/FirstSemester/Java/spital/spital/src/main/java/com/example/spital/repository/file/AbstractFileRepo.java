package com.example.spital.repository.file;

import com.example.spital.domain.Entity;
import com.example.spital.repository.memory.InMemoryRepo;

import java.io.*;
import java.util.Arrays;
import java.util.List;

public abstract class AbstractFileRepo<ID,E extends Entity<ID>> extends InMemoryRepo<ID,E> {
    String filename;

    public AbstractFileRepo(String filename) {
        this.filename = filename;
        loadData();
    }

    private void loadData() {
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String linie;
            while ((linie = br.readLine()) != null) {
                List<String> attr = Arrays.asList(linie.split(";"));
                E e = extractEntity(attr);
                super.save((E) e);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public abstract E extractEntity(List<String> attr);
    protected  abstract String createEntityAsString(E entity);
    public void save(E entity){
        super.save((E) entity);
        writeToFile(entity);
    }
    public void delete(ID id){
        super.delete(id);
        saveAll();
    }
    public void update(E entity){
        super.update((E) entity);
        saveAll();
    }
    private void saveAll() {
        try(BufferedWriter bW = new BufferedWriter(new FileWriter(filename, false))){
            for(var entity:getAll()){
                bW.write(createEntityAsString(entity));
                bW.newLine();
            }
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    protected void writeToFile(E entity){
        try (BufferedWriter bW = new BufferedWriter(new FileWriter(filename,true))) {
            bW.write(createEntityAsString(entity));
            bW.newLine();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
