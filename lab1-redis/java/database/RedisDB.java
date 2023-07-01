package database;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

import file.FileLoader;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.params.ScanParams;

public class RedisDB {

	private final String REDIS_SERVER_IP = "192.168.64.10"; // a server is run on the local VM
	private final int REDIS_SERVER_PORT = 6379;
	private Jedis jedis;
	public static String USERS = "users";
	public static String CSV_USERS = "csv_users";
	public static String MSG_USERS = "msg_users";

	public RedisDB() {
		this.jedis = new Jedis(REDIS_SERVER_IP, REDIS_SERVER_PORT);
	}

	public void saveUserSadd(String key, String username) {
		jedis.sadd(key, username);
	}

	public void saveUsersZadd(Map<String, Double> userData) {
		jedis.zadd(CSV_USERS, userData);
	}

	public void saveUsersFromTxt(String filename) {
		String[] users = FileLoader.readLines(filename);
		for (String user: users) {
			saveUserSadd(USERS, user);
		}
	}
	public void saveUsersFromCsv(String filename) throws IOException {
		String[] csvUsers = FileLoader.readLines(filename);
		Map<String, Double> userData = new HashMap<>();
		for(String csvUser: csvUsers){
			String[] data = csvUser.split(";");
			userData.put(data[0], Double.valueOf(data[1]));
		}
		saveUsersZadd(userData);
	}
	public List<String> autocompleteDecreasing(){
		return jedis.zrevrange(CSV_USERS, 0, 9000);
	}

	public List<String> autocomplete(String pattern){
		return jedis.sscan(USERS, "", new ScanParams().match(String.format("%s*", pattern)).count(9000))
				.getResult()
				.stream()
				.sorted()
				.toList();
	}

	public Set<String> getUser() {
		return jedis.smembers(USERS);
	}

	public Set<String> getAllKeys() {
		return jedis.keys("*");
	}

	public void close(){
		jedis.close();
	}
	public void addUser(String username){
		saveUserSadd(MSG_USERS, username);
	}
	public void sendMsg(String userFrom, String userTo, String msg){

	}
}
