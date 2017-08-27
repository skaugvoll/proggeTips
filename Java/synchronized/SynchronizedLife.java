
/**
* This is a Java tutorial about the Java mesa monitor which is implemented through the Java keyword synchronized.
* We want to make sure that after going through the method life, (going through life, get it?) the balance is still 0.
* I will show to examples one working, using synchronized and one that doesent work (not using synchronized).
*
* In this tutorial I have used different resources and some of the explainations are my own, and others not.
* The ones that arent mine, is because I found it online and could not explain any better my self.
* I may have altered and combined different explainations.
*
* What is synchronized ?
* Synchronized is in a very, very small nutshell: When you have two threads that are reading and writing to the same 'resource',
* say a variable named balance, you need to ensure that these threads access the variable in an atomic way. Without the synchronized keyword,
* your thread 1 may not see the change thread 2 made to balance, or worse, it may only be half changed. This would not be what you logically expect.
* Resource[0]
*
* Synchronized means that in a multi threaded environment,
* an object having synchronized method(s)/block(s) does not let two threads to access the synchronized method(s)/block(s) of code at the same time.
* This means that one thread can't read while another thread updates it.
* The second thread will instead wait until the first thread completes its execution.
* The overhead is speed, but the advantage is guaranteed consistency of data.
* Resource[0]
*
*
* How to use synchronized!
* There are two ways
* 1. synchronized block.
* 2. syncrhonized method.
*
* Synchronized block effects:
*   -  synchronized statements. Unlike synchronized methods, synchronized statements MUST SPECIFY the OBJECT that provides the intrinsic lock:
*
* Synchronized method effects:
*   - First, it is not possible for two invocations of synchronized methods on the same object to interleave.
*    When one thread is executing a synchronized method for an object, all other threads that invoke synchronized methods for the same object block (suspend execution) until the first thread is done with the object.
*   - Second, when a synchronized method exits, it automatically establishes a happens-before relationship with any subsequent invocation of a synchronized method for the same object.
*    This guarantees that changes to the state of the object are visible to all threads.
*
*
* Resources:
* 0. http://stackoverflow.com/questions/1085709/what-does-synchronized-mean
* 1. https://www.youtube.com/watch?v=UppFRatTTzs
*
*/
public class SynchronizedLife {

    private int balance = 0; // field to hold the shared resource we want to encapsulate in the monitor.

    // This method is only used for the purpose of the tutorial to reset the balance when it did not work, so that I can show that the synchronized works.
    public void resetBalance(){
        balance = 0;
    }

    // We will be needing two methods, one to add to the balance, and one to subtract from the balance. THIS is the two methods that will not work.
    public void add(){
        balance++; // equals balance = balance + 1
    }

    public void subtract(){
        balance--; // equals balance = balance - 1
    }


    // Here are the add and subtract methdos that works (using the synchronized)
    public synchronized void addInSynch(){
        balance++; // equals balance = balance + 1
    }

    public synchronized void subtractInSynch(){
        balance--; // equals balance = balance - 1
    }

    // Now we will need the method that has to threads / using the shared resource 'balance'.

    /**
    * This methods is to illustrate the NOT WORKING method and thus not getting the balance we want.
    * the reason this wont work is because the two threads can opperate and update the shared resource while the other is doing it aswell.
    * thus the values is not incremented, decremented, incremented, decremented, etc. but perhaps it is incremented, incremented, incremented, decremented, etc.
    *
    * When the useSynch flag is false,
    * The threads dosent see the other thread and updates the shared resoure just as it suites it. this means that one thread can subtract from the resouce while the other
    * thread is adding. This gives the wrong result, because if t1 tries to add 1 to the balance 50, while the other is subtracting and the other subtracted last,
    * there would be two sequential subtractions and cause the value to be off, and not becomeing 51, but 49.
    * Because of this the balance will not be correct.
    *
    * When the useSynch flag is true,
    * The treads uses methods to add and subtract from the shared resource that is synchronized on the shared resource.
    * This means that when one of the threads want to use the object to update it. It locks the object from everyone else, does it update, then unlocks.
    * This ensures that the threads doent substract when the other is adding, etc.  This means that the threads runs '1,2,1,2,1,2,1,2, etc.' Thus the values is always correct.
    */
    public void goThroughLife(boolean useSynch){
        // create the first thread that wants to use the shared resource.
        Thread t1 = new Thread(new Runnable(){
            // run is a method that is required by the Runnable interface. It's basically specifies the code that the thread will run.
            public void run(){
                // Now we want to add to the balance quite a lot. 7998 is the number of days I have lived until today (when I write this tutorial);
                for(int i = 0; i < 7998; i++){
                    if(!useSynch){ // check wether to use the working methods or not
                        add(); // not synchronized
                    }
                    else{
                        addInSynch(); // synchronized
                    }
                }
            }
        });
        // create the second thread that wants to use the shared resource.
        Thread t2 = new Thread(new Runnable(){
            // run is a method that is required by the Runnable interface. It's basically specifies the code that the thread will run.
            public void run(){
                // Now we want to add to the balance quite a lot. 7998 is the number of days I have lived until today (when I write this tutorial);
                for(int i = 0; i < 7998; i++){
                    if(!useSynch){ // check wether to use the working methods or not
                        subtract(); // not synchronized
                    }
                    else{
                        subtractInSynch(); // synchronized
                    }
                }
            }
        });

        // Now we need to start the threads so they can go to work.
        t1.start(); // start() is a method we have use to start the thread. We have only declared it until now.
        t2.start(); // start() is a method we have use to start the thread. We have only declared it until now.

        // Now we have to make sure that we doent try and print the balance before the threads are done working. If we do, the balance would most likely print 0. Which is wrong.
        try{
            t1.join(); // .join() is a method that makes the program wait until the thread has reacht it termination or is interrupted.
            t2.join(); // .join() is a method that makes the program wait until the thread has reacht it termination or is interrupted.
        }
        catch(InterruptedException e) {
            System.out.println("Oh hell na, I think I just died.."); // print this message if something bad happend, that made the program not work as it should
        }

        System.out.println("Balance is: " + balance); // statement to print the balance after the threads have run and is turminated
    }


    public static void main(String[] args){
        SynchronizedLife Tutorial = new SynchronizedLife();
        Tutorial.goThroughLife(false); // This gives almost wrong balance every time.
        Tutorial.resetBalance(); // reset the balance to check if using synchronized works.
        Tutorial.goThroughLife(true); // This will always give correct balance = 0
    }

}
