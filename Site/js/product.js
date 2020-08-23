const mongoose = require("mongoose");
const uniqueValidator = require("mongoose-unique-validator");

const productSchema = mongoose.Schema(
    {
        name : {},
        email : {type : String, require : true, unique : true},
    }
);

userSchema.plugin(uniqueValidator);

module.exports = mongoose.model('Product', productSchema);