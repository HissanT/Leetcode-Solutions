# Valid Parentheses – LeetCode 20  

This is my Python solution for the **Valid Parentheses** problem.  

I’m not super proud of this one — the code isn’t simple to look at, and I ended up using a more unconventional method with `counter` and two dicts for open/close checks. That said, I felt good about finally getting it to pass, because I pieced it together in my own way rather than just copying the “standard stack solution.”  

At first, this didn’t work when running on **Python 2** (LeetCode default) because dict key ordering wasn’t consistent there. I had to switch the submission to **Python 3** where dicts preserve insertion order, and then my approach worked fine.  

I’ll definitely come back to this problem later to refactor and aim for better performance and readability. For now, this is my working version.  
