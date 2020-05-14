class 17. Letter Combinations of a Phone Number {
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


    }
    private void dfs(digits, d, ans, curLettCombo, curIndex)
    {
    	if ( curIndex == digits.length()){
    		ans.add(new String(curLettCombo));
    		return;
    	}
    	String s = d[Character.getNumricValue(digits.charAt(curIndex))];
    	for (int i = curIndex; i < s.length(); ++i) {
    		curLettCombo[curIndex] = s.charAt(i);
    		dfs(digits, d, ans, curLettCombo, curIndex + 1);
//    		curL
//    		Char c = s.get(i);
//    		curLettCombo.add(c);

    	}

    }
}