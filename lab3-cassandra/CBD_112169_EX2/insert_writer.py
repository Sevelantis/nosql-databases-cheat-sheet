import uuid
import datetime
from random import randrange

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

class ExampleData:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def usernames():
        return [
            "pop_vii",
            "super_user",
            "film_star",
            "bestactor",
            "justwatchin",
            "myname",
            "not_your_name",
            "whats_poppin",
            "crazymovies",
            "popcorn420",
            "Hanswurst",
            "The_Rock",
            "Dumbledore",
            "Master123",
            "Sith66",
            "Jedi",
            "Yoda",
            "Snape",
            "sevelantis",
            "magus",
            "powerrade",
            "late_or_never",
            "chikita",
            "snickers",
            "earth_planet",
            "programmer99",
            "hackerz123",
            "chocolatee",
            "chupa_chups",
            "i_like_trains",
            "jimi_henrix",
            "jim_morrison"
        ]
    
    @staticmethod
    def video_names():
        return [
            "Avatar",
            "Interstellar",
            "Pulp Fiction",
            "Titanic",
            "Black Hawk Down",
            "American Sniper",
            "Once upon a time in Hollywood",
            "Crazy scooter action",
            "Saw",
            "Tenet",
            "stunning movie",
            "Jack Ass",
            "Harry Potter and the ordem of the phoenix",
            "Super movie 420",
            "Avengers",
            "Shutter Island",
            "Matrix",
            "Mr. Robot",
            "True Man Show",
            "2012",
            "Baywatch",
            "Yesterday",
            "Grand Budapest Hotel",
            "Pirates of the Caribbean",
            "Stranger Things",
            "House of cards",
            "Money Heist",
            "The Crown",
            "How I met your mother",
            "Friends",
            "Taxidermia",
            "Trainspotting",
            "Hulk",
            "Spiderman",
            "Batman",
            "Cinderella"
        ]
        
    @staticmethod
    def names():
        return [
            "Jannis",
            "Miron",
            "Pablo",
            "Hans",
            "Peter",
            "Wilhelm",
            "Lukas",
            "Maya",
            "Emil",
            "Burrr",
            "Moritz",
            "Carl",
            "Albert",
            "Euler",
            "Stephen",
            "Zuzanna",
            "Zofia",
            "Staszek",
            "Hannah",
            "Mirabel",
            "Adam",
            "David",
            "Bob",
            "Justus"
        ]

    @staticmethod
    def video_descriptions():
        return [
            "Hollywood pure",
            "The best actors in one film",
            "latest film techniques",
            "worth an oscar",
            "most expensive film of all the time",
            "best fantasie film",
            "bettern than the book",
            "Unbelievable sience fiction movie",
            "James Cameron was the regisseur",
            "Super action paired with super action",
            "Mother with child with cancer",
            "Amazing scenary in the mountains",
            "The top ten actors in one very bad movie",
            "Big snakes against a Lion"
        ]
    
    @staticmethod
    def events():
        return [
            "play",
            "pause",
            "stop",
            "forward",
            "backward",
            "skip"
        ]

    @staticmethod
    def video_tags():
        return [
            "raccon",
            "cat",
            "funny",
            "sport",
            "skateboard",
            "macbook",
            "hardware",
            "software engineering",
            "networking",
            "dancing",
            "singing",
            "30s",
            "40s",
            "50s",
            "60s",
            "70s",
            "80s",
            "90s",
            "2000",
            "2022",
            "covid",
            "covid",
            "Gibraltar",
            "Aveiro",
            "Lisboa",
            "Madrid",
            "Barcelona",
            "Berlin",
            "Hamburg",
            "Rome",
            "London",
            "Paris",
            "Lyon"
        ]

    @staticmethod
    def comments():
        return [
            "wow",
            "Very bad",
            "Very good",
            "yeah",
            "amazing",
            "unbelieveable",
            "no way",
            "so bad",
            "so good",
            "Uhhhhhhhh",
            "Impossible !!!",
            "Well done!",
            "Stunning",
            "I love it",
            "I recommend",
            "What a mess.",
            "Total crap",
            "Total crazy",
            "Superb",
            "Craaaaaap"
        ]

class Randomizer:
    def __init__(self) -> None:
        self.names = ExampleData.names()
        self.usernames = ExampleData.usernames()
        self.video_names = ExampleData.video_names()
        self.video_tags = ExampleData.video_tags()
        self.video_descriptions = ExampleData.video_descriptions()
        self.comments = ExampleData.comments()
        self.usernames_idx = -1
        self.video_names_idx = -1
    
    def next_name(self):
        return self.names[randrange(0,len(self.names))]
        
    def rand_username(self):
        self.usernames_idx += 1
        return self.usernames[self.usernames_idx]  
    
    def next_video_name(self):
        self.video_names_idx += 1
        return self.video_names[self.video_names_idx]

    def rand_video_tags(self, min, max):
        tags = set()
        [tags.add(self.video_tags[randrange(0,len(self.video_tags))]) for i in range(randrange(min, max))]
        return tags
    
    def rand_timestamp(self):
        # format: 2017-05-05 00:00:00
        # format: "%Y-%m-%d %H:%M:%S"
        year = randrange(2018,2023)
        month = randrange(1,13)
        day = randrange(1,28)
        hour = randrange(0,24)
        minute = randrange(0,60)
        second = randrange(0,60)
        timestamp = datetime.datetime(year, month, day, hour, minute, second).strftime(TIMESTAMP_FORMAT)
        return timestamp
    
    def rand_video_description(self):
        return self.video_descriptions[randrange(0,len(self.video_descriptions))]   

    def rand_comment(self):
        return self.comments[randrange(0,len(self.comments))]
    
    def rand_rating_meta(self, min, max):
        rating_meta = {}
        votes = randrange(min, max)
        ratings = [randrange(0, 6) for i in range(votes)]
        avg_rating = int(sum(ratings) / len(ratings))
        rating_meta["ratings"] = ratings
        rating_meta["avg_rating"] = avg_rating
        rating_meta["votes"] = votes
        return rating_meta
    
    def rand_events(self):
        events = {}
        
        start = datetime.datetime.strptime(self.rand_timestamp(), "%Y-%m-%d %H:%M:%S")
        total_time = 0
        pauses = set()
        resumes = set()
        amount_of_pauses = randrange(0, 5)
        for i in range(amount_of_pauses):
            video_play_time = randrange(1, 600)
            pause = start + datetime.timedelta(seconds=video_play_time)
            video_pause_time = randrange(1, 600)
            resume = pause + datetime.timedelta(seconds=video_pause_time)

            pauses.add(pause.strftime("%Y-%m-%d %H:%M:%S"))
            resumes.add(resume.strftime("%Y-%m-%d %H:%M:%S"))
            total_time += video_play_time + video_pause_time
        if amount_of_pauses == 0:
            total_time = randrange(1, 1500)
        stop = start + datetime.timedelta(seconds=total_time)
    
        events["start"] = start
        events["stop"] = stop
        events["pauses"] = pauses if len(pauses) != 0 else '{}' 
        events["resumes"] = resumes if len(resumes) != 0  else '{}' 
        events["total_time"] = total_time
        return events

    
class CacheStorage:
    def __init__(self) -> None:
        self.user_meta_cache = list()
        self.video_meta_cache = list()
        self.comment_meta_cache = list()
    
    ### rand

    def rand_user_meta(self):
        return self.user_meta_cache[randrange(0, len(self.user_meta_cache))]
    
    def rand_video_meta(self):
        return self.video_meta_cache[randrange(0, len(self.video_meta_cache))]
    
    def rand_comment_meta(self):
        return self.comment_meta_cache[randrange(0, len(self.comment_meta_cache))]
    
    def rand_followers_usernames(self, min, max):
        rand_amount = randrange(min, max)
        followers_usernames = set()
        [followers_usernames.add(str(self.rand_user_meta()["name"])) for i in range(rand_amount)]
        return followers_usernames
    
    ### save

    def save_user_meta(self, user_name):
        user_meta = {}
        user_meta["name"] = user_name
        self.user_meta_cache.append(user_meta)
    
    def save_video_meta(self, video_name, rating_meta):
        video_meta = {}
        video_meta["name"] = video_name
        video_meta["votes"] = rating_meta["votes"]
        video_meta["ratings"] = rating_meta["ratings"]
        video_meta["avg_rating"] = rating_meta["avg_rating"]
        self.video_meta_cache.append(video_meta)
    
    def save_comment_meta(self, comment_content):
        comment_meta = {}
        comment_meta["name"] = comment_content
        self.comment_meta_cache.append(comment_meta)


class InsertGenerator:
    def __init__(self, cache_storage : CacheStorage, randomizer : Randomizer) -> None:
        self.cache_storage = cache_storage
        self.randomizer = randomizer
        
    def insert_rand_user(self) -> str:
        username = self.randomizer.rand_username()
        name = self.randomizer.next_name()
        email = f"{username}@gmail.com"
        created_date = self.randomizer.rand_timestamp()
        cql = f"INSERT INTO user \
            (username, name, email, created_date) VALUES \
            ('{username}', '{name}', '{email}', '{created_date}');\n"
            
        self.cache_storage.save_user_meta(username)
    
        return cql
    
    def insert_video_by_rating(self, video_meta_details):
        cql = f"INSERT INTO videos_by_rating \
            (video_name, avg_rating, votes, ratings) values \
            ('{video_meta_details['name']}', {video_meta_details['avg_rating']}, {video_meta_details['votes']}, {video_meta_details['ratings']});\n"
        return cql
    
    def insert_rand_video(self) -> str:
        name = self.randomizer.next_video_name()
        description = self.randomizer.rand_video_description()
        tags = self.randomizer.rand_video_tags(2, 6)
        created_date = self.randomizer.rand_timestamp()
        
        user_meta = self.cache_storage.rand_user_meta()
        user_name = user_meta["name"]
        
        followers = self.cache_storage.rand_followers_usernames(2, 8)
        
        rating_meta = self.randomizer.rand_rating_meta(5, 65)
        votes = rating_meta["votes"]
        ratings = rating_meta["ratings"]
        avg_rating = rating_meta["avg_rating"]
        
        cql = f"INSERT INTO video \
            (name, description, tags, created_date, user_name, followers, avg_rating, votes, ratings) VALUES \
            ('{name}', '{description}', {tags}, '{created_date}', '{user_name}', {followers}, {avg_rating}, {votes}, {ratings});\n"
            
        self.cache_storage.save_video_meta(name, rating_meta)
            
        return cql
    
    def insert_rand_comment(self) -> str:
        content = self.randomizer.rand_comment()
        
        user_meta = self.cache_storage.rand_user_meta()
        user_name = user_meta["name"]
        
        video_meta = self.cache_storage.rand_video_meta()
        video_name = video_meta["name"]
        
        created_date = self.randomizer.rand_timestamp()
        cql = f"INSERT INTO comment \
            (content, video_name, user_name, created_date) VALUES \
            ('{content}', '{video_name}', '{user_name}', '{created_date}');\n"
            
        self.cache_storage.save_comment_meta(content)
        
        return cql
    
    def insert_rand_event_log_video_by_user(self):
        id = uuid.uuid4()
        
        user_meta = self.cache_storage.rand_user_meta()
        user_name = user_meta["name"]
        
        video_meta = self.cache_storage.rand_video_meta()
        video_name = video_meta["name"]
        
        events = self.randomizer.rand_events()
        start = events["start"]
        stop = events["stop"]
        pauses = events["pauses"]
        resumes = events["resumes"]
        total_time = events["total_time"]
        
        cql = f"INSERT INTO video_watch \
            (video_name, user_name, start, stop, pauses, resumes, total_time) VALUES \
            ('{video_name}', '{user_name}', '{start}', '{stop}', {pauses}, {resumes}, {total_time});\n"
        
        return cql
    
    
class InsertWriter:
    def __init__(self, file, insert_generator : InsertGenerator) -> None:
        self.file = file
        self.insert_generator = insert_generator
        file.write('-- This file was generated automatically using insert_writer.py, author: Miron Oskroba 112169.\n')
    
    def generate_users(self, amount):
        [file.write(self.insert_generator.insert_rand_user()) for i in range(amount)]
    
    def generate_videos(self, amount):
        [file.write(self.insert_generator.insert_rand_video()) for i in range(amount)]
    
    def generate_videos_by_rating(self, amount):
        video_meta = self.insert_generator.cache_storage.video_meta_cache
        for video_meta_details in video_meta:
            file.write(self.insert_generator.insert_video_by_rating(video_meta_details))

    def generate_comments(self, amount):
        [file.write(self.insert_generator.insert_rand_comment()) for i in range(amount)]
    
    def generate_event_logs_video_by_user(self, amount):
        [file.write(self.insert_generator.insert_rand_event_log_video_by_user()) for i in range(amount)]


if __name__ == '__main__':
    file = open("CBD_112169_EX2_SEEDDATA.cql", "w")
    cache_storage = CacheStorage()
    randomizer = Randomizer()
    insert_generator = InsertGenerator(cache_storage, randomizer)
    insert_writer = InsertWriter(file, insert_generator)
    ###
    amount = 30
    insert_writer.generate_users(amount)
    insert_writer.generate_videos(amount)
    insert_writer.generate_videos_by_rating(amount)
    insert_writer.generate_comments(amount)
    insert_writer.generate_event_logs_video_by_user(amount)
    ###
    file.close()
