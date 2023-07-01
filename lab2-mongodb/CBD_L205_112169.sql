-- (a)
mongoimport --db cars --collection cars --drop --file cars.json

-- (b)
-- database file contains basic cars information
-- JSON Database structure:
{
    "Name":"fiat strada custom",
    "Miles_per_Gallon":37.3,
    "Cylinders":4,
    "Displacement":91,
    "Horsepower":69,
    "Weight_in_lbs":2130,
    "Acceleration":14.7,
    "Year":"1979-01-01",
    "Origin":"Europe"
}
{
    ...
}
{
    ...
}
{
    ...
}


-- (c) Create 6 expressive queries of your domain of knowledge using the operatorfind({...}, {...})
-- 1. find all cars that have 4 cylinders
db.cars.find({Cylinders: 4})

-- 2. find all cars that Origin is Europe
db.cars.find({Origin: "Europe"})

-- 3. find all cars with Horsepower more than 200
db.cars.find({Horsepower: {$gt: 200} })

-- 4. find all cars that includes "fiat" in "Name"
db.cars.find({Name: {$regex: "fiat"} })

-- 5. find the count of cars that have Acceleration less than 10.0
db.cars.find({Acceleration: {$lt: 10.0} }).count()

-- 6. find all cars that's "Weight_in_lbs" is more than 4000 and their name NOT contains "ford"
db.cars.find({
    $and:[
        {"Name": { $not: {$regex:"ford"} }},
        {"Weight_in_lbs": {$gt: 4000} }
    ]},
    {Name:1, Weight_in_lbs:1}
    )


-- (d) Create 6 expressive queries of your knowledge domain using the operator aggregate($group, $project, $unwind, $match, etc).
-- 1. find average Miles_per_Gallon for every car name that is in the datbase
db.cars.aggregate(
        {$group: {
            _id: "$Name",
            average: {$avg: "$Miles_per_Gallon"}}},
        )

-- 2.  find average Miles_per_Gallon for every car name that is "Weight_in_lbs" is less than 2000
db.cars.aggregate(
        {$match: {"Weight_in_lbs" : {$lt: 2000}} },
        {$group: {
            _id: "$Name",
            average: {$avg: "$Miles_per_Gallon"}}},
        )

-- 3. Display the number of different cars in "Europe" Origin
db.cars.aggregate(
        {$match: {"Origin": "Europe"}},
        {$group: {
                _id: "$Name",
                amount: {$sum: 1}}},
        {$group: {
                _id: null,
                total_amount_of_different_cars_in_europe: {$sum: "$amount"}
        }}
        )

-- 4. count the average accelaration in "chrysler" cars that have: more or equal than 4 cylinders & acceleration higher than 12.0
db.cars.aggregate(
        {$match: {"Name" : {$regex: "chrysler"} }},
        {$match: {"Cylinders" : {$gte: 4} }},
        {$match: {"Acceleration" : {$gt: 12.0} }},
        {$group: {
            _id: "$Name",
            average: {$avg: "$Acceleration"}}},
        )
-- 5.count how many cars there is per Origin and sort it in descending order
db.cars.aggregate(
        {$group: {
            _id: "$Origin",
            total: {$sum: 1}}},
        {$sort: {"total": -1} }
        )

-- 6. count the total horsepower of all "chevrolet" cars
db.cars.aggregate(
        {$match: {"Name": {$regex: "chevrolet"}} },
        {$group: {
            _id: "$Horsepower",
            total: {$sum: "$Horsepower"}}},
        {$group: {
            _id: null,
            total_total: {$sum:"$total"}
        }}
        )

