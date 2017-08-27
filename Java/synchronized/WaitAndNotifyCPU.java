/**
This tutorial will continue on the concept of Java mesa monitor and synchronized.
More specific, this will involve the keywords wait and notify.
The problem we will be using tutorial is a processor that produces and consumes processes.

What does wait do?
- wait is a metod that signals to all threads that have synchronized that this thread is waiting for a condition and needs to be woken up.

What does notfiy do?
- notify is a method that signals to all threads that have synchronized that this thread has done something and possibly satified the condition
another thread is waiting() for, and thus wakes up the thread that is waiting.


Resources:
0. https://youtu.be/gx_YUORX5vk
1. http://stackoverflow.com/questions/2536692/a-simple-scenario-using-wait-and-notify-in-java

*/
// Import necessary shit.
import java.util.Random;
import java.util.LinkedList;
import java.util.Queue;

public class WaitAndNotifyCPU {

    private Queue<Integer> cpuQueue = new LinkedList<>(); // this will be the shared resource 'processor'
    private int capacity; // number of simutaniously running processes in the cpu.

    // constructor to instansiate and give the cpu capacity bound.
    public WaitAndNotifyCPU(int capacity){
        this.capacity = capacity; // set the cpu capasity
    }

    // method to simulate a program creating and adding a new process to the cpuQueue
    public synchronized void produceProcess() {
        // check if there is free space in the queue to add a new process (condition)
        while(cpuQueue.size() == this.capacity){ // if there is no new space, let everyone know that you're waiting.
            try{
                wait(); // go to sleep and wait for a notify();
            }
            catch(InterruptedException e){
                System.out.println("Woopsies produceProcess made a no no!");
            }
        }
        // If there is space in the cpuQueue, add a new process, and then let everyone in the wait queue that there is a change,
        // so they can check their  condition
        Random randomGenerator = new Random(); // a object to create random integers.
        int process = randomGenerator.nextInt(100); // create a new random process between 0 and 99
        cpuQueue.add(process); // add the new process to the cpuQueue

        notifyAll(); // let everyone in the wait queue know that something has happend, and that they need to check their conditions.
    }

    // method to simulate the CPU consuming a process from the queue
    public synchronized void consumeProcess() {
        while(cpuQueue.size() < 1){ // check the condition. We cannot take out a process, if there is none. we have to wait.
            try{
                wait(); // there is no processes in the queue, so go to sleep and wait for a signal that something has changed.
            }
            catch(InterruptedException e){
                System.out.println("Woopsies produceProcess made a no no!");
            }
        }
        // If there is processes in the cpuQueue
        cpuQueue.remove(); // simulate that the cpu takes a process from the cpuQueue and terminates it.

        notifyAll(); // let everyone in the waiting queue, know that there has been a change, and that they need to check their conditions.
    }

    // A method to simulate diffrent programs trying to put processes into the cpu queue, and simulate the cpu using processes.
    public void simulateCPU(){
        // thread to simulate a program adding processes into the cpuQueue
        Thread p1 = new Thread(new Runnable(){
            public void run(){
                // try and add 100 new processes.
                for(int i = 0; i < 100; i++){
                    produceProcess(); // try and produce a new process or go to sleep
                }
            }
        });

        // thread to simulate a program adding processes into the cpuQueue
        Thread p2 = new Thread(new Runnable(){
            public void run(){
                // try and add 100 new processes.
                for(int i = 0; i < 100; i++){
                    produceProcess(); // try and produce a new process or go to sleep
                }
            }
        });

        // thread to simlate the cpu taking out a process and terminating it.
        Thread cpu = new Thread(new Runnable(){
            public void run(){
                // try and consume 200 processes.
                for(int i = 0; i < 200; i++){
                    consumeProcess(); // try and take out a process from the queue or go to sleep
                }
            }
        });
        // start all the threads
        p1.start();
        p2.start();
        cpu.start();

        try{
            // wait for the threads to terminate, before going further.
            p1.join();
            p2.join();
            cpu.join();
        }
        catch(InterruptedException e){
            System.out.println("Ops, something went wrong :S ");
        }
        // When all the threads have terminated.
        System.out.println("CPU queue is now empty: " + cpuQueue.size());
    }

    // standard public void main method to make the tutorial come to live!
    public static void main(String[] args){
        WaitAndNotifyCPU tutorial = new WaitAndNotifyCPU(40); // create a tutorial object
        tutorial.simulateCPU(); // run the tutorial
    }
}
