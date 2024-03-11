package au.com.anthonybruno.lichessclient.http;

public class ResponseContext {

    private boolean running;

    public ResponseContext(boolean running) {
        this.running = running;
    }

    boolean isRunning() {
        return running;
    }

    public void closeResponse() {
        this.running = false;
    }
}
