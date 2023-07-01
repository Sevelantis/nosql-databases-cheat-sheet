package exercise;

import com.mongodb.client.model.Indexes;

import java.io.IOException;

public class Exercise2_4b extends Exercise{
//    Create indexes: one for "localidade"; another for "gastronomia"; and a text one for the
//    "nome". Use surveys to test health and verify performance (as there are few
//            documents, the results may not improve).
    public Exercise2_4b(boolean isDryRun) {
        super(isDryRun);
    }

    @Override
    public void execute() throws IOException {
        createIndexes();
    }

    public void createIndexes(){
        System.out.println(collection.createIndex(Indexes.ascending("localidade")));
        System.out.println(collection.createIndex(Indexes.ascending("nome")));
        System.out.println(collection.createIndex(Indexes.ascending("gastronomia")));
    }

}
