package exercise;

import java.io.IOException;

public class Exercise1_4b extends Exercise{

    public Exercise1_4b(boolean isDryRun) {
        super(isDryRun);
    }

    @Override
    public void execute() throws IOException {
        /* exercise 1.4 b */
        redisDB.saveUsersFromCsv("/Users/mir/IdeaProjects/db-lab/src/main/resources/nomes-pt-2021.csv");

        redisDB.autocompleteDecreasing().forEach(System.out::println);

        redisDB.close();
    }
}
