import exercise.*;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        List<Exercise> exercises = new ArrayList<>(Arrays.asList(
                new Exercise2_4a(true), // to run an exercise please set to "false"
                new Exercise2_4b(false),
                new Exercise2_4c(false),
                new Exercise2_4d(false)
        ));
        for(var ex : exercises){
            if(!ex.isDryRun()){
                ex.execute();
            }
        }
    }
}
