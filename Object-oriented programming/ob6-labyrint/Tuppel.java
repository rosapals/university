public class Tuppel {
    private int y;
    private int x;

    public Tuppel(int y, int x) {
        this.y = y;
        this.x = x;
    }

    @Override
    public String toString() {
        return "(" + y+","+x + ")";
    }
}
