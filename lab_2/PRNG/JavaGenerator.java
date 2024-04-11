import java.util.Random;

/*
 * The class for generating a random binary
 * sequence with a length of 128 bits
 */
public class JavaGenerator{

/*
 * The function for generating a random bits
 */
    public static int random() {
        Random random = new Random();
        return random.nextInt(2);
    }

/*
 * The function for generating a random 
 * sequence and displaying it on the screen
 * @param n The number of bits in the sequence 
 */
    public static void RandomGenerator(int n){
        for(int i = 0; i < n; i++)
            System.out.print(random());
    } 

    public static void main(String[] args){
        final int NUMBER = 128;
        RandomGenerator(NUMBER);
    }
}