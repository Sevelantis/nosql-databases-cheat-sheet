import com.datastax.driver.core.Session;
import connector.CassandraConnector;

public class EX3 {
    public static final int PORT = 9999;
    public static final String NODE = "localhost";

    public void run(){
        CassandraConnector cassandraConnector = new CassandraConnector();
        cassandraConnector.connect(NODE, PORT);
        var session = cassandraConnector.getSession();

        selectUsers(session);
        selectVideosByUser(session, "Maya");
        selectCommentsByContent(session, "so bad");
        selectCommentsByVideoName(session, "Titanic");
        insertUsers(session);
        editUser(session);
        deleteUser(session);

        cassandraConnector.close();
    }

    public void deleteUser(Session session){
        var sql = "delete from cbd_112169_ex2.user where username='TO_DELETE';";
        System.out.println(sql);
        session.execute(sql);
        System.out.println();
    }

    public void editUser(Session session){
        var sql = "update cbd_112169_ex2.user set name='UPDATED' where username='INSERTED';";
        System.out.println(sql);
        session.execute(sql);
        System.out.println();
    }

    public void insertUsers(Session session){
        var sql1 = "INSERT INTO cbd_112169_ex2.user             (username, name, email, created_date) VALUES             ('INSERTED', 'Maya', 'whats_poppin@gmail.com', '2019-12-15 03:07:40');";
        var sql2 = "INSERT INTO cbd_112169_ex2.user             (username, name, email, created_date) VALUES             ('TO_DELETE', 'TO_DELETE', 'TO_DELETE@gmail.com', '2019-10-15 03:07:40');";
        System.out.println(sql1);
        session.execute(sql1);
        System.out.println(sql2);
        session.execute(sql2);
        System.out.println();
    }

    public void selectUsers(Session session){
        var sql = "select * from cbd_112169_ex2.user;";
        System.out.println(sql);
        var result = session.execute(sql).iterator();
        while(result.hasNext()){
            var next = result.next();
            var username = next.getString("username");
            var name = next.getString("name");
            var email = next.getString("email");
            var createdDate = next.getTimestamp("created_date");
            System.out.println(String.format("username: %s, name: %s, email: %s, created_date: %s", username,name,email,createdDate.toString()));
        }
        System.out.println();
    }

    public void selectVideosByUser(Session session, String userName){
        var sql = String.format("select * from cbd_112169_ex2.videos_by_user where user_name='%s' and created_date > '2019-05-26';", userName);
        System.out.println(sql);
        var result = session.execute(sql).iterator();
        while(result.hasNext()){
            var next = result.next();
            var name = next.getString("name");
            var user_name = next.getString("user_name");
            var createdDate = next.getTimestamp("created_date");
            System.out.println(String.format("name: %s, user_name: %s, created_date: %s",
                    name, user_name,createdDate.toString()));
        }
        System.out.println();
    }

    public void selectCommentsByContent(Session session, String content){
        var sql = String.format("select * from cbd_112169_ex2.comments_by_content where content='%s';", content);
        System.out.println(sql);
        var result = session.execute(sql).iterator();
        while(result.hasNext()){
            var next = result.next();
            var cont = next.getString("content");
            var video_name = next.getString("video_name");
            var user_name = next.getString("user_name");
            var createdDate = next.getTimestamp("created_date");
            System.out.println(String.format("content: %s, video_name: %s, user_name: %s, created_date: %s",
                    cont,video_name, user_name, createdDate.toString()));
        }
        System.out.println();
    }

    public void selectCommentsByVideoName(Session session, String videoName){
        var sql = String.format("select * from cbd_112169_ex2.comment where video_name='%s' order by created_date desc limit 3;", videoName);
        System.out.println(sql);
        var result = session.execute(sql).iterator();
        while(result.hasNext()){
            var next = result.next();
            var cont = next.getString("content");
            var video_name = next.getString("video_name");
            var user_name = next.getString("user_name");
            var createdDate = next.getTimestamp("created_date");
            System.out.println(String.format("content: %s, video_name: %s, user_name: %s, created_date: %s",
                    cont,video_name, user_name, createdDate.toString()));
        }
        System.out.println();
    }

}
