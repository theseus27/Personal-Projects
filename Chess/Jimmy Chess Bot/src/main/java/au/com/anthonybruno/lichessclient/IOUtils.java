package au.com.anthonybruno.lichessclient;

public class IOUtils {

    public static void closeQuietly(AutoCloseable closeable) {
        try {
            closeable.close();
        } catch (Exception e) {
            //Let's quietly ignore this!
        }
    }
}
