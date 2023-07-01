package exercise;

import com.mongodb.client.model.Accumulators;
import com.mongodb.client.model.Aggregates;
import com.mongodb.client.model.Projections;

import java.io.IOException;
import java.util.*;

import static com.mongodb.client.model.Filters.*;

public class Exercise2_4d extends Exercise {

    public Exercise2_4d(boolean isDryRun) {
        super(isDryRun);
    }

    @Override
    public void execute() {
        System.out.println("Number of different locations: " + countLocalities());
        System.out.println("Number of restaurants by location:: " + countRestByLocality());
        String name = "Park";
        System.out.println("Name of restaurants containing " + name + " in the name: " + getRestWithNameCloserTo(name));
    }

    public int countLocalities() {
        var doc = collection
                .aggregate(
                        Arrays.asList(
                                Aggregates.group("$localidade", Accumulators.sum("amount", 1)),
                                Aggregates.group("null", Accumulators.sum("different", 1))
                        )
                ).iterator();
        int different = -1;
        while (doc.hasNext()) {
            var d = doc.next();
            different = d.getInteger("different");
            System.out.println(d.toJson());
        }
        return different;
    }

    Map<String, Integer> countRestByLocality(){
        var doc = collection
                .aggregate(
                        Arrays.asList(
                                Aggregates.group("$localidade", Accumulators.sum("amount", 1))
                        )
                ).iterator();
        Map<String, Integer> map = new HashMap();
        while (doc.hasNext()) {
            var next = doc.next();
            var locality = next.getString("_id");
            var amount = next.getInteger("amount");
            map.put(locality, amount);
        }
        return map;
    }

    List<String> getRestWithNameCloserTo(String name){
        var doc = collection
                .find(regex("nome", name))
                .iterator();

        var names = new ArrayList<String>();
        while(doc.hasNext()){
            var next = doc.next();
            var nome = next.getString("nome");
            names.add(nome);
        }
        return names;
    }
}
