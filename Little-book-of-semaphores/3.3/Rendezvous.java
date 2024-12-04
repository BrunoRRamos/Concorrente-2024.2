import java.util.concurrent.Semaphore;

public class Rendezvous {
    static Semaphore mutex1 = new Semaphore(0);
    static Semaphore mutex2 = new Semaphore(0);

    public static void main(String[] args) {

        Thread threadA = new ThreadA();
        Thread threadB = new ThreadB();

        threadA.start();
        threadB.start();
    }

    static class ThreadA extends Thread {
        public void run() {
            try {
                System.out.println("action a1");
                mutex1.release();
                mutex2.acquire();
                System.out.println("action a2");
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    static class ThreadB extends Thread {
        public void run() {
            try {
                System.out.println("action b1");
                mutex2.release();
                mutex1.acquire();
                System.out.println("action b2");
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
