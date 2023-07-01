countPhonePrefixes = function() {
    return db.phones.aggregate([
        {$group: {
            _id: "$components.country",
            prefix: {$sum: 1}
        }}
    ])
}
