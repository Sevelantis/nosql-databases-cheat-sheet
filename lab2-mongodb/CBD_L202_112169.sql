-- NMEC: 112169
-- the files have .sql extension instead of .txt because of syntax highlitghing in VSCode.

-- 1. List all documents in the collection.
db.restaurants.find()

-- 2. Display the fieldsrestaurant_id,Name,localityandgastronomyfor all documents in the collection.
db.restaurants.find({},{restaurant_id:1,nome:1,localidade:1,gastronomia:1})

-- 3. Present the fieldsrestaurant_id,Name,localityand postal code (ZIP code), but delete the field_idof all documents in the collection.
db.restaurants.find({},{restaurant_id:1,nome:1,localidade:1,address:{zipcode:1},_id:0})

-- 4. Enter the total number of restaurants located in the Bronx.
db.restaurants.find({localidade:"Bronx"}).count()
309

-- 5. List the top 15 restaurants located in the Bronx, sorted in ascending order of name.
db.restaurants.find({localidade:"Bronx"}).sort({nome:1}).limit(15)

-- 6. List all restaurants that have at least onescorehigher than 85.
db.restaurants.find({"grades.score": {$gt: 85} })

-- 7. Find the restaurants that scored one or more scores (score) between [80 and 100].
db.restaurants.find({"grades": {$elemMatch: {score: {$gt: 80, $lt: 100} }} })

-- 8. Indicate restaurants with latitude lower than -95.7.
db.restaurants.find({"address.coord.0": {$lt: -95.7}}, {address: {coord:1}, nome:1, _id:0})

-- 9. Indicate the restaurants that do not have gastronomy"American", had a (or more) score greater than 70 and are at a latitude less than -65.
db.restaurants.find( {
    $and:[
        {"grades.score": {$gt:70}},
        {"gastronomia":{$not:{$regex:"American"}}},
        {"address.coord.0":{$lt:-65}}
        ]},
        { grades: { score: 1 }, _id: 0, nome: 1, gastronomia: 1 })


-- 10. List therestaurant_id, OName, alocalityandgastronomyof restaurants whose name starts with "Wil".
db.restaurants.find({nome:{$regex:"^Wil"}},
        { restaurant_id: 1, _id: 0, nome: 1, localidade: 1 })

-- 11. List theName, alocalityand thegastronomyof the restaurants that belong to the Bronx and whosegastronomyis of the "American" or "Chinese" type.
db.restaurants.find({ localidade: "Bronx", gastronomia: {$in:["American", "Chinese"]} },
        { _id: 0, nome: 1, localidade: 1, gastronomia: 1})

-- 12. List therestaurant_id, OName, alocalityand thegastronomyrestaurants located on "Staten Island", "Queens", or "Brooklyn".
db.restaurants.find({ localidade: {$in:["Staten Island", "Queens", "Brooklyn"]} },
        { restaurant_id:1, _id: 0, nome: 1, localidade: 1, gastronomia: 1})

-- 13. List theName, alocality, Oscoreandgastronomyof the restaurants that always achieved scores lower than or equal to 3.
db.restaurants.find({ "grades.score": {$not:{$gt:3}} },
        {_id: 0, nome: 1, localidade: 1, gastronomia: 1, grades:{score: 1} })

-- 14. List theNameand the reviews of the restaurants that obtained a rating with a grid "a", ascore10 on the date "2014-08-11T00: 00: 00Z" (ISODATE).
db.restaurants.find({$and:[
        {"grades.grade": 'A'},
        {"grades.score": 10},
        {"grades.date": ISODate("2014-08-11T00:00:00Z")},
        ]},
        {_id: 0, nome: 1, localidade: 1, gastronomia: 1, grades:1})



-- 15. List therestaurant_id, ONameand thescoreof the restaurants in which the second evaluation was grade "A" and occurred on ISODATE "2014-08-11T00:00:00Z".
db.restaurants.find({$and:[
        {"grades.grade": 'A'},
        {"grades.date": ISODate("2014-08-11T00:00:00Z")}
        ]},
        {_id: 0, nome: 1, localidade: 1, gastronomia: 1, grades:{grade:1, date:1}})

-- 16. List therestaurant_id, OName, Oaddress(address) and geographic coordinates ( coordinate) of restaurants where the 2nd 
-- element of the coordinate matrix has a value greater than 42 and less than or equal to 52.
db.restaurants.find({ "address.coord.1": {$gt:42, $lte:52} },
        {restaurant_id:1, _id: 0, nome: 1, address:{coord:1}})

-- 17. Listname, cuisine and locationof all restaurants in ascending order of gastronomy and second, in descending order of locality.
db.restaurants.find({}, {restaurant_id:1, _id: 0, nome: 1, gastronomia:1, localidade:1}).sort({ gastronomia:1, localidade: -1 })

-- 18. ListName,locality, grid and gastronomy of all restaurants located in Brooklyn that do not include gastronomy "American" and obtained a rating (grid) "A". You must present them in descending order ofgastronomy.
db.restaurants.find({$and:[
        {localidade: "Brooklyn"},
        {gastronomia: {$not:{$regex:"American"}}},
        {"grades.grade":'A'}
        ]},
        {grades:{grade:1}, _id: 0, nome: 1, gastronomia:1, localidade:1}).sort({ gastronomia:1, localidade: -1 }).sort({gastronomia:-1})
        
-- 19. Count the total number of restaurants in each location.
db.restaurants.aggregate({
        $group: {
            _id: "$localidade",
            how_many: {$sum: 1}
        }})

-- 20. List all restaurants whose average score is greater than 30.
db.restaurants.aggregate(
        {$unwind: "$grades"},
        {$group: {
                _id: "$nome",
                avg_score: {$avg: "$grades.score"}}},
        {$match: {avg_score: {$gt: 30}}}
        )

db.restaurants.aggregate(
        {$addFields: {
                avg_score: {$avg: "$grades.score"}}},
        {$match: {avg_score: {$gt: 30}}}
        )

-- 21. Indicate the restaurants that have gastronomy "Portuguese", the sum ofscoreis greater than 50 and are at a latitude less than -60.
db.restaurants.aggregate(
        {$match: {$and:[
                {gastronomia: "Portuguese"},
                {"address.coord.0":{$lt:-60.0}}
                ]}},
        {$unwind: "$grades"},
        {$group: {
                _id: "$nome",
                summed_score: {$sum: "$grades.score"}}},
        {$match: {summed_score: {$gt: 50.0}}}
        )

-- 22. Provide the name and score of the 3 restaurants with the highest average score.
db.restaurants.aggregate(
        {$unwind: "$grades"},
        {$group: {
                _id: "$nome",
                avg_score: {$avg: "$grades.score"}}},
        {$sort: {avg_score: -1}},
        {$limit: 3}
        )

-- 23. Display the number of different restaurants on "Fifth Avenue" street
db.restaurants.aggregate(
        {$match: {"address.rua": "Fifth Avenue"}},
        {$group: {
                _id: "$nome",
                amount: {$sum: 1}}},
        {$group: {
                _id: null,
                total_amount: {$sum: "$amount"}
        }}
        )

-- 24. Count how many restaurants there are per street and order in descending order
db.restaurants.aggregate(
        {$group: {
                _id: "$address.rua",
                amount: {$sum: 1}}},
        {$sort: {"amount": -1}}
        )

-- 25. Describe 5 additional questions to the database (items 26 to 30), significantly different from the previous ones, and also present the research solution for each question.
-- 25. Display the restaurants per zipcode and in ascending order, for restaurants that have any grade before ISODate 2013-08-27T00:00:00.000Z
db.restaurants.aggregate(
        {$match: {"grades.date": {$lte: ISODate("2013-08-27T00:00:00.000Z") }}},
        {$group: {
                _id: "$address.zipcode",
                amount: {$sum: 1}}},
        {$sort: {"amount": 1}}
        )

-- 26. Display the restaurants per building and in descending order, for restaurants that have any grade between ISODate 2013-08-27T00:00:00.000Z and 2014-08-27T00:00:00.000Z
db.restaurants.aggregate(
        {$match: {"grades.date": {$lte: ISODate("2014-08-27T00:00:00.000Z"),$gte: ISODate("2013-08-27T00:00:00.000Z") }}},
        {$group: {
                _id: "$address.building",
                amount: {$sum: 1}}},
        {$sort: {"amount": -1}}
        )

-- 27. Display an average of all grades scores in all restaurants
db.restaurants.aggregate(
        {$unwind: "$grades"},
        {$group: {
                _id: "$nome",
                averages: {$avg: "$grades.score"}}},
        {$group: {
                _id: null,
                average_of_all_averages: {$avg: "$averages"}
        }}
        )

-- 28. Display an average of all grades scores in all restaurants
db.restaurants.aggregate(
        {$unwind: "$grades"},
        {$group: {
                _id: "$nome",
                averages: {$avg: "$grades.score"}}},
        {$group: {
                _id: null,
                average_of_all_averages: {$avg: "$averages"}
        }}
        )

-- 29. Count the total number of different locations:
db.restaurants.aggregate(
        {$group: {
            _id: "$localidade",
            amount: {$sum: 1}}},
        {$group: {
            _id: null,
            different: {$sum: 1}
        }})
