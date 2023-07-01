package exercise;

import redis.clients.jedis.Jedis;

public class Exercise1_3a extends Exercise{

    public Exercise1_3a(boolean isDryRun) {
        super(isDryRun);
    }

    @Override
    public void execute() {
        // exercise 1.3 a
        Jedis jedis = new Jedis("192.168.64.10", 6379); // external redis server (VM)
        System.out.println(jedis.ping());
        System.out.println(jedis.info());
        jedis.close();
    }
}
