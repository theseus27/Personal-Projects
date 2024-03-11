package au.com.anthonybruno.lichessclient.http;


import com.fasterxml.jackson.databind.JsonNode;

public interface JsonStreamProcessor {

    void processJson(JsonNode json, ResponseContext context);
}
