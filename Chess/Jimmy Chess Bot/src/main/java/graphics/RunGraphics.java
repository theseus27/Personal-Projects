
package graphics;

import engine.AIs.AlphaBeta;

public class RunGraphics {
    public static void main(String[] args) {
        System.setProperty("apple.laf.useScreenMenuBar", "true");
        System.setProperty("com.apple.mrj.application.apple.menu.about.name", "Stack");
        new View(new AlphaBeta(), false, false, 800, 600, 3500);
    }

}
