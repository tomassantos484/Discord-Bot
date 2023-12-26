import random
from namesNL import *
#This program is for organizing the first and last
#names of every player of all 
#15 teams in the American League as of the end of the regular season

##1. AL East

#New York Yankees

YankeesFirst = ["Jimmy","Yoendrys","Wandy","Scott","Ron","Randy","Nestor","Michael","Matt","Luis","Lucas","Lou","Jonathan","Jhony","Albert","Clarke","Clay","Gerrit","Frankie",
"Greg", "Deivi","Domingo","Everson","Anthony","Ben","Oswaldo","Oswald","DJ","Estevan","Kyle","Josh","Jose","Giancarlo","Aaron","Gleyber","Isiah","Harrison","Zack","David"]

YankeesLast = ["Cordero","Gomez","Peralta","Effross","Marinaccio","Vazquez","Cortes","King","Krook","Carpenter","Severino","Gil","Luetge","Trivino","Loaisiga","Brito","Abreu",
"Schmidt","Holmes","Cole","Montas","Weissert","Garcia","German","Pereira","Rizzo","Rortvedt","Cabrera","Peraza","LeMahieu","Florial","Higashioka","Donaldson","Trevino","Stanton","Judge",
"Hicks","Torres","Kiner Falefa","Bader","Britton","McKay"]


#Tampa Bay Rays

RaysFirst = ["Francisco","Ji-Man","Brandon","Taylor","Yandy","Randy","Kevin","Manuel","Harold","Isaac","Wander","Brett","Josh","David","Jose","Vidal","Christian","Mike","Yu","Jonathan","Rene",
"Luke","Roman","Miles","Josh","Andrew","Jalen","Pete","Drew","Brooks","Chris","Ryan","Jason","Ralph","Jimmy","Phoenix","Luis","Shane","Easton","Corey","Colin","Cristofer","Garrett","Luke","Jeffrey","J.P.",
"Robert","Dusten","Calvin","Yonny","Ryan","Shawn","JT","Kevin","Matt", "Tommy","Tyler","Shane","Cooper","David","Javy"] 

RaysLast = ["Mejia","Choi","Lowe","Walls","Diaz","Arozarena","Kiermaier","Margot","Ramirez","Paredes","Franco","Phillips","Lowe","Peralta","Siri","Brujan","Bethancourt","Zunino","Chang","Aranda","Pinto",
"Raley","Quinn","Mastrobuoni","Fleming","Kittredge","Beeks","Fairbanks","Rasmussen","Raley","Mazza","Thompson","Adam","Garza","Yacabonis","Sanders","Patino","Baz","McGee","Kluber","Poche","Ogando","Cleavinger",
"Bard","Springs","Feyereisen","Dugger","Knight","Faucher","Chirinos","Yarbrough","Armstrong","Chargois","Herget","Wisler","Romero","Glasnow","McClanahan","Criswell","McKay","Guerra"]

#Boston Red Sox

RedSoxFirst = ["Christian","Bobby","Trevor","Xander","Rafael","Alex","Enrique","Jackie","J.D.","Christian","Franchy","Tommy","Jarren","Rob","Kevin","Reese","Triston","Connor","Eric","Yolmer","Jeter","Abraham","Jaylin",
"Yu","Travis","Jonathan","Garrett","Rich","Jeurys","Nathan","Hansel","Kaleb","Brayan","Chris","Nick","Michael","Eduard","Connor","Matt","Josh","Hirokazu","Kutter","Jake","Darwinson","Phillips","Ryan","John","Franklin",
"Zack","Austin","Tanner","Matt","Michael","Tyler"]

RedSoxLast = ["Vasquez","Dalbec","Story","Bogaerts","Devers","Bogaerts","Devers","Verdugo","Hernandez","Bradley Jr.","Martinez","Arroyo","Cordero","Pham","Duran","Refsnyder","Plawecki","McGuire","Casas","Wong","Hosmer",
"Sanchez","Downs","Almonte","Davis","Chang","Shaw","Arauz","Whitlock","Hill","Familia","Eovaldi","Robles","Ort","Bello","Sale","Pivetta","Wacha","Bazardo","Seabold","Strahm","Winckowski","Sawamura","Crawford","Diekman",
"Hernandez","Valdez","Braiser","Schreiber","German","Kelly","Davis","Houck","Barnes","Feliz","Danish"]

#Toronto Blue Jays

JaysFirst = ["Alejandro","Vladimir","Santiago","Bo","Matt","Lourdes","George","Teoscar","Zack","Raimel","Cavan","Danny","Whit","Bradley","Jackie","Gabriel","Tyler","Gosuke","Otto","Vinny","Trevor","Trent","Anthony","Tim","Jose","Yusei","Anthony",
"Zach","Hyun Jin","Casey","Foster","Andrew","David","Kevin","Yimi","Matt","Bowden","Sergio","Julian","Jordan","Alek","Anthony","Thomas","Mitch","Max","Adam","Ryan","Tayler","Ross","Jeremy","Shaun"]

JaysLast = ["Kirk","Guerrero Jr.","Espinal","Bichette","Gurriel Jr.","Springer","Hernandez","Collins","Tapia","Jansen","Merrifield","Zimmer","Bradley Jr.","Moreno","Heineman","Katoh","Lopez","Capra","Richards","Thorton","Bass","Mayza","Berrios","Kikuchi",
"Banda","Pop","Ryu","Lawrence","Griffin","Vasquez","Phelps","Gausman","Garcia","Gage","Francis","Romo","Merryweather","Romano","Manoah","Kay","Hatch","White","Castillo","Cimber","Borucki","Saucedo","Stripling","Beasley","Anderson"]

#Baltimore Orioles

OriolesFirst = ["Adley","Ryan","Rougned","Jorge","Ramon","Austin","Cedric","Anthony","Trey","Robinson","Tyler","Ryan","Gunnar","Terrin","Kyle","Chris","Anthony","Jesus","Richie","Kelvin","Jonathan","Brett","Rylan","DJ","Yusniel","Yennier","Jake","Cody","DL","Kyle",
"Rico","Cionel","Beau","Keegan","Louis","Denyi","Alex","Travis","Dean","Dillon","Jorge","Paul","John","Jordan","Zac","Spenser","Tyler","Bruce","Marcos","Mike","Joey","Logan","Bryan","Nick","Felix","Chris","Austin"]

OriolesLast = ["Rutschman","Mountcastle","Odor","Mateo","Urias","Hays","Mullins","Santander","Mancini","Chirinos","Nevin","McKenna","Henderson","Vavra","Stowers","Owings","Bemboom","Aguilar","Martin","Gutierrez","Arauz","Phillips","Bannon","Stewart","Diaz","Allen",
"Cano","Reed","Sedlock","Hall","Bradish","Garcia","Perez","Sulser","Akin","Head","Reyes","Wells","Lakins Sr.","Kremer","Tate","Lopez","Fry","Means","Lyles","Lowther","Watkins","Wells","Zimmermann","Diplan","Baumann","Krehbiel","Gillaspie","Baker","Vespi","Bautista","Ellis","Voth"]

##2. AL Central

#Cleveland Guardians

GuardiansFirst = ["Austin","Josh","Andres","Amed","Jose","Steven","Myles","Oscar","Franmil","Owen","Luke","Ernie","Oscar","Richie","Nolan","Tyler","Will","Gabriel","Will","Sandy","Bobby","Alex","Bryan","Yu","Bo","Logan","Anthony","Triston","Xzavion","Emmanuel","Ian","Shane","James","Hunter",
"Kirk","Konnor","Eli","Trevor","Yohan","Aaron","Cal","Nick","Bryan","Zach","Anthony","Sam","Enyel","Tanner","Cody","Alex"]

GuardiansLast = ["Hedges","Naylor","Gimenez","Rosario","Ramirez","Kwan","Straw","Gonzalez","Reyes","Miller","Maile","Clement","Mercado","Palacios","Jones","Freeman","Benson","Arias","Brennan","Leon","Bradley","Call","Lavastida","Chang","Naylor","Allen","Gose","McKenzie","Curry","Clase","Gibaut",
"Bieber","Karinchak","Gaddis","McCarty","Pilkington","Morgan","Stephan","Ramirez","Civale","Quantrill","Sandlin","Shaw","Plesac","Castro","Hentges","De Los Santos","Tully","Morris","Young"]

#Chicago White Sox

WhiteSoxFirst = ["Yasmani","Jose","Josh","Tim","Yoan","AJ","Luis","Gavin","Eloy","Andrew","Leury","Adam","Seby","Elvis","Jake","Reese","Romy","Danny","Lenyn","Mark","Adam","Carlos","Davis","Kendall","Matt","Johnny","Ryan","Bennett","Kyle","Aaron","Vince","Lance","Dallas","Dylan","Joe","Liam","Jake",
"Jose","Michael","Reynaldo","Tanner","Jimmy","Lucas","Anderson"]

WhiteSoxLast = ["Grandal","Abreu","Harrison","Anderson","Moncada","Robert","Sheets","Jimenez","Vaughn","Garcia","Engel","Zavala","Andrus","Burger","McGuire","Gonzalez","Mendick","Sosa","Payton","Haseley","Perez","Martin","Graveman","Foster","Cueto","Burr","Sousa","Crick","Bummer","Velasquez","Lynn",
"Keuchel","Cease","Kelly","Hendriks","Diekman","Ruiz","Kopech","Lopez","Banks","Lambert","Giolito","Severino"]

#Kansas City Royals

RoyalsFirst = ["Salvador","Carlos","Nicky","Bobby","Emmanuel","Andrew","Michael","Kyle","Vinnie","MJ","Hunter","Whit","Michael","Nick","Edward","Ryan","Nate","Drew","Adalberto","Cam","Sebastian","Brent","Maikel","Freddy","Dairon","Brewer","Luke","Dylan","Joel","Kris","Matt","Brady","Anthony","Scott",
"Jackson","Gabe","Albert","Foster","Daniel","Amir","Angel","Collin","Brad","Jonathan","Jose","Jake","Josh","Wyatt","Arodys","Daniel","Zack","Max","Ronald","Taylor","Carlos"]

RoyalsLast = ["Perez","Santana","Lopez","Witt","Rivera","Benintendi","Taylor","Isbel","Pasquantino","Melendez","Dozier","Merrifield","Massey","Pratto","Olivares","O'Hearn","Eaton","Waters","Mondesi","Gallagher","Rivero","Rooker","Garcia","Fermin","Blanco","Hicklen","Weaver","Coleman","Payamps","Bubic",
"Peacock","Singer","Misiewicz","Barlow","Kowar","Speier","Abreu","Griffin","Mengden","Garrett","Zerpa","Snider","Keller","Heasley","Cuas","Brentz","Staumont","Mills","Vizcaino","Lynch","Greinke","Castillo","Bolanos","Clarke","Hernandez"]

#Minnesota Twins

TwinsFirst = ["Gary","Jose","Jorge","Carlos","Gio","Nick","Gilberto","Max","Luis","Byron","Ryan","Trevor","Jake","Kyle","Alex","Jermaine","Miguel","Matt","Sandy","Mark","Royce","Tim","Caleb","Billy","Jose","Simeon Woods","Bailey","Cole","Yennier","Griffin","Ian","Joe","Louie","Tyler","Aaron","Jovani","Danny",
"Jorge","Chris","Jharel","Chris","Trevor","Emilio","Caleb","Joe","Jhoan","Cody","Dylan","Ronny","Austin","Josh","Tyler","Sonny","Michael","Juan","Devin","Dereck","Chi Chi","Jhon","Tyler"]

TwinsLast = ["Sanchez","Miranda","Polanco","Correa","Urshela","Gordon","Celestino","Kepler","Arraez","Jeffers","Larnach","Cave","Garlick","Kirilloff","Palacios","Sano","Wallner","Leon","Contreras","Lewis","Beckham","Hamilton","Hamilton","Godoy","Richardson","Ober","Sands","Cano","Jax","Hamilton","Ryan","Varland",
"Duffey","Sanchez","Moran","Coulombe","Alcala","Paddack","Cotton","Archer","Megill","Pagan","Thielbar","Lopez","Smith","Duran","Stashak","Bundy","Henriquez","Davis","Winder","Thornburg","Gray","Fulmer","Minaya","Smeltzer","Rodriguez","Gonzalez","Romero","Mahle"]

#Detroit Tigers

TigersFirst = ["Tucker","Spencer","Jonathan","Javier","Jeimer","Akil","Riley","Victor","Miguel","Harold","Willi","Eric","Robbie","Austin","Kody","Kerry","Derek","Ryan","Daz","Zack","Dustin","Brendon","Josh","Tarik","Alex","Casey",
"Drew","Andrew","Will","Drew","Wily","Joey","Angel","Elvin","Joe","Rony","Bryan","Tyler",
"Beau","Eduardo","Miguel","Garrett","Jose","Jason","Matt","Alex","Derek","Michael","Gregory","Daniel","Michael","Luis","Jacob"]

TigersLast = ["Barnhart","Torkelson","Schoop","Baez","Candelario","Baddoo","Greene","Reyes","Cabrera","Castro","Castro","Grossman","Meadows","Clemens","Carpenter","Hill",
"Kreidler","Cameron","Short","Garneau","Davis","Lester","Skubal","Lange","Mize","Hutchison","Chafin","Vest","Carlton","Peralta","Wentz","De Jesus","Rodriguez",
"Jimenez","Garcia","Garcia","Alexander","Brieske","Rodriguez","Diaz","Hill","Cisnero","Foley","Manning","Faedo","Law","Fulmer","Soto","Norris","Pineda","Castillo","Barnes"]

##3. AL West

#Houston Astros

AstrosFirst = ["Martin","Yuli","Jose","Jeremy","Alex","Michael","Chas","Kyle","Yordan","Aledmys","Mauricio","Trey","Jake","Jose","Christian","Jason","J.J.","Niko","David","Korey","Yainer","Joe","Taylor","Justin",
"Blake","Hunter","Ryan","Jake","Hector","Ronel","Ryne","Lance","Parker","Seth","Will","Cristian","Phil","Brandon","Jose","Rafael","Luis","Pedro","Framber","Enoli","Bryan"]

AstrosLast = ["Maldonado","Gurriel","Altuve","Pena","Bregman","Brantley","McCormick","Tucker","Alvarez","Diaz","Dubon","Mancini","Meyers","Siri","Vazquez","Castro","Matijevic","Goodrum","Hensley","Lee","Diaz",
"Perez","Jones","Verlander","Taylor","Brown","Pressley","Odorizzi","Neris","Blanco","Stanek","McCullers Jr.","Mushinski","Martinez","Smith","Javier","Maton","Bielak","Urquidy","Montero","Garcia","Baez","Valdez",
"Paredes","Abreu"]

#Seattle Mariners

MarinersFirst = ["Cal","Ty","Adam","J.P.","Eugenio","Jesse","Julio","Mitch","Carlos","Abraham","Dylan","Sam","Jarred","Luis","Taylor","Kyle","Justin","Curt","Tom","Mike","Jake","Steven","Kevin","Marcus","Brian","Andrew","Drew",
"Stuart","Travis","Jack","Donovan","Penn","Diego","Ken","Anthony","Chris","Erik","Paul","Luis","Roenis","Danny","Marco","George","Drew","Justus","Yohan","Andres","Matthew","Robbie","Sergio","Logan","Brennan","Wyatt","Matt",
"Matt","Matt","Ryan","Riley","Tommy"]

MarinersLast = ["Raleigh","France","Frazier","Crawford","Suarez","Winker","Rodriguez","Haniger","Santana","Toro","Moore","Haggerty","Kelenic","Torrens","Trammell","Lewis","Upton","Casali","Murphy","Ford","Lamb","Souza Jr.","Padlo",
"Wilson","O'Keefe","Knapp","Ellis","Fairchild","Jankowski","Larsen","Walton","Murfee","Castillo","Giles","Misiewicz","Flexen","Swanson","Sewald","Castillo","Elias","Young","Gonzalez","Kirby","Steckenrider","Sheffield","Ramirez","Munoz",
"Boyd","Ray","Romo","Gilbert","Bernandino","Mills","Brash","Koch","Festa","Borucki","O'Brien","Milone"]

#Los Angeles Angels 

AngelsFirst = ["Max","Jared","Luis","Andrew","Anthony","Brandon","Mike","Taylor","Shohei","Jo","Matt","David","Tyler","Kurt","Mike","Magneuris","Matt","Jack","Michael","Juan","Mickey","Livan","Jose","Jonathan","Phil","David","Chad","Ryan",
"Steven","Logan","Dillon","Monte","Aaron Whitefield","Austin","Noah","Jhonathan","Ryan","Archie","Elvis","Cesar","Kyle","Raisel","Austin","Jose","Jesse","Brian","Patrick","Janson","Tucker","Jose","Jose","Nash","Michael","Reid","Chase","Gerardo",
"Jimmy","Aaron","Oliver","Rob","Mike","Zack","Kenny","Touki","Jaime","Andrew"]

AngelsLast = ["Stassi","Walsh","'Rengifo","Velazquez","Rendon","Marsh","Trout","Ward","Ohtani","Adell","Duffy","Fletcher","Wade","Suzuki","Ford","Sierra","Thaiss","Mayfield","Stefanic","Lagares","Moniak","Soto","Rojas","Villar","Gosselin","MacKinnon",
"Wallach","Aguilar","Duggar","O'Hoppe","Thomas","Harrison","Whitefield","Romine","Syndergaard","Diaz","Tepera","Bradley","Peguero","Valdez","Barraclough","Iglesia","Warren","Suarez","Chavez","Moran","Sandoval","Junk","Davidson","Quijada","Marte","Walters",
"Lorenzen","Detmers","Silseth","Reyes","Herget","Loup","Ortega","Zastryzny","Mayers","Weiss","Rosenberg","Toussaint","Barria","Wantz"]

#Texas Rangers

RangersFirst = ["Jonah","Nathaniel","Marcus","Corey","Ezequiel","Bubba","Leody","Adolis","Mitch","Kole","Josh","Brad","Sam","Andy","Charlie","Eli","Josh","Nick","Meibrys","Mark","Willie","Elier","Zach","Steven","Steele","Kevin","Brock","Kolby","Spencer","Greg",
"John","Glenn","Brett","Jesus","Dennis","Albert","Jon","Dallas","Matt","Taylor","Tyson","Jonathan","Matt","Martin","Spencer","Dane","Kohei","Nicklaus","Jose","Yerry","Cole","Joe","A.J.","Josh","Garrett"]

RangersLast = ["Heim","Lowe","Semien","Seager","Duran","Thompson","Taveras","Garcia","Garver","Calhoun","Smith","Miller","Huff","Ibanez","Culberson","White","Jung","Solak","Viloria","Mathias","Calhoun","Hernandez","Reks","Duggar","Walker","Plawecki","Burke","Allard",
"Howard","Holland","King","Otto","Martin","Tinoco","Santana","Abreu","Gray","Keuchel","Bush","Hearn","Miller","Hernandez","Moore","Perez","Patton","Dunning","Arihara","Snyder","Leclerc","Rodriguez","Ragans","Barlow","Alexy","Sborz","Richard"]

#Oakland Athletics

OAKFirst = ["Sean","Seth","Tony","Elvis","Vimael","Chad","Cristian","Ramon","Jed","Nick","Sheldon","Stephen","Jonah","Christian","Shea","Kevin","Stephen","Dermis","Skye","Luis","Cal","Billy","Jordan","Conner","Cody","Matt","Ernie","Austin","David","Christian","Mickey",
"Drew","Nate","Zach","Paul","Parker","Ryan","Kirby","Collin","Tyler","Zach","Ken","A.J.","Frankie","Norge","Jacob","Adrian","Domingo","Daulton","Joel","Justin","Dany","Adam","James","Austin","Jared","JP","Sam","Domingo","Lou","David","Sam","Cole","Adam"]

OAKLast = ["Murphy","Brown","Kemp","Andrus","Machin","Pinder","Pache","Laureano","Lowrie","Allen","Neuse","Vogt","Bride","Bethancourt","Langeliers","Smith","Piscotty","Garcia","Bolt","Barrera","Stevenson","McKinney","Diaz","Capel","Thomas","Davidson","Clement","Allen","MacKinnon",
"Lopes","McDonald","Jackson","Mondou","Jackson","Blackburn","Markel","Castellani","Snead","Wiles","Cyr","Logue","Waldichuk","Puk","Montas","Ruiz","Lemoine","Martinez","Tapia","Jefferies","Payamps","Grimm","Jimenez","Kolarek","Kaprielian","Pruitt","Koenig","Sears","Moll","Acevedo",
"Trivino","McKay","Selman","Irvin","Oller"]


AL_FirstNames = YankeesFirst + RaysFirst + JaysFirst + RedSoxFirst + OriolesFirst + GuardiansFirst + WhiteSoxFirst + RoyalsFirst + TwinsFirst + TigersFirst + AstrosFirst + MarinersFirst + AngelsFirst + RangersFirst + OAKFirst

AL_LastNames = YankeesLast + RaysLast + JaysLast + RedSoxLast + OriolesLast + GuardiansLast + WhiteSoxLast + RoyalsLast + TwinsLast + TigersLast + AstrosLast + MarinersLast + AngelsLast + RangersLast + OAKLast

MLB_FirstNames = AL_FirstNames + NL_FirstNames

MLB_LastNames = AL_LastNames + NL_LastNames
