# Idea:
"""
delta decide direction
bound decide steps
"""

public class Solution {
    private int matrix_len;

    public List<Integer> spiralOrder(int[][] matrix) {
        if ( matrix == null || matrix.length == 0 || matrix[0] == null || matrix[0].length == 0 ) {
            return new ArrayList<Integer>();
        }
        
        this.matrix_len = matrix.length;
        int row, col;
        row = col = (matrix_len-1)/2;
        
        int[] deltaRow = new int[] {0, 1, 0, -1};
        int[] deltaCol = new int[] {1, 0, -1, 0};
        int curDir = 0;
        List<Integer> result = new ArrayList<>();
        
        for ( int bound = 1; bound <= this.matrix_len; bound++ ) {
            curDir = curDir%4;
            for ( int i = 0; i <= bound*2; i++ ) {
                if ( i == bound*2 ) {
                    curDir++;
                    break;
                }
                result.add(matrix[row][col]);
                if ( i == bound ) {
                    curDir++;
                }
                row += deltaRow[curDir];
                col += deltaCol[curDir];
                if ( !inbound(row, col) ) { break; }
            }
            if ( !inbound(row, col) ) { break; }
        }
        
        return result;
    }
    
    private boolean inbound(int row, int col) {
        return row >= 0 && row < this.matrix_len && col >= 0 && col < this.matrix_len;
    }
}
