const express = require('express')
const app = express()
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'))
var mustacheExpress = require('mustache-express');

var calendarLookup = {
	"fundraiser": "tog96t22bfsf22r2seo07lv5014%40group.calendar.google.com",
	"phonebank": "4sb63trkq9794hkpo1n1ufi3qc%40group.calendar.google.com",
	"voterreg": "2bfucjf1os35vn50jkuga1d7b0%40group.calendar.google.com"
}
var topicLookup = {
   "women's rights":[
      {
         "name":"Women for Good Government",
         "link":"http://wggaustin.wixsite.com/wggaustin/meetings"
      },
      {
         "name":"National Organization for Women",
         "link":"https://www.facebook.com/pg/TexasStateNOW/events/?ref=page_internal"
      },
      {
         "name":"NARAL Pro-Choice Texas",
         "link":"https://www.facebook.com/pg/prochoicetexas/events/?ref=page_internal"
      }
   ],
   "campaigning":[
      {
         "name":"Battleground Texas",
         "link":"https://www.facebook.com/pg/BattlegroundTexas/events/?ref=page_internal"
      },
      {
         "name":"One Texas Resistance",
         "link":"https://www.facebook.com/groups/onetexasresistance/events/"
      }
   ],
   "racial equality":[
      {
         "topic":"racial equality",
         "organization":"Black Lives Matter",
         "url":"https://www.facebook.com/pg/BlackLivesMatterAustin/events/?ref=page_internal"
      }
   ],
   "all":[
      {
         "organization":"Lake Travis Progressives",
         "url":"https://www.facebook.com/pg/LakeTravisProgressives/events/?ref=page_internal"
      },
      {
         "organization":"Indivisible Austin",
         "url":"https://www.facebook.com/pg/indivisibleatx/events/?ref=page_internal"
      }
   ],
   "LGBTQIA":[
      {
         "organization":"Equality Texas",
         "url":"https://www.facebook.com/pg/EqualityTexas/events/?ref=page_internal"
      }
   ]
}

// Register '.mustache' extension with The Mustache Express
app.engine('mustache', mustacheExpress());

app.set('view engine', 'mustache');
app.set('views', __dirname + '/views');

app.get('/', (req, res) => res.send('Hello World!'))

app.post('/form_event_type', function (req, res) {
  console.log(req.body);
  var calendars = []
  for (var i=0; i< req.body.category.length; i++) {
  	calendars.push({src:calendarLookup[req.body.category[i]]});
  }
  console.log(calendars)
  res.render('form_event_type', { calendars: calendars});
})

app.post('/form_topic', function(req,res) {
	console.log(req.body);
	var categories = [];
	categories.push({name:"Women's Rights", groups:topicLookup["women's rights"]});
	categories.push({name:"Campaigning", groups:topicLookup["campaigning"]});
	res.render('form_topic', {categories:categories});
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))