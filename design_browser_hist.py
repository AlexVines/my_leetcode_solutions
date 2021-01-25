class BrowserHistory:
    """
    You have a browser of one tab where you start on the homepage and you can visit another url,
    get back in the history number of steps or move forward in the history number of steps.

    Implement the BrowserHistory class:

    BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
    void visit(string url) Visits url from the current page. It clears up all the forward history.
    string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x,
    you will return only x steps. Return the current url after moving back in history at most steps.
    string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x,
    you will forward only x steps. Return the current url after forwarding in history at most steps.

    https://leetcode.com/problems/design-browser-history/

    """
    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.current += 1
        self.hist = self.hist[:self.current]
        self.hist.append(url)

    def back(self, steps: int) -> str:
        self.current = max(0, self.current-steps)
        return self.hist[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.hist)-1, self.current+steps)
        return self.hist[self.current]


