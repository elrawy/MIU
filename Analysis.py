import urllib.request
import re
from nltk.stem import PorterStemmer

cedilla2latin = [[u'Á', u'A'], [u'á', u'a'], [u'Č', u'C'], [u'č', u'c'], [u'Š', u'S'], [u'š', u's']]
tr = dict([(a[0], a[1]) for (a) in cedilla2latin])
def transliterate(line):
    new_line = ""
    for letter in line:
        if letter in tr:
            new_line += tr[letter]
        else:
            new_line += letter
    return new_line

def is_digit(word):
    try:
        int(word)
        return True
    except ValueError:
        return False


def FunctionGamda(PathPath,Cat):
    ps = PorterStemmer()
    file=open(PathPath,'r',encoding="utf-8")
    file1=open('rawy1','w',encoding="utf-8")
    edu=0;
    categories ={
        'film and animation':['motion picture','videotape','cinematograph','cinematics','cine','film','show','animation','comic','cartoon','comedy','action','drama','romance']
        ,'education':['edu','exam','midterm','tutorial','learn','scholarship','school','university',
                      'science','physics','chemistry','program','lecture','train','study','coach',
                      'read','tutor','information','teach','literacy','framework','biology','math',
                      'statistics','education','quiz','draw','Algebra', 'geometry', 'formula', 'equation', 'calculate', 'triangle', 'square', 'circle', 'mathematics',
                      'solve', 'split', 'result', 'theory','algorithm', 'programming', 'history', 'geography', 'project',
                       'network', 'circuits','management', 'code', "secondary", "formal", 'physical', 'primary', 'special', 'religion', 'liberal'
                      , 'medical', 'compulsory', 'technical', 'bilingual','professional', 'universal', 'industrial', 'legal', 'agricultural', 'scientific', 'undergraduate', 'postsecondary'
                      , 'rural', 'excellent', 'graduate', 'academic', 'phonic', 'postdoctoral', 'progressive', 'pure', 'remedial', 'scholastic', 'scholar', 'self-educated', 'vocational'
                      ]
        ,'autos and vehicles':['ford','bmw','honda','fiat','car','motor','wheel','vehicle','convertible','jeep','van','truck','motor','bus','coupe','ride','sedan','accident'
                               , 'all-wheel drive', 'AWD', 'astonishing', 'automatic', 'manual', 'automotive', 'classic', 'crash-tested', 'customized', 'easy-to-drive'
                               , 'electric', 'enhanced', 'environmentally-friendly', 'expensive', 'fast', 'four-wheel drive', 'front-wheel drive', 'drive', 'wheel'
                               , 'suspension', 'rims', 'spoiler', 'car boot', 'luxury', 'powerful', 'speed', 'drag', 'drift', 'slow', 'run', 'steering']
        ,'entertainment':['blast','cheer','delight','entertainment','enjoyment','feast','fun','laugh','picnic','play','joy','laugh','hobby','attract','relax'
                          , 'popular', 'live', 'theatrical', 'wingding', 'amusement', 'crack', 'craic', 'fling', 'giggle', 'horseplay', 'mischief', 'romp'
                          , 'wheeze', 'extravaganza', 'nightlife', 'cinema', 'theatre', 'circus', 'marketing', 'dance', 'tv', 'spectacle'
                          , 'multimedia', 'advertise', 'opera', 'court', 'hamlet', 'poetry', 'commoner', 'shamanism', 'nautch', 'goryeo', 'jousting', 'komnenos'
                          , 'militainment', 'beguilement', 'aristocracy', 'tournament', 'disney', 'hanging', 'decapitation', 'stoning', 'interactive'
                          , 'entertain', 'studios', 'puppet']
        ,'music': ['piano','drum','solo','guitar','violin','melody','music','opera','rap','rock','sing','tune','jazz','song','plainsong','acoustic','harmony','folk','metal','hymn','perform','lyric','rhyme'
                   , 'theme', 'concert', 'muse', 'rock music', 'chord progression', 'musical improvisation', 'concert band', 'music theory', 'mp3 player'
                   , 'counterpoint', 'harpsichord', 'part', 'tongue', 'clarion', 'interlude', 'conduct', 'slur', 'subdivision', 'concert', 'bass', 'triple - tongue'
                   , 'pianist', 'key', 'tonic', 'theatre music', 'music lesson', 'music producer', 'sound engineer', 'rhythm section', 'heavy metal music'
                   , 'auditory sensation', 'indian classical music', 'traditional music', 'music criticism' ]
        ,'sport': ['athlete','fun','game','action','ball','player','football','socker','basketball','hockey',
                   'Timberwolves', 'Rockets', 'NBA', 'season', 'Portland Trail Blazers', 'Utah Jazz', 'Miami Heat','basketball',
                   'New Orleans Pelicans', 'Los Angeles Lakers', 'Washington Wizards', 'Indiana Pacers',
                   'Toronto Raptors', 'Cleveland Cavaliers', 'Cavs',
                   'Minnesota Timberwolves', 'Tottenham Hotspur F.C.', 'Atlanta Hawks', 'Memphis Grizzlies',
                   'LeBron James', 'San Antonio Spurs', 'Boston Celtics',
                   'Houston Rockets', 'Denver Nuggets', 'Indiana Pacers', 'Detroit Pistons', 'Champions League',
                   'Neymar', 'Edinson Cavani', 'Cristiano Ronaldo',
                   'Dallas Mavericks', 'Charlotte Hornets', 'Indiana Pacers', 'Leo Messi', 'FC Barcelona',
                   'Real Madrid', 'Paris Saint-Germain ', 'FC Bayern Munich',
                   'Manchester United', 'Manchester City', 'Besiktas', 'Borussia Dortmund', 'Atletico Madrid',
                   'Tottenham Hotspur', 'Napoli', 'LaLiga', 'UD Las Palmas',
                   'CD Leganés', 'RCD Espanyol', 'Deportivo de La Coruña', 'defender', 'premier league', 'goalkeeper',
                   'Paris Saint-Germain F.C', 'PSG', 'Mohamed Salah',
                   'tennis','swim','baseball','box','archery','golf','handball','run', 'rowing', 'ice skate', 'roller skate', 'fun' , 'regulation time', 'play'
                    , 'physical activity', 'disport', 'lark', 'blood sport' , 'daisy cutter', 'boast', 'mutation', 'frolic', 'skylark', 'romp', 'gambol', 'mutant'
                    , 'feature', 'frisk', 'coach', 'rugby', 'cavort', 'rollick', 'volleyball', 'water ski', 'sudden death', 'run around', 'lark about']
        ,'gaming':['game','match','sport','joke','gamble','bet','toy','dice','lottery','ps',
                   'Minecraft','Mario','GTA','Medal of honor','clash of clans','playstation','bingo','casino','cod','COD','fortnite','battlefield','gamey', 'party game', 'pinball', 'card game', 'score', 'player', 'board game' ,'venison'
                    ,'football', 'sport', 'video game','dice','pitch','set','diversion','mind game','parlorgame', 'strategy','table game', 'played','settlers of catan','childs game', 'game of chance','treasure hunt'
                    ,'cricket', 'poker', 'frolic', 'parlour game']
        ,'pets and animals':['Dinosaurs ','kangaroo','beast','stray','wild','creature','mammal','monkey','cat','dog','gorilla','whale','orca','fish','rat','snake','crocodile','alligator','fox'
                             , 'lion','cattle','bird','bear','deer','horse','donkey','tiger','goat','rhinoceros','sheep','wolf','squirrel','leopard','giraffe','goose','turtle','duck','ferret'
                             , 'otter','raccoon','hare','frog','bat','pet','animal','camel','cheetah','owl','penguin','kitten','puppy','chicken','butterfly','koala','heron','cow','pig','shrimp','crab']
        ,'travel and events':['trip','picnic','cruse','passage','voyage','ramble','trek','navigate','sightseeing','tour','journey','tourist','sailing','flight','plane','celebration','ceremony','holiday','occasion'
                              ,'excursion','fly','sail','transit','trek','hop','junket','peregrination','ramble','seafaring','wanderlust','accident','celebrate','ceremony','circumstance'
                              ,'episode','fact','story','coincidence','miracle','gala','venue','celebrate'
                              ,'parade','carnival','seminar','race','contest','summit','meet','conference','active','occasion','roundtable'
                              ,'show','reunion','workshop','evening','exposition','gathering','affair','occurrence','tragedy','fashion']
        ,'people and blogs':['community','crowd','nation','public','society','body','nation','tribe','human','person','blog','journal','record','diary'
                             ,'populate','dwell','folks','reside','person','citizen','adult','worker','someone','local','passenger','applicant','webpage'
                             ,'pok','wordpress','twitter','vlog','podcast','facebook','wiki','gossip','column','story','post'
                             ,'essay','email','edit','write','snip','article','muse','repost','read','publish','address','information','bibliographic']
        ,'comedy':['fun','humor','sitcom','ball','standup','comedy','drollery','meme','slapstick','humor','farce','joke','wit','laugh','broadway','playhouse','circus','charade'
                   ,'comedian','parody','cabaret','burlesque','satire','thriller','gags','burletta','campy','revue','farce'
                    ,'droll','comicality','comic','facetiousness','grin','smile','takeoff','light','drollery','clown','hilarious','lmao','lol','rofl','show']
        ,'news and politics':['report','scoop','message','news','politic','rumor','president','ambassador','bomb','terrorism','bombshell','minister'
                              , 'tiding','word','intelligence','press','media','report','headline','reporter','story','newspaper','magazine','newscast'
                              , 'television','coverage','info','information','journal','journalist','omen','release','scoop','fact','newsletter'
                              , 'newsroom','newsreel','intel','source','print','thing','telly','tell','item','knowledge','novel','cnn','newsbreak','government'
                              , 'polity','affair','policy','ideology','democracy','economic','journalism','diplomacy','election','united','republic','culture']
        ,'howto and style':['Lipstick','eyebrow','makeup','haul','Sephora','Smokey','morphe',
                            'eye','teal','wing','cut','crease','lips','glittery',
                            'rainbow','liner','stains','halloween','curl','lashes','skincare',
                            'contour','matte','beauty','blender','nose','highlighters',
                            'face','lip','sponge','brush','glitter','fingerblender','foundation',
                            'concealer','eyeshadow','maybelline','givenchy','doir','nyx','tarte',
                            'fashion','design','makeup','vogue','magazine','trend','model']
        ,'science and technology':['engineer','device','mechanism','industrial','methodology','development','hardware','software','install','system','agrobiology','biology','scientific'
                                   ,'research','study','lab','technology','scholarly','veda','lesson','innovation','biotechnology','cyber','skills','nrc','informatics'
                                   ,'dialup','ict','robot','fibre','optic','product','digital','ione','gadget','AI','artificial','intelligence','machine','deep','learning','network','data'
                                   ,'mining','security','computer','code']
        ,'Nonprofit & activism':['noncommercial','unprofitable','nonprofit','humane','organization','charity','charitable','volunteer','lucrative','for-profit','profit'
                                 ,'activism','agency','organization','private','fund','fundraising','raise','rag','advocacy','movement','campaign'
                                 ,'dynamism','action','politic','feminism','trade','orphan']
    }


    categoriesCounter={}
    for k,v in categories.items():
        for index in range(len(v)):
            v[index]=ps.stem(v[index])
        categoriesCounter[k]=0

    # print(categories)

    for line in file:
        # line = line.decode('utf8')
        line = line.replace('+', ' ').replace('\'',' ').replace('{',' ').replace('}',' ').replace('[',' ').replace(']',' ').replace(';',' ').replace('.', ' ').replace(',', ' ').replace(':', ' ').replace('(',' ').replace(')',' ').replace('/',' ').replace('\\',' ')
        # remove digits with regex
        line = re.sub("(^|\W)\d+($|\W)", " ", line)
        # OR remove digits with casting to int
        line = transliterate(line)
        line = line.lower()
        new_line = []
        for word in line.split(' '):
            if not is_digit(word):
                if '\n' in word:
                    word=word[:len(word)-1]
                word=ps.stem(word)
                new_line.append(word)
                for categoryKey,categoryValue in categories.items():
                    if word in categoryValue:
                        categoriesCounter[categoryKey]+=1

        line = " ".join(new_line)
        # transliterate to Latin characters

        file1.write(line+'\n')
        words=line.split(' ')
    print(categoriesCounter)
    file1.close()
    file.close()
    file=open('sheet3.csv','a')
    # st=''
    # for k,v in categories.items():
    #     st+=k+','
    # st+='class'
    # file.write(st+'\n')
    st=''
    for k,v in categoriesCounter.items():
        st += str(v) + ','
    st+=Cat
    file.write(st+'\n')
    file.close()

