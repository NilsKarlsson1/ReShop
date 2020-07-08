// @ts-ignore

var mysql = require('mysql');
var bodyParser = require('body-parser');

var ArticleDB = mysql.createConnection({
  host: "127.0.0.1",
  user: "root",
  database: "mydb"
});

// @ts-ignore
ArticleDB.connect(function(err) {
  if (err) throw err;
  console.log("Connected to ArtcileBD");
});


// @ts-ignore
const Produit = function(a) {
    // @ts-ignore
    this.titre = a.titre;
    // @ts-ignore
    this.prix = a.prix;
    // @ts-ignore
    this.img = a.img;
    // @ts-ignore
    this.description = a.description;
    // @ts-ignore
    this.dispo = a.dispo;
    // @ts-ignore
    this.lien = a.lien;
    // @ts-ignore
    this.tag1 = a.tag1;
    // @ts-ignore
    this.tag2 = a.tag2;
    // @ts-ignore
    this.tag3 = a.tag3;
  };

// @ts-ignore
Produit.findByLien = (req, result) => {
    // @ts-ignore
    ArticleDB.query(`SELECT * FROM listarticle WHERE lien = '${req}'`, (err, res) => {
      if (err) {
        console.log("error: ", err);
        result(err, null);
        return;
      }
  
      if (res.length) {
        console.log("found product: ", res[0]);
        result(null, res[0]);
        return;
      }
  
      // not found Customer with the id
      result({ kind: "not_found" }, null);
    });
};

Produit.findByTag = (tag, result) => {
    // @ts-ignore
    ArticleDB.query(`SELECT * FROM listarticle WHERE tag2 LIKE '%${tag}%' OR tag3 LIKE '%${tag}%'`, (err, res) => {
      if (err) {
        console.log("error: ", err);
        result(err, null);
        return;
      }
      if (res.length) {
        
        result(null, res);
        return;
      }
      result({ kind: "not_found" }, null);
    });
};

Produit.findByName = (Name, result) => {
    // @ts-ignore
    ArticleDB.query(`SELECT * FROM listarticle WHERE titre LIKE '%${Name}%' OR tag2 LIKE '%${Name}%' OR tag3 LIKE '%${Name}%`, (err, res) => {
      if (err) {
        console.log("error: ", err);
        result(err, null);
        return;
      }
      if (res.length) {
        
        result(null, res);
        return;
      }
      result({ kind: "not_found" }, null);
    });
};


var UserDB = mysql.createConnection({
    host: "127.0.0.1",
    user: "root",
    database: "listuser"
}); 
  
// @ts-ignore
UserDB.connect(function(err) {
    if (err) throw err;
    console.log("Connected to UsersDB");
  });

// @ts-ignore
var format = require('util').format;


// @ts-ignore
const express = require('express'),
app = express()

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
// @ts-ignore
const {spawn} = require('child_process');
const { resolve } = require('path');
const { isUndefined } = require('util');
// @ts-ignore
server = require('http').createServer(app);


// @ts-ignore
// @ts-ignore
app.get('/', (req, res) => 
    {
     res.sendFile(__dirname + '/index.html')
    }
);


// @ts-ignore
// @ts-ignore
app.get('/connexion', (req, res) => 
    {
        res.sendFile(__dirname+ '/routes/connexion.html')
    }
);

// @ts-ignore
// @ts-ignore
app.get('/caddy', (req, res) => 
    {
        res.sendFile(__dirname+ '/routes/caddy.html')
    }
);

// @ts-ignore
// @ts-ignore
app.get('/informations', (req, res) => 
    {
     res.sendFile(__dirname + '/routes/informations.html')
    }
);

// @ts-ignore
// @ts-ignore
app.get('/inscription', (req, res) => 
    {
     res.sendFile(__dirname + '/routes/inscription.html')
    }
);

// @ts-ignore
// @ts-ignore
app.get('/product', (req, res) => 
    {
     res.sendFile(__dirname + '/routes/product.html')
    }
);

// @ts-ignore
// @ts-ignore
app.get('/search', (req, res) => 
    {
     res.sendFile(__dirname + '/routes/search.html')
    }
);

// @ts-ignore
app.get('/profile', (req, res) => 
    {
     res.sendFile(__dirname + '/routes/profile.html')
    }
);

app.get('/user', function  (req, res) {
    res.send(req.query);
});




// @ts-ignore
app.get('/product/by', (req, res) => {
    // @ts-ignore
    Produit.findByLien(req.query.lien, (err, data) => {
      if (err) {
        if (err.kind === "not_found") {
          res.status(404).send({
            message: `Not found Product with lien ${req.query.lien}.`
          });
        } else {
          res.status(500).send({
            message: "Error retrieving Product with lien " + req.query.lien
          });
        }
      } else res.send(data);
    });
  });

  // @ts-ignore
app.get('/product/look', (req, res) => {
    // @ts-ignore
    Produit.findByTag(req.query.tag, (err, data) => {
      if (err) {
        if (err.kind === "not_found") {
          res.status(404).send({
            message: `Not found Product with lien ${req.query.tag}.`
          });
        } else {
          res.status(500).send({
            message: "Error retrieving Product with lien " + req.query.tag
          });
        }
      } else res.send(data);
    });
});

    // @ts-ignore
app.get('/product/search', (req, res) => {
    // @ts-ignore
    Produit.findByTag(req.query.name, (err, data) => {
      if (err) {
        if (err.kind === "not_found") {
          res.status(404).send({
            message: `Not found Product with lien ${req.query.name}.`
          });
        } else {
          res.status(500).send({
            message: "Error retrieving Product with lien " + req.query.name
          });
        }
      } else res.send(data);
    });
});



app.use(express.static(__dirname + '/'));
app.listen(8081)
console.log('http://localhost:8081')


