package HCL;
import java.util.ArrayList;
/**
 * two_max_values
 */
public class two_max_values {

    // find max value from given array

    // static int get_max1_value(int[] array){
    //     int max1 = 0;
    //     for (int i = 0; i < array.length; i++) {
    //         if (array[i]>max1){
    //             max1 = array[i];
    //         }
    //     }        
    //     return max1;
    // }

    static ArrayList<Integer> get_max1_and_max2_value(int[] array){
        // Create an empty ArrayList
        ArrayList<Integer> result = new ArrayList<>();
        int max1 = 0;
        int max2 = 0;

        for (int i = 0; i < array.length; i++) {
            if (array[i]>max1){
                max1 = array[i];
            }
        }     
        
        for (int i = 0; i < array.length; i++) {
            if (array[i]>max2 && array[i]<max1){
                max2 = array[i];
            }
        }   
        // Add values to the ArrayList
        result.add(max1);
        result.add(max2);
        return result; // Return the ArrayList
    }

    

    public static void main(String[] args) {
        int[] numbers = {15, 24, 48, 21, 43, 11, 79, 93}; // Array of integers
        System.out.println(get_max1_and_max2_value(numbers));
    }
}