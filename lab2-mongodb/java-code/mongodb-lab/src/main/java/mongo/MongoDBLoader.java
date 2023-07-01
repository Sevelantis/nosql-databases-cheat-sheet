package mongo;

import com.mongodb.ConnectionString;
import com.mongodb.MongoClientSettings;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoDatabase;

public class MongoDBLoader {
    private final String HOST = "192.168.64.10";
    private final String PORT = "27017";
    private final String URI = "mongodb://"+HOST+":"+PORT+"/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.0";

    public MongoClient getClient(){
        MongoClientSettings settings =
                MongoClientSettings.builder()
                        .applyConnectionString(new ConnectionString(URI))
                        .addCommandListener(new CommandCounter())
                        .build();
        return MongoClients.create(settings);
    }

    public MongoDatabase getDatabase(String databaseName){
        return getClient().getDatabase(databaseName);
    }
}
