# iptvcrawl

a scrapy project for crawl IPTV playlist.

## Dependency

* Python3
* pip install scrapy

## Usage
 ```
 scrapy crawl ejatv
 ```

## Output

Output playlist file is `playlist.m3u`. You should note that this file will be overwritten every time when you run spider.

## Customize

You can customer the filter condition. Just edit the `start_urls` in [ejatv.py](iptvcrawl/spiders/ejatv.py)

Example:

this url

https://eja.tv/?limit=0&country=js&language=Chinese&category=&level=0&search=

means channel from Japan, language is Chinese, and any category

### Avaliable parameters value are follow:

#### Category

```
Animation => Animation
Auto => Auto
Business => Business
Classic => Classic
Comedy => Comedy
Cooking => Cooking
Culture => Culture
Documentary => Documentary
Education => Education
Entertainment => Entertainment
Family => Family
Fashion => Fashion
General => General
Kids => Kids
Legislative => Legislative
Lifestyle => Lifestyle
Local => Local
Movies => Movies
Music => Music
News => News
Outdoor => Outdoor
Relax => Relax
Religious => Religious
Science => Science
Series => Series
Shop => Shop
Sport => Sport
Sports => Sports
Travel => Travel
Weather => Weather
XXX => XXX
Youtube => Youtube
VOD => VOD
```

#### Language

```
Akan => Akan
Albanian => Albanian
Amharic => Amharic
Arabic => Arabic
Armenian => Armenian
Azerbaijani => Azerbaijani
Bosnian => Bosnian
Bulgarian => Bulgarian
Catalan => Catalan
Chinese => Chinese
Croatian => Croatian
Czech => Czech
Danish => Danish
Divehi => Divehi
Dutch => Dutch
English => English
Estonian => Estonian
Faroese => Faroese
Finnish => Finnish
French => French
Galician => Galician
Georgian => Georgian
German => German
Greek => Greek
Hebrew => Hebrew
Hindi => Hindi
Hungarian => Hungarian
Icelandic => Icelandic
Ignota => Ignota
Indonesian => Indonesian
Italian => Italian
Japanese => Japanese
Javanese => Javanese
Kannada => Kannada
Kazakh => Kazakh
Khmer => Khmer
Kinyarwanda => Kinyarwanda
Korean => Korean
Kurdish => Kurdish
Lao => Lao
Latvian => Latvian
Lithuanian => Lithuanian
Luxembourgish => Luxembourgish
Macedonian => Macedonian
Malay => Malay
Malay => Malay 
Malayalam => Malayalam
Maltese => Maltese
Mandarin%20Chinese => Mandarin Chinese
Min%20Nan%20Chinese => Min Nan Chinese
Modern%20Greek => Modern Greek 
Montenegrin => Montenegrin
Music => Music
Māori => Māori
Norwegian%20Bokmål => Norwegian Bokmål
Persian => Persian
Polish => Polish
Portuguese => Portuguese
Punjabi => Punjabi
Pushto => Pushto
Romanian => Romanian
Russian => Russian
Serbian => Serbian
Sinhala => Sinhala
Slovak => Slovak
Slovenian => Slovenian
Somali => Somali
Spanish => Spanish
Sundanese => Sundanese
Swahili => Swahili
Swedish => Swedish
Tagalog => Tagalog
Tamil => Tamil
Telugu => Telugu
Thai => Thai
Turkish => Turkish
Ukrainian => Ukrainian
Urdu => Urdu
Uzbek => Uzbek
Vietnamese => Vietnamese
Western%20Frisian => Western Frisian
Yue%20Chinese => Yue Chinese
```

#### Country
```
af => Afghanistan
al => Albania
dz => Algeria
ar => Argentina
am => Armenia
aw => Aruba
au => Australia
at => Austria
az => Azerbaijan
bh => Bahrain
bb => Barbados
by => Belarus
be => Belgium
bo => Bolivia
ba => Bosnia and Herzegovina
br => Brazil
bg => Bulgaria
bf => Burkina Faso
kh => Cambodia
cm => Cameroon
ca => Canada
cl => Chile
cn => China
co => Colombia
cr => Costa Rica
hr => Croatia
cw => Curacao
cy => Cyprus
cz => Czechia
cd => Democratic Republic of the Congo
dk => Denmark
do => Dominican Republic
ec => Ecuador
eg => Egypt
sv => El Salvador
gq => Equatorial Guinea
ee => Estonia
et => Ethiopia
fo => Faroe Islands
fj => Fiji
fi => Finland
fr => France
ge => Georgia
de => Germany
gh => Ghana
gr => Greece
gt => Guatemala
gy => Guyana
ht => Haiti
hn => Honduras
hk => Hong Kong
hu => Hungary
is => Iceland
in => India
id => Indonesia
int => International
ir => Iran
iq => Iraq
ie => Ireland
il => Israel
it => Italy
jm => Jamaica
jp => Japan
jo => Jordan
kz => Kazakhstan
ke => Kenya
xk => Kosovo
kw => Kuwait
kg => Kyrgyzstan
la => Laos
lv => Latvia
lb => Lebanon
ly => Libya
li => Liechtenstein
lt => Lithuania
lu => Luxembourg
mo => Macao
my => Malaysia
mv => Maldives
mt => Malta
mx => Mexico
md => Moldova
mc => Monaco
me => Montenegro
ma => Morocco
mz => Mozambique
nl => Netherlands
an => Netherlands Antilles
nz => New Zealand
ni => Nicaragua
ng => Nigeria
mk => North Macedonia
no => Norway
om => Oman
pk => Pakistan
ps => Palestinian Territory
pa => Panama
py => Paraguay
pe => Peru
ph => Philippines
pl => Poland
pt => Portugal
pr => Puerto Rico
qa => Qatar
cg => Republic of the Congo
ro => Romania
ru => Russia
rw => Rwanda
sm => San Marino
sa => Saudi Arabia
sn => Senegal
rs => Serbia
sl => Sierra Leone
sg => Singapore
sk => Slovakia
si => Slovenia
so => Somalia
kr => South Korea
es => Spain
lk => Sri Lanka
sd => Sudan
se => Sweden
ch => Switzerland
sy => Syria
tw => Taiwan
tj => Tajikistan
tz => Tanzania
th => Thailand
tn => Tunisia
tr => Turkey
vi => U.S. Virgin Islands
ug => Uganda
ua => Ukraine
ae => United Arab Emirates
gb => United Kingdom
us => United States
uy => Uruguay
uz => Uzbekistan
va => Vatican
ve => Venezuela
vn => Vietnam
ye => Yemen
zm => Zambia
```
