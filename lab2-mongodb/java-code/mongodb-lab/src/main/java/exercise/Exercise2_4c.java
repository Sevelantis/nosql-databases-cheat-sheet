package exercise;

import com.mongodb.client.model.Accumulators;
import com.mongodb.client.model.Aggregates;
import com.mongodb.client.model.Projections;

import java.io.IOException;
import java.util.Arrays;

import static com.mongodb.client.model.Filters.*;

public class Exercise2_4c extends Exercise{

    public Exercise2_4c(boolean isDryRun) {
        super(isDryRun);
    }

    @Override
    public void execute() throws IOException {
        query1();
        query2();
        query3();
        query4();
        query5();
    }

    public void query1(){
//        -- 4. Enter the total number of restaurants located in the Bronx.
//        db.restaurants.find({localidade:"Bronx"}).count()
        var doc = collection
                .find(eq("localidade", "Bronx"))
                .iterator();
        int count = 0;
        while(doc.hasNext()){
            System.out.println(doc.next());
            count++;
        }
        System.out.println("Restaurants in Bronx: "+count);
    }
    public void query2(){
//        -- 8. Indicate restaurants with latitude lower than -95.7.
//        db.restaurants.find({"address.coord.0": {$lt: -95.7}}, {address: {coord:1}, nome:1, _id:0})
        var projectionFields = Projections.fields(Projections.include("address.coord", "nome", "_id"));
        var doc = collection
                .find(lt("address.coord.0", -95.7))
                .projection(projectionFields)
                .iterator();
        while(doc.hasNext()){
            System.out.println(doc.next().toJson());
        }
    }
    public void query3(){
//        -- 12. List therestaurant_id, OName, alocalityand thegastronomyrestaurants located on "Staten Island", "Queens", or "Brooklyn".
//                db.restaurants.find({ localidade: {$in:["Staten Island", "Queens", "Brooklyn"]} },
//        { restaurant_id:1, _id: 0, nome: 1, localidade: 1, gastronomia: 1})
        var projectionFields = Projections.fields(Projections.include("nome", "restaurant_id", "localidade", "gastronomia"));
        var doc = collection
                .find(in("localidade","Staten Island", "Queens", "Brooklyn"))
                .projection(projectionFields)
                .iterator();
        while(doc.hasNext()){
            System.out.println(doc.next().toJson());
        }
    }
    public void query4(){
//        -- 16. List therestaurant_id, OName, Oaddress(address) and geographic coordinates ( coordinate) of restaurants where the 2nd
//                -- element of the coordinate matrix has a value greater than 42 and less than or equal to 52.
//        db.restaurants.find({ "address.coord.1": {$gt:42, $lte:52} },
//        {restaurant_id:1, _id: 0, nome: 1, address:{coord:1}})
        var projectionFields = Projections.fields(Projections.include("nome", "restaurant_id", "address.coord"));
        var doc = collection
                .find(and(gt("address.coord.1", 42), lte("address.coord.1", 52)))
                .projection(projectionFields)
                .iterator();
        while(doc.hasNext()){
            System.out.println(doc.next().toJson());
        }
    }
    public void query5(){
//        -- 20. List all restaurants whose average score is greater than 30.
//        db.restaurants.aggregate(
//                {$unwind: "$grades"},
//        {$group: {
//            _id: "$nome",
//                    avg_score: {$avg: "$grades.score"}}},
//        {$match: {avg_score: {$gt: 30}}}
//        )
        var doc = collection
                .aggregate(
                        Arrays.asList(
                                Aggregates.unwind("$grades"),
                                Aggregates.group("$nome", Accumulators.avg("avg_score", "$grades.score")),
                                Aggregates.match(gt("avg_score", 30))
                        )
                ).iterator();
        while(doc.hasNext()){
            System.out.println(doc.next().toJson());
        }
    }
}
