package exercise;

import database.RedisDB;

public class Exercise1_3b extends Exercise{
    public Exercise1_3b(boolean isDryRun) {
        super(isDryRun);
    }

    @Override
    public void execute() {
        // exercise 1.3 b
        String[] users = { "Ana", "Pedro", "Maria", "Luis" };
        for (String user: users) {
            redisDB.saveUserSadd(RedisDB.USERS, user);
        }
        redisDB.getAllKeys().stream().forEach(System.out::println);
        redisDB.getUser().stream().forEach(System.out::println);

        redisDB.close();
    }
}
