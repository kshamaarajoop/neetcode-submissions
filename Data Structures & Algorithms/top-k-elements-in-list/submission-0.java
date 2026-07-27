class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for(int num : nums){

        hashMap.put(num, hashMap.getOrDefault(num,0)+1);
        }
        //converting into a list and sorting it
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(hashMap.entrySet());
        
        list.sort((a,b)-> b.getValue()-a.getValue());
        
        //return the first K elements
        int[] ans = new int[k];
        for(int i = 0; i < k; i++){
            ans[i] = list.get(i).getKey();
        }
        return ans;
        
    }
}