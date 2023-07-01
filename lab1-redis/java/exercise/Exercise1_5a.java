package exercise;

import java.util.Scanner;

public class Exercise1_5a extends Exercise{

    private final String JON = "jon";
    private final String MIKE = "mike";
    private final String BOB = "bob";
    private final String CHANNEL1 = "channel1";
    private final String CHANNEL2 = "channel2";
    public Exercise1_5a(boolean isDryRun) {
        super(isDryRun);
    }

    @Override
    public void execute() {
        setup();
        demo();
        loop();
    }

    private void demo(){
        redisDB.readAllMsgs(JON, CHANNEL1).forEach(System.out::println);
        redisDB.readAllMsgs(JON, CHANNEL2).forEach(System.out::println);

        redisDB.readAllMsgs(MIKE, CHANNEL1).forEach(System.out::println);
        redisDB.readAllMsgs(MIKE, CHANNEL2).forEach(System.out::println);

        redisDB.readAllMsgs(BOB, CHANNEL1).forEach(System.out::println);
        redisDB.readAllMsgs(BOB, CHANNEL2).forEach(System.out::println);
    }

    private void loop(){
        boolean running = true;
        String currentUser = JON;
        while(running){
            String in = getInput("choose your figher: 1 Jon 2 Mike 3 Bob");
            switch (in){
                case "1":
                    currentUser = JON;break;
                case "2":
                    currentUser = MIKE;break;
                case "3":
                    currentUser = BOB;break;
                default: break;
            }
            System.out.println("Chosen: " + currentUser +", your messages: ");
            redisDB.readAllMsgs(currentUser, CHANNEL1).forEach(System.out::println);
            redisDB.readAllMsgs(currentUser, CHANNEL2).forEach(System.out::println);

            // add more functionalities etc..
        }
    }

    private void setup(){
        redisDB.clear();
        redisDB.addUser(JON);
        redisDB.addUser(MIKE);
        redisDB.addUser(BOB);
        redisDB.subscribeUserToChannel(JON, CHANNEL1);
        redisDB.subscribeUserToChannel(MIKE, CHANNEL1);
        redisDB.subscribeUserToChannel(MIKE, CHANNEL2);
        redisDB.subscribeUserToChannel(BOB, CHANNEL2);
        redisDB.storeMsg(CHANNEL1, "welcome in channel1 $$$ 1");
        redisDB.storeMsg(CHANNEL1, "welcome in channel1 $$$ 2");
        redisDB.storeMsg(CHANNEL1, "welcome in channel1 $$$ 3");
        redisDB.storeMsg(CHANNEL2, "WILKOMMEN IM CHANNEL ZWEI ^^^ 1");
        redisDB.storeMsg(CHANNEL2, "WILKOMMEN IM CHANNEL ZWEI ^^^ 2");
        redisDB.storeMsg(CHANNEL2, "WILKOMMEN IM CHANNEL ZWEI ^^^ 3");
    }

    private String getInput(String msg){
        Scanner scanner = new Scanner(System.in);
        System.out.println(msg);
        return scanner.nextLine();
    }
}
