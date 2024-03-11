package au.com.anthonybruno.lichessclient.http;

public class ResponseException extends RuntimeException {

    private final int statusCode;
    private final String message;

    public ResponseException(int statusCode, String message) {
        super(message);
        this.statusCode = statusCode;
        this.message = message;
    }

    public int getStatusCode() {
        return statusCode;
    }

    @Override
    public String getMessage() {
        return message;
    }
}
