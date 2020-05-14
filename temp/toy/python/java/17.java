class Solution {
	public List<String> letterCombinations(String digits) {
		String[] d = new String[]
				{
						" ",
						"",
						"abc",
						"def",
						"ghi",
						"jkl",
						"mno",
						"pqrs",
						"tuv",
						"wxyz"
				};
		List<String> ans = new ArrayList<>();
		char[] curLettCombo = new char[digits.length()];
		dfs(digits, d, ans, curLettCombo, 0);
		return ans;


	}
	private void dfs(String digits, String[] d, List<String> ans, char[] curLettCombo, int curIndex)
	{
		if ( curIndex == digits.length()){
			if (curIndex > 0) {
				ans.add(new String(curLettCombo));
			};
			return;
		}
		String s = d[Character.getNumericValue(digits.charAt(curIndex))];
		for (int i = 0; i < s.length(); ++i) {
			curLettCombo[curIndex] = s.charAt(i);
			dfs(digits, d, ans, curLettCombo, curIndex + 1);

		}

	}
}
