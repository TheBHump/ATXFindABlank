const express = require('express')
const app = express()
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'))
var mustacheExpress = require('mustache-express');

var calendarLookup = {"Community Event": "joq21bu6k8t4momlfc7a1g5dlo@group.calendar.google.com", "Paid Canvass": "mpg6lp06tdsco1n2u46is39fcs@group.calendar.google.com", "Training": "146mggfjsc05ioiib8n26khnno@group.calendar.google.com", "Office": "i0fn10bb38f3d1fh6ceahqu97c@group.calendar.google.com", "Fundraiser": "7jp2qhjservh2jn5479ckmui78@group.calendar.google.com", "Other": "n3lcu539gm3kq9gc82fu1989uo@group.calendar.google.com", "Phone Bank": "ddeovfvtce5d7aqftftb50hgjc@group.calendar.google.com", "Voter Reg": "eh85l44fbd24qpqb6eb2ou2uh8@group.calendar.google.com", "Canvass": "hfb3u2e46mg3gemdb2c23tb7qk@group.calendar.google.com", "Meeting": "j299log736vom6putkmflmb914@group.calendar.google.com"}

// Register '.mustache' extension with The Mustache Express
app.engine('mustache', mustacheExpress());

app.set('view engine', 'mustache');
app.set('views', __dirname + '/views');

app.get('/', (req, res) => res.send('Hello World!'))

app.post('/form', function (req, res) {
  console.log(req.body);
  res.render('form', { calendars: [calendarLookup['Other']]});
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))