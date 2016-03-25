public class Solution {
    public int[] countBits(int num) {
        if (num == 0) return new int[] {0};
        int[] res = new int[num + 1];
        res[0] = 0; res[1] = 1;
        for (int i = 2; i < num + 1; i++ ){
            int pow = (int)(Math.log(i)/Math.log(2));
            res[i] = 1 + res[i - (int)Math.pow(2, pow)];
        }
        return res;
    }
}