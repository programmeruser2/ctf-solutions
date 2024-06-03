import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static ArrayList<String> command(final String cmdline,
    final String directory) {
        try {
            Process process = 
                new ProcessBuilder(new String[] {"bash", "-c", cmdline})
                    .redirectErrorStream(true)
                    .directory(new File(directory))
                    .start();

            ArrayList<String> output = new ArrayList<String>();
            BufferedReader br = new BufferedReader(
                new InputStreamReader(process.getInputStream()));
            String line = null;
            while ( (line = br.readLine()) != null )
                output.add(line);

            //There should really be a timeout here.
            if (0 != process.waitFor())
                return null;

            return output;

        } catch (Exception e) {
            //Warning: doing this is no good in high quality applications.
            //Instead, present appropriate error messages to the user.
            //But it's perfectly fine for prototyping.

            return null;
        }
    }
    public static void main(String[] args) {
        test("ls");
        test("cat flag.txt");
    }
    static void test(String cmdline) {
        ArrayList<String> output = command(cmdline, ".");
        if (null == output)
            System.out.println("\n\n\t\tCOMMAND FAILED: " + cmdline);
        else
            for (String line : output)
                System.out.println(line);

    }

}
