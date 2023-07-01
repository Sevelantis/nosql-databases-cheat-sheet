findPattern = function(pattern) {
    return db.phones.find({ display: {$regex: pattern} })
}
