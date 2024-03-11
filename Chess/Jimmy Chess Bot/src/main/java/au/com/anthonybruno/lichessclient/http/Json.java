package au.com.anthonybruno.lichessclient.http;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.JsonNodeFactory;
import com.fasterxml.jackson.databind.node.ObjectNode;

import java.io.IOException;
import java.io.InputStream;

public class Json {

    private final static ObjectMapper objectMapper = new ObjectMapper();

    public static JsonNode readJson(String json) {
        try {
            return objectMapper.readTree(json);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static JsonNode readJson(InputStream inputStream) {
        try {
            return objectMapper.readTree(inputStream);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }


    public static <T> T parseJson(InputStream inputStream, Class<T> c) {
        try {
            return objectMapper.readValue(inputStream, c);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static <T> T parseJson(JsonNode node, Class<T> c) {
        try {
            return objectMapper.treeToValue(node, c);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static ObjectNode writeObjectToJson(Object object) {
        try {
            return (ObjectNode) readJson(objectMapper.writeValueAsString(object));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static ObjectNode createJsonObject() {
        return JsonNodeFactory.instance.objectNode();
    }
}
