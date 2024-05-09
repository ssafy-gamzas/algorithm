public class Main {
	static class Solution {
		public int longestOnes(int[] nums, int k) {
			int start = 0, end =0, repeat = 0;
			int max =0;
			while(end <= nums.length -1){
				if(nums[end] == 1) repeat++;
				int data = end - start +1 -repeat;
				while(data > k){
					if(nums[start] == 1)repeat--;
					start++;
				}

				max = Math.max(max,end-start+1);
				end++;
			}

			return max;
		}
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		solution.longestOnes(new int[] {0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1}, 3);
	}
}
