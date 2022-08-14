const express = require('express');
const bodyParser = require('body-parser');
var dbConn  = require('./config/db.config');

// create express app
const app = express();

// setup the server port
const port = process.env.PORT || 5000;

// parse request data content type application/x-www-form-rulencoded
app.use(bodyParser.urlencoded({extended: false}));

// parse request data content type application/json
app.use(bodyParser.json());

// define root route
app.get('/greet', (req, res)=>{
    res.send('Hello World');
});

//greet-user
app.get('/greet-user', function(req, res){
    res.send("Hello "+req.query.username);
 });

 //add-villian
 app.get('/add-villian', function(req, result){

    const villian_name = req.query.name;
    var sql = "INSERT INTO myavengers(avenger_character,avenger_type) VALUES(?,'Villian')";
    dbConn.query(sql,villian_name, (err, res)=>{
        if(err){
            console.log('Error while adding villian: ', err);
            result.send(villian_name+" already exists try adding another villian");
        }else{
            console.log('Villain added successfully');
            result.send(villian_name+ ' Villain added successfully');
        }
    })


 });

 //add-hero
 app.get('/add-hero', function(req, result){

    const hero_name = req.query.name;
    var sql = "INSERT INTO myavengers(avenger_character,avenger_type) VALUES(?,'Hero')";
    dbConn.query(sql,hero_name, (err, res)=>{
        if(err){
            console.log('Error while adding hero: ', err);
            result.send(hero_name+" already exists try adding another hero");
        }else{
            console.log('Hero added successfully');
            result.send(hero_name+' Hero added successfully');
        }
    })


 });

 //get-characters
 app.get('/get-characters', function(req, result){

    var sql = "SELECT * FROM myavengers";
    dbConn.query(sql, (err, res)=>{
        if(err){
            console.log('Error : ', err);
            result.send(err);
        }else{
            console.log(res);
            result.send(res);
        }
    })


 });

 //avengers-assemble
 app.get('/avengers-assemble', function(req, result){

    var sql = "SELECT * FROM myavengers WHERE avenger_type='Hero'";
    dbConn.query(sql, (err, res)=>{
        if(err){
            console.log('Error : ', err);
            result.send(err);
        }else{
            console.log(res);
            result.send(res);
        }
    })


 });




// listen to the port
app.listen(port, ()=>{
    console.log(`Express is running at port ${port}`);
});