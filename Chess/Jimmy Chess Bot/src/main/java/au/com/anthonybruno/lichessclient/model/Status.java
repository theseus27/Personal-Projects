package au.com.anthonybruno.lichessclient.model;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Status {

    private final boolean ok;

    public Status(@JsonProperty("ok") boolean ok) {
        this.ok = ok;
    }

    public boolean isOk() {
        return ok;
    }
}
