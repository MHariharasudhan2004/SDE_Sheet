from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        prefix_sum = self._calculate_prefix_sum(mat)

        answer = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                r1 = max(0, r - k)
                c1 = max(0, c - k)
                r2 = min(m - 1, r + k)
                c2 = min(n - 1, c + k)

                answer[r][c] = self._get_sum_region(
                    prefix_sum, r1, c1, r2, c2
                )

        return answer

    def _calculate_prefix_sum(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                prefix_sum[r + 1][c + 1] = (
                    mat[r][c]
                    + prefix_sum[r][c + 1]
                    + prefix_sum[r + 1][c]
                    - prefix_sum[r][c]
                )

        return prefix_sum

    def _get_sum_region(
        self,
        prefix_sum: List[List[int]],
        r1: int,
        c1: int,
        r2: int,
        c2: int
    ) -> int:
        # Convert to 1-based indexing
        r1 += 1
        c1 += 1
        r2 += 1
        c2 += 1

        return (
            prefix_sum[r2][c2]
            - prefix_sum[r1 - 1][c2]
            - prefix_sum[r2][c1 - 1]
            + prefix_sum[r1 - 1][c1 - 1]
        )
