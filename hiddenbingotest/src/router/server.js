const express =require('express');
const path=require('path');
const app=express();
import mysql from "../mysql.js"
import db from 'mysql';
let getdb;
const db =require('../App');

const port=8080;

app.use(express.json());
var cors=require('cors');
app.use(cors());

app.use(express.static(path.join(__dirname, 'hiddenbingotest/public')));


app.listen(port,()=>{
    console.log("port : 8080 연결")
})

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, '/hiddenbingotest/public/index.html'));
  db.query('select * from customer', function(err, results, fields){
    if (err) throw err;
    res.send(results);
    console.log(results);
  })
});



//url란에 어떠한 문자가 들어와도 메인 index.html으로 보내라는 뜻
app.get('*', function (req, res) {
    res.sendFile(path.join(__dirname, '/hiddenbingotest/build/index.html'));
  });