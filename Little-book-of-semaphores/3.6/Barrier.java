import java.util.concurrent.Semaphore;

public class Barrier {
    public static void main(String[] args) {
        Semaphore mutex = new Semaphore(1);
        Semaphore sem1 = new Semaphore(0);
        Semaphore sem2 = new Semaphore(1);
        final int[] count = {0};
        int barrierSize = 4;

        Runnable barrier = () -> {
            try {
                mutex.acquire();
                count[0]++;
                mutex.release();

                if (count[0] == barrierSize) {
                    sem1.release();
                }

                sem1.acquire();
                sem1.release();

                System.out.println(Thread.currentThread().getName() + " passou pela barreira");

            } catch (Exception e) {
                e.printStackTrace();
            }
        };

        int totalThreads = 4;
        for (int i = 0; i < totalThreads; i++) {
            new Thread(barrier, "Thread-" + (i + 1)).start();
        }
    }
}
