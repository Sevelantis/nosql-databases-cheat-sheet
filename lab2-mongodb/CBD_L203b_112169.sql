test> load("/home/mir/Desktop/Lab-2/populatePhones.js")
true
test> populatePhones
[Function: populatePhones]
test> populatePhones(351,1,5)
DeprecationWarning: Collection.insert() is deprecated. Use insertOne, insertMany, or bulkWrite.
Inserted number +351-233000001
Inserted number +351-220000002
Inserted number +351-233000003
Inserted number +351-231000004
Inserted number +351-234000005
Done!

test> db.phones
db.phones

test> db.phones.find()
[
  {
    _id: 351233000001,
    components: { country: 351, prefix: 233, number: 1 },
    display: '+351-233000001'
  },
  {
    _id: 351220000002,
    components: { country: 351, prefix: 22, number: 2 },
    display: '+351-220000002'
  },
  {
    _id: 351233000003,
    components: { country: 351, prefix: 233, number: 3 },
    display: '+351-233000003'
  },
  {
    _id: 351231000004,
    components: { country: 351, prefix: 231, number: 4 },
    display: '+351-231000004'
  },
  {
    _id: 351234000005,
    components: { country: 351, prefix: 234, number: 5 },
    display: '+351-234000005'
  }
]
test> db.phones.find().count()
5
test> 
