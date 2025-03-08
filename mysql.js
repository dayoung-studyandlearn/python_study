const mysql=require('mysql');

const connect=mysql.createConnection({
  host:'localhost',
  port:'3306',
  user:'root',
  password:'gPwjddl35@-@',
  database:"hiddenace"
});
connect.connect((err)=>{
  if(err) console.log(err);
  else console.log("connected to the mysql");
})

module.exports=connect;