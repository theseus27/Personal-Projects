package au.com.anthonybruno.lichessclient.http;

import au.com.anthonybruno.lichessclient.IOUtils;
import com.fasterxml.jackson.databind.JsonNode;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.StatusLine;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.methods.HttpUriRequest;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class JsonClient implements AutoCloseable {

    private final CloseableHttpClient client;

    private static final Logger log = LoggerFactory.getLogger(JsonClient.class);

    public JsonClient(CloseableHttpClient httpClient) {
        this.client = httpClient;
    }

    public void getAndStream(String url, JsonStreamProcessor processor) {
        try (CloseableHttpResponse response = execute(new HttpGet(url))) {
            streamJsonResponse(response, processor);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private void streamJsonResponse(HttpResponse response, JsonStreamProcessor processor) {
        HttpEntity entity = response.getEntity();
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(entity.getContent())); //Reader will close when connection closes
            ResponseContext responseContext = new ResponseContext(true);
            while (true) {
                Thread.sleep(10);
                if (!responseContext.isRunning()) {
                    break;
                }
                String line = reader.readLine();
                if (line != null && !line.equals("")) {
                    processor.processJson(Json.readJson(line), responseContext);
                }
            }
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }

    }

    public JsonResponse get(String url) {
        return new JsonResponse(execute(new HttpGet(url)));
    }

    public JsonResponse post(String url) {
        return post(url, null);
    }

    public JsonResponse post(String url, Object body) {
        return post(url, Json.writeObjectToJson(body));
    }

    public JsonResponse post(String url, JsonNode json) {
        HttpPost httpPost = new HttpPost(url);
        if (json != null) {
            HttpEntity body = new StringEntity(json.toString(), ContentType.APPLICATION_JSON);
            httpPost.setEntity(body);
        }
        return new JsonResponse(execute(httpPost));
    }

    private CloseableHttpResponse execute(HttpUriRequest request) {
        log.info("Making request: " + request.getMethod() + " " + request.getURI());
        CloseableHttpResponse response;
        try {
            response = this.client.execute(request);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        checkResponse(response);
        return response;
    }

    private void checkResponse(CloseableHttpResponse response) {
        StatusLine statusLine = response.getStatusLine();
        log.info("Got response: " + response.getStatusLine());
        int statusCode = response.getStatusLine().getStatusCode();
        if (statusCode >= 400 && statusCode < 600) { //400 or 500 error
            IOUtils.closeQuietly(response);
            throw new ResponseException(statusCode, statusLine.getReasonPhrase());
        }
    }

    @Override
    public void close() throws Exception {
        client.close();
    }
}
