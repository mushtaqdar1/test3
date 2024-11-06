import java.time.LocalDateTime;

public class Main {
    
    // Returns a seed value based on current system time.
    public static long newTime() {
        // Acquiring the current date and time
        LocalDateTime now = LocalDateTime.now();
        
        // Extracting components: hour, minute, second, day, and year
        long x = now.getHour() * 10000000 + now.getMinute() * 100000 +
                 now.getSecond() * 1000 + now.getDayOfMonth() * 10 + now.getYear();
        
        // Return the calculated seed value
        return x;
    }

    // Returns a random 8-digit key.
    public static long getKey() {
        // Taking the key from system time to generate a seed value
        long key = newTime();
        
        // Squaring the key
        key = key * key;

        // Extracting required number of digits (here, 8).
        if (key < 1000000000000000L) {
            key = key / 10000;
            key = key % 100000000;
        } else {
            key = key / 10000;
            key = key % 100000000;
        }

        // Returning the key value
        return key;
    }

    // Driver Code
    public static void main(String[] args) {
        // Get the first key
        System.out.println(getKey());
        
        // Get the second key
        System.out.println(getKey());
    }
}
//Note: The output will change according to the date and time.
