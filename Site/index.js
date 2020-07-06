var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

const express = require('express'),
app = express(),
server = require('http').createServer(app);

app.get('/', (req, res) => 
    {
     res.sendFile(__dirname + '/index.html')
    }
);


app.get('/connexion', (req, res) => 
    {
     res.sendFile(__dirname + '/routes/connexion.html')
    }
);

app.get('/caddy', (req, res) => 
    {
     res.sendFile(__dirname + '/routes/caddy.html')
    }
);

app.get('/informations', (req, res) => 
    {
     res.sendFile(__dirname + '/routes/informations.html')
    }
);

app.get('/inscription', (req, res) => 
    {
     res.sendFile(__dirname + '/routes/inscription.html')
    }
);

app.get('/product', (req, res) => 
    {
     res.sendFile(__dirname + '/routes/product.html')
    }
);

app.get('/profile', (req, res) => 
    {
     res.sendFile(__dirname + '/routes/profile.html')
    }
);

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("listArticle");
  var myobj = { name: "Company Inc", address: "Highway 37" };
  /* dbo.collection("customers").insertOne(myobj, function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });*/
});

const updateBDD = (req, res) => {
  var dbo = db.db("listArticle");
  
  dbo.collection("article").updateBDD("scrapingKimonoObi.json", function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
  dbo.collection("article").updateBDD("ShinSekai.json", function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
  dbo.collection("article").updateBDD("scrapingFigurine.json", function(err, res) {
    if (err) throw err;
    console.log("1 document inserted");
    db.close();
  });
};


app.use(express.static(__dirname + '/'));
app.listen(8081)
console.log('http://localhost:8081')

module.exports = updateBDD;