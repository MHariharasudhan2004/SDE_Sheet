class Solution:
    def largestRectangleArea(self, heights):
        st, res = [], 0
        for bar in heights + [-1]:  # add -1 to flush remaining bars
            step = 0
            while st and st[-1][1] >= bar:
                w, h = st.pop()
                step += w
                res = max(res, step * h)
            st.append((step + 1, bar))
        return res
