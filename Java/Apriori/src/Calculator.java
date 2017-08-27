import java.util.*;

/**
 * Created by skaugvoll on 28.05.2017.
 */
public class Calculator {

    private final double minSup;
    private final double support;
    private List<Point> points = new ArrayList<>();// only used once, to get the counts.
    private List<List<Point>> transactions = new ArrayList<>();
    HashMap<String, Integer> counts; // this is used through after getting the first counts.


    public Calculator(double minSup, List<List<Point>> transactions) {
        this.minSup = minSup;
        this.transactions = transactions;
        System.out.println("Number of transactions: " + this.transactions.size());
        System.out.println("MinSup: " + this.minSup);

        this.support =  this.minSup * this.transactions.size();
        System.out.println("Support: " + this.support);
    }

    private void count() {
        this.counts = new HashMap();
        for (List<Point> trans : this.transactions) {
            System.out.println(trans);
            for (Point point : trans) {
                String label = point.getName();
                if (counts.containsKey(label)) {
                    counts.put(label, counts.get(label) + 1);
                } else {
                    counts.put(label, 1);
                }
            }
        }
        this.checkSupportAndRemove();
    }


    private void checkSupportAndRemove(){
        List<String> toBeRemoved = new ArrayList<>();
        System.out.println("Before: " + this.counts);
        for(Map.Entry<String, Integer> point : this.counts.entrySet()){ // make the HashMap iterable!
            if(point.getValue() < this.support){ // check if the point does not satisfy the support
                toBeRemoved.add(point.getKey());
            }
        }
        for(String p : toBeRemoved){
            this.counts.remove(p);
        }

        System.out.println("Removed: " + toBeRemoved);
        System.out.println("Remaining: " + this.counts);
    }


    public static void main(String[] args) {
        Point A = new Point("A",3,2);
        Point B = new Point("B",4,3);
        Point C = new Point("C",5,7);
        Point D = new Point("D",6,9);
        Point E = new Point("E",6,9);
        Point F = new Point("F",6,9);
        Point G= new Point("G",6,9);
        List<List<Point>> transactions = new ArrayList<>();
        ArrayList<Point> t1 = new ArrayList<>(Arrays.asList(A,B,D,E));
        ArrayList<Point> t2 = new ArrayList<>(Arrays.asList(B,C,E,G));
        ArrayList<Point> t3 = new ArrayList<>(Arrays.asList(A,B,D));
        ArrayList<Point> t4 = new ArrayList<>(Arrays.asList(B,C,E,F,G));
        ArrayList<Point> t5 = new ArrayList<>(Arrays.asList(B,C,G));
        ArrayList<Point> t6 = new ArrayList<>(Arrays.asList(A,B,C));
        ArrayList<Point> t7 = new ArrayList<>(Arrays.asList(A,B,C,E,G));
        ArrayList<Point> t8 = new ArrayList<>(Arrays.asList(C,D,E,F));
        ArrayList<Point> t9 = new ArrayList<>(Arrays.asList(A,B,C,E,G));
        ArrayList<Point> t10 = new ArrayList<>(Arrays.asList(B,C,D,E,G));



        transactions.add(t1);
        transactions.add(t2);
        transactions.add(t3);
        transactions.add(t4);
        transactions.add(t5);
        transactions.add(t6);
        transactions.add(t7);
        transactions.add(t8);
        transactions.add(t9);
        transactions.add(t10);


        Calculator calc = new Calculator(0.5, transactions);
        calc.count();

    }


}