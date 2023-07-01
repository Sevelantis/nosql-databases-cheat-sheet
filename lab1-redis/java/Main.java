import exercise.*;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        List<Exercise> exercises = new ArrayList<>(Arrays.asList(
                new Exercise1_3a(true),
                new Exercise1_3b(true),
                new Exercise1_4a(true),
                new Exercise1_4b(false),
                new Exercise1_5a(true),
                new Exercise1_5b(true)
        ));
        for(var ex : exercises){
            if(!ex.isDryRun()){
                ex.execute();
            }
        }
    }
}
