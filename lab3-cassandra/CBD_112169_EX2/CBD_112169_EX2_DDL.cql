DROP KEYSPACE cbd_112169_ex2;
CREATE KEYSPACE cbd_112169_ex2 WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
USE cbd_112169_ex2;
-- pretty output (uncomment)
-- EXPAND ON;
-- 1. User management: among others, register the username, name, email, registration timestamp on the platform;
create table user(
    username text,
    name text,
    email text,
    created_date timestamp,
    primary key((username))
);

-- 2. Video management: among others, register the author of the share, video name, description, one or more tags and upload/share time stamp
-- 4. Management of video followers: allow the registration of user who follow a certain video. In an information system, it will allow, for example, to notify all followers of a new comment inserted for the video;
-- 6. Video Rating: Integer value from 1-5, per video and does not require author registration.
create table video (
    name text,
    description text,
    tags set<text>,
    created_date timestamp,
    user_name text,
    followers set<text>,
    avg_rating int,
    votes int,
    ratings list<int>,
    primary key((name), created_date)
)
WITH CLUSTERING ORDER BY (created_date DESC);

-- 3. Management of comments: made for a video at a given moment in time and authored by a user;
-- c9. Allow searching for comments by videos, sorted inversely by date;
-- d1. The last 3 comments entered for a video;
create table comment (
    content text,
    video_name text,
    user_name text,
    created_date timestamp,
    primary key ((video_name), created_date)
)
WITH CLUSTERING ORDER BY (created_date DESC);

-- 5. Event recording: by video and user and can be of the play/pause/stop type, including the
-- temporal recording of the event and the (temporal) moment in which it occurs in the
-- video. For example, user XPTO played the YGZ video at 2:35:54 on October 2, 2017, 300 seconds into the video;
-- d12 show all events for a given video ordered by oldest
create table video_watch(
    user_name text,
    video_name text,
    start timestamp,
    stop timestamp,
    pauses set<timestamp>,
    resumes set<timestamp>,
    total_time int,
    primary key((video_name), start)
)
WITH CLUSTERING ORDER BY (start DESC);

-- c10. Allow searching the average rating of a video and how many times it was voted;
CREATE table videos_by_rating (
    video_name text,
    avg_rating int,
    votes int,
    ratings list<int>,
    primary key (avg_rating, votes)
);

-- c7. Allow searching for all videos by a given author;
-- d5. Videos shared by a certain user (maria1987, for example) in a certain period of time (August 2017, for example);
CREATE MATERIALIZED VIEW videos_by_user 
    AS SELECT name, user_name, created_date
    FROM video
    WHERE user_name IS NOT NULL AND created_date IS NOT NULL AND name IS NOT NULL
PRIMARY KEY ((user_name), created_date, name);

-- c8. Allow the user to search for comments, sorted inversely by date;
CREATE MATERIALIZED VIEW comments_by_content 
    AS SELECT content, video_name, user_name, created_date
    FROM comment
    WHERE content IS NOT NULL AND video_name IS NOT NULL AND created_date IS NOT NULL
PRIMARY KEY ((content), created_date, video_name);

-- d2. List of tags for a given video;
CREATE MATERIALIZED VIEW tags_by_video
    AS SELECT name, tags, created_date
    FROM video
    WHERE name IS NOT NULL AND created_date IS NOT NULL
PRIMARY KEY ((name), created_date);

-- d3. All videos tagged Aveiro;
create index on video(tags); -- create a secondary index on tags to enable searching

-- d4. The last 5 events of a given video made by a user;
CREATE MATERIALIZED VIEW events_by_user
    AS SELECT *
    FROM video_watch
    WHERE user_name IS NOT NULL AND video_name IS NOT NULL AND start IS NOT NULL
PRIMARY KEY ((user_name), start, video_name);

-- d7. All followers (followers) of a given video;
CREATE MATERIALIZED VIEW followers_by_video
    AS SELECT name, followers, created_date
    FROM video
    WHERE name IS NOT NULL AND created_date IS NOT NULL
PRIMARY KEY ((name), created_date);

-- d8. All comments (of videos) that a user is following (following);
-- This would be too much time-consuming to implement.

-- d9. The 5 highest rated videos;

-- d10. A query that returns all the videos and that clearly shows the way in which they are ordered;
-- d11. List with the existing Tags and the number of videos cataloged with each one of them;
-- d12. .. d13. Describe 2 additional questions to the database (items 12 to 13), significantly different from the previous ones, and also present the research solution for each question.

-- d13 show all comments by a given user
CREATE MATERIALIZED VIEW comments_by_user
    AS SELECT content, video_name, user_name, created_date
    FROM comment
    WHERE user_name IS NOT NULL AND video_name IS NOT NULL AND created_date IS NOT NULL
PRIMARY KEY ((user_name), created_date, video_name);
