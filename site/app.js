const express = require('express')
const app = express()
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'))
var mustacheExpress = require('mustache-express');

var calendarLookup = {"test": "traviscountydemocrats.org_m762fpckuehu3n5o2n54o2leks%40group.calendar.google.com"}
// Register '.mustache' extension with The Mustache Express
app.engine('mustache', mustacheExpress());

app.set('view engine', 'mustache');
app.set('views', __dirname + '/views');

app.get('/', (req, res) => res.send('Hello World!'))

app.post('/form', function (req, res) {
  console.log(req.body);
  res.render('form', { srcs: "src=" + calendarLookup['test']});
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))