// @ts-ignore
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";
var format = require('util').format;


// @ts-ignore
const express = require('express'),
app = express(),
client = new MongoClient(url, { useNewUrlParser: true });
// @ts-ignore
server = require('http').createServer(app);

const path = require('path');
app.use(express.static(path.join(__dirname)));

// @ts-ignore
app.get('/', (req, res) => 
    {
     res.sendFile(path.join(__dirname, 'index.html'))
    }
);


// @ts-ignore
app.get('/connexion', (req, res) => 
    {
        res.sendFile(path.join(__dirname, '/routes/connexion.html'))
    }
);

// @ts-ignore
app.get('/caddy', (req, res) => 
    {
        res.sendFile(path.join(__dirname, '/routes/caddy.html'))
    }
);

// @ts-ignore
app.get('/informations', (req, res) => 
    {
     res.sendFile(__dirname + '/routes/informations.html')
    }
);

// @ts-ignore
app.get('/inscription', (req, res) => 
    {
     res.sendFile(__dirname + '/routes/inscription.html')
    }
);

// @ts-ignore
app.get('/product', (req, res) => 
    {
     res.sendFile(__dirname + '/routes/product.html')
    }
);

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

app.use(express.static(__dirname + '/'));
app.listen(8081)
console.log('http://localhost:8081')


