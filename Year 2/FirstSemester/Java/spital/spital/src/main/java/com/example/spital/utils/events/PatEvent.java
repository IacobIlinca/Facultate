package com.example.spital.utils.events;

import com.example.spital.domain.Pat;

public class PatEvent implements Event{
    private ChangeEvent type;
    private Pat pat;

    public PatEvent(ChangeEvent type, Pat pat) {
        this.type = type;
        this.pat = pat;
    }

    public ChangeEvent getType() {
        return type;
    }

    public Pat getPat() {
        return pat;
    }
}
