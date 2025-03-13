// import mysql from "../mysql.js"
import db from 'mysql';
let getdb;
function Test() {
    db.query('select * from customer', function (err, results, fields) {
        if (err) throw err;
        getdb=results
        console.log(results);
    }
)

return(
<div>
    {getdb}
</div>

);
}

export default Test;