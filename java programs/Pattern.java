class Pattern {
    public static void main(String[] args) {

        String word = "PROGRAM";
        int n = word.length();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {

                if (j == i) {
                    System.out.print(word.charAt(i));
                }
                else if (i+j == n-1) {
                    System.out.print(word.charAt(n - i - 1));
                }
                else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
