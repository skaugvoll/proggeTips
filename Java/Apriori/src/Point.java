/**
 * Created by skaugvoll on 28.05.2017.
 */
public class Point {

    private final String name;
    private final int x;
    private final int y;

    public Point(String name, int x, int y){
        this.name = name;
        this.x = x;
        this.y = y;
    }

    public String getName(){
        return this.name;
    }

    public int getX(){
        return this.x;
    }

    public int getY(){
        return this.y;
    }

    public String toString(){
        return getName();
    }
}
