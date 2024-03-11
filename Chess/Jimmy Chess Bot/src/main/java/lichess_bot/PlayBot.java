// TOKEN: Gxjrxnpc7yIm59Es

package lichess_bot;

public class PlayBot {
    public static void main(String[] args) {

        String apiToken = "";
        boolean challenger = false;
        String opponent = "";
        String me = args[0];

        if (args[0].equals("maslenj5")) {
            apiToken = "Gxjrxnpc7yIm59Es";
        } else if (args[0].equals("maslenj30")) {
            apiToken = "Au2R5qzdy7i3LRTf";
            challenger = true;
            opponent = "Virutor";
        }

        new LichessBot(apiToken, me, challenger, opponent, 3000);
    }
}
