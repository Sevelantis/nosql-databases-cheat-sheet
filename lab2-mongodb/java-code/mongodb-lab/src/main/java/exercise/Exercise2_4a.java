package exercise;

import com.mongodb.client.model.Projections;
import com.mongodb.client.model.UpdateOptions;
import com.mongodb.client.model.Updates;
import org.bson.Document;
import org.bson.conversions.Bson;

import java.io.IOException;
import java.util.Arrays;

import static com.mongodb.client.model.Filters.regex;

public class Exercise2_4a extends Exercise{
    /*Develop a simple program that allows testing insertion, editing and searching of records about the collection.*/

    public Exercise2_4a(boolean isDryRun) {
        super(isDryRun);
    }

    @Override
    public void execute() throws IOException {
        exampleDelete();
        exampleInsert();
        exampleEdit();
        exampleSearch();
    }

    public void exampleInsert() {
        var object = new Document()
                .append("opinions", Arrays.asList("very nice", "indeed"))
                .append("localidade", "Kraków")
                .append("grades", Arrays.asList("99", "88"))
                .append("restaurant_id", "123456");
        collection.insertOne(object);
    }

    public void exampleEdit(){
        var query = new Document().append("localidade", "Kraków");
        var updates = Updates.combine(
                Updates.set("localidade", "Wrocław"),
                Updates.set("restaurant_id", "654321"),
                Updates.addToSet("grades", "111"),
                Updates.addToSet("opinions", "excellente"),
                Updates.currentTimestamp("lastUpdated"));
        var options = new UpdateOptions().upsert(true);
        collection.updateOne(query, updates, options);
    }

    public void exampleSearch(){
        var projectionFields = Projections.fields(
                Projections.include("_id", "localidade", "opinions", "restaurant_id", "grades"));
        var doc = collection
                .find(regex("opinions", "excell*"))
                .projection(projectionFields)
                .first();
        System.out.println(doc);
    }

    public void exampleDelete(){
        Bson query = regex("opinions", "excell*");
        var result = collection.deleteOne(query);
        System.out.println("rows deleted: "+result.getDeletedCount());
    }
}
