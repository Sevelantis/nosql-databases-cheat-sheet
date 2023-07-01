-- c7. Allow searching for all videos by a given author;
select * from videos_by_user where user_name='Jedi'; -- order by created_date desc; <- not necessary

-- c8. Allow the user to search for comments, sorted inversely by date;
select * from comments_by_content where content='so bad'; -- order by created_date desc; <- not necessary

-- c9 s. Allow searching for comments by videos, sorted inversely by date;
select * from comment where video_name='Yesterday'; -- order by created_date desc; <- not necessary

-- c10. Allow searching the average rating of a video and how many times it was voted;
select * from videos_by_rating where avg_rating=3;
select * from videos_by_rating where avg_rating=2 and votes > 20;


-- d1. The last 3 comments entered for a video;
select * from comment where video_name='Baywatch' order by created_date desc limit 3;

-- d2. List of tags for a given video;
select * from tags_by_video where name='Yesterday';

-- d3. All videos tagged Aveiro;
select * from video where tags contains 'Aveiro';

-- d4. The last 5 events of a given video made by a user;
select * from events_by_user where user_name='chocolatee' order by start desc limit 5; -- by 'event' I understand all video session events:  start, stop, resumes and pauses timestamps

-- d5. Videos shared by a certain user (maria1987, for example) in a certain period of time (August 2017, for example);
select * from videos_by_user where user_name='Jedi' and created_date > '2019-05-26';
select * from videos_by_user where user_name='Jedi' and created_date < '2020-05-26';

-- d6. The last 10 videos, sorted inversely by shared date;
-- This is not possible since I can not access all the videos and I have to restrict it with where clause.

-- d7. All followers (followers) of a given video;
select * from followers_by_video where name='Yesterday';

-- d8. All comments (of videos) that a user is following (following);
-- This is not possible using only one query.

-- d9. The 5 highest rated videos;
-- This would be possible using table 'videos_by_rating', but my solution's primary key is using two partition keys(avg_rating, votes)
-- If there was just one it would look like:
-- SELECT * FROM videos_by_rating order by avg_rating desc limit 5;

-- d10. A query that returns all the videos and that clearly shows the way in which they are ordered;
-- This is not possible using query.

-- d11. List with the existing Tags and the number of videos cataloged with each one of them;
-- This is not possible.

-- d12. .. d13. Describe 2 additional questions to the database (items 12 to 13), significantly different from the previous ones, and also present the research solution for each question.

-- d12 show all events for a given video ordered by oldest
select * from video_watch where video_name='Jack Ass' order by start asc;

-- d13 show all comments by a given user ordered by newest
select * from comments_by_user where user_name='justwatchin' order by created_date desc;

-- get json from tables
select json * from user;
select json * from video;
select json * from comment;
select json * from videos_by_rating;
select json * from video_watch;