class Solution {
     final static int range = Integer.MAX_VALUE;
    
    public int reverse(int x) {
        
        if ((x >= range -1) || (x <= range * -1))
            return 0;
        
        else{
          
            int sign = 1;
            if (x <0)
            {
                sign = -1;
                x = x * (-1);
            }
            
            return getRev(x,0) * sign;
            
        }
        
    
        
        
    }
    
    public static int getRev(int x,long res)
    {
        while (x>0)
        {
            res = (res*10) + (x%10);
            
              if ((res >= range -1) || (res <= range * -1)){
              return 0;
              }
            x = x/10  ; 
        }   
        return (int) res;
     
        
    }
}