class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dot_product_matrix = [[0] * 505 for _ in range(505)]  # Dynamic programming array
        nums1_size = len(nums1)
        nums2_size = len(nums2)

        first_max = float('-inf')
        second_max = float('-inf')
        first_min = float('inf')
        second_min = float('inf')

        # Calculate maximum and minimum values for nums1
        for num in nums1:
            first_max = max(first_max, num)
            first_min = min(first_min, num)

        # Calculate maximum and minimum values for nums2
        for num in nums2:
            second_max = max(second_max, num)
            second_min = min(second_min, num)

        # Check special cases where all elements are negative
        if (first_max < 0 and second_min > 0) or (first_min > 0 and second_max < 0):
            return max(first_max * second_min, first_min * second_max)

        # Initialize the dot product matrix with 0
        for i in range(505):
            dot_product_matrix[i] = [0] * 505

        # Calculate dot products and populate the dot product matrix
        for i in range(nums1_size - 1, -1, -1):
            for j in range(nums2_size - 1, -1, -1):
                current_dot_product = nums1[i] * nums2[j] + dot_product_matrix[i + 1][j + 1]
                dot_product_matrix[i][j] = max(current_dot_product, dot_product_matrix[i + 1][j], dot_product_matrix[i][j + 1])

        return dot_product_matrix[0][0]  # Return the maximum dot product