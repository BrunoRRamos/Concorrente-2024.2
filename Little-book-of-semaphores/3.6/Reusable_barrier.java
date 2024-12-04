import java.util.concurrent.Semaphore;

public class Reusable_barrier {
    public static void main(String[] args) {
        int barrierSize = 4;
        Semaphore mutex = new Semaphore(1);
        Semaphore sem1 = new Semaphore(0);
        Semaphore sem2 = new Semaphore(1);
        final int[] count = {0};

        Runnable barrier = () -> {
            try {
                mutex.acquire();
                count[0]++;
                if (count[0] == barrierSize) {
                    sem1.release();
                    sem2.acquire();
                }
                mutex.release();

                sem1.acquire();
                sem1.release();

                System.out.println(Thread.currentThread().getName() + " passou pela barreira");

                mutex.acquire();
                count[0]--;
                if (count[0] == 0) {
                    sem2.release();
                    sem1.acquire();
                }
                mutex.release();
            } catch (Exception e) {
                e.printStackTrace();
            }
        };

        int totalThreads = 8;
        for (int i = 0; i < totalThreads; i++) {
            new Thread(barrier, "Thread-" + (i + 1)).start();
        }
    }
}
