from collections import deque


class BrowserHistory:
    history = deque()
    history_forward = deque()

    def __init__(self, homepage: str):
        self.history.appendleft(homepage)

    def visit(self, url: str) -> None:
        if self.history_forward:
            self.history_forward.clear()
        self.history.appendleft(url)

    def back(self, steps: int) -> str:
        while len(self.history) > 1 and steps:
            self.history_forward.appendleft(self.history.popleft())
            steps -= 1

        return self.history[0]

    def forward(self, steps: int) -> str:
        while self.history_forward and steps:
            self.history.appendleft(self.history_forward.popleft())
            steps -= 1

        return self.history[0]


if __name__ == '__main__':
    # Your BrowserHistory object will be instantiated and called as such:

    obj = BrowserHistory("leetcode.com")
    obj.visit("google.com")
    obj.visit("facebook.com")
    obj.visit("youtube.com")
    print(obj.back(1))
    print(obj.back(1))
    print(obj.forward(1))
    obj.visit("linkedin.com")
    print(obj.forward(2))
    print(obj.back(2))
    print(obj.back(7))
