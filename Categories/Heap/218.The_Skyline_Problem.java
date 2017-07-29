class CriticalPoint {
    public int x;
    public int h;

    public CriticalPoint (int x, int h) {
        this.x = x;
        this.h = h;
    }
    
    public String toString() {
        return String.format("[%d, %d]", this.x, this.h);
    }
    
    public boolean equals(Object o) {
        CriticalPoint other = (CriticalPoint)o;
        return this.h == other.h;
    }
}

public class Solution {
    
    public List<int[]> getSkyline(int[][] buildings) {
        if ( buildings == null || buildings.length == 0 ) {
            return new ArrayList<>();
        }
        
        List<CriticalPoint> cps = new ArrayList<>();
        for ( int[] building : buildings) {
            cps.add(new CriticalPoint(building[0], building[2]));
            cps.add(new CriticalPoint(building[1], -building[2]));
        }
        
        Collections.sort(cps, new Comparator<CriticalPoint>(){
            public int compare(CriticalPoint cp1, CriticalPoint cp2){
                if ( cp1.x != cp2.x ) {
                    return cp1.x - cp2.x;
                }
                return cp2.h - cp1.h;
            }
        });
        
        Queue<CriticalPoint> q = new PriorityQueue<>(1, new Comparator<CriticalPoint>(){
            public int compare(CriticalPoint cp1, CriticalPoint cp2) {
                return cp2.h - cp1.h;
            }
        });
        
        int i = 0;
        List<int[]> result = new ArrayList<>();
        while ( i < cps.size() ) {
            int curX = cps.get(i).x;
            while ( true ) {
                if ( cps.get(i).h < 0 ) {
                    CriticalPoint newOne = new CriticalPoint(curX, -cps.get(i).h);
                    q.remove(newOne);
                } else {
                    q.offer(cps.get(i));
                }
                
                if ( i + 1 < cps.size() && cps.get(i + 1).x == curX ){
                    i++;
                } else {
                    break;
                }
            }
            
            if ( q.isEmpty() ) {
                result.add(new int[]{curX, 0});
            } else {
                CriticalPoint curCp = q.peek();
                if ( result.isEmpty() || curCp.h != result.get(result.size() - 1)[1] ) {
                    result.add(new int[]{curX, curCp.h});
                }
            }
            
            i++;
        }
        
        return result;
    }
}
