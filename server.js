const express =require('express');
const path=require('path');
const app=express();

app.use(express.json());
var cors=require('cors');
app.use(cors());

app.use(express.static(path.join(__dirname, 'hiddenbingotest/build')));


app.listen(8080,()=>{
    console.log("8080 연결")
})

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, '/hiddenbingotest/build/index.html'));
});





//url란에 어떠한 문자가 들어와도 메인 index.html으로 보내라는 뜻
app.get('*', function (req, res) {
    res.sendFile(path.join(__dirname, '/hiddenbingotest/build/index.html'));
  });