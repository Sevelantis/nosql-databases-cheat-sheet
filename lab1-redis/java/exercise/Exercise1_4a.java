package exercise;

import database.RedisDB;

import java.util.Scanner;

public class Exercise1_4a extends Exercise{
    public Exercise1_4a(boolean isDryRun) {
        super(isDryRun);
    }

    @Override
    public void execute() {
        /* exercise 1.4 a */
        redisDB.saveUsersFromTxt("/Users/mir/IdeaProjects/db-lab/src/main/resources/names.txt");

        Scanner scanner = new Scanner(System.in);
        System.out.println("Search for ('Enter' for quit): ");
        String line = scanner.nextLine();

        redisDB.autocomplete(line).forEach(System.out::println);

        redisDB.close();
    }
}
