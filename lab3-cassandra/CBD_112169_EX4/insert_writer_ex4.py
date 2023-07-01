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
            "The_Rock"
        ]
    
    @staticmethod
    def product_names():
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
        ]
    
    @staticmethod
    def colors():
        return [
            "GOLD",
            "GREEN",
            "RED",
            "PURPLE",
            "WHITE",
            "BLACK",
            "PINK",
            "BLUE",
            "ORANGE",
            "YELLOW",
            "MILKY",
            "DARK GREEN",
        ] 
        
    @staticmethod
    def producers():
        return [
            "SWEETS LAB",
            "ACTIVE KENDAMA",
            "KENDAMA ISRAEL",
            "YEPPA",
            "SixFingerStrings",
        ]
        
    @staticmethod
    def statuses():
        return [
            "AWAITING_PAYMENT",
            "FINISHED",
            "REFUND_REQUEST"
        ]
    
    @staticmethod
    def product_names():
        return [
            "KENDAMA ISRAEL BIG BROTHER MAPLE OS",
            "LOTUS KENDAMA SACRED!",
            "V27 - GREAT SCOTT CUSHION CLEAR !!!",
            "V27 - CLEVER GIRL",
            "Sea Safari Model - BOOST - CUSHION CLEAR- KENDAMA",
            "Elite Thunderbolt Beech Tacky - MAPLE KEN",
            "BIG BROTHER BAMBOO",
            "Waldo Bamboo Tacky",
            "Krom Pop",
            "TEXTILE - SPACE KENDAMA NOWOŚĆ",
            "Premium String 5-packs - linki zapasowe - Kendama",
            "Extra-Long - linki zapasowe - Kendama",
        ]
        
    @staticmethod
    def product_descriptions():
        return [
            "Hollywood pure",
            "kendama connects worlds, and Reed Stark has been a leader in facilitating that connection for years.",
            "Reed is a professional BMX rider for BSD, a clothing designer for his own brand Safari State, and the best at crossing the line between genius and madness.",
            "Light and strong",
            "Very expensive but it is worth it",
            "Best in Portugal",
            "bettern than other models",
            "Unbelievablde weight / comfort / grip",
            "Maple Safari Ken  Enlarged cups (BOOST Shape) Engraving Safari on the sarado",
            "Reed Stark Signature engraved on the spike",
            "Engraved giraffe design on cup stands -Big Ball (BOOST Beech Tama)",
            "Adhesion paint - matte (CUSHION CLEAR ) - Blue giraffe pattern -Bottom 30% makes it easier to track the dial",
            "Metal spinner bead -Extra line -Safari Mod Stickers",
            "We have scoured the submissions from our 2018 Design a Prime contest and picked up some new favorites! In 2018, we hand-painted every dam, so our options were limited, but now we can do almost ANY project."
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
    def tags():
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
    def opinions():
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

    
class CacheStorage:
    def __init__(self) -> None:
        self.users = list()
        self.products = list()
        self.opinions = list()
    
    ### rand

    def rand_user(self):
        return self.users[randrange(0, len(self.users))]
    
    def rand_product(self):
        return self.products[randrange(0, len(self.products))]
    
    def rand_opinion(self):
        return self.opinions[randrange(0, len(self.opinions))]
    
    def rand_followers_usernames(self, min, max):
        rand_amount = randrange(min, max)
        followers_usernames = set()
        [followers_usernames.add(str(self.rand_user()["name"])) for i in range(rand_amount)]
        return followers_usernames
    
    ### save

    def save_user(self, user):
        self.users.append(user)
    
    def save_product(self, product):
        self.products.append(product)
    
    def save_opinion(self, opinion):
        self.opinions.append(opinion)
        
    def save_purchase(self, purchase):
        self.opinions.append(purchase)
        

class Randomizer:
    def __init__(self, cache_storage : CacheStorage) -> None:
        self.usernames = ExampleData.usernames()
        self.product_names = ExampleData.product_names()
        self.tags = ExampleData.tags()
        self.statuses = ExampleData.statuses()
        self.product_descriptions = ExampleData.product_descriptions()
        self.opinions = ExampleData.opinions()
        self.colors = ExampleData.colors()
        self.producers = ExampleData.producers()
        self.cache_storage = cache_storage
        self.usernames_idx = -1
        self.product_names_idx = -1
    
    ### build

    def build_user(self):
        user = {}
        user["user_name"]       = self.next_username()
        user["email"]           = f"{user['user_name']}@gmail.com"
        user["created_date"]    = self.rand_timestamp()
        return user
    
    def build_product(self):
        product = {}
        product["product_name"]     = self.next_product_name()
        product["producer"]         = self.rand_producer()
        product["price"]            = randrange(120, 250)
        product["color"]            = self.rand_color()
        product["description"]      = self.rand_product_description()
        product["release_date"]     = self.rand_timestamp()
        return product
    
    def build_purchase(self):
        purchase = {}
        purchase["user_name"]       = self.rand_username()
        amount = randrange(1, 7)
        products = {}
        total = 0
        for i in range(amount):
            p = self.cache_storage.rand_product()
            total += p["price"]
            products[f"product_name{i}"] = p["product_name"]
        purchase["products"]        = products
        purchase["total"]           = total
        purchase["status"]          = self.rand_status()
        purchase["purchased_date"]  = self.rand_timestamp()
        return purchase
    
    def build_opinion(self):
        opinion = {}
        opinion["user_name"]        = self.rand_username()
        opinion["product_name"]     = self.cache_storage.rand_product()["product_name"]
        opinion["content"]          = self.rand_comment()
        rating = self.rand_rating(2,66)
        opinion["avg_rating"]       = rating["avg_rating"]
        opinion["votes"]            = rating["votes"]
        opinion["ratings"]          = rating["ratings"]
        opinion["created_date"]     = self.rand_timestamp()
        return opinion
    
    ### rand
    
    def rand_status(self):
        return self.statuses[randrange(0,len(self.statuses))]
    
    def rand_username(self):
        return self.usernames[randrange(0,len(self.usernames))]
    
    def rand_producer(self):
        return self.producers[randrange(0,len(self.producers))]
    
    def rand_color(self):
        return self.colors[randrange(0,len(self.colors))]
        
    def next_username(self):
        self.usernames_idx += 1
        return self.usernames[self.usernames_idx]  
    
    def next_product_name(self):
        self.product_names_idx += 1
        return self.product_names[self.product_names_idx]

    # def rand_video_tags(self, min, max):
    #     tags = set()
    #     [tags.add(self.video_tags[randrange(0,len(self.video_tags))]) for i in range(randrange(min, max))]
    #     return tags
    
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
    
    def rand_product_description(self):
        return self.product_descriptions[randrange(0,len(self.product_descriptions))]   

    def rand_comment(self):
        return self.opinions[randrange(0,len(self.opinions))]
    
    def rand_rating(self, min, max):
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



class InsertGenerator:
    def __init__(self, cache_storage : CacheStorage, randomizer : Randomizer) -> None:
        self.cache_storage = cache_storage
        self.randomizer = randomizer
 
    def insert_rand_user(self) -> str:
        user            = self.randomizer.build_user()
        user_name       = user["user_name"]
        email           = user["email"]
        created_date    = user["created_date"]
        
        cql = f"INSERT INTO user \
            (user_name, email, created_date) VALUES \
            ('{user_name}', '{email}', '{created_date}');\n"
            
        self.cache_storage.save_user(user)
    
        return cql
    
    def insert_rand_product(self) -> str:
        product         = self.randomizer.build_product()
        product_name    = product["product_name"]
        producer        = product["producer"]
        price           = product["price"]
        color           = product["color"]
        description     = product["description"]
        release_date    = product["release_date"]
        
        cql = f"INSERT INTO product \
            (product_name, producer, price, color, description, release_date) VALUES \
            ('{product_name}', '{producer}', {price}, '{color}', '{description}', '{release_date}');\n"
            
        self.cache_storage.save_product(product)
            
        return cql
    
    def insert_rand_purchase(self):
        purchase        = self.randomizer.build_purchase()
        user_name       = purchase["user_name"]
        total           = purchase["total"]
        products        = purchase["products"]
        purchased_date  = purchase["purchased_date"]        
        status          = purchase["status"]
                
        cql = f"INSERT INTO purchase \
            (status, user_name, total, products, purchased_date) VALUES \
            ('{status}', '{user_name}', {total}, {products}, '{purchased_date}');\n"
        
        self.cache_storage.save_purchase(purchase)
        
        return cql
    
    def insert_rand_opinion(self) -> str:
        opinion         = self.randomizer.build_opinion()
        user_name       = opinion["user_name"]
        product_name    = opinion["product_name"]
        content         = opinion["content"]
        avg_rating      = opinion["avg_rating"]
        votes           = opinion["votes"]
        ratings         = opinion["ratings"]
        created_date    = opinion["created_date"]
        
        created_date = self.randomizer.rand_timestamp()
        cql = f"INSERT INTO opinion \
            (user_name, product_name, content, avg_rating, votes, ratings, created_date) VALUES \
            ('{user_name}', '{product_name}', '{content}', {avg_rating}, {votes}, {ratings}, '{created_date}');\n"
            
        self.cache_storage.save_opinion(opinion)
        
        return cql
    
class InsertWriter:
    def __init__(self, file, insert_generator : InsertGenerator) -> None:
        self.file = file
        self.insert_generator = insert_generator
        file.write('-- This file was generated automatically using insert_writer.py, author: Miron Oskroba 112169.\n')
    
    def generate_users(self, amount):
        [file.write(self.insert_generator.insert_rand_user()) for i in range(amount)]
    
    def generate_products(self, amount):
        [file.write(self.insert_generator.insert_rand_product()) for i in range(amount)]
    
    # def generate_videos_by_rating(self, amount):
    #     video_meta = self.insert_generator.cache_storage.products
    #     for video_meta_details in video_meta:
    #         file.write(self.insert_generator.insert_video_by_rating(video_meta_details))

    def generate_opinions(self, amount):
        [file.write(self.insert_generator.insert_rand_opinion()) for i in range(amount)]
    
    def generate_purchases(self, amount):
        [file.write(self.insert_generator.insert_rand_purchase()) for i in range(amount)]


if __name__ == '__main__':
    file = open("CBD_112169_EX4_SEEDDATA.cql", "w")
    cache_storage = CacheStorage()
    randomizer = Randomizer(cache_storage)
    insert_generator = InsertGenerator(cache_storage, randomizer)
    insert_writer = InsertWriter(file, insert_generator)
    ###
    amount = 12
    insert_writer.generate_users(amount)
    insert_writer.generate_products(amount)
    insert_writer.generate_opinions(amount)
    insert_writer.generate_purchases(amount)
    ###
    file.close()
