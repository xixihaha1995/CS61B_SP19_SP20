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
    private void dfs(digits, d, ans, curLettCombo, curLen)
    {
    	if ( curLettCombo.length() == digits.length()){
    		ans.add(new String(curLettCombo));
    		return;
    	}
    	String s = d[Character.getNumricValue(digits.charAt(curLen))];
    	for (int i = curLen; i < s.length(); ++i) {
    		curLettCombo[curLen] = s.charAt(i);
    		dfs(digits, d, ans, curLettCombo, curLen);
//    		curL
//    		Char c = s.get(i);
//    		curLettCombo.add(c);

    	}

    }
}