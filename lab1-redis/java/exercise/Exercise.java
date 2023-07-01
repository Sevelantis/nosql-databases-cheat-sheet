package exercise;

import database.RedisDB;
import java.io.IOException;

public abstract class Exercise {
    protected boolean isDryRun;
    protected RedisDB redisDB = new RedisDB();
    public Exercise(boolean isDryRun){
        this.isDryRun = isDryRun;
    }
    public abstract void execute() throws IOException;
    public boolean isDryRun() {
        return isDryRun;
    }
}
