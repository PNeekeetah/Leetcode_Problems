"""
Beats 19% in terms of runtime and 6% in terms of memory
Took me 19 minutes and 52 to solve this
First submission succesful.
"""


class StockSpanner:

    def __init__(self):
        self.prices_list = list()
        self.span_list = list()

    def next(self, price: int) -> int:
        span = 1
        index = len(self.prices_list) - 1
        while index > -1:
            if self.prices_list[index] <= price:
                span += self.span_list[index]
                index -= self.span_list[index]
            else:
                break
        self.prices_list.append(price)
        self.span_list.append(span)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
