public class ExpandString {
    public static void main(String[] args) {
        String input = "a1b10";
        
        char charToRepeat = 0;
        int repeatCount = 0;
        StringBuilder result = new StringBuilder();

        for (char current : input.toCharArray()) {
            
            if (Character.isLetter(current)) {
                // 1. If we already have a character saved, "ship" it to the result
                if (charToRepeat != 0) {
                    result.append(String.valueOf(charToRepeat).repeat(repeatCount));
                }
                
                // 2. Start a new "save" block
                charToRepeat = current;
                repeatCount = 0;
                
            } else { 
                // 3. Convert current digit character to an actual int using Integer.parseInt
                // String.valueOf(current) turns '1' into "1", then parseInt turns "1" into 1
                int digitValue = Integer.parseInt(String.valueOf(current));
                repeatCount = (repeatCount * 10) + digitValue;
            }
        }

        // 4. "Ship" the very last character block after the loop ends
        if (charToRepeat != 0) {
            result.append(String.valueOf(charToRepeat).repeat(repeatCount));
        }

        System.out.println(result.toString());
    }
}
