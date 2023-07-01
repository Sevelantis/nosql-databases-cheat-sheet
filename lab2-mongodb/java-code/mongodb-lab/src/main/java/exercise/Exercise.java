package exercise;

import com.mongodb.client.MongoCollection;
import mongo.MongoDBLoader;
import org.bson.Document;

import java.io.IOException;

public abstract class Exercise {
    private final String DATABASE_NAME = "restaurants";
    private final String COLLECTION = "restaurants";
    protected boolean isDryRun;
    protected MongoCollection<Document> collection;

    public Exercise(boolean isDryRun){
        this.isDryRun = isDryRun;
        this.collection = new MongoDBLoader().getDatabase(DATABASE_NAME).getCollection(COLLECTION);
    }
    public abstract void execute() throws IOException;
    public boolean isDryRun() {
        return isDryRun;
    }
}
