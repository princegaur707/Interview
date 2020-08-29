#JAVA code 
#Same can't be done with python as it deals with negative numbers too bitwise
class Solution {
    public int getSum(int a, int b) {
        if(b == 0){
            return a;
        }
        return getSum(a^b,(a&b) << 1);
    }
}