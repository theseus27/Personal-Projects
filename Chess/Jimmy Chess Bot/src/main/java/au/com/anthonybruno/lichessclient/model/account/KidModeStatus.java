package au.com.anthonybruno.lichessclient.model.account;

import com.fasterxml.jackson.annotation.JsonProperty;

public class KidModeStatus {

    private final boolean kid;

    public KidModeStatus(@JsonProperty("kid") boolean kid) {
        this.kid = kid;
    }

    public boolean isOn() {
        return kid;
    }

    @Override
    public String toString() {
        return "KidModeStatus=" + kid;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        KidModeStatus that = (KidModeStatus) o;

        return kid == that.kid;
    }

    @Override
    public int hashCode() {
        return (kid ? 1 : 0);
    }
}
